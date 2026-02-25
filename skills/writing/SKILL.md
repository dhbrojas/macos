---
name: writing
description: Guidelines for technical writing. Use when writing documentation, papers, technical specifications in Markdown, LaTeX, Typst, etc.
---

Good technical writing is tough to achieve for humans, even more so for language models (like you). This guide provides some tips and focuses on pitfalls of language model prose that should be avoided. It covers end-to-end document writing, coarse/fine-grained editing of existing documents, and one-off sentence or paragraph generation.

# Guidelines

**Be Concise** A common tell sign of AI writing is sentences with low information density. Is it because language models write text in a single pass and rarely revisit their prose? Possibly. In truth, succint writing (on a "word budget") is profoundly hard, requires good planning and clarity of mind. Of course, language models can process thousands of words per second. So... what's the fuss about conciseness? Well, humans are slow and, worst of all, lazy. They disengage from content almost immediately. A mere 3s into any paragraph the impatient human thinks: "Shall I keep going?", "Am I bored yet?", "OK, let's skim through this". For this reason, any piece destined for human consumption must be written with great care and optimized for length. Conciseness is the guarantee you will be read and understood.

**Don't Describe, Do Explain** Communicating complex, detail-rich ideas effectively is also hard. You must be concise (remember?) but exhaustive. You must use simple language yet be precise. You want to build intuition yet not disfigure reality. Sigh... How? Again, the answer here is thought, effort, and planning. First, you have to know exactly what it is you're trying to convey. Are we sharing an idea? An API reference? An article? If your goal is explanation, you should aim to explain not describe. Provide insights into how things work. Always start from first principles. Use simple words. Humans don't learn through bullet points or soundbites but through hierarchies, clear and concise incremental steps and examples. Most importantly, expect that every part of your explanation may be questioned with "Why?". Someone who's learning may get confused at every step. Frame explanations accordingly.

**Don't Be Boring** Engagement is the product of either content or form. The latter is our focus here. Good form is subjective, so good thing you have a "subject" here to pontificate to you. More seriously, stay away from sensationalism and douchy prose. Honest, disinterested communication of information is key. A touch of humor, informal speech, is OK. Obviously, avoid cliche patterns. Have you noticed AIs aggressively overuse bullet points? Conceptually, you could say AIs love enumeration which I doubt is what we want 90% of our text to be. Similarly, AIs overuse sections (at all granularities). If we assume that every section in a document corresponds to a distinct concept, and that no singular text should discuss more than a dozen concepts, then you probably realize that sections are misused today. For example, a README may only contain an introduction, usage, build and contributing section. A technical spec may only consist of sections: introduction, requirements, architecture, implementation.

**Write for an Audience** There is no greater sin than failing to accurately define a clear scope and intent for your document. This requires in-depth thinking about the target audience's needs. What information does my audience care about? What knowledge can I assume they already have? How do I care to present it? How long and exhaustive does my audience expect the document to be? These are all questions we should settle before writing.

# Capabilities

From now on, you are asked to exhibit the following capabilities.

## End-to-End Document Writing

When asked to write a document from scratch, it may be opportune to agree on the content and structure before any writing takes place. Leverage the tool for asking user questions as many times as necessary until we're aligned. It's also preferable to write the document in multiple passes instead of all at once .

## Coarse/Fine-Grained Document Editing

When asked to produce edits for an existing document,

## One-Off Sentence/Paragraph Generation

When asked to assist in improving a sentence or paragraph,

## Writing Feedback

When asked to provide feedback on a document.

## Collaboration

Automated tools, or myself may produce edits to the document while you are actively working on it. This may produce some conflicts or warnings (e.g. "document unexpectedly modified"). In such a case, identify what changes were made and adjust course accordingly. Do not overwrite edits made by others unless told otherwise.
