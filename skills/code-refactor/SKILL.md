---
name: code-refactor
description: Guidelines for refactoring code based on the user's opinionated preferences. Use when the user wants to reduce code footprint, improve naming, simplify logic, or find a cleaner model for a feature.
---

Code quality is a measure of code footprint. Every line, variable, and function carries a mental cost — it must be read, understood, and remembered. A codebase is clean when it says exactly what it needs to say and nothing more. The target is the most compact form that a reviewer reads once and immediately understands.

# Guidelines

## Minimize Footprint

Before calling a change done, always attempt to reduce the code footprint further. Can a variable be eliminated by inlining its value? Can two statements be rearranged so one disappears? Can a function be removed by folding its body into its caller? The answer is often yes.

## Code That Breathes

Minimizing footprint does not mean compressing code into a wall of text. Logical blocks should be separated by blank lines. Related statements belong together; unrelated ones don't. Dense and aerated are not opposites — well-golfed code still breathes.

## Don't Extract What's Only Called Once

Pulling logic into a named function is only justified when that function is called in more than one place. Single-use logic extracted into its own function adds a layer of indirection for no gain — the reader must jump somewhere else to understand what happens here. Keep it inline, or define it directly inside the body of the one caller that needs it.

## Golf, But Don't Cheat

Reducing footprint means genuinely eliminating statements — rearranging logic, collapsing conditions, inlining intermediates. It does not mean packing multiple statements onto one line to fake brevity. After any change, run the formatter. Compressed and unformatted is worse than what you started with.

## Avoid Over-Aliasing

Intermediate variables that do nothing but rename a value are noise. Assign only when the value is reused, or when a complex expression is genuinely unreadable inline. Aliasing a value once to give it a name that its context already implies is clutter.

## Keep Names Short and Precise

Long names are a smell. A name should be as short as it can be while remaining unambiguous in context. Single-letter names are appropriate for loop indices, coordinates, and other conventional shorthands. Don't pad names with type information, scope indicators, or qualifiers the reader can already infer from the surrounding code.

## Comment the Why, Never the What

A comment that restates what the code does is worthless — the code already says that. A comment is valuable only when it captures something the code cannot: why a decision was made, a constraint being respected, a tradeoff accepted, an edge case that isn't obvious. Default to no comment. Add one only when the reasoning would otherwise be lost.

## Organize Code Efficiently

Sometimes the right refactor is just moving things to where they belong. Each file, package, or module should have a clear, single responsibility. Anything that doesn't fit that responsibility should live elsewhere. Go's standard library is a good model: small, focused packages with minimal cross-dependencies, each named after what it provides. Mixing unrelated concerns into the same module because it's convenient is a form of clutter.

# Capabilities

## Starting Up

On activation, the agent says: "Understood. What are we refactoring?" The user names a file, module, function, class, or describes a pattern to clean up. The agent briefly explores the relevant code, then asks any necessary clarifying questions before proposing anything.

## Picking a Target

The user or agent identifies a concrete refactoring target — a function to inline, a type to simplify, a module to restructure, or a new model for existing logic. If the user doesn't propose one, the agent suggests the most impactful starting point and asks for confirmation. Related changes that belong together are batched into a single patch; unrelated improvements are kept separate.

## Implementing

Before touching code, the agent surfaces any meaningful open questions — naming, structure, tradeoffs between approaches. It recommends one option with brief rationale and waits for confirmation. It never silently resolves ambiguity. Once aligned, it writes the shortest correct patch.

## Feedback and Iteration

After each patch, the agent summarizes the change in one sentence and invites review. Once the target is closed, loop back to picking the next one.

# Examples

## Beautiful Multi-Head Attention

The following code snippet displays beautiful formatting, clear variable names, good use of comments and minimal footprint.

```python
from typing import Protocol

from torch.nn import Module
from torch.nn.attention import BlockMask, flex_attention


class PositionEncoder(Protocol):
    def __call__(self, q: Tensor, k: Tensor, positions: Tensor) -> Tuple[Tensor, Tensor]: ...


class MultiHeadAttention(Module):
    def __init__(
        self,
        *,
        dim: int,
        num_query_heads: int,
        num_key_value_heads: int,
        position_encoder: PositionEncoder | None = None,
    ):
        super().__init__()

        self.num_query_heads = num_query_heads
        self.num_key_value_heads = num_key_value_heads
        self.dim_per_head = dim // num_query_heads
        self.dim = dim
        self.position_encoder = position_encoder
        # Q, K, V projection matrices
        self.wq = nn.Linear(dim, num_query_heads * dim_per_head, bias=False)
        self.wk = nn.Linear(dim, num_key_value_heads * dim_per_head, bias=False)
        self.wv = nn.Linear(dim, num_key_value_heads * dim_per_head, bias=False)
        # Output projection matrix
        self.wo = nn.Linear(num_query_heads * dim_per_head, dim, bias=False)

    def forward(
        self,
        x: Tensor,
        positions: Tensor,
        mask: BlockMask,
    ) -> Tensor:
        B, L, D = x.shape

        # (B, L, D) -> (B, QH, L, HD)
        q = self.wq(x).view(B, L, self.num_query_heads, self.dim_per_head).transpose(1, 2)
        # (B, L, D) -> (B, KVH, L, HD)
        k = self.wk(x).view(B, L, self.num_key_value_heads, self.dim_per_head).transpose(1, 2)
        v = self.wv(x).view(B, L, self.num_key_value_heads, self.dim_per_head).transpose(1, 2)

        # Encode relative/absolute positional information before the attention computation.
        # (B, QH, L, HD) -> (B, QH, L, HD)
        # (B, KVH, L, HD) -> (B, KVH, L, HD)
        if self.position_encoder is not None:
            q, k = self.position_encoder(q, k, positions)

        # Perform self dot product attention.
        # (B, QH, L, HD), (B, KVH, L, HD), (B, KVH, L, HD) -> (B, QH, L, HD)
        x = flex_attention(q, k, v, enable_gqa=self.num_query_heads > self.num_key_value_heads, block_mask=mask)

        # Reassemble the attention heads
        # (B, QH, L, HD) -> (B, L, D)
        x = x.transpose(1, 2).contiguous().view(B, L, D)

        # Compute the output projection
        # (B, L, D) -> (B, L, D)
        x = self.wo(x)

        return x
```

## Linus's Take on Taste

In his TED talk, Linus Torvalds makes a point about taste: "sometimes you can see a problem in a different way and rewrite it so that a special case goes away and becomes the normal case, and that's good code".

He uses linked lists as an example. Consider the following code snippet:

```go
package linked

type Node struct {
	val  int
	next *Node
}

func Remove(head **Node, entry *Node) {
	var prev *Node
	walk := *head

	for walk != entry {
		prev = walk
		walk = walk.next
	}

	if prev == nil {
		*head = entry.next
	} else {
		prev.next = entry.next
	}
}
```

Good taste makes you realize the code can be shortened greatly, and the final `if` statement can be removed. This requires thinking of a new approach. That's the heart of refactoring.

```go
// ...

func Remove(head **Node, entry *Node) {
	walk := head

	for *walk != entry {
		walk = &(*walk).next
	}

	*walk = entry.next
}
```

# Notes

- Run the formatter when appropriate, after large batches of code changes.
