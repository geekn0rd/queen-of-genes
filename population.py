import random

class Population:
    def __init__(self, board_size: int, size: int, fitness_func: callable, mutation_rate: float):
        self.board_size = board_size
        self.size = size
        self.mutation_rate = mutation_rate
        self.fitness_func = fitness_func
        self.population = [
        random.sample(range(board_size), board_size) for _ in range(size)
        ]

    def __getitem__(self, i):
        return self.population[i]
    
    def crossover(self) -> None:
        for i in range(0, self.size, 2):
            parent1, parent2 = self.population[i], self.population[i + 1]
            # Single-point crossove
            crossover_point = random.randint(0, len(parent1) - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            self.population.append(child1)
            self.population.append(child2)
    
    def mutate(self) -> None:
        children = self.population[self.size:]
        random.shuffle(children)
        chosen_ones = children[:int(self.size * self.mutation_rate)]
        for chromosome in chosen_ones:
            n = len(chromosome)
            mutation_point = random.randint(0, n - 1)
            new_gene = random.randint(0, n - 1)
            chromosome[mutation_point] = new_gene

    def eliminate(self) -> None:
        self.population = sorted(self.population, key=lambda x: self.fitness_func(x))
        self.population = self.population[:self.size]