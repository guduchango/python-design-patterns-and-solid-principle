# Observer Design Pattern in Python

The **Observer** pattern is a behavioral design pattern used to establish a one-to-many dependency between objects. When one object (the subject) changes its state, all its dependents (observers) are automatically notified and updated.

---

## Key Concepts

1. **Subject**: The object being observed. It maintains a list of observers and notifies them of state changes.
2. **Observer**: An object that registers itself to the subject and gets updated whenever the subject changes.
3. **Decoupling**: The pattern decouples the subject from its observers, allowing them to interact without tightly binding them.

---

## Use Cases

- Real-time event systems (e.g., stock market price updates).
- Model-View-Controller (MVC) frameworks.
- Notification systems.

---

## Example: Weather Monitoring System

### Code Example in Python

```python
class Subject:
    """The Subject keeps a list of observers and notifies them of changes."""
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """Attach an observer."""
        self._observers.append(observer)

    def detach(self, observer):
        """Detach an observer."""
        self._observers.remove(observer)

    def notify(self):
        """Notify all observers."""
        for observer in self._observers:
            observer.update(self)


class WeatherData(Subject):
    """The WeatherData class acts as the Subject."""
    def __init__(self):
        super().__init__()
        self._temperature = None

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.notify()


class Observer:
    """The Observer interface."""
    def update(self, subject):
        raise NotImplementedError("Subclass must implement `update` method")


class WeatherApp(Observer):
    """A concrete observer that displays the temperature."""
    def update(self, subject):
        print(f"WeatherApp: The temperature is now {subject.temperature}°C.")


class NewsChannel(Observer):
    """Another concrete observer."""
    def update(self, subject):
        print(f"NewsChannel: Breaking news! Temperature update: {subject.temperature}°C.")


# Example usage:
if __name__ == "__main__":
    weather_data = WeatherData()

    # Create observers
    app = WeatherApp()
    news_channel = NewsChannel()

    # Attach observers to the subject
    weather_data.attach(app)
    weather_data.attach(news_channel)

    # Change the temperature
    print("Setting temperature to 25°C:")
    weather_data.temperature = 25

    print("\nSetting temperature to 30°C:")
    weather_data.temperature = 30
