# Import Lybraries
from random import uniform, choice
from operator import attrgetter
import random


def random_sel(population):
    """
    :param population: A list of individuals to select from.
    :returns: An Individual.
    This function uses the :func:`~random.choice` function from the
    python base :mod:`random` module.
    """
    return random.choice(population)



def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """

    if population.optim == "max":
        # Sum total fitness
        # We sum the total of fitnessess and proportional to the total will be the chances of the individuals of being chosen
        # which is the sum of i.fitness for every element in the population.
        total_fitness = sum([i.fitness for i in population])
        # Get a 'position' on the wheel
        # uniform chooses a number between 2 numbers, so from 0 to the total_fitness.
        spin = uniform(0, total_fitness)
        # our initial position is 0
        position = 0
        # Find individual in the position of the spin.
        # For every individual in population we want to add the fitness of this individual.
        for individual in population:
            position += individual.fitness
            # and if that position is higher than the spin, then return the individual, meaning he is chosen.
            if position > spin:
                # the return will be an individual.
                return individual

    elif population.optim == "min":
        """
        For minimization will be similar, individuals with smaller 
        fitness will have higher chance to get chosen 
        """
        total_fitness = sum([1/i.fitness for i in population])
        # here we'll get the position on the 'wheel'
        spin = uniform(0, total_fitness)
        position = 0
        # This for loop is made to find the individual's position in the spin.
        for individual in population:
            position += (1/individual.fitness)
            if position > spin:
                return individual

    else:
        raise Exception("No optimization specified (min or max).")





def tournament(population, size=10):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    # Select individuals based on tournament size
    # the individuals just come in randomly without checking their fitnessess.
    # We use choice to give a chance for the Individuals with worse fitness to get picked.
    tournament = [choice(population.individuals) for i in range(size)]
    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("fitness"))

    elif population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))

    else:
        raise Exception("No optimization specified (min or max).")

