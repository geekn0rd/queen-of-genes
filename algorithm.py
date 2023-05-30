from population import Population

# Setting parameters
POPULATION_SIZE = 200
MAX_GENERATIONS = 1000
MUTATION_RATE = 0.6

# Fitness function
def calc_fitness(chromosome: list) -> int:
    clashes = 0
    n = len(chromosome)
    # Checking for horizontal and diagonal clashes
    for i in range(n):
        for j in range(i + 1, n):
            if (chromosome[i] == chromosome[j]
                or abs(chromosome[i] - chromosome[j]) == j - i):
                clashes += 1
    return clashes 

# Genetic Algorithm implementation
def genetic_algorithm(
        board_size: int, pop_size: int = POPULATION_SIZE,
        mut_rate: float = MUTATION_RATE, max_gen: int = MAX_GENERATIONS
        ) -> tuple:
    curr_population = Population(
        board_size, pop_size, calc_fitness, mut_rate
    )
    curr_population.sort()
    if calc_fitness(curr_population[0]) == 0:
        return curr_population[0], "Soultion found!", 1
    for generaion in range(max_gen):
        curr_population.crossover()
        curr_population.mutate()
        curr_population.eliminate()
        if calc_fitness(curr_population[0]) == 0:
            return curr_population[0], "Soultion found!", generaion + 1
    best_chromosome = curr_population[0]
    return best_chromosome, "Soultion wasn't found!", -1
