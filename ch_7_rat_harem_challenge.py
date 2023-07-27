"""Use genetic algorithm to simulate breeding race of super rats."""
import time
import random
import statistics

# CONSTANTS (weights in grams)
GOAL = 50000
NUM_RATS = 20  # number of adult breeding rats in each generation
INITIAL_MIN_WT = 200
INITIAL_MAX_WT = 600
INITIAL_MODE_WT = 300
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

# ensure even-number of rats for breeding pairs:
if NUM_RATS % 2 != 0:
    NUM_RATS += 1


def populate(num_rats, min_wt, max_wt, mode_wt):
    return [int(random.triangular(min_wt, max_wt, mode_wt)) for i in range(num_rats)]


def fitness(population, goal):
    average = statistics.mean(population)
    return average / goal


def select(population, to_retain):
    sorted_population = sorted(population)
    females_to_retain = to_retain - 4
    males_to_retain = to_retain - 16
    members_per_sex = len(sorted_population) // 2
    females = sorted_population[:members_per_sex]
    males = sorted_population[members_per_sex:]
    selected_females = females[-females_to_retain:]
    selected_males = males[-males_to_retain:]
    return selected_females, selected_males


def breed(females, males, litter_size):
    random.shuffle(females)
    random.shuffle(males)
    children = []
    for female in females:
        male = random.choice(males)
        for child in range(litter_size):
            child = random.randint(female, male)
            children.append(child)
    return children


def mutate(children, mutate_odds, mutate_min, mutate_max):
    for idx, rat in enumerate(children):
        if mutate_odds >= random.random():
            children[idx] = round(rat * random.uniform(mutate_min, mutate_max))
    return children


def main():
    generations = 0
    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    print(f"Initian population weights: {parents}")
    population_fitness = fitness(parents, GOAL)
    print(f"Initial population fitness: {population_fitness}")
    average_weight = []
    while population_fitness < 1 and generations < GENERATION_LIMIT:
        selected_females, selected_males = select(parents, NUM_RATS)
        children = breed(selected_females, selected_males, LITTER_SIZE)
        children = mutate(children, MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_females + selected_males + children
        population_fitness = fitness(parents, GOAL)
        average_weight.append(int(statistics.mean(parents)))
        generations += 1

    print(f"Average weight per generation: {average_weight}")
    print(f"Number of generations: {generations}")
    print(f"Number of years: {int(generations/LITTERS_PER_YEAR)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Time to get really big rats: {end_time-start_time:.4f} seconds.")
