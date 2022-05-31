# Import lybraries
from charles.charles import Population, Individual
from copy import deepcopy


# Defining the GA for TSP problem
def tsp_function(dm, size, gens, select, crossover, mutate, co_p, mu_p, elitism):
    def get_fitness(self):
        """A simple objective function to calculate distances
        for the TSP problem.

        Returns:
            int: the total distance of the path
        """

        # the fitness will start as 0
        # in each iteration, I'll add something to the fitness. So we'll get from the distance matrix a value.
        # self.representation is what the solution looks like. TSP case: [0, 1, 2, ...]
        fitness = 0

        for i in range(len(self.representation)):
            fitness += dm[self.representation[i - 1]][self.representation[i]]
        # return the integer part of the fitness
        return int(fitness)

    def get_neighbours(self):
        """A neighbourhood function for the TSP problem. Switches
        indexes around in pairs.

        Returns:
            list: a list of individuals
        """
        # we're using deepcopy
        # deepcopy means I want to copy a list, but I want to make changes to that list. So we're copying the original
        # the original serves as the first solution, and the copies will be the neighbours.
        # in the 'n' below a list is being created  and in each iteration, in each iteration we're deepcopying this.
        # if we do not use deepcopy, we'd be always changing the original list in each iteration.
        n = [deepcopy(self.representation) for i in range(len(self.representation) - 1)]
        # enumerate: go over the individuals by also counting them
        # i: individuals, count: starts from 0
        # with enumerate we can print the count and the value.
        for count, i in enumerate(n):
            # here we do the swaping, in each iteration we swap 2 cities.
            i[count], i[count + 1] = i[count + 1], i[count]
        # for every possible solution of 'n' I want it to belong to the class 'Individual'.
        n = [Individual(i) for i in n]
        return n

    # Monkey patching
    Individual.get_fitness = get_fitness
    Individual.get_neighbours = get_neighbours

    pop = Population(
        size=size,
        # distance_matrix[0] means the size will be equal to the size of the first line of the distance matrix.
        sol_size=len(dm[0]),
        valid_set=[i for i in range(len(dm[0]))],
        # replacement means that after the valid_set (when we create the individual), do we want a replacement or not?
        # false means we will not get that again. Means every element can be used only once.
        replacement=False,
        optim="min",
    )

    pop.evolve(
        gens=gens,
        select=select,
        crossover=crossover,
        mutate=mutate,
        co_p=co_p,
        mu_p=mu_p,
        elitism=elitism
    )

    # for loop to store the best fitness score for each generation.
    fitness_scores = {}
    for i in range(gens):
        fitness_scores[i + 1] = pop.fitness_scores[i].fitness

    return fitness_scores



