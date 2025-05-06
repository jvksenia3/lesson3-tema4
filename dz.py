class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")
    def eat(self):
        return f"{self.name} is eating."
class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says chirp!"
class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} says roar!"
class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} says hiss!"
def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []
    def add_animal(self, animal):
        self.animals.append(animal)
    def add_employee(self, employee):
        self.employees.append(employee)
class ZooKeeper:
    def feed_animal(self, animal):
        return f"ZooKeeper is feeding {animal.name}."
class Veterinarian:
    def heal_animal(self, animal):
        return f"Veterinarian is healing {animal.name}."

# Пример использования
zoo = Zoo()
# Добавление животных
zoo.add_animal(Bird("Parrot", 2))
zoo.add_animal(Mammal("Lion", 5))
zoo.add_animal(Reptile("Snake", 3))

# Добавление сотрудников
zoo.add_employee(ZooKeeper())
zoo.add_employee(Veterinarian())

# Демонстрация полиморфизма
animal_sound(zoo.animals)
# Сохранение и загрузка данных о зоопарке
import json
def save_zoo(zoo, filename):
    with open(filename, 'w') as file:
        zoo_data = {"animals": [{"name": animal.name, "age": animal.age, "type":
            type(animal).__name__} for animal in zoo.animals],  "employees":
            [type(employee).__name__ for employee in zoo.employees]}
        json.dump(zoo_data, file)
def load_zoo(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        loaded_zoo = Zoo()
        for animal_data in data["animals"]:
            animal_type = animal_data["type"]
            if animal_type == "Bird":
                loaded_zoo.add_animal(Bird(animal_data["name"], animal_data["age"]))
            elif animal_type == "Mammal":
                loaded_zoo.add_animal(Mammal(animal_data["name"], animal_data["age"]))
            elif animal_type == "Reptile":
                loaded_zoo.add_animal(Reptile(animal_data["name"], animal_data["age"]))
        for employee_type in data["employees"]:
            if employee_type == "ZooKeeper":
                loaded_zoo.add_employee(ZooKeeper())
            elif employee_type == "Veterinarian":
                loaded_zoo.add_employee(Veterinarian())
        return loaded_zoo

# Сохранение текущего состояния зоопарка
save_zoo(zoo, "zoo_data.json")
# Загрузка зоопарка из файла
loaded_zoo = load_zoo("zoo_data.json")
animal_sound(loaded_zoo.animals)
