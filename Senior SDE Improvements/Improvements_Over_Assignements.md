# Improvements Over Assignments

---

## Assignment 1: TicTacToe (Starting Point)
- Single class design, no patterns
- Basic OOP with encapsulation (private methods)
- Hard-coded logic, print statements for feedback
- Functional but not extensible
- **Independence: ~20%** — needed step-by-step guidance for everything

---

## Assignment 3: Library & Parking Lot (First Leap)
- Introduced **Strategy Pattern** for swappable behaviors (late fees, pricing)
- Used **abstract base classes** to enforce contracts
- Split code into multiple files with clear separation of concerns
- Applied encapsulation with properties and private attributes
- Began thinking about extensibility and open/closed principle
- **Independence: ~60%** — understood structure, needed help with edge cases

**What improved:** Went from one file to multiple files. Started thinking about "who owns this responsibility?"

---

## Assignment 4: Stock Market (Pattern Confidence)
- Implemented **Observer Pattern** with an Event Bus (pub/sub architecture)
- Designed a full event-driven system across 5 modules (events, observers, event_bus, stocks, stock_market)
- Used polymorphism to handle multiple event types and observer behaviors independently
- Achieved loose coupling: Stock doesn't know about observers, observers don't know about Stock
- Demonstrated that new observer types can be added without modifying existing code
- **Independence: ~70%** — understood concepts quickly, logic errors were the main issue

**What improved:** Asking better questions ("do I store old_volume or pass threshold?"). Self-correcting typos. Moving from needing all answers to needing only hints.

**Remaining issues:** Typos in parameter names (`time_stamp` vs `timestamp`, `>` vs `>=`), accessing wrong event attributes, logic inversions.

---

## Assignment 2: Ultimate TicTacToe (The Real Test)

This was an interview redemption — previously failed by modifying the base class instead of subclassing.

### board_manager.py — Strongest File
- Pure composition: 9 TicTacToe instances in a tuple-keyed dictionary
- Reused base class methods (`get_cell`, `.winner`, `_is_board_full`) instead of rewriting
- Clean API with focused methods
- Nearly independent on first attempt
- **Independence: ~90%**

### rules.py — Clean Structure
- Stateless validator with no stored game state
- Correct use of SubBoardManager API
- Logic needed clarification (inverted conditions, wrong return values)
- Got the final order right: decided check -> free choice -> match check
- **Independence: ~75%**

### ultimate.py — Orchestration Struggle
- Correct inheritance and composition setup
- Understood the concept of overriding `make_move`
- Struggled with: what `active_sub_board` is (tuple vs object), double references (`self.sub_board_manager.sub_board_manager`), missing arguments to method calls
- Needed pseudocode flow before writing implementation
- Forgot query methods and player sync — had to be reminded
- **Independence: ~40%**

**What improved from stock market:**
- `board_manager.py` was nearly perfect on first try (vs stock market where every file needed fixes)
- Understood composition vs inheritance clearly
- Asked architectural questions instead of just "what do I write?"
- Base class left untouched (the exact mistake from the interview, now corrected)

**What still needs work:**
- Orchestration: wiring multiple components in one class
- Type awareness: knowing if a variable is a tuple, object, or string at each point
- Completeness: remembering all required methods before running tests

---

## Progression Summary

| Skill | Assignment 1 | Assignment 3 | Assignment 4 (Stock) | Assignment 2 (Ultimate) |
|-------|-------------|-------------|---------------------|------------------------|
| **OOP** | Basic | ABC + inheritance | Full hierarchy | Inheritance + composition |
| **Patterns** | None | Strategy | Observer + Event Bus | Composition + delegation |
| **File separation** | 1 file | Multiple | 5 modules | 4 files with clear roles |
| **Reuse vs rewrite** | All custom | Some reuse | Good reuse | Excellent (zero new win logic) |
| **Independence** | ~20% | ~60% | ~70% | 40-90% (varies by file) |
| **Design questions** | None | Few | Good | Excellent |

---

## Key Growth Trajectory
1. **Pattern recognition**: None -> Strategy -> Observer -> Composition + Inheritance combined
2. **Abstraction**: Hard-coded -> Interfaces -> Event-driven -> Stateless validators
3. **Design thinking**: "How do I make it work?" -> "Where does this responsibility belong?"
4. **Separation of concerns**: One class -> Multiple files -> Each file has one clear job
5. **Reuse mindset**: Copy-paste -> Inheritance -> `super().make_move()` delegation

---

## Identified Weaknesses (Next Focus Areas)

### 1. Orchestration (Critical)
The class that ties everything together is consistently the weakest. Need to practice writing the "wiring" class independently without pseudocode.

### 2. Type Precision
Mixing up what a variable actually is — tuple vs object, string vs bool, method vs attribute. Need to mentally track types through the entire flow.

### 3. Argument Completeness
Forgetting to pass required parameters to methods. Need to check method signatures before calling them.

### 4. Test-First Thinking
Not reading tests before coding. Tests define the contract — they tell you exact parameter names, return types, and expected behavior.

### 5. Syntax Precision
Small typos that cause test failures: `time_stamp` vs `timestamp`, `inner_row` written twice, `>` vs `>=`. Slow down and proofread.

---

## Next Assignment: Task Scheduler
Designed to directly target weaknesses #1-4. Focus areas:
- Write the orchestrator (`scheduler.py`) without pseudocode
- Track types precisely (strings vs Task objects)
- Read tests first, match signatures exactly
- Implement cycle detection (new: graph algorithms)
