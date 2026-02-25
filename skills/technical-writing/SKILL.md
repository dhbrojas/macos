---
name: technical-writing
description: Guidelines for technical writing. Use when writing documentation, papers, technical specifications in Markdown, LaTeX, Typst, etc.
---

Good technical writing is tough to achieve for humans, even more so for language models. This guide provides some useful guidelines for end-to-end document writing, coarse/fine-grained editing of existing documents, and one-off sentence or paragraph generation.

# Guidelines

## Be Concise

Information dense writing (on a "word budget") is hard, requires planning and clarity of mind about what to convey and how. Yet, today, it's an absolute necessity, a primary requirement. Humans (who are lazy and slow) disengage from content almost immediately. In mere seconds, readers think: "Shall I keep going?", "Am I bored yet?", "OK, let's skim through this". For this reason, any piece destined for human consumption must be written with great care and optimized for length. Conciseness is the guarantee you will be read and understood.

## Don't Describe, Do Explain

Communicating complex, detail-rich ideas effectively is challenging. You must be concise yet exhaustive, use simple language yet be precise, build intuition yet not disfigure reality. This is achieved through planning. First, you have to know exactly what it is you're trying to convey. Are we sharing an idea? An API reference? An article? If your goal is explanation, you should aim to explain not describe. Provide insights into how things work. Always start from first principles. Use simple words. Humans don't learn through bullet points or soundbites but through hierarchies, clear and concise incremental steps and examples. Most importantly, expect that every part of your explanation may be questioned with "Why?". Someone who's learning may get confused at every step. Frame explanations accordingly.

## Write Narratively

Language models tend to aggressively overuse bullet points, headings, dividers, etc. Conceptually, AIs love enumeration and structure. Unfortunately, this produces sub-par, hard to digest documents. Writing narratively requires good planning at the macro and micro level. This section evaluates how to approach both.

The **macro** level is concerned with the high-level structure and throughline of the piece. Before any writing takes place, you should have an exhaustive outline of all sections and subsections. It's unlikely you need more than a few (2-5). Otherwise, the document's scope is probably too large or ambiguous.

The **micro** level is concerned with the organization and structure of paragraphs, sentences and other elements. When writing, consider what idea each paragraph conveys, what linking words are used, how to ensure information is not repeated or omitted.

## Write for an Audience

Writing requires thinking deeply about the scope and intent for a piece. You must identify the reader and the specific questions they seek answers to through your document. In particular, you may ask:
* What information does my audience care about?
* What knowledge can I assume in my audience?
* What level of detail is expected?
* What order and structure is best?

# Capabilities

From now on, you are asked to exhibit the following capabilities.

## End-to-End Document Writing

When asked to write a document from scratch, you should seek to understand the desired content and structure before any writing takes place. Leverage the tool for asking user questions as many times as necessary until we're aligned. Then, write the tentative outline to the target file using the `Write` tool. End your turn, and wait for the user to provide some feedback. The user may leave some notes by editing the target file directly. Below, is an example of what an outline might look like:

```md
# Posts Database Schema Technical Spec

<!-- Introductory paragraph, explain the posts feature (140 character text, posted by an account, which other accounts may like), what's out of scope (no comments, bookmarks, or other settings at this stage), and that this document introduces the relevant Postgres schema -->

## Background

<!-- Relevant information about the current Postgres schema. -->

<!-- Code snippet showing the SQL definition of the users table, only relevant fields. -->

## Solution

<!-- Introductory sentence indicating the spec introduces two tables. -->

### Tables

#### Posts

<!-- SQL code snippet of posts table with id, author_user_id, text. Primary key (id). Index on author_user_id. -->

#### Likes

<!-- SQL code snippet of likes table with user_id, post_id. Primary key (user_id, post_id). Index on post_id.  -->

### Queries

#### Select Posts by User

<!-- SQL code snippet of query to select posts by user -->

#### Count Likes for Post

<!-- SQL code snippet of query to count likes for a post -->

## Notes

### Performance

<!-- Some rationale on performance profile of proposed schema, scalability, future directions -->
```

Once the user confirms the outline is appropriate, you should edit each placeholder one by one with the final text. Don't hesitate to pause, and check in with the user if uncertain about content or form.

## Coarse/Fine-Grained Document Editing

When asked to produce edits for an existing document, leverage the ask question tool the content which must be updated. Consider whether the form or structure should change and to what degree. Don't hesitate to pitch multiple suggestions to increase your chances of matching the user's intent. If requirements are clear, perform the edits directly.

## Writing Feedback

When asked to provide feedback on a document, perform a thorough evaluation of its content, structure, and style. Identify areas that need improvement and suggest specific changes. Consider the audience and purpose of the document, and ensure that it is clear, concise, and accurate.

## Collaboration

Automated tools, or myself may produce edits to the document while you are actively working on it. This may produce some conflicts or warnings (e.g. "document unexpectedly modified"). In such a case, identify what changes were made and adjust course accordingly. Do not overwrite edits made by others unless told otherwise.

# Notes

- When writing tentative document outlines, DO NOT display the outline in the conversation. Directly write the outline to a file using the `Write` tool.
