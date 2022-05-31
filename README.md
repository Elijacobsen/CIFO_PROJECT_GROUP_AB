# CIFO - PROJECT FINAL
This is the final project for the Computational Intelligence for Optimization class at Nova IMS, in S1/2022.

## The problem
The scope of this project is to develop a genetic algorithm ‘GA’ to be able to solve a traveling salesperson problem, for that, the GA will receive many different combinations of parameters along with different methods for selection, crossover, and mutation. 

The traveling salesperson problem is a problem in combinatorial optimization that will try to find the shortest route between locations in a given set of locations with a declared distance between each pair of cities, in this travel, the salesperson has to visit each location once and return to the initial location.

## The methodology
Our methodology consisted of applying some selection, crossover and mutation methods. After a given configuration has been defined, we run it 10 times to analyze how that configuration performed to bring us a possible (individual) route with the lowest fitness in its generation.
For selection, we use 2 classic selection methods, which are: fps and tournament. In addition, we added a third one, which consisted of randomly selecting individuals from the population. These codes have in common the prerequisite of having an existing population, and the tournament as a distinct characteristic of having to previously define the size of the parameter.

## Team members
Eliane Gotuzzo m20210996,
Marcos Oliveira m20210593,
Tiago Seca m20210564.
