# Triage Labels

This repo uses the default triage label vocabulary for the `triage` skill.

## Label Mapping

| Role | Label | Description |
|------|-------|-------------|
| `needs-triage` | `needs-triage` | Maintainer needs to evaluate |
| `needs-info` | `needs-info` | Waiting on reporter for more details |
| `ready-for-agent` | `ready-for-agent` | Fully specified, AFK-ready |
| `ready-for-human` | `ready-for-human` | Needs human implementation |
| `wontfix` | `wontfix` | Will not be actioned |

## Creating Labels

If these labels don't exist in the repo yet, create them:

```bash
gh label create "needs-triage" --description "Needs maintainer evaluation" --color "FBCA04"
gh label create "needs-info" --description "Waiting on reporter for more details" --color "D4C5F9"
gh label create "ready-for-agent" --description "Fully specified, ready for AFK agent" --color "0E8A16"
gh label create "ready-for-human" --description "Ready for human implementation" --color "1D76DB"
gh label create "wontfix" --description "Will not be actioned" --color "B60205"
```
