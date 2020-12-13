# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:57:54 2020

@author: Grant
"""

num_variables = 5

class Belief_Edge:
    def __init__(self, src, dest, source_state, destination_state):
        self.src = src
        self.dest = dest
        self.source_state = source_state
        self.destination_state = destination_state

class Belief_Node:
    def __init__(self, value, source_state, destination_state):
        self.value = value
        self.source_state = source_state
        self.destination_state = destination_state

class Belief_Graph:
    def __init__(self, edges):
        self.adj = [None] * num_variables

        for i in range(num_variables):
            self.adj[i] = []

        for e in edges:
            if e[0].src == e[0].dest:
                continue
            
            node = Belief_Node(e[0].dest, e[0].source_state, e[0].destination_state)
            self.adj[e[0].src].append(node)

probabilities = [[[1, 0], [0.2, 0.2, 0.5, 0.1]], [[2, 1], [0.1, 0.5, 0.3, 0.1]],
                 [[3, 2], [0.3, 0.2, 0.2, 0.3]],
                 [[4, 3], [0.1, 0.1, 0.3, 0.5]],
                 [[4, 4], [0.5, 0.5, 0.5, 0.5]]]

sample_data = [[True, None, True, None, False], [True, None, True, None, True], [True, None, False, None, True]]

convergence = False

hidden_variables = [1, 3]
convergence_requirement = 0.01
previous_probabilities = []

while convergence == False:
    #E step
    chosen_potentials = []
    for a in hidden_variables:
        for p in probabilities:
            if p[0][1] == a:
                chosen_potentials.append(p)
    print(chosen_potentials)
    
    sample_potential_q = []
    for s in sample_data:
        temp = []
        for b in chosen_potentials:
            visible_state = s[b[0][0]]
            
            temp_solution = 0
            
            if visible_state == True:
                temp_solution = b[1][2]
            
            if visible_state == False:
                temp_solution = b[1][3]
            
            hidden_variable = []
            for m in hidden_variables:
                if m in b[0]:
                    hidden_variable.append(m)
            
            temp.append([b[0], hidden_variable, temp_solution])
        sample_potential_q.append(temp)
    
    print(sample_potential_q)
    
    #M Step
    for e in range(5):
        chosen_variables = probabilities[e][0]
        print(chosen_variables)
        
        numerators = []
        denominators = []
        for i in range(len(probabilities[e][1])):
            numerator = probabilities[e][1][i]
            
            numerators.append(numerator)
            
            denominator = 1
            if i == 0:
                denominator = probabilities[e][1][0] + probabilities[e][1][1]
            if i == 1:
                denominator = probabilities[e][1][0] + probabilities[e][1][1]
            if i == 2:
                denominator = probabilities[e][1][2] + probabilities[e][1][3]
            if i == 3:
                denominator = probabilities[e][1][2] + probabilities[e][1][3]
            
            denominators.append(denominator)
            
            numerator_summation = 0
            denominator_summation = 0
            for s in sample_potential_q:
                if s[0][1][0] in probabilities[e][0]:
                    numerator_summation = numerator_summation + (numerator * s[0][2])
                    denominator_summation = denominator_summation + (denominator * s[0][2])
                    continue
                
                if s[1][1][0] in probabilities[e][0]:
                    numerator_summation = numerator_summation + (numerator * s[1][2])
                    denominator_summation = denominator_summation + (denominator * s[1][2])
                    continue
                
                numerator_summation = numerator_summation + numerator
                denominator_summation = denominator_summation + denominator
            
            solution = numerator_summation / denominator_summation
            
            probabilities[e][1][i] = solution
        
    print(probabilities)
    
    if previous_probabilities == []:
        previous_probabilities = probabilities[:]
        continue
    
    convergence = True
    
    for w in range(len(previous_probabilities)):
        for x in range(len(previous_probabilities[w][1])):
            c = abs(previous_probabilities[w][1][x] - probabilities[w][1][x])
            if c > convergence_requirement:
                convergence = False
    
    previous_probabilities = probabilities[:]
            
                
