# ALGO-X – Interactive Algorithm Learning, Problem-Solving and Analysis Toolkit

## 1. Overview

ALGO-X is a command-line Python application designed to help students learn, practice, execute, and analyze fundamental algorithms.

The project brings multiple algorithmic techniques into a single terminal-based toolkit. Users can solve algorithms, learn their concepts, practice through randomly generated questions, measure execution time, and maintain a history of operations.

The project is designed around fundamental computer problem-solving concepts and Python programming techniques taught in the course.

---

## 2. Objectives

The main objectives of ALGO-X are:

* To implement fundamental algorithms using Python.
* To provide a centralized platform for solving algorithmic problems.
* To explain algorithms using descriptions, examples, pseudocode, and complexity analysis.
* To provide an interactive practice environment.
* To measure algorithm execution time.
* To demonstrate algorithm efficiency and analysis.
* To apply Python concepts such as functions, loops, lists, tuples, sets, and dictionaries.
* To demonstrate modular programming and software organization.
* To provide input validation and error handling.
* To maintain and store user operation history.

---

## 3. Features

### Algorithm Solver

Provides implementations of algorithms from the course syllabus, including:

* Exchange of values
* Counting
* Summation
* Factorial
* Fibonacci sequence
* Number reversal
* Character-to-number conversion
* Square root
* Smallest divisor
* GCD
* Prime number generation
* Prime factorization
* Pseudo-random number generation
* Large power computation
* Array operations
* Array partitioning
* Kth smallest element
* Python list, tuple, set, and dictionary operations
* Number base conversions

### Learning Module

Provides learning material for selected algorithms, including:

* Algorithm descriptions
* Examples
* Pseudocode
* Time complexity
* Space complexity

### Practice Mode

Generates random algorithmic questions and evaluates the user's answers.

### Performance Analysis

Measures execution time for selected algorithms using Python's timing facilities.

### History and Storage

Records successful algorithm operations and allows users to:

* View history
* Save history
* Load history
* Clear history

### Input Validation

Handles invalid numerical input and prevents common input errors through reusable validation functions.

---

## 4. Technology Stack

* **Programming Language:** Python
* **Interface:** Command Line / Terminal
* **Version Control:** Git and GitHub
* **Storage:** Text file
* **Testing:** Python unittest
* **Documentation:** Markdown and PDF

The project primarily uses Python's standard library and does not require external Python packages.

---

## 5. Project Structure

```text
ALGO-X/
│
├── main.py
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
│
├── Algorithms/
│   ├── __init__.py
│   ├── fundamental.py
│   ├── factoring.py
│   ├── arrays.py
│   ├── collections.py
│   └── conversions.py
│
├── Learning/
│   ├── __init__.py
│   └── explanations.py
│
├── Practice/
│   ├── __init__.py
│   └── questions.py
│
├── Utilities/
│   ├── __init__.py
│   ├── validation.py
│   ├── performance.py
│   ├── history.py
│   └── file_manager.py
│
├── tests/
│   ├── test_fundamental.py
│   ├── test_factoring.py
│   ├── test_arrays.py
│   ├── test_conversions.py
│   └── test_collections.py
│
└── data/
    └── history.txt
```

---

## 6. Installation and Execution

### Requirements

Python 3.x must be installed on the system.

Check the Python installation using:

```bash
python --version
```

### Running the Project

Clone or download the project and navigate to the project directory.

Run:

```bash
python main.py
```

The application will display the ALGO-X main menu in the terminal.

No GUI setup is required.

---

## 7. Testing

ALGO-X uses Python's built-in `unittest` framework.

To run all tests:

```bash
python -m unittest discover -s tests
```

The test suite verifies important functions from the algorithm modules, including fundamental algorithms, factoring methods, array techniques, conversions, and Python collections.

---

## 8. Error Handling

The project includes reusable input validation functions for:

* Integers
* Positive integers
* Non-negative integers
* Floating-point values
* Lists of integers

Invalid input is detected and the user is asked to provide valid input instead of terminating the application unexpectedly.

---

## 9. Performance Analysis

ALGO-X includes a performance analysis module that measures the execution time of selected algorithms.

The project uses `time.perf_counter()` to obtain high-resolution execution timing.

This allows users to observe how execution time changes for different inputs.

---

## 10. History and File Storage

The application maintains an in-memory history of successful operations.

Users can save this history to:

```text
data/history.txt
```

Previously saved history can also be loaded back into the application.

---

## 11. Design Approach

ALGO-X follows a modular architecture.

Different responsibilities are separated into different Python modules:

* Algorithm implementation
* Learning content
* Practice questions
* Input validation
* Performance measurement
* History management
* File management

The main program acts as the controller that connects these modules and provides the command-line interface.

---

## 12. Scope

The project focuses on fundamental algorithms and Python programming concepts covered in the course.

The current implementation is intentionally command-line based and does not include:

* Graphical user interfaces
* Web applications
* Machine learning systems
* AI chatbot functionality
* Relational database systems

---

## 13. Future Enhancements

Possible future improvements include:

* Additional algorithms and learning material
* More practice question categories
* Difficulty levels
* More detailed performance comparisons
* Additional file formats for history
* Expanded automated testing
* Interactive algorithm step visualization in the terminal
* Database-based persistent storage
* Graphical or web-based versions

---

## 14. Author

**Project:** ALGO-X
**Course:** Computer Problem Solving / Python Programming
**Platform:** Command Line / Terminal
