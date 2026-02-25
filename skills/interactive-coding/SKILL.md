---
name: interactive-coding
description: Instructions for interactive, pair-programming style coding sessions. Use when the user wants to drive implementation through conversation rather than delegating a task end-to-end.
---

By default, an AI agent completes a task end-to-end and returns when done. In interactive coding mode, the dynamic is different: the user collaborates with the agent like a pair programming session. Implementation becomes incremental, step-by-step and more discussion happens around the design choices and coding style.

# Guidelines

An interactive coding session follows a predictable process. First, the user or agent identify a small, scoped task. If needed, discussion happens to settle on an implementation. A quick review round, then repeat.

## Starting Up

On activation, the agent says: "Understood. What are we working on today?". The user provides some details on the feature or refactor to be implemented. Then, the agent very briefly explores the relevant parts of the codebase. If anything is unclear, the agent must reach for its ask user question tool.

## Picking a Task

The user or agent proposes the next concrete task — something narrow like "Let's define the DB schema" or "Let's write the API handler". If the user doesn't propose one, the agent suggests the most logical starting point and asks for confirmation before proceeding.

## Implementing

Before touching code, if necessary, the agent surfaces any meaningful questions — architecture, naming, structure, style. It presents options with brief tradeoffs, recommends one, and waits for confirmation. It never silently resolves ambiguity. Once aligned, it writes the patch.

## Feedback and Iteration

After each patch, the agent pauses and summarizes what changed in one sentence, then invites the user to review, redirect, or approve. The agent may also proactively flag risks, suggest alternatives, or note follow-on improvements — always framed as suggestions, not blockers. Once the task is closed, loop back to Picking a Task.

# Notes

- When appropriate, the agent may steer away from the exact process in the guidelines in order to accomodate the user's desire to move at a faster or slower pace.
