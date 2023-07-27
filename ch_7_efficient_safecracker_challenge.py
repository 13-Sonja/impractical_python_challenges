import time
from itertools import product
from random import randint, randrange, choice


combo = [randint(0, 9) for _ in range(10)]


def fitness(combo, attempt):
    grade = 0
    indices = []
    for idx, (i, j) in enumerate(zip(combo, attempt)):
        if i == j:
            grade += 1
            indices.append(idx)
    return grade, indices


def main():
    print(combo)
    numbers_found = []
    best_attempt = [0] * len(combo)
    best_attempt_grade, index = fitness(combo, best_attempt)
    if index:
        numbers_found += index
    count = 0
    while best_attempt != combo:
        next_try = best_attempt[:]
        lock_wheel = choice([i for i in range(0, len(combo)) if i not in numbers_found])
        next_try[lock_wheel] = randint(0, 9)
        next_try_grade, index = fitness(combo, next_try)
        if index:
            numbers_found += index
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        print(next_try, best_attempt)
        count += 1
    print(f"Cracked! {best_attempt} in {count} tries.")


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Time to crack the safe: {end_time-start_time:.5f} seconds.")
