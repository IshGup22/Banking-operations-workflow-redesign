# Stakeholder workshop notes — simulated discovery session
**Status:** Fictional personas for a portfolio case study; not actual client meetings

| Persona | Reported need | BA clarification | Decision captured |
|---|---|---|---|
| Finance lead | "Reports don't reconcile fast enough" | Is the issue timing, completeness, or mismatch detection? | Keep every input record and provide totals |
| Operations lead | "Too many manual checks" | Which entries are truly exceptions? | Separate clean matches from exceptions |
| Product Owner | "We need a practical first release" | What is the MVP scope? | CSV-based workflow; defer integration |
| Developer | "What makes an exception?" | Define priority and tolerance | $0.01 monetary tolerance; clear precedence |
| QA tester | "How will we know it works?" | Define observable acceptance | Link stories, criteria and UAT scenarios |

## Open questions
- Who owns final sign-off in an actual bank?
- Should aged-item threshold differ by product segment?
- What is the true manual handling-time baseline?
- How should duplicate detection work beyond a supplied marker?

All questions would require real stakeholder validation before implementation.
