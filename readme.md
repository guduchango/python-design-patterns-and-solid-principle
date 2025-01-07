# Platzi Course: Design Patterns and SOLID Principles in a Payment Processor
[Course Link](https://platzi.com/cursos/solid-python/)


This project is a practical example of using **design patterns** and **SOLID principles** in Python, integrating the **Stripe API**. The goal is to iteratively refactor the code, applying best practices while focusing on clean and maintainable design.

---

## 🎯 **Project Goals**
- Demonstrate how to implement design patterns (Singleton, Factory, Strategy, etc.).
- Apply SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, etc.).
- Integrate a real API, like Stripe, to illustrate a practical use case.
- Gradually improve the code design through refactoring.

---

## 🚀 **Technologies Used**
- **Python 3.10+**
- **Stripe API**: For payment processing.
- **Virtual Environments**: `venv` for dependency isolation.
- **Docker**: More flexible

---

## 🛠️ **Setup and Installation**
### 1. Clone this repository
```bash
git clone git@github.com:guduchango/python-design-patterns-and-solid-principle.git
cd python-design-patterns-and-solid-principle.git

```
### 2. Set up the virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate  
```
### 3.  Install dependencies
```bash
pip install -r app/requirements.txt
```
### 4.  Configure the .env file
- Create a new account stripe https://stripe.com/
- Go to https://dashboard.stripe.com/test/apikeys
- Read transacctions on https://dashboard.stripe.com/test/payments
### 5.  run
```bash
python3.11 app/main.py
```