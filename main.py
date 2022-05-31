# Import Lybraries
import numpy

from charles.charles import Population, Individual
from tsp_data import dm_1,dm_2, dm_3
from copy import deepcopy
from charles.selection import fps, tournament, random_sel
from charles.mutation import swap_mutation, inversion_mutation, exponencial_mutation
from charles.crossover import cycle_co, pmx_co, switch_crossover
from tsp import tsp_function
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from multiprocessing import Process

'''
This is where the magic happens!

We used this section to run our code and produce all of our results, 
from the graphics to the tables.

We ran this code in parts and commented the irrelevant parts. 

'''


# Code to compare the elitism and produce a graphic

# Define data values
func_1 = tsp_function(dm_1, 100, 5000, tournament, cycle_co, exponencial_mutation, 0.8, 0.1, True)
func_2 = tsp_function(dm_1, 100, 5000, tournament, cycle_co, exponencial_mutation, 0.8, 0.1, False)
x = func_1.keys()
y_1 = func_1.values()
y_2 = func_2.values()

# Plot a simple line chart
plt.plot(x, y_1, label="Yes")
plt.plot(x, y_2, label="No")

#
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.legend(title="Elitism")
plt.title("Evolution of the GA with and without Elitism")

plt.show()






# Code to produce a graphic to analyse the evolution of different configuration thru a lot of generations
# We change the necessary values to do this. We tried for the different datasets and different configurations

func_1 = tsp_function(dm_3, 100, 10000, tournament, cycle_co, inversion_mutation, 0.9, 0.1, True)
func_2 = tsp_function(dm_3, 100, 10000, tournament, pmx_co, exponencial_mutation, 0.9, 0.1, True)
func_3 = tsp_function(dm_3, 100, 10000, fps, cycle_co, exponencial_mutation, 0.9, 0.1, True)
func_4 = tsp_function(dm_3, 100, 10000, random_sel, cycle_co, swap_mutation, 0.9, 0.1, True)
func_5 = tsp_function(dm_3, 100, 10000, tournament, switch_crossover, inversion_mutation, 0.9, 0.1, True)
x = func_1.keys()
y_1 = func_1.values()
y_2 = func_2.values()
y_3 = func_3.values()
y_4 = func_4.values()
y_5 = func_5.values()

# Plot a simple line chart
plt.plot(x, y_1, label="tournament, cycle_co, inversion_mutation")
plt.plot(x, y_2, label="tournament, pmx_co, exponencial_mutation")
plt.plot(x, y_3, label="fps, cycle_co, exponencial_mutation")
plt.plot(x, y_4, label="random_sel, cycle_co, swap_mutation")
plt.plot(x, y_5, label="tournament, switch_crossover, inversion_mutation")

#
plt.xlabel('Generations')
plt.ylabel('Fitness')
plt.legend(title="Configurations")
plt.title("Convergence of the GA with different operators")

plt.show()


# Code to create the tables where we tested different configurations

dataset_name = []
selector_name = []
crossover_name = []
mutation_name = []
minimum_fitness = []
avg_fitness = []
std_fitness = []
global_optimum = []
tiktok = []




for dataset in [dm_1, dm_2, dm_3]:
    for selector in [random_sel, fps, tournament]:
        for crossover in [cycle_co, pmx_co, switch_crossover]:
            for mutation in [swap_mutation, inversion_mutation, exponencial_mutation]:
                store_fitness_list = []
                # Run each configuration 10 times
                for i in range(10):
                    time_start = time.perf_counter()
                    func = tsp_function(dataset, 100, 500, selector, crossover, mutation, 0.9, 0.1, True)
                    store_fitness_list.append(func[list(func)[-1]])
                time_elapsed = (time.perf_counter() - time_start)/10
                tiktok.append(time_elapsed)

                if np.array_equal(dataset, dm_1) == True:
                    dataset_name.append('berlin52')
                    global_optimum.append(7542)
                elif np.array_equal(dataset, dm_2) == True:
                    dataset_name.append('pcb442')
                    global_optimum.append(50778)
                else:
                    dataset_name.append('')
                    global_optimum.append(564)

                selector_name.append(selector.__name__)
                crossover_name.append(crossover.__name__)
                mutation_name.append(mutation.__name__)
                minimum_fitness.append(np.min(store_fitness_list))
                avg_fitness.append(int(np.mean(store_fitness_list)))
                std_fitness.append(int(np.std(store_fitness_list)))
                print(f"Checkpoint: {dataset_name[-1]} | {selector_name[-1]} | {crossover_name[-1]} | {mutation_name[-1]}")

data = {'Dataset': dataset_name,
        'Selector':selector_name,
        'Crossover': crossover_name,
        'Mutation': mutation_name,
        'Minimum_Fitness': minimum_fitness,
        'Avg_Fitness': avg_fitness,
        'Std_Fitness': std_fitness,
        'Global_Optimum': global_optimum,
        'Time': tiktok
        }

performance_df = pd.DataFrame(data)
performance_df.to_csv(r'C:\Users\tiago\desktop\Performance_File.csv', index = False)



# Code to produce a graphic to compare different values of crossover and mutation probability

x_cord = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
y_cord = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
x_cordinates = []
y_cordinates = []
store_fitness_list = []
avg_fitness = []
for x in x_cord:
    for y in y_cord:
        store_fitness_list = []
        for i in range(10):
            func = tsp_function(dm_1, 100, 200, fps, cycle_co, inversion_mutation, x, y, True)
            store_fitness_list.append(func[list(func)[-1]])

        x_cordinates.append(x)
        y_cordinates.append(y)
        avg_fitness.append(int(np.mean(store_fitness_list)))
        print(f"Checkpoint: {x} | {y}")

data = {'X_cord': x_cordinates,
        'Y_cord': y_cordinates,
        'Avg_Fitness': avg_fitness
        }

performance_df = pd.DataFrame(data)
performance_df.to_csv(r'C:\Users\tiago\desktop\Performance_File_XOM_2.csv', index = False)








