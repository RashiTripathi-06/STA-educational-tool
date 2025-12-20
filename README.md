# EduSTA- An Educational Static Timing Analysis Tool
EduSTA is a Python-based educational project that demonstrates the fundamentals of **Static Timing Analysis (STA)** through clear,programmatic implementation.

Built alongside coursework in Digital Design, the project moves beyond formula-based examples to provide an implementation-level understandingof STA, inspired by the internal workings of real timing analysis tools.

## What is Static Timing Analysis (STA)?
Static Timing Analysis is a method used in synchronous digital circuits to check whether data propagates through logic within the **timing constraints set by the clock.**
So,Instead of simulating input patterns, STA evaluates timing paths statically and verifies conditions such as:
- Whether data arrives before the required clock edge (setup condition)
- Whether data remains stable long enough after a clock edge (hold condition)
- Which data path limits the maximum clock frequency (critical path)

STA is widely used in VLSI design to ensure timing correctness before fabrication.

## Why this project?
Most STA learning in classrooms focused on equations and constraints.
However, real STA tools work by:
- Enumerating **multiple timing paths**
- Finding the **worst-case (critical) path**
- Analyzing circuits as **graphs**, not isolated paths
This project was created to bridge that gap by translating STA concepts
from formulas into clear, programmatic implementations using Python.

## Core Concepts Covered
- Timing paths between launch and capture flip-flops
- Combinational delay and slack calculation
- Setup and hold timing analysis
- Single-path STA for conceptual clarity
- Multi-path timing analysis using graph traversal
- Critical path identification using Depth First Search (DFS)

## Project Structure
STA-educational-tool/
├── src/
│   ├── sta_engine.py        # Core STA equations and single-path analysis
│   ├── multi_path_sta.py   # Multi-path timing analysis and critical path detection
│   └── circuit_models.py   # User-defined circuit descriptions
└── README.md

## Project Status
- [x] Single-path static timing analysis
- [x] Setup and hold timing verification
- [x] Slack computation
- [x] Multi-path timing analysis (educational)
- [x] Critical path identification

The project currently emphasizes conceptual clarity and correctness.
Additional refinements may be explored as learning progresses.

## Learning Outcomes

Working on this project helped reinforce:
- How Static Timing Analysis works beyond formula-based examples
- How timing paths between flip-flops can be represented programmatically
- How basic graph traversal ideas apply to timing analysis in digital circuits

## Intended Use
This project was built as a personal learning exercise alongside coursework in Digital Design and VLSI. It may be useful as a reference for others exploring STA concepts at an introductory level.
