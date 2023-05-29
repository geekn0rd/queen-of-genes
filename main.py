# Importing dependecies
import random

# Setting parameters
POPULATION_SIZE = 200
MAX_GENERATIONS = 1000 
MUTATION_RATE = 0.2

# Generating intial population
def init_population(board_size, size):
    population = [
        random.sample(range(board_size), board_size) for _ in range(size)
    ]
    return population

# Single-point crossover function
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function to perform mutation on a chromosome
def mutate(chromosome):
    n = len(chromosome)
    mutation_point = random.randint(0, n - 1)
    new_gene = random.randint(0, n - 1)
    chromosome[mutation_point] = new_gene
    return chromosome

# Fitness function
def calculate_fitness(chromosome):
    clashes = 0
    n = len(chromosome)

    for i in range(n):
        for j in range(i + 1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == j - i:
                clashes += 1
    
    # Higher fitness for fewer clashes
    return 1 / (clashes + 1) 

if __name__ == "__main__":
    board_size = 4
    curr_population = init_population(board_size, 5)
    print(curr_population)
    curr_population[0] = mutate(curr_population[0])
    print(curr_population)