# Junior Engineer Training & Evaluation Framework

This repository documents the **6-month structured traineeship plan** for progressing into a **Junior Engineer** role.  
It defines **expectations, evaluation criteria, training modules, decision gates, and failure handling** to ensure clarity, fairness, and measurable growth.

---

## 🎯 Target Role

**Junior Engineer**

### 6-Month Competence Requirements
By the end of the program, the engineer should be able to:

- Independently debug and fix bugs in assigned subsystems
- Implement well-specified features with minimal supervision
- Participate effectively in code reviews (both giving and receiving)
- Follow team workflows without creating process debt
- Understand system architecture well enough to predict downstream impacts

---

## 📊 Weekly Evaluation Criteria (1–5 Scale)

Each week is scored across the following dimensions:

1. **Process Compliance**  
   Follows Git workflow, Jira updates, and PR standards without reminders

2. **Code Quality**  
   Variable naming, function size, readability, and maintainability

3. **Communication**  
   Asks clarifying questions before starting work and documents decisions

4. **Self-Sufficiency**  
   Attempts debugging and research before escalating questions

5. **Delivery Pace**  
   Completes assigned tasks within estimated timeframes

### Score Interpretation
- **4.0 – 5.0** → On track  
- **3.0 – 3.9** → Needs targeted intervention  
- **< 3.0** → Triggers escalation discussion  

---

## 🚦 Decision Gates

### Month 3 Decision

- **STOP**
  - < 2.5 weekly average over 8+ weeks **OR**
  - Failed 3+ module assessments **OR**
  - Created a production incident

- **ESCALATE**
  - 2.5 – 3.5 weekly average **OR**
  - Struggling with 2+ core modules  
  → Intensive mentoring plan

- **GO**
  - > 3.5 weekly average **AND**
  - Passed all core modules  
  → Continue to Month 6

---

### Month 6 Decision

- **STOP**
  - < 3.0 weekly average **OR**
  - Cannot independently own a component

- **EXTEND**
  - 3.0 – 3.5 weekly average  
  → Additional 3 months with a specific improvement plan

- **TRANSITION**
  - > 3.5 weekly average **AND**
  - Demonstrates component ownership  
  → Full team member

---

## 🧭 Training Timeline & Modules

### Weeks 1–2: Process Foundation (**Critical Path**)

#### Module 1: Git & Team Workflow
- Trunk-based development
- Branch naming and commit messages
- PR creation, reviews, and feedback handling

**Assessment:**  
Create a PR for a documentation fix and respond to review comments  
**Pass Threshold:** PR merged without process violations

---

#### Module 2: Agile & Jira
- Ticket lifecycle and estimation
- Status updates
- When to ask questions vs. unblock yourself

**Assessment:**  
Manage 3 tickets through the full lifecycle  
**Pass Threshold:** Zero missed updates, accurate time tracking

---

#### Module 3: Python Fundamentals
- Reading existing codebases (not comprehensive Python theory)
- Type hints and common standard library patterns

**Assessment:**  
Fix 3 pre-selected bugs in the existing codebase  
**Pass Threshold:** Fixes work, pass review, and can explain decisions in a walkthrough

---

### Weeks 3–4: Code Quality Foundation

#### Module 4: Clean Code Practices
- SOLID principles
- DRY
- Variable naming and function decomposition
- Team-specific linting and formatting rules

**Assessment:**  
Refactor a provided messy code sample  
**Pass Threshold:** Code review approval + clear explanation of design decisions

---

#### Module 5: OOP in Python
- Classes, inheritance, composition
- When to use OOP vs. functional approaches

**Assessment:**  
Implement a simple abstraction in the existing system  
**Pass Threshold:** Code works, passes review, and tradeoffs are explained

---

### Weeks 5–6: Testing & Validation

**Business Value:** Enables independent feature work without QA bottlenecks

#### Module 6: Test-Driven Development
- Unit and integration tests
- Mocking, fixtures, and test data management

**Assessment:**  
Add a feature using a TDD approach  
**Pass Threshold:**  
- ≥ 90% test coverage  
- Tests pass  
- Clear explanation of test strategy

---

### Weeks 7–8: Infrastructure Basics

#### Module 7: Docker & Docker Compose
- Container concepts
- Dockerfile best practices
- Local environment setup and debugging

**Assessment:**  
Fix a broken Docker setup  
**Pass Threshold:** Service runs and root cause is explained

---

#### Module 8: Logging & Observability
- Structured logging
- Log levels and logging strategy
- Debugging using logs and metrics

**Assessment:**  
Add logging to a feature and debug an issue using logs  
**Pass Threshold:** Logs are useful and root cause is found independently

---

### Weeks 9–12: Advanced Patterns & Ownership

#### Module 9: Design Patterns
- Factory, Adapter, Observer (only patterns used by the team)
- When to apply vs. over-engineering

**Assessment:**  
Implement a pattern where appropriate in the real codebase  
**Pass Threshold:** Design fits the use case and is approved by the team

---

#### Module 10: CI/CD Pipelines
- GitHub workflows
- Build, test, and deploy pipeline understanding

**Assessment:**  
Add a pipeline step or fix a broken workflow  
**Pass Threshold:** Pipeline works and each step can be explained

---

#### Module 11: Component Ownership
- Ownership of a clearly bounded component (API endpoints, validation layer, or data transformation module)
- Responsibility for bugs, improvements, and documentation

**Assessment:**  
Ongoing ownership through Month 6  
**Pass Threshold:**  
- No production incidents  
- Proactive improvements proposed  

---

## 🧪 Assessment Methods

### Per-Module Assessment
1. **Practical Task** (60%) — Solve a real problem in the actual codebase  
2. **Code Walkthrough** (40%) — Explain solution and design decisions  
3. **Optional MCQ** — Used only if conceptual clarity is uncertain  

**Pass Criteria**
- Task completed and merged
- Decisions explained coherently
- No major conceptual misunderstandings

---

### Monthly Comprehensive Review
- 1-hour session: **Nish + colleague + Avishkar**
- Review weekly scores, module performance, and PR quality
- Discuss strengths, improvement areas, and next-month focus
- Document **specific, actionable goals**

---

## ⚙️ Integration with Production Work

1. **Weeks 1–4:**  
   100% training, no production expectations

2. **Weeks 5–8:**  
   70% training, 30% supervised production work (bugs, small features)

3. **Weeks 9–12:**  
   50% training, 50% production work with decreasing supervision

4. **Months 4–6:**  
   20% continued learning, 80% production work with component ownership

---

## 🚨 Failure Mode Analysis

### Git / Agile Module Failure
- Cannot proceed to code modules
- 1-week intensive remediation
- Continued failure → role may not be suitable

### Multiple Code Quality Failures
- Indicates foundational programming gaps
- Consider timeline extension or expectation adjustment

### Infrastructure Failures with Strong Coding
- Engineer can still be productive with DevOps support
- Not necessarily disqualifying

---

## ✅ Guiding Principle

This framework optimizes for **clarity, predictability, ownership, and long-term team value**—not speed at the cost of quality.
