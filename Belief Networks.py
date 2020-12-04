# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:53:11 2020

@author: Grant
"""

num_variables = 4

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

class Graph:
	def __init__(self, edges):

		self.adj = [None] * num_variables

		for i in range(num_variables):
			self.adj[i] = []

		for e in edges:
			node = Node(e.dest, e.source_state, e.destination_state)
			self.adj[e.src].append(node)

#P(B = 1| A = 1)

#Numerator States
numerator_edges1 = [Edge(0, 2, True, True), Edge(1, 2, True, True), Edge(1, 3, True, True)]
numerator_edges2 = [Edge(0, 2, True, True), Edge(1, 2, False, True), Edge(1, 3, False, False)]
numerator_edges3 = [Edge(0, 2, True, True), Edge(1, 2, True, True), Edge(1, 3, True, False)]
numerator_edges4 = [Edge(0, 2, True, True), Edge(1, 2, False, True), Edge(1, 3, False, True)]

#Denominator States
normalisation_edges1 = [Edge(0, 2, True, True), Edge(1, 2, True, True), Edge(1, 3, True, True)]
normalisation_edges2 = [Edge(0, 2, False, True), Edge(1, 2, False, True), Edge(1, 3, False, False)]
normalisation_edges3 = [Edge(0, 2, True, True), Edge(1, 2, False, True), Edge(1, 3, False, False)]
normalisation_edges4 = [Edge(0, 2, False, True), Edge(1, 2, True, True), Edge(1, 3, True, False)]
normalisation_edges5 = [Edge(0, 2, False, True), Edge(1, 2, False, True), Edge(1, 3, False, True)]
normalisation_edges6 = [Edge(0, 2, True, True), Edge(1, 2, True, True), Edge(1, 3, True, False)]
normalisation_edges7 = [Edge(0, 2, True, True), Edge(1, 2, False, True), Edge(1, 3, False, True)]
normalisation_edges8 = [Edge(0, 2, False, True), Edge(1, 2, True, True), Edge(1, 3, True, True)]

graph_numerator_edges1 = Graph(numerator_edges1)
graph_numerator_edges2 = Graph(numerator_edges2)
graph_numerator_edges3 = Graph(numerator_edges3)
graph_numerator_edges4 = Graph(numerator_edges4)

graph_normalisation_edges1 = Graph(normalisation_edges1)
graph_normalisation_edges2 = Graph(normalisation_edges2)
graph_normalisation_edges3 = Graph(normalisation_edges3)
graph_normalisation_edges4 = Graph(normalisation_edges4)
graph_normalisation_edges5 = Graph(normalisation_edges5)
graph_normalisation_edges6 = Graph(normalisation_edges6)
graph_normalisation_edges7 = Graph(normalisation_edges7)
graph_normalisation_edges8 = Graph(normalisation_edges8)


for i in range(len(graph_numerator_edges1.adj)):
    for j in range(len(graph_numerator_edges1.adj[i])):
        print(i)
        print(graph_numerator_edges1.adj[i][j].value)
        print(graph_numerator_edges1.adj[i][j].source_state)
        print(graph_numerator_edges1.adj[i][j].destination_state)
        print()

states = [[0, 0.01], [1, 0.000001], [1, 3, [True, 1], [False, 0]], [0, 1, 2, [True, True, 0.9999], [True, False, 0.99], [False, True, 0.99], [False, False, 0.0001]]]

def calculate_graph_probability(graph):
    answer = 1
    temp_states = states[:]
    
    for count in range(len(temp_states)):
        if len(temp_states[count]) == 2:
            s_1 = graph.adj[temp_states[count][0]][0].source_state
            
            if s_1 == True:
                answer = answer * temp_states[count][1]
            else:
                answer = answer * (1 - temp_states[count][1])
            
        
        if len(temp_states[count]) == 4:
            s_1 = graph.adj[temp_states[count][0]][0].source_state
            
            for j in range(len(graph_numerator_edges1.adj[temp_states[count][0]])):
                if graph_numerator_edges1.adj[temp_states[count][0]][j].value == temp_states[count][1]:
                    d_1 = graph_numerator_edges1.adj[temp_states[count][0]][j].destination_state
            
            if s_1 == True and d_1 == True:
                answer = answer * temp_states[count][2][1]
            
            if s_1 == False and d_1 == True:
                answer = answer * temp_states[count][3][1]
            
            if s_1 == True and d_1 == False:
                answer = answer * (1 - temp_states[count][2][1])
            
            if s_1 == False and d_1 == False:
                answer = answer * (1 - temp_states[count][3][1])
        
        if len(temp_states[count]) == 7:
            s_1 = graph.adj[temp_states[count][0]][0].source_state
            s_2 = graph.adj[temp_states[count][1]][0].source_state
            
            for j in range(len(graph_numerator_edges1.adj[temp_states[count][0]])):
                if graph_numerator_edges1.adj[temp_states[count][0]][j].value == temp_states[count][2]:
                    d_1 = graph_numerator_edges1.adj[temp_states[count][0]][j].destination_state
            
            if s_1 == True and s_2 == True and d_1 == True:
                answer = answer * temp_states[count][3][2]
            
            if s_1 == True and s_2 == False and d_1 == True:
                answer = answer * temp_states[count][4][2]
            
            if s_1 == False and s_2 == True and d_1 == True:
                answer = answer * temp_states[count][5][2]
            
            if s_1 == True and s_2 == False and d_1 == True:
                answer = answer * temp_states[count][6][2]
            
            
            
            if s_1 == True and s_2 == True and d_1 == False:
                answer = answer * (1 - temp_states[count][3][2])
            
            if s_1 == True and s_2 == False and d_1 == False:
                answer = answer * (1 - temp_states[count][4][2])
            
            if s_1 == False and s_2 == True and d_1 == False:
                answer = answer * (1 - temp_states[count][5][2])
            
            if s_1 == True and s_2 == False and d_1 == False:
                answer = answer * (1 - temp_states[count][6][2])
    
    return answer

print(calculate_graph_probability(graph_numerator_edges4))

numerator = calculate_graph_probability(graph_numerator_edges1) + calculate_graph_probability(graph_numerator_edges2) + calculate_graph_probability(graph_numerator_edges3) + calculate_graph_probability(graph_numerator_edges4)

denominator = calculate_graph_probability(graph_normalisation_edges1) + calculate_graph_probability(graph_normalisation_edges2) + calculate_graph_probability(graph_normalisation_edges3) + round(calculate_graph_probability(graph_normalisation_edges4), 5) + calculate_graph_probability(graph_normalisation_edges5) + calculate_graph_probability(graph_normalisation_edges6) + calculate_graph_probability(graph_normalisation_edges7) + round(calculate_graph_probability(graph_normalisation_edges8), 5)

print(numerator / denominator)

print(numerator)
print(denominator)