# Importing dependecies
from population import Population

# Setting parameters
POPULATION_SIZE = 100
MAX_GENERATIONS = 1000 
MUTATION_RATE = 0.2

# Fitness function
def calc_fitness(chromosome):
    clashes = 0
    n = len(chromosome)
    # Checking for horizontal and diagonal clashes
    for i in range(n):
        for j in range(i + 1, n):
            if (chromosome[i] == chromosome[j]
                or abs(chromosome[i] - chromosome[j]) == j - i):
                clashes += 1
    return clashes 

if __name__ == "__main__":
    board_size = 8
    curr_population = Population(
        board_size, POPULATION_SIZE, calc_fitness, MUTATION_RATE
    )
    curr_population.crossover()
    curr_population.mutate()
    curr_population.eliminate()
    print(curr_population[0])
    if calc_fitness(curr_population[0]) == 0:
        print("Solution found!") 