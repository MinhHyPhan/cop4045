import random
import matplotlib.pyplot as plt


class Island:
    def __init__(self, n: int, prey_count: int = 0,
                 predator_count: int = 0, count_humans: int = 0) -> None:
        if n <= 0 or min(prey_count, predator_count, count_humans) < 0:
            raise ValueError("Invalid island size or animal count")
        if prey_count + predator_count + count_humans > n * n:
            raise ValueError("Too many animals for the island")
        self.grid_size = n
        self.grid: list[list[Animal | int]] = []
        for i in range(n):
            self.grid.append([0] * n)
        self.init_animals(prey_count, predator_count, count_humans)

    def init_animals(self, prey_count: int, predator_count: int,
                     count_humans: int) -> None:
        for animal_class, count in ((Prey, prey_count),
                                    (Predator, predator_count),
                                    (Human, count_humans)):
            placed = 0
            while placed < count:
                x = random.randint(0, self.grid_size - 1)
                y = random.randint(0, self.grid_size - 1)
                if not self.animal(x, y):
                    new_animal = animal_class(self, x=x, y=y)
                    self.register(new_animal)
                    placed += 1

    def clear_all_moved_flags(self) -> None:
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                animal = self.grid[x][y]
                if isinstance(animal, Animal):
                    animal.clear_moved_flag()
    def size(self) -> int:
        return self.grid_size

    def register(self, animal: "Animal") -> None:
        self.grid[animal.x][animal.y] = animal

    def remove(self, animal: "Animal") -> None:
        if self.grid[animal.x][animal.y] is animal:
            self.grid[animal.x][animal.y] = 0

    def animal(self, x: int, y: int) -> "Animal | int":
        if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
            return self.grid[x][y]
        return -1
    def __str__(self) -> str:
        s = ""
        for j in range(self.grid_size - 1, -1, -1):
            for i in range(self.grid_size):
                animal = self.grid[i][j]
                s += f"{str(animal) if animal else '.':<2} "
            s += "\n"
        return s
    def count_prey(self) -> int:
        return sum(isinstance(a, Prey) for row in self.grid for a in row)

    def count_predators(self) -> int:
        return sum(isinstance(a, Predator) for row in self.grid for a in row)

    def count_humans(self) -> int:
        return sum(isinstance(a, Human) for row in self.grid for a in row)

class Animal:
    breed_time: int = 1
    def __init__(self, island: Island, x: int = 0,
                 y: int = 0, s: str = "A") -> None:
        self.island = island
        self.name = s
        self.x = x
        self.y = y
        self.moved = False
        self.breed_clock = self.breed_time
    def position(self) -> tuple[int, int]:
        return self.x, self.y
    def __str__(self) -> str:
        return self.name
    def check_grid(self, type_looking_for: type = int) -> tuple[int, int] | None:
        offsets = [(-1, 1), (0, 1), (1, 1),
                   (-1, 0), (1, 0),
                   (-1, -1), (0, -1), (1, -1)]

        for dx, dy in offsets:
            x = self.x + dx
            y = self.y + dy

            if 0 <= x < self.island.size() and 0 <= y < self.island.size():
                if type(self.island.animal(x, y)) == type_looking_for:
                    return (x, y)

        return None
    def move(self) -> None:
        if not self.moved:
            location = self.check_grid(int)
            if location:
                self.island.remove(self)
                self.x, self.y = location
                self.island.register(self)
                self.moved = True

    def breed(self) -> None:
        if self.breed_clock <= 0:
            location = self.check_grid(int)
            if location:
                self.breed_clock = self.breed_time
                new_animal = self.__class__(self.island, x=location[0],
                                            y=location[1])
                new_animal.moved = True
                self.island.register(new_animal)

    def clear_moved_flag(self) -> None:
        self.moved = False

class Prey(Animal):
    breed_time: int = 3

    def __init__(self, island: Island, x: int = 0,
                 y: int = 0, s: str = "O") -> None:
        super().__init__(island, x, y, s)

    def clock_tick(self) -> None:
        self.breed_clock -= 1

class Predator(Animal):
    breed_time: int = 6
    starve_time: int = 3

    def __init__(self, island: Island, x: int = 0,
                 y: int = 0, s: str = "X") -> None:
        super().__init__(island, x, y, s)
        self.starve_clock = self.starve_time

    def clock_tick(self) -> None:
        self.breed_clock -= 1
        self.starve_clock -= 1
        if self.starve_clock <= 0:
            self.island.remove(self)

    def eat(self) -> None:
        if not self.moved:
            location = self.check_grid(Prey)
            if location:
                prey = self.island.animal(*location)
                self.island.remove(prey)
                self.island.remove(self)
                self.x, self.y = location
                self.island.register(self)
                self.starve_clock = self.starve_time
                self.moved = True

class Human(Animal):
    breed_time: int = 8
    starve_time: int = 6
    hunt_time: int = 2

    def __init__(self, island: Island, x: int = 0,
                 y: int = 0, s: str = "H") -> None:
        super().__init__(island, x, y, s)
        self.starve_clock = self.starve_time
        self.hunt_clock = self.hunt_time

    def clock_tick(self) -> None:
        self.breed_clock -= 1
        self.starve_clock -= 1
        self.hunt_clock -= 1

        if self.starve_clock <= 0:
            self.island.remove(self)

    def eat(self) -> None:
        if self.hunt_clock > 0 or self.moved:
            return

        self.hunt_clock = self.hunt_time
        location = self.check_grid(Predator)

        if location:
            predator = self.island.animal(*location)
            self.island.remove(predator)
            self.island.remove(self)
            self.x, self.y = location
            self.island.register(self)
            self.starve_clock = self.starve_time
            self.moved = True

def main(predator_breed_time: int = 6,
         predator_starve_time: int = 3,
         initial_predators: int = 10,
         prey_breed_time: int = 3,
         initial_prey: int = 50,
         size: int = 10,
         ticks: int = 300,
         human_breed_time: int = 8,
         human_starve_time: int = 6,
         human_hunt_time: int = 2,
         initial_humans: int = 5) -> None:
    if min(predator_breed_time, predator_starve_time, prey_breed_time,
           human_breed_time, human_starve_time, human_hunt_time) <= 0:
        raise ValueError("Time periods must be positive")

    Predator.breed_time = predator_breed_time
    Predator.starve_time = predator_starve_time
    Prey.breed_time = prey_breed_time
    Human.breed_time = human_breed_time
    Human.starve_time = human_starve_time
    Human.hunt_time = human_hunt_time

    isle = Island(size, initial_prey, initial_predators, initial_humans)

    print("Initial island:")
    print(isle)

    prey_list = [isle.count_prey()]
    predator_list = [isle.count_predators()]
    human_list = [isle.count_humans()]

    stable_ticks = 0
    max_ticks = min(ticks, 1000)

    for tick in range(1, max_ticks + 1):
        isle.clear_all_moved_flags()

        # Take a snapshot so each animal acts only once per clock tick.
        animals = [isle.grid[x][y]
                   for x in range(size)
                   for y in range(size)
                   if isinstance(isle.grid[x][y], Animal)]

        for animal in animals:
            # Skip animals that have already been eaten or removed.
            if isle.animal(animal.x, animal.y) is not animal:
                continue

            if isinstance(animal, (Predator, Human)):
                animal.eat()

            animal.move()
            animal.breed()
            animal.clock_tick()

        prey_count = isle.count_prey()
        predator_count = isle.count_predators()
        human_count = isle.count_humans()

        prey_list.append(prey_count)
        predator_list.append(predator_count)
        human_list.append(human_count)

        if tick % 10 == 0 or tick == 1:
            print(f"Tick {tick}: Prey={prey_count}, "
                  f"Predators={predator_count}, Humans={human_count}")

        current = (prey_count, predator_count, human_count)
        previous = (prey_list[-2], predator_list[-2], human_list[-2])

        if current == previous:
            stable_ticks += 1
        else:
            stable_ticks = 0

        if stable_ticks >= 30:
            print(f"Populations converged after {tick} ticks.")
            break

    print("\nFinal island:")
    print(isle)

    print(f"Final populations: Prey={prey_list[-1]}, "
          f"Predators={predator_list[-1]}, Humans={human_list[-1]}")
    print("Name: Phan Minh Hy")
    print("Student ID: Z23766758")

    plt.plot(prey_list, label="Prey", color="green", linewidth=2)
    plt.plot(predator_list, label="Predators", color="red", linewidth=2)
    plt.plot(human_list, label="Humans", color="pink", linewidth=2)

    plt.xlabel("Time (clock ticks)")
    plt.ylabel("Population")
    plt.title("Predator-Prey-Human Population Simulation")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
