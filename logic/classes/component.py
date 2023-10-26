from abc import ABC, abstractmethod

class Component (ABC):
    """
    A class that represents a Component
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def show_details(self, depth: int) -> None:
        pass