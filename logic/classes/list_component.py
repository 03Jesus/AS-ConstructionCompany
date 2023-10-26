from abc import ABC, abstractmethod

from logic.classes.component import Component


class ListComponent (Component):
    """
    A Class that represents a Component that is a list of Components
    """

    def get_name(self) -> str:
        return super().get_name()

    def show_details(self, depth: int) -> None:
        return super().show_details(depth)

    @abstractmethod
    def add_child(self, child: Component) -> None:
        pass

    @abstractmethod
    def remove_child(self, child: Component) -> None:
        pass
