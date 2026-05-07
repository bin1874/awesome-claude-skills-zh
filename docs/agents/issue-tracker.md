# Issue Tracker

This repo uses **GitHub Issues** for issue tracking.

## Location

Issues live at: https://github.com/LessUp/awesome-claude-skills-zh/issues

## Workflow

Skills interact with issues using the `gh` CLI:

- **Create issue**: `gh issue create`
- **List issues**: `gh issue list`
- **View issue**: `gh issue view <number>`
- **Close issue**: `gh issue close <number>`
- **Add labels**: `gh label create` / `gh issue edit --add-label`

## Prerequisites

Ensure `gh` CLI is installed and authenticated:

```bash
gh auth status
```

If not authenticated, run:

```bash
gh auth login
```
