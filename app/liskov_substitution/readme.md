# The Liskov Substitution Principle (LSP)

The Liskov Substitution Principle ensures that subclasses or implementations can replace their parent classes or interfaces without altering the behavior of the program. In this project, we demonstrate how to apply LSP using Python protocols and explore challenges in maintaining consistent method signatures.

---

## **How Did We Replace Abstract Classes with Protocols?**

- Replaced abstract classes with **protocols** in Python.
- Protocols act similarly to **interfaces** in other programming languages.
- Converted key components like `Notifier` and `PaymentProcessor` into protocols for improved flexibility.
- Enhanced clarity by documenting methods within the protocols using **NumPy-style docstrings**.

---

## **How Was the Bug Introduced and Detected?**

1. **Deliberately Introduced Bug**:  
   - Altered the `SMSNotifier` class to include an additional parameter (`SMSGateway`) in its `send_confirmation` method.
   - This deviation from the required method signature made `SMSNotifier` non-interchangeable with `EmailNotifier`.  

2. **Detection**:  
   - Used **debugging tools** and manual inspection of method signatures to identify the issue.  

---

## **Challenges of Applying LSP**

- **Consistency in Method Signatures**:  
  - Subclasses and protocols must have identical method signatures to maintain interchangeability.  

- **Avoiding Parameter Changes**:  
  - Introducing extra parameters or modifying method signatures can break LSP, leading to reduced flexibility and reusability.

---

## **Lessons Learned**

By adhering to the Liskov Substitution Principle:  
- We maintained **interchangeability** between notification classes without modifying the base code.  
- We demonstrated how **protocols** in Python can serve as powerful tools for enforcing LSP.  
- Debugging and adhering to consistent method signatures ensure scalable and maintainable software.

---

This project serves as a practical example of how to implement LSP in Python while addressing real-world challenges in software development.
