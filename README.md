# 🧠 Learning Tracks

A personal repository for hands-on learning — covering **Data Structures & Algorithms** and **Rust** fundamentals, implemented across multiple languages.

---

## 📁 Repository Structure

```
Learning-Tracks/
├── dsa/                        # Data Structures & Algorithms
│   ├── linked-lists/
│   │   ├── go/                 # Linked list in Go
│   │   └── python/             # Linked list in Python
│   └── graphs/
│       └── graph.py            # Graph with DFS & BFS in Python
│
└── rust/                       # Rust Language Fundamentals
    ├── hello_world/            # Hello World (no Cargo)
    ├── hello_cargo/            # Hello World with Cargo
    ├── data_types/             # Scalar & compound types
    └── guessing_game/          # Interactive guessing game (uses `rand`)
```

---

## 📚 Topics Covered

### DSA

| Topic | Language(s) | Key Concepts |
|---|---|---|
| **Linked Lists** | Go, Python | Append, prepend, pop, remove, reverse, size tracking |
| **Graphs** | Python | Adjacency list representation, DFS (recursive), BFS (iterative) |

### Rust

| Project | Description |
|---|---|
| **hello_world** | Bare-bones `rustc`-compiled Hello World |
| **hello_cargo** | Hello World using the Cargo build system |
| **data_types** | Scalar types (`u32`, `f32`, `bool`, `char`), arithmetic operators, tuples, and arrays |
| **guessing_game** | CLI number-guessing game — covers `rand`, `io::stdin`, `match`, `loop`, and error handling |

---

## 🚀 Getting Started

### Prerequisites

- **Go** ≥ 1.20 — [Install Go](https://go.dev/doc/install)
- **Python** ≥ 3.10 — [Install Python](https://www.python.org/downloads/)
- **Rust** (via `rustup`) — [Install Rust](https://www.rust-lang.org/tools/install)

### Running the Code

#### DSA — Python

```bash
python dsa/linked-lists/python/linked_list.py
python dsa/graphs/graph.py
```

#### DSA — Go

```bash
go run dsa/linked-lists/go/linked_list.go
```

#### Rust

```bash
# Hello World (no Cargo)
rustc rust/hello_world/main.rs -o hello && ./hello

# Cargo projects
cd rust/hello_cargo && cargo run
cd rust/data_types && cargo run
cd rust/guessing_game && cargo run
```

---

## 🛣️ Roadmap

- [ ] More DSA topics (trees, heaps, sorting, dynamic programming)
- [ ] Rust implementations of DSA problems
- [ ] Add unit tests across all languages

---

## 📄 License

This project is for personal learning purposes.
