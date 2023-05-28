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

if __name__ == "__main__":
    board_size = 4
    curr_population = init_population(board_size, 5)
    print(curr_population)