## Strategy Pattern Skeleton

```python
from abc import ABC, abstractmethod

# Define the Strategy interface
class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# Implement concrete strategies
class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Strategy A's method invoked"

class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Strategy B's method invoked"

# Context class that uses a Strategy
class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_something(self):
        return self._strategy.execute()

# Client code
strategy_a = ConcreteStrategyA()
strategy_b = ConcreteStrategyB()

context = Context(strategy_a)
print(context.do_something())  # Strategy A's method invoked

context.set_strategy(strategy_b)
print(context.do_something())  # Strategy B's method invoked
