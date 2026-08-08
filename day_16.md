## 📘 SOLID Principles Learned

During the development of the **Bank Management System**, I learned and applied the SOLID principles through practical implementation instead of memorizing definitions.

### ✅ Single Responsibility Principle (SRP)
- Designed each class with a single responsibility.
- `Account` manages a single account.
- `Bank` manages multiple accounts.
- `file_manager` handles file persistence.
- `main.py` manages the user interface.

### ✅ Open/Closed Principle (OCP)
- Extended the system by creating `SavingsAccount` and `CurrentAccount` without modifying the existing `Account` class.
- New account types can be added through inheritance.

### ✅ Liskov Substitution Principle (LSP)
- Any subclass (`SavingsAccount`, `CurrentAccount`) can be used wherever an `Account` object is expected without breaking the program's behavior.

### ✅ Interface Segregation Principle (ISP)
- Learned that classes should only depend on the functionality they actually need.
- Explored designing smaller interfaces (using Python Abstract Base Classes) instead of forcing every class to implement unnecessary methods.

### ✅ Dependency Inversion Principle (DIP)
- Separated business logic from data storage.
- `Bank` delegates persistence to `file_manager` instead of handling file operations directly, reducing coupling and improving maintainability.

---

### 💡 Key Takeaway

Rather than memorizing SOLID definitions, I learned to apply them by designing and improving a real-world **Bank Management System**, focusing on clean architecture, maintainability, scalability, and separation of concerns.