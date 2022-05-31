# Import Lybraries
from __future__ import division
from random import randint, sample
from numpy import random
import math
import random as rand

try:
    from collections.abc import Sequence
except ImportError:
    from collections import Sequence


# Doesn't work on ours :(
def binary_mutation(individual):
    """Binary mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    mut_point = randint(0, len(individual) - 1)

    if individual[mut_point] == 0:
        individual[mut_point] = 1
    elif individual[mut_point] == 1:
        individual[mut_point] = 0
    else:
        raise Exception(
            f"Trying to do binary mutation on {individual}. But it's not binary.")

    return individual

# Swap 2 elements from the Individual
def swap_mutation(individual):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points
    mut_points = sample(range(len(individual)), 2)
    # Swap them
    individual[mut_points[0]], individual[mut_points[1]] = individual[mut_points[1]], individual[mut_points[0]]

    return individual


def inversion_mutation(individual):
    """Inversion mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Position of the start and end of substring
    mut_points = sample(range(len(individual)), 2)
    # This method assumes that the second point is after (on the right of) the first one
    # Sort the list
    mut_points.sort()
    # Invert for the mutation
    individual[mut_points[0]:mut_points[1]] = individual[mut_points[0]:mut_points[1]][::-1]

    return individual




'''
Similar to swap mutation but for a random number of individuals.
Idea behind: The numbers of mutations that happen to an Individual occur from time to time.
             We described hose occurrences with an Exponencial Distribution.
Example: 
Individual: [1,2,3,4,5]
Step 1: Hom many mutations: k = 3
Step 2: What elements: [3,5,2]
Result: [1,3,5,4,2]
'''
def exponencial_mutation(individual):
    """Exponencial mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Position of the start and end of substring
    k = math.ceil(random.exponential(scale=0.05 * len(individual)))
    if k < len(individual):

        l1 = rand.sample(range(len(individual)), k)

        l2 =[]

        for i in l1:
            l2.append(individual.index(i))

        l2.sort()

        for i, j in enumerate(l2):
            individual[j] = l1[i]

        return individual

    else:
        raise Exception(
            f"The number of mutations {k} is bigger than the size  {len(individual)} of the individual")