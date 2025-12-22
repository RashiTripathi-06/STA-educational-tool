# EduSTA – An Educational Static Timing Analysis Tool

EduSTA is a Python-based educational project that demonstrates the fundamentals of **Static Timing Analysis (STA)** through clear, programmatic implementation.

Built alongside coursework in Digital Design, the project moves beyond formula-based examples to provide an implementation-level understanding of STA, inspired by how real timing analysis tools reason about circuits.

## What is Static Timing Analysis (STA)?

Static Timing Analysis is a method used in synchronous digital circuits to verify whether data propagates through combinational logic within the **timing constraints imposed by the clock**.

Instead of simulating specific input patterns, STA analyzes timing paths statically and checks conditions such as:
- Whether data arrives at the capture flip-flop before the required clock edge (**setup condition**)
- Whether data remains stable long enough after the clock edge (**hold condition**)
- Which data path limits the maximum achievable clock frequency (**critical path**)

STA is a core technique used in VLSI design to ensure timing correctness before fabrication.

## Why this project?

In many classroom settings, STA is introduced mainly through equations and isolated examples.  
However, real STA tools work by:
- Enumerating **multiple timing paths**
- Identifying the **worst-case (critical) path**
- Modeling circuits as **graphs**, not just single linear paths

This project was created to bridge that gap by translating STA concepts from equations into clear, executable Python code.

## Core Concepts Covered

- Timing paths between launch and capture flip-flops  
- Combinational delay accumulation  
- Setup and hold slack calculation  
- Single-path STA for conceptual clarity  
- Multi-path STA using graph traversal  
- Critical path identification using Depth First Search (DFS)  

## Project Structure
STA-educational-tool/
│
├── sta_engine.py              # Core STA logic
├── circuit_models.py          # Example circuit (multi-path)
│
├── examples/
│   ├── single_path_demo.py    # Conceptual single-path STA
│   └── multi_path_demo.py     # Multi-path STA + critical path
│
└── README.md

### File Overview
- **sta_engine.py**  
  Contains the core STA logic, including combinational delay computation, setup and hold slack calculation, timing graph construction, and path enumeration using DFS.
  
- **circuit_models.py**  
  Defines example circuit descriptions (topology and delays), which act as simplified input netlists for the STA engine.

- **examples/single_path_demo.py**  
  Demonstrates single-path STA to build intuition for timing equations and slack computation.
  
- **examples/multi_path_demo.py**  
  Demonstrates multi-path STA by enumerating multiple timing paths, computing slack for each path, and identifying the critical path based on worst setup slack.

## Project Status
- [x] Single-path static timing analysis  
- [x] Setup and hold timing verification  
- [x] Slack computation  
- [x] Multi-path timing analysis using DFS  
- [x] Critical path identification  

The project emphasizes **conceptual clarity and correctness** rather than full industrial completeness.

## Learning Outcomes
Working on this project helped reinforce:
- How Static Timing Analysis works beyond formula-based examples  
- How timing paths between flip-flops can be represented as graphs  
- How basic graph traversal algorithms apply to timing analysis  
- How STA tools conceptually identify critical timing paths  

## Intended Use
This project was built as a personal learning exercise alongside coursework in Digital Design and VLSI.  
It is intended as an **educational reference** for students exploring Static Timing Analysis at an introductory level.

> *EduSTA focuses on understanding how STA works internally, not on replicating full-scale commercial timing tools.*


