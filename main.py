from algorithm import genetic_algorithm

if __name__ == "__main__":
    board_size = int(input("Enter the board size: "))
    best_chromosome, msg, gen = genetic_algorithm(board_size)
    print(best_chromosome, msg, gen, )