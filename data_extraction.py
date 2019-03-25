with open('automobile.csv') as f:
    data = f.readlines() 

iteration_var = []
result = []
try:
    for i in range(205):
        for j in range(25):
            iteration_var = data[i].rstrip().split(',')
        result.append(iteration_var)
except IndexError:
    pass


print(result[5][4])