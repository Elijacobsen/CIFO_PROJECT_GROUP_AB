from tsp import tsp_function

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
            func = tsp_function(dm_1, 100, 200, tournament, switch_crossover, swap_mutation, x, y, True)
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
performance_df.to_csv(performance_df.to_csv(r'C:\Users\elian_iioak3c\CIFO_Project\Performance_File_XOM_1.csv', index = False)