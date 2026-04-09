# Improvements Over Assignments

## Assignment 1: TicTacToe
- Single class design, no patterns
- Basic OOP with encapsulation (private methods)
- Hard-coded logic, print statements for feedback
- Functional but not extensible

## Assignment 3: Library & Parking Lot
- Introduced **Strategy Pattern** for swappable behaviors (late fees, pricing)
- Used **abstract base classes** to enforce contracts
- Split code into multiple files with clear separation of concerns
- Applied encapsulation with properties and private attributes
- Began thinking about extensibility and open/closed principle

## Assignment 4: Stock Market
- Implemented **Observer Pattern** with an Event Bus (pub/sub architecture)
- Designed a full event-driven system across 5 modules (events, observers, event_bus, stocks, stock_market)
- Used polymorphism to handle multiple event types and observer behaviors independently
- Achieved loose coupling: Stock doesn't know about observers, observers don't know about Stock
- Demonstrated that new observer types can be added without modifying existing code

## Key Growth Areas
- **Pattern recognition**: None -> Strategy -> Observer/Event Bus
- **Abstraction**: Hard-coded logic -> Interfaces and contracts -> Event-driven decoupling
- **Design thinking**: Started asking "should I pass this or inherit it?" and "where does this responsibility belong?"
- **Separation of concerns**: Single class -> Multi-file with clear module boundaries

## Areas to Keep Improving
- Syntax precision (matching parameter names, operators)
- Reading tests first to understand the contract before coding
- Implementing without hints before asking for help
- Adding defensive error handling at system boundaries