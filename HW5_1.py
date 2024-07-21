import uuid
import random

class Animal():
    def __init__(self, name, large, ration, habitat, age, max_age, sex, satiety):
        self.id = str(uuid.uuid4())
        self.name = name
        self.large = int(large)
        self.ration_code = ration
        self.ration = {
            '1': 'plant food',
            '2': 'all other animals',
            '3': 'air-animals',
            '4': 'land-animals',
            '5': 'water-animals'
        }.get(ration, '-')
        self.habitat_code = habitat
        self.habitat = {
            '1': 'air',
            '2': 'land',
            '3': 'water'
        }.get(habitat, '-')
        self.age = int(age)
        self.max_age=int(max_age)
        self.sex = {
            '1': 'male',
            '2': 'female'
        }.get(sex, '-')
        self.satiety = int(satiety)

    def increase_satiety(self, amount):
        self.satiety = min(self.satiety + amount, 100)

    def decrease_satiety(self, amount):
        self.satiety = max(self.satiety - amount, 0)

    def output(self, number):
        print(f'{number}) id: {self.id}; name: {self.name}; large: {self.large}kg; ration: {self.ration}; habitat: {self.habitat}; age: {self.age}e.o.; max_age: {self.max_age}e.o.; sex: {self.sex}; satiety: {self.satiety}%.')

def generate_random_animal():
    names = ['Elephant', 'Wolf', 'Rabbit', 'Lion', 'Eagle', 'Shark', 'Horse', 'Bear', 'Penguin', 'Dolphin']
    rations = ['1', '2', '3', '4', '5']
    habitats = ['1', '2', '3']
    sexes = ['1', '2']

    name = random.choice(names)
    large = random.randint(5, 1000)
    ration = random.choice(rations)
    habitat = random.choice(habitats)
    age = random.randint(1, 50)
    max_age = random.randint(50, 100)
    sex = random.choice(sexes)
    satiety = random.randint(0, 100)

    return Animal(name, large, ration, habitat, age, max_age, sex, satiety)


def add_animal(animals_dict):
    try:
        a, b, c, d, e, f, g, h = input('Input name, large, ration, habitat, current age, maximum age, sex and satiety: ' + '\n').split(' ')
        animal = Animal(a, b, c, d, e, f, g, h)
        animals_dict[animal.id] = animal
    except ValueError:
        print("Incorrect input. Please provide all values separated by space.")

def reproduce_animals(animals_dict):
    male_id, female_id = input('Enter the IDs of the male and female animals to reproduce: ').split()
    if male_id in animals_dict and female_id in animals_dict:
        male = animals_dict[male_id]
        female = animals_dict[female_id]
        if male.name == female.name and male.sex == 'male' and female.sex == 'female':
            if male.habitat == 'water' and male.satiety > 50 and female.satiety > 50:
                for _ in range(10):
                    new_animal = Animal(male.name, male.large, male.ration_code, male.habitat_code, 0, male.max_age,
                                        random.choice(['1', '2']), 23)
                    animals_dict[new_animal.id] = new_animal
            elif male.habitat == 'air' and male.satiety > 42 and female.satiety > 42 and male.age > 3 and female.age > 3:
                for _ in range(4):
                    new_animal = Animal(male.name, male.large, male.ration_code, male.habitat_code, 0, male.max_age,
                                        random.choice(['1', '2']), 64)
                    animals_dict[new_animal.id] = new_animal
            elif male.habitat == 'land' and male.satiety > 20 and female.satiety > 20 and male.age > 5 and female.age > 5:
                for _ in range(2):
                    new_animal = Animal(male.name, male.large, male.ration_code, male.habitat_code, 0, male.max_age,
                                        random.choice(['1', '2']), 73)
                    animals_dict[new_animal.id] = new_animal
            else:
                print("The conditions for reproduction are not met.")
        else:
            print("Both animals must be of the same species and different sexes.")
    else:
        print("Invalid IDs provided.")

def simulate_year(animals_dict, info):
    info['year'] += 1

    for animal_id in list(animals_dict.keys()):
        animal = animals_dict[animal_id]
        animal.age += 1

        if animal.age > animal.max_age:
            info['plant_food'] += animal.large
            print(f'{animal.name} has died of old age.')
            del animals_dict[animal_id]
            continue

        if animal.ration == 'plant food':
            if info["plant_food"] > 0:
                animal.increase_satiety(26)
                info["plant_food"] -= 1
            else:
                animal.decrease_satiety(9)

        elif animal.ration in ['all other animals', 'flying animals', 'land animals', 'water animals']:
            prey_found = False
            for prey_id in list(animals_dict.keys()):
                prey = animals_dict[prey_id]
                if prey.id != animal.id and (
                        animal.ration == 'all other animals' or prey.habitat == animal.ration.split('-')[0]
                ):
                    if random.random() < 0.5:
                        animal.increase_satiety(53)
                        print(f'{animal.name} has eaten {prey.name}.')
                        del animals_dict[prey_id]
                        prey_found = True
                        break

            if not prey_found:
                animal.decrease_satiety(16)

        if animal.satiety < 10:
            info['plant_food'] += animal.large
            print(f'{animal.name} has died of low satiety.')
            del animals_dict[animal_id]

def menu(animals_dict, info):
    print('1) Create an animal\n'
          '2) See animals list\n'
          '3) See planet status\n'
          '4) Simulate 1 year\n'
          '5) Reproduce animals\n'
          '6) Exit')

    number = input()
    if number == '1':
        add_animal(animals_dict)
    elif number == '2':
        for idx, animal in enumerate(animals_dict.values(), start=1):
            animal.output(idx)
    elif number == '3':
        print(f'Year: {info["year"]}\n'
              f'Plant food: {info["plant_food"]}\n'
              f'Total amount of animals: {len(animals_dict)}\n')
    elif number == '4':
        simulate_year(animals_dict, info)
    elif number =='5':
        reproduce_animals(animals_dict)
    elif number == '6':
        exit('Bye!')

def main():
    animals_dict = {}
    info = {'year': 0,
            'plant_food': 100000}
    animals = []
    #Создаю сам несколько животных для проверки некоторых условий
    animals.append(Animal('Elephant', 1000, '1', '2', 30, 100, '1', 60))
    animals.append(Animal('Elephant', 1200, '1', '2', 45, 100, '2', 50))
    animals.append(Animal('wolf', 50, '1', '2', 50, 50, '1', 30))

    for animal in animals:
        animals_dict[animal.id] = animal

    for _ in range(10):
        random_animal = generate_random_animal()
        animals_dict[random_animal.id] = random_animal

    while True:
        menu(animals_dict, info)

if __name__ == '__main__':
    main()



# Примеры:
# Elephant 100 1 3 20 120 2 55