---
name: ieee-citations
description: Skill for ensuring high-quality citation references according to IEEE standards in texts sourced from the knowledge base or the internet. Using this skill is mandatory whenever I draw from and provide information from external sources.
---

# IEEE Citation Standard

This skill ensures that in texts I create that are based on sources (especially from the knowledge base or the internet), I always provide high-quality citation references according to the IEEE standard.

## Rules for using citations:

1. **Mandatory use in Knowledge Base:** In all documents in the knowledge base (`knowledge/`), the use of citations is always **required**.
2. **General use:** When providing texts, answers, or documents based on sources (knowledge base, internet, files), I must always include citations in IEEE format.
3. **In-text citations:** For in-text citations, I use numbers in square brackets (e.g., [1], [2]). Numbers correspond to a chronologically ordered list of references at the end of the text. Multiple citations are formatted as [1], [3] or [1]–[5].
4. **Reference list:** At the end of the text, there must always be a numbered list of sources used (under the heading "References" or "Sources Used").

## IEEE formatting rules for different source types:

### Books and monographs
[1] J. M. Author, *Book Title*, x ed. City of publication: Publisher, Year, pp. xxx-xxx.

### Journal articles / Scientific papers
[2] J. M. Author, "Article title," *Shortened Journal Title*, vol. x, no. x, pp. xxx-xxx, Month, Year.

### Internet sources (Websites)
[3] J. M. Author (or Organization). "Document/article title." Website name. [Online]. Available: http://www.url.com. [Accessed: Day Month Year].
*(If author is unknown, begin with the document title.)*

### Knowledge Base (Knowledge Base) and internal memory
[4] "Document title in knowledge base," Descart-OS Knowledge Base, [Internal]. Available: knowledge/path/to/document.md. [Accessed: Day Month Year].

## Implementation
Whenever I generate an answer, document, or entry in the knowledge base based on objective facts:
- I automatically insert in-text citations [1], [2], etc. directly into flowing text to minimize hallucinations and maintain accuracy.
- I always append a "Sources Used" section at the end of the output or document.
- I format sources precisely according to the IEEE rules stated above, using the user's preferred language.