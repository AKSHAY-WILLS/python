from abc import ABC,abstractmethod

class Bike:

    @abstractmethod
    def start(self):

        pass

    @abstractmethod
    def accelerate(self):

        pass

    @abstractmethod
    def stop(self):

        pass

class Hunter(Bike):

    def start(self):
        print("hunter start method")

    def accelerate(self):
        print("hunter accelerate method")

    def stop(self):
        print("hunter stop method")

hunter_instance=Hunter()

hunter_instance.start()

hunter_instance.accelerate()

hunter_instance.stop()