# ParseFlow Interpreter

## Overview
ParseFlow is a custom interpreter built to parse and execute a programming language with constructs like variables, functions, loops, conditionals, and arithmetic expressions. The interpreter is implemented in Python with a lexer, parser, interpreter, and runtime environment.

This project consists of the following files:
- `parseflow.py`: Core file containing the lexer, parser, interpreter, runtime handling, and error reporting.
- `shell.py`: A simple shell interface to interact with the interpreter.
- `strings_with_arrows.py`: Utility for displaying error messages with precise location highlighting.
- `grammar.txt`: Defines the grammar of the language being interpreted.

---

## Getting Started
### Requirements
- Python 3.x

### Installation
1. Clone this repository.
2. Install required packages if any (though this project uses only Python's standard libraries).

### Usage
Run the interpreter using the `shell.py` file:
```bash
python3 shell.py
```

Use the `exit` command to terminate the interpreter session.

---

## File Descriptions
### `parseflow.py`
This file contains the core interpreter code which can be broken down into several components:

- **Imports and Constants:**
  - Imports `strings_with_arrows` for error visualization.
  - Defines constants for handling digits, letters, and file paths.

---

## Components

### Errors
- `Error`: Base class for all errors. Displays error name, details, and highlighted position in code.
- `IllegalCharError`: Raised for unknown characters.
- `ExpectedCharError`: Raised when a specific character is expected but not found.
- `InvalidSyntaxError`: Raised when syntax rules are violated.
- `RTError`: Raised during runtime errors, such as division by zero.

#### Usage of `strings_with_arrows.py`
The `strings_with_arrows` module is used by `Error` classes to generate visual error messages with highlighted portions of code where the error occurred.

---

### Position
- `Position`: Tracks the position of characters within the code, including line, column, and index numbers.
- Provides methods to advance through the code and create copies for error reporting.

---

### Tokens
- `Token`: Represents individual units of code such as integers, identifiers, keywords, etc.
- Contains methods for comparing tokens and representing them as strings.
- The constants `TT_INT`, `TT_FLOAT`, etc., define all the possible token types.

---

### Lexer
- `Lexer`: Responsible for breaking down the raw input text into tokens.
- Handles comments, numbers, strings, identifiers, keywords, and various operators.
- Implements methods for building tokens, including `make_number()`, `make_string()`, `make_identifier()`, etc.
- Uses `Token` objects to generate a list of tokens that are then parsed.

---

### Nodes
The `Node` classes are used to build an Abstract Syntax Tree (AST) from tokens. They include:
- `NumberNode`, `StringNode`, `ListNode` for handling literals and lists.
- `VarAccessNode`, `VarAssignNode` for variable access and assignment.
- `BinOpNode`, `UnaryOpNode` for binary and unary operations.
- `IfNode`, `ForNode`, `WhileNode` for control structures.
- `FuncDefNode`, `CallNode` for function definitions and calls.
- `ReturnNode`, `ContinueNode`, `BreakNode` for flow control.

---

### Parser
- `Parser`: Takes tokens and produces an AST.
- Uses the classes from the `Nodes` section to build the AST based on the grammar defined in `grammar.txt`.
- Handles complex constructs such as function definitions, loops, conditionals, and expressions.
- Uses `ParseResult` to store the result of parsing and handle errors.

---

### Interpreter
- `Interpreter`: Walks through the AST and executes each node.
- Uses `visit_*` methods to process nodes of various types.
- Handles built-in functions like `PRINT`, `INPUT`, etc.
- Supports mathematical operations, boolean logic, string manipulation, and function calls.

---

### Runtime
- `RTResult`: Manages results and errors during interpretation.
- `Value`: Base class for all runtime values, including `Number`, `String`, `List`, and `Function`.
- `Context`: Maintains execution state for functions and tracks parent contexts.
- `SymbolTable`: Stores variable definitions and allows for nested scopes.

---

### Built-in Functions
- `PRINT`, `INPUT`, `LEN`, `APPEND`, `POP`, etc.
- Defined using the `BuiltInFunction` class.

---

### Intermediate Code Generation
- The interpreter generates intermediate code for every parsed program and saves it to `intermediate_code.txt`.
- The function `write_intermediate_code()` in `parseflow.py` handles this.
- `shell.py` notifies users when intermediate code is generated.

---

## Grammar Definition (`grammar.txt`)
This file defines the grammar rules used by the parser. It supports constructs like:
- Statements (e.g., variable assignment, loops, functions).
- Expressions (e.g., arithmetic, boolean logic).
- Conditional blocks (IF-ELIF-ELSE).
- Looping constructs (FOR, WHILE).
- Function definitions and calls.

---

## Future Improvements
- Adding more built-in functions.
- Enhancing the syntax and supporting additional data types.
- Improving error handling and reporting.

---