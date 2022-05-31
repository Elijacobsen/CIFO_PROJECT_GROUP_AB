# Import Lybraries
from random import randint, uniform, sample
import random as rand

# This type of crossover does not work for our case.
# This is due to the nature of our problem, we cannot have repeated numbers in the representation of the individual.
def single_point_co(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = randint(1, len(p1) - 2)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2



def cycle_co(p1, p2):
    """Implementation of cycle crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    # Offspring placeholders - None values make it easy to debug for errors
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p2)
    # While there are still None values in offspring, get the first index of
    # None and start a "cycle" according to the cycle crossover method
    while None in offspring1:
        # this where the dunder function in 'charles' comes useful, it allows us indexing
        # offspring1 which is an object, like it was a list.
        index = offspring1.index(None)

        # we'll keep doing it, but if val1 is equal to val2, the cycle would be over.
        val1 = p1[index]
        val2 = p2[index]

        while val1 != val2:
            offspring1[index] = p1[index]
            offspring2[index] = p2[index]
            val2 = p2[index]
            index = p1.index(val2)

        for element in offspring1:
            if element is None:
                index = offspring1.index(None)
                if offspring1[index] is None:
                    offspring1[index] = p2[index]
                    offspring2[index] = p1[index]

    return offspring1, offspring2



def pmx_co(p1, p2):
    """Implementation of partially matched/mapped crossover.
    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_points = sample(range(len(p1)), 2)
    co_points.sort()

    def PMX(x, y):
        # 'o' will have the length of the parent and will be filled for now with 'None' values.
        o = [None] * len(x)
        # starting to use the interval to create the segment.
        o[co_points[0]:co_points[1]] = x[co_points[0]:co_points[1]]

        z = set(y[co_points[0]:co_points[1]]) - set(x[co_points[0]:co_points[1]])

        for i in z:
            temp = i
            index = y.index(x[y.index(temp)])
            while o[index] is not None:
                temp = index
                index = y.index(x[temp])
            o[index] = i

        while None in o:
            index = o.index(None)
            o[index] = y[index]
        return o

    o1, o2 = PMX(p1, p2), PMX(p2, p1)
    return o1, o2

# Doesn't work on TSP problem!!!
def arithmetic_co(p1, p2):
    """Implementation of arithmetic crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # Offspring placeholders - None values make it easy to debug for errors
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p1)
    # Set a value for alpha between 0 and 1
    alpha = uniform(0, 1)
    # Take weighted sum of two parents, invert alpha for second offspring
    for i in range(len(p1)):
        offspring1[i] = p1[i] * alpha + (1 - alpha) * p2[i]
        offspring2[i] = p2[i] * alpha + (1 - alpha) * p1[i]

    return offspring1, offspring2


'''
Switch a random number (between 25% to 75%) of the total elements between the parents.
Example:
Parents: p1 = [2,3,1,5,4]   p2 = [3,4,5,1,2]  
Step 1: Choose how many elements - 3 
Step 2: Choose the elements - [1,4,3]
Result: o1 =  [2,1,4,5,3]   o2 = [3,1,5,4,2]
'''
def switch_crossover(p1, p2):
    """Implementation of switch crossover
    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.
    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """

    o1 = [None] * len(p1)
    o2 = [None] * len(p1)

    # Choose how many elements
    temp = round(rand.uniform(0.25, 0.75) * len(p1))

    # Choose the elements
    k = rand.sample(range(len(p1)), temp)

    # lists
    l1 = []
    l2 = []

    # Store the index of the chosen elements
    for i in k:
        l1.append(p1.index(i))
        l2.append(p2.index(i))

    # Sort the list
    l1.sort()
    l2.sort()

    j = 0
    for i in range(len(p1)):

        if i in k:
            # Switch
            o1[l1[j]] = p2[l2[j]]
            o2[l2[j]] = p1[l1[j]]
            j += 1

        else:
            # The ohter elements remains the same of the parent
            o1[p1.index(i)] = i
            o2[p2.index(i)] = i

    return o1, o2
