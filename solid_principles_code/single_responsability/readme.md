## **Overview**

The original `PaymentProcessor` class was responsible for multiple tasks:

- Customer data validation.
- Payment data validation.
- Payment processing with Stripe.
- Sending notifications (email or SMS).
- Logging transaction data.

This violated SRP, as a single class was responsible for too many operations, making the code hard to maintain and scale.

---

## **Refactored Structure**

The refactoring process identified four key responsibilities and reorganized them into separate classes:

### 1. **Customer Data Validation**
- A new class: `CustomerValidator`.
- Responsibility: Validate customer details such as name and contact information.

### 2. **Payment Data Validation**
- A new class: `PaymentDataValidator`.
- Responsibility: Ensure the validity of payment data, such as card or token information.

### 3. **Payment Processing**
- A new class: `StripePaymentProcessor`.
- Responsibility: Process payments through the Stripe API.

### 4. **Notifications**
- A new class: `Notifier`.
- Responsibility: Send notifications via email or SMS.

### 5. **Transaction Logging**
- A new class: `TransactionLogger`.
- Responsibility: Record and store transaction details in system logs.

---

## **Orchestrating the Components**

A new class, `PaymentService`, was introduced to coordinate interactions between all components:

- Validates customer and payment data.
- Processes payments through `StripePaymentProcessor`.
- Handles notifications using the `Notifier`.
- Logs transactions with `TransactionLogger`.

---

## **Error Handling**

- Each class raises specific exceptions for its domain (e.g., invalid customer data or payment failure).
- Errors are managed centrally in `PaymentService` using `try-except` blocks for controlled failure handling.

---

## **Benefits of SRP Implementation**

- **Improved maintainability**: Each class has a single, well-defined responsibility.
- **Scalability**: New features can be added without modifying unrelated code.
- **Error isolation**: Clear separation of responsibilities makes debugging easier.

---