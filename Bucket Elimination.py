# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:31:26 2020

@author: Grant
"""

num_variables = 7

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
    def __init__(self, edges, stops):
        self.adj = [None] * num_variables

        for i in range(num_variables):
            self.adj[i] = []

        for e in edges:
            if e.src in stops or e.dest in stops:
                continue
            
            node1 = Node(e.dest, e.source_state, e.destination_state)
            node2 = Node(e.src, e.destination_state, e.source_state)
            self.adj[e.src].append(node1)
            self.adj[e.dest].append(node2)

edges = [Edge(0, 2, True, True), Edge(0, 3, True, True), 
         Edge(1, 3, True, True),
         Edge(3, 5, True, True), Edge(3, 6, True, True),
         Edge(4, 6, True, True)]

states = [[0, [True, 0.1], [False, 0.9]],
          [1, [True, 0.9], [False, 0.1]],
          [2, 0, [True, True, 0.2], [True, False, 0.5], [False, True, 0.2], [False, False, 0.1]],
          [3, 0, 1, [True, True, True, 0.1], [False, False, False, 0.1], [True, False, False, 0.2], [False, True, False, 0.1], [False, False, True, 0.1], [True, True, False, 0.2], [True, False, True, 0.1], [False, True, True, 0.1]],
          [4, [True, 0.5], [False, 0.5]],
          [5, [True, 0.9], [False, 0.1]],
          [6, 3, 4, [True, True, True, 0.1], [False, False, False, 0.1], [True, False, False, 0.2], [False, True, False, 0.1], [False, False, True, 0.1], [True, True, False, 0.2], [True, False, True, 0.1], [False, True, True, 0.1]]]

buckets = [0, 0, 0, 0, 0, 0, 0]

target_variable = 5

stops = []

graph = Graph(edges, stops)

def print_graph(graph):
    for i in range(len(graph.adj)):
        for j in range(len(graph.adj[i])):
            print("Variable")
            print(i)
            print(graph.adj[i][j].value)
            #print(graph.adj[i][j].source_state)
            #print(graph.adj[i][j].destination_state)
            #print(graph.adj[i][j].rank)

print_graph(graph)
print()
print()

def find_variables_calculate_buckets_delete_variables():
    global graph
    global states
    global buckets
    global stops
    global edges
    bucket_selection = []
    states_selection = []
    
    for a in range(len(graph.adj)):
        if len(graph.adj[a]) == 1 and a != target_variable:
            bucket_selection.append(a)
    
    print(bucket_selection)
    
    for b in bucket_selection:
        temp_bucket = []
        set_states = False
        for c in states:
            if b in c:
                temp_bucket.append(c)
                set_states = True
        
        if set_states == True:
            temp_bucket.append(b)
            
        states_selection.append(temp_bucket[:])
    
    chosen_states = [True, False]
    
    for d in states_selection:
        new_answer = 0
        for chosen_state in chosen_states:
            temp_answer = 1
            for e in range(len(d) - 1):
                if len(d[e]) == 3:
                    if chosen_state == True:
                        temp_answer = temp_answer * d[e][1][1]
                    else:
                        temp_answer = temp_answer * d[e][2][1]
        
                if len(d[e]) == 6:
                    position = d[e].index(d[-1])
                
                    if position == 0:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][2][2] + d[e][3][2])
                        else:
                            temp_answer = temp_answer * (d[e][4][2] + d[e][5][2])
                    
                    if position == 1:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][2][2] + d[e][4][2])
                        else:
                            temp_answer = temp_answer * (d[e][3][2] + d[e][5][2])
                
                if len(d[e]) == 11:
                    position = d[e].index(d[-1])
                
                    if position == 0:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][3][3] + d[e][5][3] + d[e][8][3] + d[e][9][3])
                        else:
                            temp_answer = temp_answer * (d[e][4][3] + d[e][6][3] + d[e][7][3] + d[e][10][3])
                    
                    if position == 1:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][3][3] + d[e][6][3] + d[e][8][3] + d[e][10][3])
                        else:
                            temp_answer = temp_answer * (d[e][4][3] + d[e][5][3] + d[e][7][3] + d[e][9][3])
                    
                    if position == 2:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][3][3] + d[e][7][3] + d[e][9][3] + d[e][10][3])
                        else:
                            temp_answer = temp_answer * (d[e][4][3] + d[e][5][3] + d[e][6][3] + d[e][8][3])
                
            new_answer = new_answer + temp_answer 
                    
        solution = new_answer
        
        buckets[d[-1]] = solution
    
    for w in bucket_selection:
        stops.append(w)
    
    graph = Graph(edges, stops)
    
    setting = False
    for j in range(len(graph.adj)):
        if graph.adj[j] != []:
            setting = True
    
    print(setting)
    if setting == False:
        for j in range(len(buckets)):
            #print("HERE")
            if buckets[j] == 0:
                #print("HERE")
                buckets[j] = 1.0

find_variables_calculate_buckets_delete_variables()
print_graph(graph)
print(buckets)

find_variables_calculate_buckets_delete_variables()
print_graph(graph)
print(buckets)

find_variables_calculate_buckets_delete_variables()
print_graph(graph)
print(buckets)

print()
print()
print()

#empty buckets and construct final inference
stops = []

graph = Graph(edges, stops)

calculation_answer = 0

def calculate_inference():
    global graph
    global states
    global buckets
    global calculation_answer
    
    bucket_selection = []
    bucket_transfer_selection = []
    bucket_probability = []
    
    states_selection = []
    
    for a in range(len(graph.adj)):
        if len(graph.adj[a]) == 1 and a != target_variable:
            bucket_selection.append(a)
    
    #print(bucket_selection)
    
    for b in bucket_selection:
        bucket_transfer_selection.append(graph.adj[b][0].value)
    
    #print(bucket_transfer_selection)
    
    for c in bucket_selection:        
        bucket_probability.append(buckets[c])
        buckets[c] = 0
    
    #print(bucket_probability)
    
    b_count = 0
    for b in bucket_transfer_selection:
        temp_bucket = []
        set_states = False
        b_count_state = False
        for c in states:
            if b in c and bucket_selection[b_count] in c:
                temp_bucket.append(c)
                #set_states = True
                if bucket_selection[b_count] == c[0]:
                    b_count_state = True
                else:
                    set_states = True
        
        if set_states == False and b_count_state == False:
            for c in states:
                if b == c[0]:
                    temp_bucket.append(c)
                    set_states = True
        
        if b_count_state == True:
            temp_bucket.append(bucket_selection[b_count])
        else:
            if set_states == True:
                temp_bucket.append(b)
            
        states_selection.append(temp_bucket[:])
        
        b_count = b_count + 1
    
    print(states_selection)
    
    chosen_states = [True, False]
    
    count = 0
    for d in states_selection:
        new_answer = 0
        for chosen_state in chosen_states:
            temp_answer = 1
            
            for e in range(len(d) - 1):
                if len(d[e]) == 3:
                    if chosen_state == True:
                        temp_answer = temp_answer * d[e][1][1] * bucket_probability[count]
                    else:
                        temp_answer = temp_answer * d[e][2][1] * bucket_probability[count]
        
                if len(d[e]) == 6:
                    position = d[e].index(d[-1])
                
                    if position == 0:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][2][2] + d[e][3][2]) * bucket_probability[count]
                        else:
                            temp_answer = temp_answer * (d[e][4][2] + d[e][5][2]) * bucket_probability[count]
                    
                    if position == 1:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][2][2] + d[e][4][2]) * bucket_probability[count]
                        else:
                            temp_answer = temp_answer * (d[e][3][2] + d[e][5][2]) * bucket_probability[count]
                
                if len(d[e]) == 11:
                    position = d[e].index(d[-1])
                
                    if position == 0:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][3][3] + d[e][5][3] + d[e][8][3] + d[e][9][3]) * bucket_probability[count]
                        else:
                            temp_answer = temp_answer * (d[e][4][3] + d[e][6][3] + d[e][7][3] + d[e][10][3]) * bucket_probability[count]
                    
                    if position == 1:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][3][3] + d[e][6][3] + d[e][8][3] + d[e][10][3]) * bucket_probability[count]
                        else:
                            temp_answer = temp_answer * (d[e][4][3] + d[e][5][3] + d[e][7][3] + d[e][9][3]) * bucket_probability[count]
                    
                    if position == 2:
                        if chosen_state == True:
                            temp_answer = temp_answer * (d[e][3][3] + d[e][7][3] + d[e][9][3] + d[e][10][3]) * bucket_probability[count]
                        else:
                            temp_answer = temp_answer * (d[e][4][3] + d[e][5][3] + d[e][6][3] + d[e][8][3]) * bucket_probability[count]
                
            new_answer = new_answer + temp_answer 
        
        #print("HERE")
        #print(new_answer)
                    
        solution = new_answer * buckets[d[-1]]
        
        buckets[d[-1]] = solution
        
        buckets[bucket_selection[count]] = 0
        
        count = count + 1
        
    for w in bucket_selection:
        stops.append(w)
    
    graph = Graph(edges, stops)
    
    print(buckets)
    
    setting = False
    for j in range(len(graph.adj)):
        if graph.adj[j] != []:
            setting = True
    
    #print(setting)
    if setting == False:
        for j in range(len(buckets)):
            #print("HERE")
            if buckets[j] != 0:
                #print("HERE")
                calculation_answer = buckets[j]
    
calculate_inference()
calculate_inference()
calculate_inference()

print(round(calculation_answer, 5))

    
            