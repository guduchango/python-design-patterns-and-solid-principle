# Implementing the Interface Segregation Principle (ISP) in a Payment Processor

The Interface Segregation Principle (ISP) helps maintain clean and flexible code by ensuring classes depend only on methods they need. In this project, we applied ISP to a payment processor, introducing new methods for refunds and recurring payments while properly segregating interfaces based on each processor's capabilities.

---

## **Key Changes to the Payment Processor**

1. **New Methods**:
   - Refund processing.
   - Recurring payment creation.

2. **Offline Payment Processor**:
   - Simulates cash payments but does not support refunds or recurring payments.

3. **Refactored Transaction Handling**:
   - The `processTransaction` method now supports multiple processors instead of being tied to Stripe.

---

## **Resolving ISP Violations**

### **Initial Problem**
The offline processor was forced to implement methods (refunds and recurring payments) it could not use, violating ISP.

### **Solution**
1. **New Protocols**:
   - `RefundPaymentProtocol`: For refund-specific methods.
   - `RecurringPaymentProtocol`: For recurring payment-specific methods.

2. **Processor Refactoring**:
   - Offline processors no longer implement unnecessary methods.
   - Stripe processor implements all relevant protocols: charging, refunds, and recurring payments.

---

## **Additional Adjustments**

- **Optional Attributes**:
  - Introduced attributes for `RefundProcessor` and `RecurringProcessor` to assign responsibilities based on processor capabilities.

- **Error Handling**:
  - Validations added to prevent unsupported actions (e.g., refunds or recurring payments) from causing exceptions.
  - Clear error messages are raised for unsupported operations.

---

## **Impact on Payment Processors**

### **Stripe Processor**
- Fully supports all operations:
  - Charges.
  - Refunds.
  - Recurring payments.

### **Offline Processor**
- Supports only charges.
- No longer requires refunds or recurring payments, ensuring compliance with ISP.

---

By adhering to the Interface Segregation Principle, this project achieves better modularity, flexibility, and clarity in handling payment processing. These improvements ensure that each processor only implements methods relevant to its capabilities, avoiding unnecessary dependencies and maintaining a clean architecture.
