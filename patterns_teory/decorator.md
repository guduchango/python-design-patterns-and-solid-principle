# Decorator Pattern in Python

The **Decorator** pattern is a structural design pattern that allows adding additional functionality to objects dynamically without modifying their existing structure. This is achieved by using a function or class "decorator" that wraps around the target object or function.

In Python, decorators are widely used to add behavior to functions or methods, such as validations, logging, or data manipulation.

## Key Features of the Decorator Pattern
- Facilitates the extension of functionality without modifying the base code.
- Adheres to the **OCP (Open/Closed Principle)**: Open for extension, closed for modification.
- Implements composition instead of inheritance to add behavior.

---

## Practical Example

This example demonstrates how to use a decorator to add logging functionality to a payment processing function.

### Code

```python
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Logging decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Result from function '{func.__name__}': {result}")
        return result
    return wrapper

# Main function
@log_decorator
def process_payment(amount, currency):
    if amount <= 0:
        raise ValueError("The amount must be positive.")
    return f"Payment processed: {amount} {currency}"

# Using the decorated function
if __name__ == "__main__":
    try:
        process_payment(150, "USD")
    except Exception as e:
        logging.error(f"Error processing payment: {e}")
