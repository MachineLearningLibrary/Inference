# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:48:04 2020

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

ranks_array = [0, 1]
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

functions_array = [[1, [0, 1]], [2, [1, 2]], [3, [3]], [4, [2, 4]], [5, [2]]]

states = [[0, 1, [True, 0.5], [False, 0.5]], [3, 1, [True, 0.5], [False, 0.5]], [4, 2, [True, 0.5], [False, 0.5]],
          [2, 1, 4, [True, True, 0.2], [True, False, 0.2], [False, True, 0.2], [False, False, 0.2]],
          [1, 0, 2, 3, [True, True, True, 0.1], [False, False, False, 0.1], [True, False, False, 0.1], [False, True, False, 0.1], [False, False, True, 0.1], [True, True, False, 0.1], [True, False, True, 0.1], [False, True, True, 0.1]]]

def calculate_function(graph, input_function):
    global functions_array
    global states
    
    function_selection = []
    function_value = 1
    
    for a in functions_array:
        if a[0] == input_function:
            function_selection = a
    
    for b in function_selection[1]:
        for c in states:
            if b == c[0]:
                if len(c) == 4:
                    point_1_state = graph.adj[c[1]][0].source_state
                    
                    for x in range(2, 4):
                        if point_1_state == c[x][0] and graph.adj[b][0].source_state == True:
                            function_value = function_value * c[x][1]
                        if point_1_state == c[x][0] and graph.adj[b][0].source_state == False:
                            function_value = function_value * (1 - c[x][1])
                
                if len(c) == 7:
                    point_1_state = graph.adj[c[1]][0].source_state
                    point_2_state = graph.adj[c[2]][0].source_state
                    
                    for x in range(3, 7):
                        if point_1_state == c[x][0] and point_2_state == c[x][1] and graph.adj[b][0].source_state == True:
                            function_value = function_value * c[x][2]
                        if point_1_state == c[x][0] and point_2_state == c[x][1] and graph.adj[b][0].source_state == False:
                            function_value = function_value * (1 - c[x][2])
                
                if len(c) == 12:
                    point_1_state = graph.adj[c[1]][0].source_state
                    point_2_state = graph.adj[c[2]][0].source_state
                    point_3_state = graph.adj[c[3]][0].source_state
                    
                    for x in range(4, 12):
                        if point_1_state == c[x][0] and point_2_state == c[x][1] and point_3_state == c[x][2] and graph.adj[b][0].source_state == True:
                            function_value = function_value * c[x][3]
                        if point_1_state == c[x][0] and point_2_state == c[x][1] and point_3_state == c[x][2] and graph.adj[b][0].source_state == False:
                            function_value = function_value * (1 - c[x][3])
    
    return function_value

answer = 1

current_rank = 3

overall_functions = []

def sum_product(new_graph):
    global current_rank
    global functions_array
    global answer
    global graph
    
    temp_answer = 0
    occupied_array = []
    limit_tracker = []
    
    if current_rank == 1: 
        for a in range(len(new_graph.adj)):
            if new_graph.adj[a][0].rank == current_rank:
                for b in range(len(functions_array)):
                    if a in functions_array[b][1] and functions_array[b] not in overall_functions:
                        answer = answer * calculate_function(new_graph, functions_array[b][0])
                        overall_functions.append(functions_array[b])
        
        return
    
    selected_functions = []
    for a in range(len(new_graph.adj)):
        if new_graph.adj[a][0].rank == current_rank:
            for b in range(len(functions_array)):
                if a in functions_array[b][1] and functions_array[b] not in overall_functions:
                    selected_functions.append(functions_array[b])
    
    limit = 1
    set_count = 0
    counted = []
    for m in selected_functions:
        for n in m[1]:
            if new_graph.adj[n][0].rank == 1 and n not in counted:
                set_count = set_count + 1
                counted.append(n)
    
    for b in range(len(selected_functions)):
        limit = limit * (2**(len(functions_array[b][1])))
    limit = limit / (2**(set_count))
        
    n = 10000
    count = 0
    while len(limit_tracker) <= limit and count < n:
        weak_answer = 1
        collection_limit = []
        
        for x in selected_functions:
            temp_limit = []
            for y in x[1]:
                selection = random.choice([True, False])
                if new_graph.adj[y][0].rank != 1:
                    new_graph.adj[y][0].source_state = selection
                    temp_limit.append(selection)
                else:
                    temp_limit.append(new_graph.adj[y][0].source_state)
            
            collection_limit.append(temp_limit)
        
        if collection_limit not in limit_tracker:
            for x in selected_functions:
                weak_answer = weak_answer * calculate_function(new_graph, x[0])
            
            limit_tracker.append(collection_limit)
            
            temp_answer = temp_answer + weak_answer
        
        count = count + 1
    
    limit_tracker.clear()
    
    for x in selected_functions:
        overall_functions.append(x[:])
    
    selected_functions.clear()
    
    current_rank = current_rank - 1
    answer = answer * temp_answer
    sum_product(new_graph)
                    
sum_product(graph)

print(round(answer, 5))

            
    