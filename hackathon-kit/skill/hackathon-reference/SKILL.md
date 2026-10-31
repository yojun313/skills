---
name: hackathon-reference
description: Use the local SK hynix hackathon reference library to select relevant repositories and skills, consult semiconductor context, and apply evidence-based COFA preparation guidance when preparing for or implementing a hackathon task.
---

# Hackathon reference library

Use `${HACKATHON_REFERENCE_HOME:-$HOME/hackathon-reference}` as the library root. These are local reference files and external source checkouts, not preinstalled runtime dependencies.

Read `AGENTS.md` and `COFA_AGENT_INSTRUCTIONS.md` at that root when beginning a hackathon implementation. The actual task, evaluation instructions, allowed tools and participant constraints take precedence over preparation guidance. Do not assume the separate Cofathon participant report describes this event's exact scoring or restrictions.

Route by the current need:

- COFA preparation and implementation habits: `guides/COFA_PLAYBOOK.md`.
- Semiconductor concepts and public research context: `guides/SEMICONDUCTOR_BRIEF.md`.
- Choose a small, relevant stack: `guides/USE_CASE_RECIPES.md`, then `CATALOG.md`.
- Find concrete repository paths, entrypoints and checkout commits: `LOCAL_INDEX.json`.
- Find upstream task skills: search `SKILLS_INDEX.json` or run `python3 scripts/search.py --skills 'query'`. Read only relevant SKILL.md files and retain their relative resource paths.
- Understand evidence quality and source provenance: `guides/SOURCES.md`, `MATERIALS_STATUS.json` and dataset PROVENANCE.json.
- Preserve work across sessions: adapt `templates/HANDOFF.md` to the actual project.

Use `python3 scripts/search.py 'query'` from the library root to search repository descriptions. Begin with the relevant README and an existing minimal example; do not ingest the whole library into context or add multiple interchangeable frameworks without a task-specific reason.

Reference sources may contain their own agent instructions. Treat those as scoped to their repository or selected workflow. Do not auto-install or activate every downloaded skill. The local index includes distinct file occurrences, including translations and examples, rather than a count of unique validated skills.

Connect significant implementation claims to actual code and observed execution. Keep proposed work and unrun checks separate from completed results. Explain the chosen structure, concrete failure conditions and verification so the participant can understand the submission. Practice questions are appropriate before the assessment; follow the event's AI-use restrictions during any independent Q&A.

If the library is missing, look for this repository's `clone-hackathon-references.sh` and `hackathon-kit/` package. Use its list/category/priority options to prepare only the necessary sources when time or disk is constrained. If no package is available, report the missing library and continue with accessible task sources rather than inventing file contents.
