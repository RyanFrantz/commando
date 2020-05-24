# Use Markdown Architectural Decision Records

## Context and Problem Statement

Decision-making is as critical as the end result of those decisions.

We want to record architectural decisions made in this project.
Which format and structure should these records follow?

## Considered Options

* [MADR](https://adr.github.io/madr/) 2.1.2 – The Markdown Architectural Decision Records
* [Michael Nygard's template](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) – The first incarnation of the term "ADR"
* [Sustainable Architectural Decisions](https://www.infoq.com/articles/sustainable-architectural-design-decisions) – The Y-Statements
* Other templates listed at <https://github.com/joelparkerhenderson/architecture_decision_record>
* Google Docs
* Formless – No conventions for file format and structure

## Decision Outcome

Chosen option: "MADR 2.1.2", because

* Implicit assumptions should be made explicit.
  Design documentation is important to enable people understanding the decisions later on.
  See also [A rational design process: How and why to fake it](https://doi.org/10.1109/TSE.1986.6312940).
* The MADR format is lean and fits our development style.
* The MADR structure is comprehensible and facilitates usage & maintenance.
* The MADR project is vivid.
* Version 2.1.2 is the latest one available when starting to document ADRs.

### Positive Consequences

* We have a consistent process for generating and maintaining a history of our
  decision-making.
* We have a single format for capturing the minimum information necessary to
  provide context on decisions.

### Negative Consequences

* There is some ramp-up time required to internalize the format and use of ADRs.

## Pros and Cons of the Options

Rather than exhaustively describe each of the ADR options, suffice it to say
that they range broadly in scope from very little detail to extremely specific
(or domain-specific). The MADR option seems like a good balance among them all.
Further, we can tailor it to meet our needs.

We've previously been using Google Docs to capture some of this content but
finding documents in Google Drive can be challenging unless one already knows
what to search for.

A benefit of using ADRs is that they can reside within Github projects, keeping
decision-making context close to the relevant work.
