class Vehicle:  # 父类
    def __init__(self, brand, speed):
        self.__brand = brand  # 私有属性
        self._speed = speed

    def get_brand(self):  # 公开方法
        return self.__brand

    def set_brand(self, brand):
        if not brand:
            raise ValueError("Name cannot be empty")
        self.__brand = brand

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):  # 公开方法
        if not isinstance(speed, int) or speed < 0:
            raise ValueError("Age must be a positive integer")
        self._speed = speed

    brand = property(get_brand, set_brand)  # 公开属性
    speed = property(get_speed, set_speed)

    def accelerate(self):  # 子类可以重写
        raise NotImplementedError("子类必须实现此方法")

class Car(Vehicle):  # 子类
    def __init__(self, brand, speed):
        super().__init__(brand, speed)
    def accelerate(self):
        self._speed += 20
        # self.set__speed(self.get__speed() + 20)
        return f"{self.get_brand()} 加速中, 当前速度: {self.get_speed()} km/h"

class Bicycle(Vehicle):  # 子类
    def __init__(self, brand, speed):
        super().__init__(brand, speed)
    def accelerate(self):
        self._speed += 5
        return f"{self.get_brand()} 加速中, 当前速度: {self.get_speed()} km/h"

# 测试
car = Car("宝马", 60)
bicycle = Bicycle("捷安特", 10)

# print(car.accelerate())  # 宝马 加速中, 当前速度: 80 km/h
vehicles = [car, bicycle]
for vehicle in vehicles:
    print(vehicle.accelerate())  # 多态性
