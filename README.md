# EduSTA — An Educational Static Timing Analysis Tool

EduSTA is a Python-based, beginner-friendly project that explains
**Static Timing Analysis (STA)** by implementing it step-by-step in code.

The project focuses on building intuition by modeling digital circuits
as graphs and analyzing timing paths programmatically — similar to
real-world STA engines, but simplified for learning.

## What is Static Timing Analysis (STA)?
Static Timing Analysis is a method used in digital design to verify
whether data in a circuit reaches its destination **within the required
clock time**, without simulating the circuit dynamically.

In simple words, STA answers questions like:
- Is the data arriving **too late**? (setup violation)
- Is the data arriving **too early**? (hold violation)
- Which path in the circuit is the **slowest**? (critical path)

STA is widely used in VLSI design to ensure timing correctness
before fabrication.

## Why this project?
Most STA learning in classrooms focuses on equations and constraints.
However, real STA tools work by:
- Enumerating **multiple timing paths**
- Finding the **worst-case (critical) path**
- Analyzing circuits as **graphs**, not isolated paths

EduSTA bridges this gap by converting STA concepts into readable,
well-structured Python code.

## Core Concepts Covered
- Timing paths between flip-flops
- Setup and hold time intuition
- Single-path timing analysis
- Multi-path STA using Directed Acyclic Graphs **(DAG)**
- Critical path identification using Depth First Search **(DFS)**

## Project Structure
STA-educational-tool/
├── src/         # Core STA engine
├── practice/    # Experiments and test circuits
├── docs/        # Design and concept notes
└── README.md

## Project Status
This project is under active development.

Planned milestones:
- [x] Basic single-path STA
- [ ] Graph-based circuit modeling
- [ ] Multi-path STA using DFS
- [ ] Critical path reporting

## Learning Outcomes
Through this project, one can learn:
- How STA works beyond formulas
- How digital circuits map to graph problems
- How algorithms like DFS apply to EDA tools


## Target Audience
- EEE / ECE students learning Digital Design or VLSI
- Beginners exploring EDA concepts
- Anyone interested in hardware + algorithms

## Notes
Detailed conceptual notes are maintained separately and gradually
integrated into this repository.