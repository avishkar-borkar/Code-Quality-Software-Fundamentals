# Assignment 5: In-Memory Key-Value Store (Encapsulation, Observer Pattern & Separation of Concerns)

## Difficulty: ★★★★☆
## Focus: Encapsulation, Observer Pattern, Separation of Concerns, Composable API Design

---

## Overview

You're given a working KV store with TTL. It's functional but flat — everything in one class, no way to organize keys, no way to react to changes. Your job: add **namespaces** (logical isolation) and **event listeners** (observer pattern) while keeping the core clean.

---

## Files

| File | What To Do |
|------|-----------|
| `store.py` | Starter code. **Extend this.** Keep `KeyValueStore` but add namespaces + events. |
| `test_store.py` | Test suite. **Do NOT modify.** All tests must pass. |

---

## Part A: Core KV Store (Already Working)

The starter code handles set/get/delete/TTL. The Part A tests should already pass (or nearly pass) without changes. Make sure they do before moving on.

---

## Part B: Namespaces

### The Problem
All keys live in one flat space. In a real system you'd want logical separation: `users:alice`, `config:timeout`, `cache:homepage`. But prefix-based naming is fragile and leaks internals.

### What You Need To Build

- `store.create_namespace(name)` → returns a **namespace object** that has the same API as KeyValueStore (set, get, delete, exists, keys, clear, size)
- Keys in a namespace are **isolated** from the root store and from other namespaces
- Calling `create_namespace("data")` twice returns the **same namespace instance**
- `store.list_namespaces()` → returns list of namespace names
- TTL works within namespaces
- Namespace keys do NOT appear in `store.keys()`

### Design Decisions
- **How do you implement the namespace object?** Does it inherit from KeyValueStore? Compose one? Something else?
- **Where is data stored?** Does each namespace have its own dict, or does the root store prefix keys internally?
- **How do you share the TTL/expiry logic** without duplicating it?

---

## Part C: Event Listeners (Observer Pattern)

### The Problem
There's no way to react to changes. In real systems, you need hooks: invalidate a cache when a key changes, log when something expires, trigger a webhook on delete.

### What You Need To Build

- `store.on(event_type, handler)` — register a listener
  - `"set"` — fires on every set. Handler receives `(key, value)`
  - `"delete"` — fires on every successful delete. Handler receives `(key,)`. Does NOT fire if key doesn't exist.
  - `"expire"` — fires when a key is lazily expired (on access after TTL). Handler receives `(key,)`

- `store.off(event_type, handler)` — remove a specific listener

- **Namespace events bubble up** to the root store with a namespaced key:
  - Setting `"item"` in namespace `"cache"` fires a `"set"` event on the root store with key `"cache:item"`

### Design Decisions
- **Where does event dispatching live?** In KeyValueStore directly? In a separate EventEmitter class? (Think: what if you want events on other things later?)
- **How do namespace events bubble?** Does the namespace fire events itself, or does it delegate to the root?
- **What's the handler signature?** Different events have different arguments — how do you handle that cleanly?

---

## Hints

1. A `Namespace` class that wraps or composes a `KeyValueStore` is a clean approach
2. For events, consider a simple `EventEmitter` mixin or composed object with `on/off/emit` methods
3. Namespace event bubbling: when a namespace does a `set`, it can call the root store's event system with a prefixed key
4. Don't make this more complex than it needs to be — the observer pattern at its core is just "keep a list of callbacks and call them"

---

## Run Tests

```bash
cd assignment_5_kv_store
pytest test_store.py -v
```

---

## Evaluation Criteria

| Criteria | What I'm Looking For |
|----------|---------------------|
| **Encapsulation** | Namespace internals are hidden — users interact through a clean API |
| **Separation of Concerns** | Event system is not tangled with storage logic |
| **Observer Pattern** | on/off/emit is clean, supports multiple listeners, cleanup works |
| **Composition** | Namespaces reuse KV logic without copy-pasting |
| **No Leaky Abstractions** | Namespace keys don't leak into root, events carry the right context |
| **Edge Cases** | Delete non-existent = no event, expired keys fire expire event, overwrites fire set |

---

## Get Started

1. Read `store.py` — understand the current implementation
2. Run Part A tests — they should pass already (fix if not)
3. Add namespace support — create_namespace, list_namespaces, namespace API
4. Add event system — on, off, emit for set/delete/expire
5. Wire namespace events to bubble up to root
6. Run tests: `pytest test_store.py -v`

This is the capstone — it combines everything from the previous assignments. Good luck.
