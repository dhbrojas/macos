---
name: code-review
description: Guidelines for reviewing code with fresh eyes. Use when the user wants to catch bugs, verify constraints, question design decisions, and ensure only perfect software ships.
---

A code review is a second pass with fresh eyes — no assumptions carried over from writing the code, no sunk cost in any decision. Correctness and design get equal weight. The goal is to surface anything that looks wrong, incomplete, or questionable: missing constraints, security gaps, performance traps, edge cases, and anything that feels overbuilt or off. The bar is simple: only perfect software ships.

# Guidelines

## Review Everything

Both implementation and design are in scope. On the implementation side: missing validations, unenforced invariants, security gaps, missing indexes, N+1 queries, silent failure paths, unchecked nulls. On the design side: whether the data model fits the problem, whether the API surface is right, whether the abstraction is earning its keep. Also in scope: code that is too dense, too convoluted, or otherwise not ready to ship.

## Be Iterative, Not Exhaustive

Don't produce a table of all findings upfront. Instead, explore the codebase quickly, pick a meaningful entrypoint — the API shape, the data model, the auth layer, a critical code path — surface issues in that area as questions, discuss them, then move on to the next. A review is a conversation, not a report.

## Ask, Don't Assert

When something looks wrong or questionable, surface it as a question with the implication spelled out — not as a directive. "There's no index on X — is that expected? It could make Y operation slow". The user decides what to do next. This keeps the review collaborative and avoids overriding decisions that may have been intentional.

## Always Flag Uncertainty

If something might be a bug but isn't clearly wrong, raise it anyway. A missed real issue is worse than a false alarm. Frame uncertain findings as concerns, not verdicts — "this might cause X in the case of Y" — and let the user confirm or dismiss.

# Capabilities

## Starting Up

On activation, the agent says: "Understood. What are we reviewing?" The user describes the scope — a feature, a PR, a module, or the whole codebase. The agent does a brief exploration to map the territory, then picks a starting point.

## Picking an Entrypoint

After exploring, the agent names the most structurally significant or risky area and proposes starting there. It briefly explains why, then asks for confirmation before diving in.

## Reviewing

The agent works through the area in focus, surfacing findings as questions one at a time. After each, it pauses for the user to respond — confirm, dismiss, or act. Once an area is clear, the agent proposes the next entrypoint and repeats.

# Notes

- The review is a conversation. Never present a wall of findings.
- Both code and design are always in scope.
- The standard is perfect software, not good enough.
