# Builder Design Pattern in Python

The Builder pattern is a creational design pattern used to construct complex objects step by step. It separates the construction of an object from its representation, allowing the same construction process to create different representations.

---

## Problem Statement

When constructing a complex object, you may want to:
- Control the construction process.
- Avoid creating large, unreadable constructors with multiple parameters.
- Support multiple representations of the object.

---

## Solution: Builder Pattern

The Builder pattern provides a way to build an object step-by-step using a separate builder class. It keeps the creation logic out of the main class, improving readability and flexibility.

---

## Implementation

### Example: Building a Computer

```python
class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.memory = None
        self.storage = None

    def __str__(self):
        return (f"Computer Specifications:\n"
                f"CPU: {self.cpu}\n"
                f"GPU: {self.gpu}\n"
                f"Memory: {self.memory}GB\n"
                f"Storage: {self.storage}GB")


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_memory(self, memory):
        self.computer.memory = memory
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer


# Using the Builder
if __name__ == "__main__":
    builder = ComputerBuilder()
    gaming_pc = (builder
                 .set_cpu("Intel i9")
                 .set_gpu("NVIDIA RTX 4090")
                 .set_memory(32)
                 .set_storage(2048)
                 .build())

    office_pc = (builder
                 .set_cpu("Intel i5")
                 .set_gpu("Integrated GPU")
                 .set_memory(16)
                 .set_storage(512)
                 .build())

    print(gaming_pc)
    print(office_pc)
