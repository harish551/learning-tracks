# GitHub Copilot Instructions

This repository is a personal learning space for algorithms and systems concepts, with examples in **Python**, **Go**, and **Rust**.

## What to know

- Primary folders:
  - `dsa/` — data structures and algorithms across Python, Go, and sometimes Rust.
  - `concurrency/` — Go concurrency examples.
  - `rust/` — Rust language fundamentals and small Cargo projects.
  - `system-design/` — higher-level and low-level system-design examples, including Python rate limiter implementations and Go service samples.
- Most code is sample-driven rather than production-ready.
- Preserve the existing folder layout and language-specific file locations unless the user explicitly asks to reorganize.
- Use the repository README as the canonical overview of repo purpose and structure.

## How to run things

- Python examples:
  - `python <path/to/file.py>`
  - Example: `python dsa/graphs/graph.py`
- Go examples:
  - `go run <path/to/file.go>`
  - Example: `go run dsa/linked-lists/go/linked_list.go`
- Rust examples:
  - `cargo run` inside Cargo project directories
  - Example: `cd rust/hello_cargo && cargo run`
  - Bare Rust source can be compiled with `rustc` when no Cargo project exists.
- Python tests:
  - Run rate limiter tests with `python -m pytest system-design/low-level/python/rate-limiters`

## Editing guidance

- Keep changes small and focused on the requested topic.
- Prefer idiomatic code for the target language.
- Avoid adding frameworks, build systems or extra dependencies unless the user requests them.
- If a change touches multiple folders, confirm the intended scope with the user.
- When writing new examples, mirror the repository's existing style: educational, self-contained, and easy to run.

## When to ask the user

- If a task would benefit from a project-level test harness or repo-wide refactor.
- If the requested change would affect repository structure beyond a single topic.
- If there is ambiguity about which language or subfolder should own a new implementation.

## Example prompts

- "Add a Python implementation of binary search under `dsa/patterns/binary-search`."
- "Refactor the Go worker pool example for clarity and concurrency safety."
- "Add unit tests for the rate limiter implementations in `system-design/low-level/python/rate-limiters`."
- "Create a new Rust DSA example for binary trees under `rust/`."
