# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:21:07 2020

@author: Grant
"""

num_variables = 5

from random import randrange
import time

import itertools

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

class Node:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self, edges):
        self.adj = [None] * num_variables

        for i in range(num_variables):
            self.adj[i] = []

        for e in edges:
            node1 = Node(e.dest)
            node2 = Node(e.src)
            self.adj[e.src].append(node1)
            self.adj[e.dest].append(node2)

edge_sets = []

for m in range(num_variables):
    for n in range(num_variables):
        if m == n:
            continue
        
        if [m, n] in edge_sets or [n, m] in edge_sets:
            continue
        
        edge_sets.append([m, n])

print(edge_sets)

edges = []

for e in edge_sets:
    edges.append(Edge(e[0], e[1]))

print(edges)

initial_graph = Graph(edges)

for i in range(len(initial_graph.adj)):
    for j in range(len(initial_graph.adj[i])):
        print(i)
        print(initial_graph.adj[i][j].value)
        print()

print()
print()
print()

dependence_data = [[0, 1, [False], [[[2], False], [[3], False], [[4], False]], [[[2, 3], False], [[2, 4], False], [[3, 4], False]], [[[2, 3, 4], False]]], [0, 2, [True], [[[1], True], [[3], True], [[4], True]], [[[1, 3], True], [[1, 4], True], [[3, 4], True]], [[[1, 3, 4], True]]], 
                   [0, 3, [False], [[[1], False], [[2], False], [[4], False]], [[[1, 2], False], [[1, 4], False], [[2, 4], False]], [[[1, 2, 4], False]]], [0, 4, [True], [[[1], True], [[2], True], [[3], True]], [[[1, 2], True], [[1, 3], True], [[2, 3], False]], [[[1, 2, 3], False]]], 
                   [1, 2, [True], [[[0], True], [[3], True], [[4], True]], [[[0, 3], True], [[0, 4], True], [[3, 4], True]], [[[0, 3, 4], True]]], [1, 3, [True], [[[0], True], [[2], True], [[4], True]], [[[0, 2], True], [[0, 4], True], [[2, 4], True]], [[[0, 2, 4], True]]], 
                   [1, 4, [True], [[[0], True], [[2], True], [[3], True]], [[[0, 2], True], [[0, 3], True], [[2, 3], False]], [[[0, 2, 3], False]]], 
                   [2, 3, [True], [[[0], True], [[1], False], [[4], True]], [[[0, 1], False], [[0, 4], True], [[1, 4], False]], [[[0, 1, 4], False]]], [2, 4, [True], [[[0], True], [[1], True], [[3], True]], [[[0, 1], True], [[0, 2], True], [[1, 3], True]], [[[0, 1, 3], True]]],
                   [3, 4, [True], [[[0], True], [[1], True], [[2], True]], [[[0, 1], True], [[0, 2], True], [[1, 2], True]], [[[0, 1, 2], True]]]]

sets = []

def test_dependence(links, neighbours, graph):
    global dependence_data
    
    #if links == [4, 0]:
    #    print("HERE")
    #    print(neighbours)
    
    chosen_data = 0
    for a in range(len(dependence_data)):
        if links[0] in dependence_data[a] and links[1] in dependence_data[a]:
            chosen_data = a
            break
    
    if len(neighbours[0]) == 0:
        if dependence_data[chosen_data][2][0] == False:
            sets.append([links, None])
        
        return dependence_data[chosen_data][2][0]
    
    if len(neighbours[0]) == 1:
        for c in neighbours:
            for d in dependence_data[chosen_data][3]:
                if c[0] in d[0]:
                    if d[1] == False:
                        sets.append([links, [c[0]]])
                        return False
                    
                    #return d[1]
    
    if len(neighbours[0]) == 2:
        #if links == [4, 0]:
        #    print("HERE")
        #    print(neighbours)
        for c in neighbours:
        #    if links == [4, 0]:
        #        print(dependence_data[chosen_data][4])
            for d in dependence_data[chosen_data][4]:
        #        if links == [4, 0]:
        #            print(d)
                if c[0] in d[0] and c[1] in d[0]:
                    if d[1] == False:
                        sets.append([links, [c[0], c[1]]])
                        return False
                    #return d[1]
    
    if len(neighbours[0]) == 3:
        for c in neighbours:
            for d in dependence_data[chosen_data][5]:
                if c[0] in d[0] and c[1] in d[0] and c[2] in d[0]:
                    if d[1] == False:
                        sets.append([links, [c[0], c[1], c[2]]])
                        return False
                    #return d[1]
    
    return True

"""
def test_dependence(links, neighbours, graph):
    variable = randrange(100)
    
    if len(graph.adj[links[0]]) < 2 or len(graph.adj[links[1]]) < 2:
        return True
    
    if variable > 80:
        return False
    else:
        return True
"""

i = 0
less_neighbours = False

remove_links = []

while less_neighbours == False:
    for a in range(len(initial_graph.adj)):
        for b in range(len(initial_graph.adj[a])):
            source = a
            destination = initial_graph.adj[a][b].value
            
            if [source, destination] in remove_links or [destination, source] in remove_links:
                continue
            
            links = [source, destination]
            
            neighbours = []
            for c in range(len(initial_graph.adj[a])):
                if initial_graph.adj[a][c].value == destination:
                    continue
                neighbours.append(initial_graph.adj[a][c].value)
            
            #print(neighbours)
            
            if i > len(neighbours):
                continue
            
            neighbours_combination = list(itertools.combinations(neighbours, i))
            #print(links)
            #print(neighbours_combination)
            #print(len(neighbours_combination[0]))
            #print()
            
            dependence = test_dependence(links, neighbours_combination, initial_graph)
            #print(dependence)
            
            if dependence == False:
                remove_links.append(links)
    
    #print("HERE")
    #print(remove_links)
    for m in remove_links:
        for d in range(len(initial_graph.adj)):
            for e in range(len(initial_graph.adj[d])):
                source = d
                destination = initial_graph.adj[d][e].value
                
                #print("HERE")
                
                if source in m and destination in m:
                    #print("HERE")
                    initial_graph.adj[d].remove(initial_graph.adj[d][e])
                    
                    for h in range(len(initial_graph.adj[destination])):
                        if initial_graph.adj[destination][h].value == source:
                            initial_graph.adj[destination].remove(initial_graph.adj[destination][h])
                            break
                    break
            
    i = i + 1
    #print(i)
    
    #print("HERE")
    
    test_neighbours = False
    for d in range(len(initial_graph.adj)):
        if len(initial_graph.adj[d]) > i:
            test_neighbours = True
    
    if test_neighbours == False:
        less_neighbours = True




for i in range(len(initial_graph.adj)):
    for j in range(len(initial_graph.adj[i])):
        print(i)
        print(initial_graph.adj[i][j].value)
        print()
        
print(sets)

#unmarried collider
for s in sets:
    point_1 = s[0][0]
    point_2 = s[0][1]
    
    collider = 100
    
    for a in initial_graph.adj[point_1]:
        for b in initial_graph.adj[point_2]:
            if a.value == b.value and s[1] == None:
                collider = a.value
                continue
            
            if a.value == b.value and a.value not in s[1]:
                collider = a.value
    
    if collider != 100:
        remove_links = []
        for c in range(len(initial_graph.adj[collider])):
            if initial_graph.adj[collider][c].value == point_1 or initial_graph.adj[collider][c].value == point_2:
                remove_links.append(c)
                break
        #print(remove_links)
        initial_graph.adj[collider].remove(initial_graph.adj[collider][remove_links[0]])
        
        for c in range(len(initial_graph.adj[collider])):
            if initial_graph.adj[collider][c].value == point_1 or initial_graph.adj[collider][c].value == point_2:
                remove_links.append(c)
                break
        #print(remove_links)
        initial_graph.adj[collider].remove(initial_graph.adj[collider][remove_links[1]])

#path
def paths(source, destination, current_node, graph):
    if source == current_node:
        for a in graph.adj[current_node]:
            current_node = a.value
            
            if current_node == destination or current_node == source:
                return
            else:
                paths(source, destination, current_node, graph)
        
        return
    
    for a in graph.adj[current_node]:
        if a.value == destination:
            for b in range(len(graph.adj[destination])):
                if graph.adj[destination][b].value == current_node:
                    graph.adj[destination].remove(graph.adj[destination][b])
                    return
                
        current_node = a.value
        
        if current_node == source:
            return
        paths(source, destination, current_node, graph)
    return

points = []
for m in range(len(initial_graph.adj)):
    points.append(m)

combination_points = list(itertools.combinations(points, 2))


for c in combination_points:
    paths(c[0], c[1], c[0], initial_graph)
    #paths(c[1], c[0], c[1], initial_graph)

#Common orientation
for s in sets:
    point_1 = s[0][0]
    point_2 = s[0][1]
    
    collider = []
    
    for a in initial_graph.adj[point_1]:
        for b in initial_graph.adj[point_2]:
            if a.value == b.value:
                collider.append(a.value)
    
    for c in collider:
        for a in initial_graph.adj[point_1]:
            for b in initial_graph.adj[point_2]:
                for d in initial_graph.adj[c]:
                    if a.value == b.value == d.value:
                        for e in range(len(initial_graph.adj[a.value])):
                            if initial_graph.adj[a.value][e].value == c:
                                initial_graph.adj[a.value].remove(initial_graph.adj[a.value][e])

for i in range(len(initial_graph.adj)):
    for j in range(len(initial_graph.adj[i])):
        print(i)
        print(initial_graph.adj[i][j].value)
        print()

