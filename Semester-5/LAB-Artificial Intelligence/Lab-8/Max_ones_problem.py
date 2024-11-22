import random

def initialize_population(pop_size, string_length):
  population = []
  for _ in range(pop_size):
    individual = ''.join(str(random.randint(0, 1)) for _ in range(string_length))
    population.append(individual)

  return population

def calculate_fitness(individual):
  fitness = individual.count('1')
  return fitness


def select_parents(population, fitness_scores):
  total_fitness = sum(fitness_scores)
  probabilities = [fitness / total_fitness for fitness in fitness_scores]
  parent1 = random.choices(population, weights=probabilities)[0]
  parent2 = random.choices(population, weights=probabilities)[0]

  return parent1, parent2

def crossover(parent1, parent2):
  crossover_point = random.randint(1, len(parent1) - 1)

  offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
  offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

  return offspring1, offspring2

def mutate(individual, mutation_rate):
  mutated_individual = ""
  for bit in individual:
    if random.random() < mutation_rate:
      mutated_individual += "1" if bit == "0" else "0"
    else:
      mutated_individual += bit

  return mutated_individual

def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
  population = initialize_population(pop_size, string_length)

  for generation in range(num_generations):
    fitness_scores = [calculate_fitness(individual) for individual in population]

    parents = []
    for _ in range(pop_size // 2):
      parent1, parent2 = select_parents(population, fitness_scores)
      parents.append((parent1, parent2))

    offspring = []
    for parent1, parent2 in parents:
      child1, child2 = crossover(parent1, parent2)
      offspring.append(mutate(child1, mutation_rate))
      offspring.append(mutate(child2, mutation_rate))

    population = offspring

  best_fitness = max(fitness_scores)
  best_individual = population[fitness_scores.index(best_fitness)]

  return best_individual

def main():
    experiments = [
        (10, 20, 0.01),
        (20, 50, 0.05),
        (50, 100, 0.1)
    ]

    for string_length, pop_size, mutation_rate in experiments:
        best_individual = genetic_algorithm(string_length, pop_size, 100, mutation_rate)
        print(f"String length: {string_length}, Population size: {pop_size}, Mutation rate: {mutation_rate}")
        print(f"Best individual: {best_individual}")

main()