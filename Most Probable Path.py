# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:11:18 2020

@author: Grant
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:06:08 2020

@author: Grant
"""

num_variables = 5

import random

class Edge:
    def __init__(self, src, dest, source_state, destination_state):
        self.src = src
        self.dest = dest
        self.source_state = source_state
        self.destination_state = destination_state

class Node:
    def __init__(self, value, source_state, destination_state):
        self.value = value
        self.source_state = source_state
        self.destination_state = destination_state
        self.rank = 0
        self.visited = 0

class Graph:
    def __init__(self, edges):
        self.adj = [None] * num_variables

        for i in range(num_variables):
            self.adj[i] = []

        for e in edges:
            node1 = Node(e.dest, e.source_state, e.destination_state)
            node2 = Node(e.src, e.destination_state, e.source_state)
            self.adj[e.src].append(node1)
            self.adj[e.dest].append(node2)

edges = [Edge(0, 1, True, False), Edge(1, 2, False, True), Edge(1, 3, False, True),
         Edge(2, 4, True, True)]

graph = Graph(edges)

ranks_array = [0]
current_rank = 1

def set_rank(graph, ranks_array):
    global current_rank
    new_ranks_array = []
    
    for i in ranks_array:
        for j in range(len(graph.adj[i])):
            if graph.adj[i][j].visited == 0:
                graph.adj[i][j].rank = current_rank
                new_ranks_array.append(graph.adj[i][j].value)
                graph.adj[i][j].visited = 1
    
    current_rank += 1
    
    if len(new_ranks_array) == 0:
        return
    else:
        set_rank(graph, new_ranks_array)

set_rank(graph, ranks_array)

for i in range(len(graph.adj)):
    for j in range(len(graph.adj[i])):
        print(i)
        print(graph.adj[i][j].value)
        print(graph.adj[i][j].source_state)
        print(graph.adj[i][j].destination_state)
        print(graph.adj[i][j].rank)
        print()

states = [[0, 1, [True, 0.1], [False, 0.1]], [1, 0, [True, 0.8], [False, 0.8]],
          [1, 2, [True, 0.1], [False, 0.1]], [2, 1, [True, 0.2], [False, 0.2]],
          [1, 3, [True, 0.1], [False, 0.1]], [3, 1, [True, 0.2], [False, 0.2]],
          [2, 4, [True, 0.1], [False, 0.1]], [4, 2, [True, 0.8], [False, 0.8]]]

def calculate_probability(graph, source_variable, destination_variable):
    probability = 0
    for s in states:
        if s[0] == source_variable and s[1] == destination_variable:
            point_1_state = graph.adj[s[0]][0].source_state
            point_2_state = graph.adj[s[1]][0].source_state
            
            for x in range(2, 4):
                if point_1_state == s[2][0] and point_2_state == True:
                    probability = s[2][1]
                if point_1_state == s[3][0] and point_2_state == False:
                    probability = 1 - s[3][1]
    
    return probability

answer = 0
answer_states = []
answer_point_states = []

current_rank = 4

overall_functions = []
set_graph_states = []

def most_probable_path(new_graph, new_answer):
    global current_rank
    global answer
    global answer_states
    global answer_point_states
    
    max_value = 0
    max_states = []
    max_points = []
    
    collection_limit = []
    
    for x in range(100):
        temp_answer = 1
        
        temp_limit = []
        temp_numerical_limit = []
        
        temp_graph_states = []
        for a in range(len(new_graph.adj)):
            if new_graph.adj[a][0].rank == current_rank:
                if a not in set_graph_states:
                    selection = random.choice([True, False])
                    
                    if a not in temp_graph_states:
                        new_graph.adj[a][0].source_state = selection
                        temp_graph_states.append(a)
                    
                    n_selection = new_graph.adj[a][0].source_state
                    temp_limit.append(n_selection)
                    temp_numerical_limit.append(a)
                
                for b in new_graph.adj[a]:
                    if new_graph.adj[b.value][0].rank < current_rank and new_graph.adj[b.value][0] not in set_graph_states:
                        selection = random.choice([True, False])
                        
                        if b.value not in temp_graph_states:
                            new_graph.adj[b.value][0].source_state = selection
                            temp_graph_states.append(b.value)
                            
                            
                        n_selection = new_graph.adj[b.value][0].source_state
                        temp_limit.append(n_selection)
                        temp_numerical_limit.append(b.value)
        
        if temp_limit not in collection_limit:
            collection_limit.append(temp_limit)
            for a in range(len(new_graph.adj)):
                if new_graph.adj[a][0].rank == current_rank:
                    for b in new_graph.adj[a]:
                        if new_graph.adj[b.value][0].rank < current_rank:
                            temp_answer = temp_answer * calculate_probability(new_graph, a, b.value)
        
            if temp_answer > max_value:
                max_value = temp_answer
                max_states = temp_limit[:]
                max_points = temp_numerical_limit        
    
    for y in max_points:
        set_graph_states.append(y)
    
    current_rank = current_rank - 1
    new_answer = new_answer * max_value
    
    if max_states != []:
        answer_states.append(max_states)
        answer_point_states.append(max_points)
    
    collection_limit.clear()
    
    if current_rank == 0:
        answer = new_answer
        return
    else:
        most_probable_path(new_graph, new_answer)

max_answer = 0
max_answer_states= []
max_answer_points = []

for i in range(30):
    temp_graph = Graph(edges)
    current_rank = 1
    set_rank(temp_graph, ranks_array)
    current_rank = 4
    most_probable_path(temp_graph, 1)
    
    if answer > max_answer:
        max_answer = answer
        max_answer_states = answer_states[:]
        max_answer_points = answer_point_states[:]
    
    answer = 0
    set_graph_states.clear()
    answer_states.clear()
    answer_point_states.clear()
    

print(round(max_answer, 5))
print(max_answer_states)
print(max_answer_points)


