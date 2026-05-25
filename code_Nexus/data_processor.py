from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.counter = 0
        self.data: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        return self.data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float) )and not isinstance(data, bool):
            return True
        if isinstance(data, list) and all(
                isinstance(i, (int, float)) for i in data) and not any(isinstance(i, bool) for i in data):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        self.data.append((self.counter, str(data)))
        self.counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and all(isinstance(i, str) for i in data):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        self.data.append((self.counter, data))
        self.counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict) and data.keys() == {
                "log_level", "log_message"}:
            return True
        if isinstance(data, list) and all(isinstance(i, dict) and i.keys() == {"log_level", "log_message"} for i in data):
            return True

        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        self.data.append((self.counter, str(data)))
        self.counter += 1


if __name__ == "__main__":
    print("Testing Numeric Processor...")
    print("Trying to validate input '42': ")
    print("Trying to validate input 'Hello': ")
    print("Test invalid ingestion of string 'foo' without prior validation: ")
    x = TextProcessor()
    print(x.validate(True))
    print(x.validate("Hello"))