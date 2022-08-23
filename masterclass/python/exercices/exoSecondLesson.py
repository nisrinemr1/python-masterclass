

# def get_higher(dico):
#     #return max(dico.values())
#     hight_key = None
#     hight_val = None

#     for key, value in dico.items():
#         if hight_key is None or value > hight_val:
#             hight_key = key
#             hight_val = value

#     return hight_key

## autre manière
def get_higher(dico):
    hight_val = max(dico.values())

    for key, value in dico.items():
        if value == hight_val:
            return key


scores = {
    "Judy": 3, 
    "Kiki": 9, 
    "Obligatif":10, 
    "Cacahuete":4, 
    "Sonia": 1}

print(get_higher(scores))


print("-----------")

# def get(array):
#     data = {}
#     data["max"] = max(array)
#     data["min"] = min(array)
#     data["avg"] = sum(array) / len(array)

#     return data


def get(array):
    return {
        "min" : min(array),
        "max" : max(array),
        "avg" : sum(array) / len(array)
    }


ma_liste = [1, 2, 4, 8]

data = get(ma_liste)

print(f"Plus petite donnée:{data['min']}")
print(f"Plus petite donnée:{data['max']}")
print(f"Plus petite donnée:{data['avg']}")



class Calculator:
    def __init__(self, initial_value):
        #pass passer pour continuer de lire les autres lignes
        self.result = initial_value

    def add(self, value):
        self.result += value
        return self.result
    
    def sub(self, value):
        self.result -= value
        return self.result
    
    def mul(self, value):
        self.result *= value
        return self.result
    
    def div(self, value):
        self.result /= value
        return self.result

    def reset(self):
        self.result = 0
        return self.result

calc = Calculator(10)

r = calc.mul(5)
print(r) #50

r = calc.sub(6) 
print(r) #44’




class Vehicle:

    def __init__(self, speed):
        self.speed = speed
        self.distance = 0

    def ride(self, duration):
        travel = self.speed * duration
        self.distance += travel

class Bike(Vehicle):

    def __init__(self):
        super().__init__(15)


bike = Bike()
print(bike.speed)
bike.ride(2)
print(bike.distance)

print("-----CAR-----")

class Car(Vehicle):
    def __init__(self):
        super().__init__(100)
        self.fuel = 100
        self.consumption = 0.05
    
    def ride(self, duration): ##en plus de ça on ajoute la consomation
        super.ride(duration)

        fuel_loss = self.consumption * self.speed * duration
        self.fuel -= fuel_loss

    def fill_thank(self, fuel_volume):
        self.fuel += fuel_volume

car = Car()
print(car.speed)
car.ride(2)
print(car.distance)



class Train(Vehicle):
    def __init__(self, max_capacity):
        super().__init__(150)
        self.passengers = 0
        self.max_capacity = max_capacity

    def take_on_board(self, passengers):
        self.passengers += passengers
        self.passengers = min(self.passengers, self.max_capacity) #meme si self.passenger est plus de 100, il remettra self.max_capacity



class TrainInterCity(Train):
    def __init__(self):
        super().__init__(100)
        self.profit = 0
        self.profit_by_kilometer = 2.5

    def ride(self, duration):
        super().ride(duration)
        self.profit = self.distance * self.profit_by_kilometer



class FreightTrain(Train):
    def __init__(self):
        super().__init__(4)
        self.cargo = 0
        
    def load_cargo(self, cargo):
        self.cargo += cargo


