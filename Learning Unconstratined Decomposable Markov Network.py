# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:56:31 2020

@author: Grant
"""

import itertools

num_variables = 6

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

#Numerator States
belief_potential_data = [[Belief_Edge(0, 0, True, True), [0.5, 0.5, 0.5, 0.5]], [Belief_Edge(0, 1, True, True), [0.25, 0.25, 0.25, 0.25]], [Belief_Edge(0, 2, True, True), [0.25, 0.25, 0.25, 0.25]], [Belief_Edge(0, 3, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Belief_Edge(1, 4, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Belief_Edge(2, 6, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Belief_Edge(3, 4, True, True), [0.25, 0.25, 0.25, 0.25]], [Belief_Edge(3, 5, True, True), [0.25, 0.25, 0.25, 0.25]], [Belief_Edge(3, 6, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Belief_Edge(4, 7, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Belief_Edge(5, 7, True, True), [0.25, 0.25, 0.25, 0.25]], [Belief_Edge(5, 8, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Belief_Edge(6, 8, True, True), [0.25, 0.25, 0.25, 0.25]]]            

markov_potential_data = [[Edge(0, 1, True, True), [0.25, 0.25, 0.25, 0.25]], [Edge(1, 2, True, True), [0.25, 0.25, 0.25, 0.25]], 
                         [Edge(1, 3, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Edge(1, 4, True, True), [0.25, 0.25, 0.25, 0.25]], [Edge(1, 4, True, True), [0.25, 0.25, 0.25, 0.25]], [Edge(2, 4, True, True), [0.25, 0.25, 0.25, 0.25]], 
                         [Edge(3, 4, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Edge(4, 5, True, True), [0.25, 0.25, 0.25, 0.25]]]

markov_separator_potential_data = [[[1, 4], 0.5], [[1], 0.5], [[4], 0.5]]

decomposable_markov_network = [Edge(0, 1, True, True), Edge(1, 2, True, True), Edge(1, 3, True, True),
                               Edge(1, 4, True, True), Edge(2, 4, True, True), Edge(3, 4, True, True),
                               Edge(4, 5, True, True)]

new_edges = []
for m in decomposable_markov_network:
    new_edges.append(m)

"""
new_graph = Graph(new_edges)

for i in range(len(new_graph.adj)):
    for j in range(len(new_graph.adj[i])):
        print(i)
        print(new_graph.adj[i][j].value)
        print(new_graph.adj[i][j].source_state)
        print(new_graph.adj[i][j].destination_state)
        print()
"""


#triangulation
newer_edges = []
for n in new_edges:
    newer_edges.append(n)
temp_edges = newer_edges


temp_network = Graph(temp_edges)


vertices = len(temp_network.adj)

remove_point_count = []

#while len(temp_edges) > 2:
#for e in range(3):
while (len(temp_edges) - vertices) > 1:
    for chosen_elimination_count in range(2, num_variables):
        remove_point_count.clear()
        temp_network = Graph(temp_edges)
        final_items = []
        for x in range(len(temp_network.adj)):
            items = []
            if len(temp_network.adj[x]) == chosen_elimination_count:
                for y in range(chosen_elimination_count):
                    items.append(temp_network.adj[x][y].value)
            if items == []:
                continue
            s = [[x, items[i], items[j]] for i in range(len(items)) for j in range(i+1, len(items))]
            if s == []:
                continue
            print(s)
            
            for t in s:
                final_items.append([t[0], t[1], t[2]])
        print(final_items)
        
        remove_point = 100
        changed = False
        if final_items != []:
            for r in final_items:
                links = False
                for a in range(len(temp_network.adj)):
                    for b in range(len(temp_network.adj[a])):
                        if r[1] == a and r[2] == temp_network.adj[a][b].value:
                            links = True
                        if r[1] == temp_network.adj[a][b].value and r[2] == a:
                            links = True
                            
                if links == False:
                    print("HERE")
                    remove_point = r[0]
                    remove_point_count.append(remove_point)
                    temp_edges.append(Edge(r[1], r[2], temp_network.adj[r[1]][0].source_state, temp_network.adj[r[2]][0].source_state))
                    new_edges.append(Edge(r[1], r[2], temp_network.adj[r[1]][0].source_state, temp_network.adj[r[2]][0].source_state))
                    changed = True
                    break
        
        if remove_point != 100:
            for c in temp_edges:
                if c.src == remove_point or c.dest == remove_point:
                #if c.src in remove_point_count or c.dest in remove_point_count:
                    #print("HERE")
                    temp_edges.remove(c)
        else:
            if final_items == []:
                continue
            
            for d in final_items:
                for c in temp_edges:
                    if c.src == d[0] or c.dest == d[0]:
                        temp_edges.remove(c)
                        break
                        
        
        if changed == True:
            break
    
    temp_network = Graph(temp_edges)
    vertices = len(temp_network.adj)
    
    print()

new_network = Graph(new_edges)

for p in range(len(new_network.adj)):
    for q in range(len(new_network.adj[p])):
        print(p)
        print(new_network.adj[p][q].value)
        print(new_network.adj[p][q].source_state)
        print(new_network.adj[p][q].destination_state)
        print()


variables_list = []

for n in range(num_variables):
    variables_list.append(n)

print(variables_list)

possible_options = []
for L in range(2, len(variables_list)+1):
    for subset in itertools.combinations(variables_list, L):
        possible_options.append(subset)

inclusion_factor = 0.2
clique_selection = []
included_variables = []
for a in reversed(possible_options):
    clique = False
    count = 0
    for b in a:
        length = len(a)
        for c in a:
            if b == c:
                continue
            for d in new_network.adj[b]:
                if d.value == c:
                    count = count + 1
    if count == length* (length - 1) and a not in clique_selection:
        clique_selection.append(a)

print(clique_selection)

set_length = len(clique_selection[0])

initial_selection = []
for a in clique_selection:
    if len(a) == set_length:
        initial_selection.append(a)

initial_selection.sort(key=sum)

clique_final_selection = []
clique_final_selection.append(initial_selection[0])

print(clique_final_selection)

for m in initial_selection[0]:
    included_variables.append(m)

similarity_limit = 0.8

while len(included_variables) != len(variables_list):
    common_separator = []
    for a in clique_final_selection:
        for b in clique_selection:
            if b == a:
                continue
            
            c_count = 0
            for c in b:
                if c in included_variables:
                    c_count = c_count + 1
            if c_count == len(b):
                #print("HERE")
                continue
            
            similarity_count = 0
            for x in a:
                for y in b:
                    if x == y:
                        similarity_count = similarity_count + 1
            
            #if similarity_count / len(a) > similarity_limit:
            #    continue
            
            common_separator.append([b, similarity_count / len(a)])
    
    common_separator.sort(key=lambda x: x[1], reverse=True)
    
    #print(common_separator)
    
    clique_final_selection.append(common_separator[0][0])
    
    for e in common_separator[0][0]:
        if e not in included_variables:
            included_variables.append(e)
        
print(clique_final_selection)

junction_tree = []

for a in clique_final_selection:
    temp = []
    for b in a:
        temp.append(b)
    junction_tree.append([temp, []])

print(junction_tree)
print(clique_final_selection)

for h in range(len(clique_final_selection)):
    if junction_tree[h][1] != []:
        #print("HERE")
        #print(junction_tree[h][1])
        continue
    
    temp_selection = []
    
    for i in range(len(clique_final_selection)):
        if clique_final_selection[h] == clique_final_selection[i]:
            continue
        
        similarity_count = 0
        for a in clique_final_selection[h]:
            for b in clique_final_selection[i]:
                if a == b:
                    similarity_count = similarity_count + 1
        if similarity_count == 0:
            continue
        
        temp_selection.append([h, i, similarity_count])
    
    #print("HERE")
    
    #print(temp_selection)
    
    temp_selection.sort(key=lambda x: x[2], reverse=True)
    insert_selection = []
    
    length = temp_selection[0][2]
    
    #print(temp_selection)
    
    limit = 0
    for j in temp_selection:
        if j[2] == length and limit < 1:
            insert_selection.append([j[0], j[1]])
            limit = limit + 1
    
    for k in insert_selection:
        junction_tree[k[0]][1].append(k[1])
        junction_tree[k[1]][1].append(k[0])

print(junction_tree)

#list out all the potentials
potentials = []
temp_record = []
for h in markov_potential_data:
    temp = [h[0].src, h[0].dest]
    temp_record.append(temp)
    
    counts = temp_record.count(temp)                   
    
    for j in range(len(junction_tree)):
        if h[0].src in junction_tree[j][0] and h[0].dest in junction_tree[j][0]:
            
            if counts > 1:
                counts = counts - 1
                continue
            
            temp_potential = 0
            
            if h[0].source_state == True and h[0].destination_state == True:
                temp_potential = h[1][0]
            elif h[0].source_state == True and h[0].destination_state == False:
                temp_potential = h[1][1]
            elif h[0].source_state == False and h[0].destination_state == True:
                temp_potential = h[1][2]
            else:
                temp_potential = h[1][3]
            
            potentials.append([temp, j, temp_potential])
            break

print(potentials)

for j in range(len(junction_tree)):
    junction_tree_potential = 1
    for k in potentials:
        if k[1] == j:
            junction_tree_potential = junction_tree_potential * k[2]
    junction_tree[j].append(junction_tree_potential)

print(junction_tree)

separator_potentials = []

for r in range(len(junction_tree)):
    #temp = []
    for s in junction_tree[r][1]:
        #if r == s:
        #    continue
        
        included = False
        for t in separator_potentials:
            if r in t[0] and s in t[0]:
                included = True
        
        similar_nodes = []
        
        for a in junction_tree[r][0]:
            for b in junction_tree[s][0]:
                if a == b:
                    similar_nodes.append(a)
        
        if included == False:
            separator_potential = 1
            
            for a in markov_separator_potential_data:
                if similar_nodes == a[0]:
                    separator_potential = separator_potential * a[1]
            
            separator_potentials.append([[r, s], similar_nodes, separator_potential])
    #separator_potentials.append(temp)

print(separator_potentials)

root = 0

past_trees = []

def max_likelihood_solution(root):
    global junction_tree
    global separator_potential
    
    cliques = junction_tree[root][1]
    past_trees.append(root)
    
    for c in cliques:
        separator_trees = [root, c]
        
        separator_potential = 1
        for y in separator_potentials:
            if separator_trees == y[0]:
                separator_potential = y[2]
                break
        
        junction_tree[c][2] = junction_tree[c][2] / separator_potential
        
        for d in junction_tree[c][1]:
            if d not in past_trees:
                max_likelihood_solution(d)
    
    return
        
max_likelihood_solution(0) 
print(junction_tree)
