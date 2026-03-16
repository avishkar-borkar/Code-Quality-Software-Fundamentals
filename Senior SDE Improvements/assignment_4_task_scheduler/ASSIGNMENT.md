# Assignment 4: Task Scheduler with Dependencies (Abstraction & Data Structures)

## Difficulty: ★★★★☆
## Focus: Abstraction, Encapsulation, Graph-Based Dependencies, Proper Class Design

---

## Overview

You're given a working task scheduler that executes tasks by priority. It works, but tasks are stored as dicts, and there's no concept of dependencies. Your job: refactor tasks into proper classes and add dependency management (task B can't run until task A completes).

---

## Files

| File | What To Do |
|------|-----------|
| `scheduler.py` | Starter code. **Refactor this** — keep the `TaskScheduler` class name but rework internals. |
| `tasks.py` | **Create this file.** The `Task` class. |
| `test_scheduler.py` | Test suite. **Do NOT modify.** All tests must pass. |

---

## Part A: Task as a Proper Class

### The Problem
Tasks are dicts: `{"name": ..., "priority": ..., "action": ..., "status": ...}`. No behavior, no validation, no encapsulation.

### What You Need To Build

**`tasks.py` — Task Class**

- `Task(name, priority, action)` — a task with a name, priority (int, lower = more important), and action (callable)
- `task.status` — `"pending"`, `"completed"`, or `"cancelled"`
- `task.execute()` — runs the action, sets status to completed. Raises exception if not pending.
- `task.cancel()` — sets status to cancelled
- Tasks must be **comparable by priority** (support `<` operator) — needed for heap operations
- A completed task cannot be executed again (raise exception)
- A cancelled task cannot be executed (raise exception)

**Refactored `scheduler.py`**

- `add_task(task)` — takes a `Task` object (not name/priority/action separately)
- `execute_next()` → task name or None
- `execute_all()` → list of task names executed
- `cancel_task(name)` → True/False
- `get_task_status(name)` → status string or None
- `get_pending_tasks()` → list of names in priority order

---

## Part B: Task Dependencies

### The Problem
Real task schedulers have dependencies: "don't deploy until tests pass", "don't send email until data is processed". Currently there's no way to express this.

### What You Need To Build

Add these methods to `TaskScheduler`:

- `add_dependency(task_name, depends_on_name)` → True/False
  - Task `task_name` will NOT execute until `depends_on_name` is completed (or cancelled)
  - Returns False if either task doesn't exist
  - **Returns False if adding this dependency would create a circular dependency**

- `get_dependencies(task_name)` → list of dependency task names (empty list if none)

- `execute_next()` — Updated behavior:
  - A task is **blocked** if any of its dependencies are still pending (not completed/cancelled)
  - Blocked tasks are **skipped** in the queue — the scheduler picks the next unblocked task
  - Once a dependency completes or is cancelled, dependent tasks become unblocked

- `execute_all()` — executes all tasks respecting both priority AND dependencies

### Circular Dependency Detection
- If adding A→B and B→A already exists, reject it
- If adding A→C and B→A, C→B already exist (A→B→C→A), reject it
- This requires checking for cycles in a directed graph

---

## Design Decisions You Need to Make

- **How to represent the dependency graph?** Adjacency list? Set of edges? Think about what queries you need (check if blocked, detect cycles).
- **How does execute_next() handle blocked tasks?** You can't just pop from the heap blindly anymore. What's the strategy?
- **Where does dependency logic live?** In the Task class? In the Scheduler? (Hint: tasks shouldn't know about other tasks)
- **How to detect cycles efficiently?** DFS? BFS? Think about when to check — on every `add_dependency` call.

---

## Hints

1. For the dependency graph, a dict of `{task_name: set(dependency_names)}` works well.
2. For cycle detection, a DFS from the target node checking if you can reach the source is sufficient.
3. For `execute_next()` with dependencies: you may need to look past the top of the heap. Consider popping blocked tasks and re-inserting them, or iterating the sorted queue.
4. A task is "ready" when: status is pending AND all dependencies are completed or cancelled.

---

## Run Tests

```bash
cd assignment_4_task_scheduler
pytest test_scheduler.py -v
```

---

## Evaluation Criteria

| Criteria | What I'm Looking For |
|----------|---------------------|
| **Encapsulation** | Task manages its own state transitions — scheduler doesn't poke at internals |
| **Abstraction** | Dependency graph is cleanly separated from priority queue logic |
| **Data Structure Choice** | Did you pick the right structures for the dependency graph and ready-queue? |
| **Cycle Detection** | Actually works for chains, not just direct A↔B cycles |
| **Edge Cases** | Cancel unblocks dependents, empty scheduler, duplicate names |
| **No Over-Engineering** | You didn't build a full DAG executor when a simple check suffices |

---

## Get Started

1. Read `scheduler.py` — understand the current heap-based approach
2. Read `test_scheduler.py` — understand expected interface
3. Create `tasks.py` with the `Task` class — get Part A tests passing
4. Refactor `scheduler.py` to use `Task` objects
5. Add dependency methods — `add_dependency`, `get_dependencies`
6. Update `execute_next` to respect dependencies
7. Run tests: `pytest test_scheduler.py -v`

Good luck.
