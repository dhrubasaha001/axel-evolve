---
name: python
description: Enforces strict Python 3.12+ production standards, type safety, explicit error handling, and modern toolchains (uv, ruff, pytest). Activating whenever Python files are created, refactored, or reviewed.
license: MIT
metadata:
  author: AI-Collaborator
  version: "1.0.0"
---

# Python Production Engineering Guidelines

You are an expert Python developer and automation agent. When writing, refactored, or reviewing Python code in this repository, you must strictly adhere to the following rules, toolchains, and design patterns.

## 1. Toolchain & Environment Defaults
* **Dependency Management**: Use `uv` for all package management, virtual environments, and script executions. Never invoke raw `pip`.
* **Linting & Formatting**: Use `ruff check --fix` and `ruff format` to ensure styling conforms to Black/PEP 8 standards.
* **Type Checking**: Use `mypy --strict` or `pyright` to validate structural type safety.
* **Testing**: Use `pytest` for all unit and integration testing.

## 2. Code Style & Architecture

### Type Hinting
* **Strict Typing**: All function signatures, including internal helpers, must have explicit argument and return types.
* **Modern Syntax**: Use modern standard collections for typing (e.g., `list[str]`, `dict[str, int]`) instead of importing from the deprecated `typing` module.
* **Optional Values**: Prefer `str | None` over `Optional[str]`.

### Error Handling
* **Explicit Exceptions**: Never use bare `except:`. Always catch specific exceptions (e.g., `except ValueError:`).
* **Custom Exceptions**: Create domain-specific exception classes deriving from a base `AppError` for distinct internal failure states.
* **No Silent Failures**: Never use `pass` in an exception block unless the intentional silence is explicitly documented with a comment explaining *why*.

### Async & Concurrency
* **Structured Concurrency**: Use `asyncio.TaskGroup` for managing multiple concurrent tasks safely.
* **Non-blocking I/O**: Ensure any I/O operation inside an `async def` function uses an asynchronous library or is offloaded to a thread pool via `asyncio.to_thread()`.

## 3. Testing & Documentation Workflow

### Automated Testing
* **Test Location**: Place all tests in the `tests/` directory mirroring the source tree layout.
* **Fixtures**: Use clean `pytest.fixture` definitions with explicit type hints for setup and teardown.
* **Coverage**: Aim for 90%+ statement coverage on all new logical structures.

### Documentation
* **Docstrings**: Write docstrings using the **Google Style** format for all public modules, classes, and functions.
* **Docstring Requirements**: Must include a clear single-line summary, `Args:`, `Returns:`, and `Raises:` sections if exceptions are thrown.

## 4. Verification Checklists

Before declaring a task complete, you must internally verify:
1. `ruff check .` returns 0 warnings/errors.
2. `mypy .` reports clear type compliance.
3. `pytest` executes successfully without regressions.
