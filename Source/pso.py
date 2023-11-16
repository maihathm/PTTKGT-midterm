import random
import os
import functions
import math
# Function
def target_function(x):
    return

# Function: Initialize Variables
def initial_position(N=None, min_val=None, max_val=None, function=target_function, initial=1, distance_matrix=None):
    if N is None:
        N = 3
    if max_val is None:
        max_val = [5, 5, 5]
    if min_val is None:
        min_val = [0.001, 0.001, 0.001]
    position = []
    for i in range(0, N):
        temp = []
        for j in range(0, len(min_val)):
            random_val = random.uniform(min_val[j], max_val[j])
            temp.append(random_val)
        position.append(temp)
    for i in range(0, N):
        val = position[i][0: len(position[i])]
        alpha, beta, decay = val
        # print(type(alpha),type(beta),type(decay))
        print(f'alpha: {alpha}, beta: {beta}, decay {decay}')
        route, distance = function(initial, distance_matrix, alpha=float(alpha), beta=float(beta), decay=float(decay))
        position[i].append(distance)
    return position

# Function: Initialize Velocity
def initial_velocity(position, min_values=None, max_values=None):
    if min_values is None:
        min_values = [0, 0, 0]
    if max_values is None:
        max_values = [5, 5, 5]

    init_velocity = functions.create_empty_matrix(len(position[0]), len(min_values))
    for i in range(0, len(init_velocity[0])):
        for j in range(0, len(init_velocity[1])):
            init_velocity[i][j] = random.uniform(min_values[j], max_values[j])
    return init_velocity

# Function: Individual Best
# def individual_best_matrix(position, i_b_matrix):
#     for i in range(len(position)):
#         if i_b_matrix[i][-1] > position[i][-1]:
#             i_b_matrix[i] = position[i][:]
#     return i_b_matrix

def individual_best_matrix(position, i_b_matrix): 
    for i in range(0, len(position[0])):
        if(i_b_matrix[i][-1] > position[i][-1]):
            for j in range(0, len(position[1])):
                i_b_matrix[i][j] = position[i][j]
    return i_b_matrix

# Function: Velocity
def velocity_vector(position, init_velocity, i_b_matrix, best_global, w=0.5, c1=2, c2=2):
    r1 = int.from_bytes(os.urandom(8), byteorder='big') / ((1 << 64) - 1)
    r2 = int.from_bytes(os.urandom(8), byteorder='big') / ((1 << 64) - 1)
    velocity = []
    for i in range(len(init_velocity)):
        particle_velocity = [
            w * v + c1 * r1 * (i_b_matrix[i][j] - position[i][j]) + c2 * r2 * (best_global[j] - position[i][j])
            for j, v in enumerate(init_velocity[i])
        ]
        velocity.append(particle_velocity)
    return velocity

# Function: Update Position
def update_position(position, velocity, min_values=[-5, -5], max_values=[5, 5]):
    for i in range(len(position)):
        for j in range(len(position[i]) - 1):
            position[i][j] = max(min(position[i][j] + velocity[i][j], max_values[j]), min_values[j])
        # position[i][-1] = target_function(position[i][:-1])
        position[i][-1] = target_function(position[i][0:(len(position[1])-1)])
        print(position[i][-1])
    return position

# PSO Function
def particle_swarm_optimization(swarm_size=3, min_values=[0, 0, 0], max_values=[5, 5, 5], iterations=5, decay=0,
                                 w=0.9, c1=2, c2=2, target_function=target_function, verbose=True, initial=None
                               , distance_matrix=None):
    count = 0
    position = initial_position(N=swarm_size,min_val= min_values,max_val= max_values,function=target_function, initial=initial
                               , distance_matrix=distance_matrix)
    init_velocity = initial_velocity(position=position,min_values= min_values, max_values= max_values)
    i_b_matrix = [p[:] for p in position]
    best_global = sorted(position, key=lambda x: x[-1])[0][:]
    while count <= iterations:
        if verbose:
            print('Iteration = ', count, ' f(x) = ', best_global[-1])
        position = update_position(position, init_velocity, min_values, max_values)
        i_b_matrix = individual_best_matrix(position, i_b_matrix)
        value = sorted(i_b_matrix, key=lambda x: x[-1])[0][:]
        if best_global[-1] > value[-1]:
            best_global = value[:]
        if decay > 0:
            n = decay
            w *= (1 - ((count - 1) ** n) / (iterations ** n))
            c1 = (1 - c1) * (count / iterations) + c1
            c2 = (1 - c2) * (count / iterations) + c2
        init_velocity = velocity_vector(position, init_velocity, i_b_matrix, best_global, w=w, c1=c1, c2=c2)
        count += 1
    return best_global