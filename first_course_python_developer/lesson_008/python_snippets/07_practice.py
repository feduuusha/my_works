# -*- coding: utf-8 -*-

from termcolor import cprint

# Реализуем модель доставки грузов

# Дорога - хранит расстояния между объектами
# Склад - хранит груз и управляет очередями грузовиков

# Базовый класс - Машина,
# имеет
#   кол-во топлива
# может
#   заправляться

# Грузовик (производный от Машина)
# имеет
#   емкость кузова, скорость движения, расход топлива за час поездки
# может
#   стоят под погрузкой/разгрузкой
#   ехать со скоростью

# Погрузчик (производный от Машина)
# имеет
#   скорость погрузки, расход топлива в час при работе
# может
#   загружать/разгружать грузовик
#   ждать грузовик


class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:
    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return f'Склад {self.name} груза {self.content}'

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        truck.place = self
        print(f'{self.name} прибыл грузовик {truck}')

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print(f'{self.name} грузовик готов {truck}')

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Vehicle:
    total_fuel = 0
    fuel_rate = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return f'{self.model} топлива {self.fuel}'

    def tank_up(self):
        self.fuel += 1000
        Vehicle.total_fuel += 1000
        print(f'{self.model} заправился')

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
            return False
        return True


class Truck(Vehicle):
    fuel_rate = 50
    dead_time = 0

    def __init__(self, model, body_space=1000):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        res = super(Truck, self).__str__()
        return res + f' груза {self.cargo}'

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance
        print(f'{self.model} выехал в путь')

    def ride(self):
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print(f'{self.model} едет по дороге, осталось {self.distance_to_target}')
        else:
            self.place.end.truck_arrived(self)
            print(f'{self.model} доехал ')

    def act(self):
        if super().act():
            if isinstance(self.place, Road):
                self.ride()
            else:
                Truck.dead_time += 1


class OtherTruck(Truck):
    fuel_rate = 100


class AutoLoader(Vehicle):
    dead_time = 0
    fuel_rate = 30

    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.track = None

    def __str__(self):
        res = super().__str__()
        return res + f' грузим {self.track}'

    def act(self):
        if super().act():
            if self.track is None:
                self.track = self.warehouse.get_next_truck()
                if self.track is None:
                    AutoLoader.dead_time += 1
                    print(f'{self.model} нет грузовиков для работы')
                else:
                    print(f'{self.model} взял в работу {self.track}')
            elif self.role == 'loader':
                self.load()
            else:
                self.unload()

    def load(self):
        if self.warehouse.content == 0:
            print(f'На {self.warehouse.name} складе ничего нет')
            if self.track:
                self.warehouse.truck_ready(self.track)
                self.track = None
            return
        self.fuel -= self.fuel_rate
        track_cargo_rest = self.track.body_space - self.track.cargo
        if track_cargo_rest >= self.bucket_capacity:
            cargo = self.bucket_capacity
        else:
            cargo = track_cargo_rest
        if self.warehouse.content < cargo:
            cargo = self.warehouse.content
        self.warehouse.content -= cargo
        self.track.cargo += cargo
        print(f'{self.model} загружал {self.track}')
        if self.track.cargo == self.track.body_space:
            self.warehouse.truck_ready(self.track)
            self.track = None

    def unload(self):
        self.fuel -= self.fuel_rate
        if self.track.cargo >= self.bucket_capacity:
            self.track.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.track.cargo -= self.track.cargo
            self.warehouse.content += self.track.cargo
        print(f'{self.model} разгружал {self.track.model}')
        if self.track.cargo == 0:
            self.warehouse.truck_ready(self.track)
            self.track = None


TOTAL_CARGO = 100000

moscow = Warehouse(name='Москва', content=TOTAL_CARGO)
piter = Warehouse(name='Питер', content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model='Bobcat', bucket_capacity=1000, warehouse=moscow, role='loader')
loader_2 = AutoLoader(model='Lonking', bucket_capacity=500, warehouse=piter, role='unloader')

trucks = []
for number in range(1, 4):
    truck1 = Truck(model=f'КАМАЗ №{number}', body_space=5000)
    moscow.truck_arrived(truck=truck1)
    trucks.append(truck1)

hour = 0
while piter.content < TOTAL_CARGO:
    hour += 1
    cprint(f'========== Час {hour} ==========', color='red')
    for truck1 in trucks:
        truck1.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    for truck1 in trucks:
        cprint(str(truck1), color='cyan')
    cprint(str(loader_1), color='cyan')
    cprint(str(loader_2), color='cyan')
    cprint(str(moscow), color='cyan')
    cprint(str(piter), color='cyan')

cprint(f'Всего затрачено {Vehicle.total_fuel} топлива', color='yellow')
cprint(f'Общий простой грузовиков {Truck.dead_time} часов', color='yellow')
cprint(f'Общий простой погрузчиков {AutoLoader.dead_time} часов', color='yellow')
