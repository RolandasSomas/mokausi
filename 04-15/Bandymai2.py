from abc import ABC, abstractmethod


class Device(ABC):

    @abstractmethod
    def turn_on_device(self):
        pass

    @abstractmethod
    def turn_off_device(self):
        pass

    @abstractmethod
    def create_sound(self):
        pass


class TV(Device):
    def __init__(self):
        self.a = 5

    def turn_off_device(self):
        pass

    def turn_on_device(self):
        pass

    def create_sound(self):
        pass


tv = TV()
tv.turn_on_device()
