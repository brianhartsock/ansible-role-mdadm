# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ansible role (`brianhartsock.mdadm`) that installs mdadm and mounts RAID arrays. Supports Ubuntu Jammy (22.04) and Noble (24.04).

## Commands

```bash
# Install dependencies
uv sync

# Linting
uv run ansible-lint
uv run yamllint .
uv run flake8

# Integration tests (requires Docker)
uv run molecule test
```

Dependencies are managed with uv (`pyproject.toml` + `uv.lock`).

## Architecture

Standard Ansible role structure with two tasks in `tasks/main.yml`:
1. Install mdadm via apt
2. Mount RAID arrays from the `mdadm_mounts` list variable (defined in `defaults/main.yml`, defaults to `[]`)

Testing uses Molecule with Docker driver and pytest-testinfra as verifier. The single test scenario in `molecule/default/` runs against ubuntu:22.04 and ubuntu:24.04 containers in privileged mode. Tests are in `molecule/default/tests/test_default.py`.

## CI

GitHub Actions runs two jobs on push to master and PRs: lint (ansible-lint, yamllint, flake8) and molecule test (runs after lint passes). Releases publish to Ansible Galaxy.

## Development Workflow

Follow this workflow for all code changes.

```
Code → Document → Verify → Code Review
  ^                              |
  └──── fix issues ──────────────┘
```

### 1. Code

Make the implementation changes. Use FQCNs, name all tasks, and follow the patterns in existing task files.

### 2. Document

Update README.md and CLAUDE.md to reflect any changes to variables, platforms, commands, or architecture. If the ansible plugin is installed, use the `documentator` agent.

### 3. Verify

Run linters (yamllint, ansible-lint, flake8), pre-commit hooks, and molecule tests. All checks must pass before proceeding. If the ansible plugin is installed, use the `verifier` agent.

### 4. Code Review

Review the changes for Ansible best practices, idempotency, security, cross-platform correctness, and test coverage. If the ansible plugin is installed, use the `code-reviewer` agent.

### 5. Iterate

If verification or code review flags issues, fix them and repeat from step 2. Continue until all checks pass and the review is clean.
