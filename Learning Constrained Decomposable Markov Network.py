# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:56:31 2020

@author: Grant
"""

import itertools

from random import randrange

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

markov_potential_data = [[Edge(0, 1, True, True), [0.25, 0.25, 0.25, 0.25]], [Edge(0, 3, True, True), [0.25, 0.25, 0.25, 0.25]], 
                         [Edge(0, 4, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Edge(1, 2, True, True), [0.25, 0.25, 0.25, 0.25]], [Edge(1, 3, True, True), [0.25, 0.25, 0.25, 0.25]], 
                         [Edge(2, 3, True, True), [0.25, 0.25, 0.25, 0.25]],
                         [Edge(3, 4, True, True), [0.25, 0.25, 0.25, 0.25]]]

markov_separator_potential_data = [[[1, 4], 0.5], [[1], 0.5], [[4], 0.5]]

decomposable_markov_network = [Edge(0, 1, True, True), Edge(0, 3, True, True), Edge(0, 4, True, True),
                               Edge(1, 2, True, True), Edge(1, 3, True, True), 
                               Edge(2, 3, True, True),
                               Edge(3, 4, True, True)]

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
"""
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
    
    #print("HERE")
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

past_trees = []

def propagate(current_tree):
    global junction_tree
    global separator_potentials
    global past_trees
    global markov_potential_data
    
    tree_node = junction_tree[current_tree][0][:]
    
    separator = []
    for a in junction_tree[current_tree][1]:
        if a not in past_trees:
            separator.append(a)
            past_trees.append(a)
    
    if current_tree not in past_trees:
        past_trees.append(current_tree)
    
    #print(past_trees)
    
    if separator == []:
        return
    
    separator_node = []
    for m in separator:
        for n in range(len(separator_potentials)):
            if current_tree in separator_potentials[n][0] and m in separator_potentials[n][0]:
                temp = separator_potentials[n][1]
                temp_tree = junction_tree[current_tree][0][:]
                
                for a in temp:
                    if a in temp_tree:
                        temp_tree.remove(a)
                
                separator_node.append([temp_tree, n, [current_tree, m]])
    #print("HERE")
    #print(tree_node)
    #print(separator_node)
    
    #print(potentials)    
    
    branches = []
    for p in potentials:
        if p[1] == current_tree:
            branches.append(p)
    #print(branches)
    
    
    
    #print(belief_potential_data[0][0].dest)
    
    for e in separator_node:
        for b in branches:
            temp_potential = 0
            
            for h in markov_potential_data:
                source = h[0].src
                destination = h[0].dest
                
                #print(source)
                #print(destination)
                #print(b[0][0])
                #print(b[0][1])
                #print("HERE")
                
                if b[0][0] == h[0].src and b[0][1] == h[0].dest:
                    if b[0][0] in e[0] and b[0][1] in e[0]:
                        temp_potential = h[1][0] + h[1][1] + h[1][2] + h[1][3]
                    elif b[0][0] in e[0]:
                        temp_potential = h[1][0] + h[1][1]
                    elif b[0][1] in e[0]:
                        temp_potential = h[1][2] + h[1][3]
                    
                    break
            
            if temp_potential != 0:
                b[2] = temp_potential
    
        solution = 1
        for r in branches:
            #print(r)
            
            for y in potentials:
                if y[0] == r[0]:
                    y[2] = r[2]
            
            solution = solution * r[2]
        
        old_solution = separator_potentials[e[1]][2]
        separator_potentials[e[1]][2] = solution
        #print(old_solution)
        #print(separator_potentials[e[1]][2])
        
        #print(junction_tree)
        
        junction_tree[e[2][1]][2] = junction_tree[e[2][1]][2] * solution / old_solution
    
        #print(junction_tree)
        
        propagate(e[2][1])

for n in range(10):
    clique = randrange(3)
    
    past_trees = []
    
    if clique == 0:
        past_trees = [1]
        propagate(2)
        
        past_trees = [2]
        propagate(1)
    
    if clique == 1:
        propagate(2)
    
    if clique == 2:
        propagate(1)
    
    print(potentials)
    
    select_potentials = []
    for p in range(len(potentials)):
        if potentials[p][1] == clique:
            select_potentials.append(p)
    
    convergence = False
    while convergence == False:
        for q in select_potentials:
            variables = junction_tree[clique][0]
            
            #changing the denominator based on this variable
            modify_variables = []
            for v in variables:
                if v not in potentials[q][0]:
                    modify_variables.append(v)
            
            e = 1
            for m in markov_potential_data:
                if m[0].src in potentials[q][0] and m[0].dest in potentials[q][0]:
                    s_state = new_network.adj[m[0].src][0].source_state
                    d_state = new_network.adj[m[0].dest][0].source_state
                    
                    if s_state == True and d_state == True:
                        e = e * (m[1][0])
                    elif s_state == True and d_state == False:
                        e = e * (m[1][1])
                    elif s_state == False and d_state == True:
                        e = e * (m[1][2])
                    else:
                        e = e * (m[1][3])
                        
                    break
            
            other_potentials = []
            for r in select_potentials:
                if r != potentials[q]:
                    other_potentials.append(r)
            
            select_separator_potentials = []
            for s in separator_potentials:
                if s[1][0] in junction_tree[clique][0] and s[1][1] in junction_tree[clique][0]:
                    select_separator_potentials.append(s)
            
            denominator = 1
            
            for o in other_potentials:
                first_changing = False
                if potentials[o][0][0] in modify_variables:
                    first_changing = True
                
                second_changing = False
                if potentials[o][0][1] in modify_variables:
                    second_changing = True
                
                for m in markov_potential_data:
                    if m[0].src in potentials[o][0] and m[0].dest in potentials[o][0]:
                        if first_changing == True and second_changing == True:
                            denominator = denominator * (m[1][0] + m[1][1] + m[1][2] + m[1][3])
                        elif first_changing == True:
                            denominator = denominator * (m[1][0] + m[1][1])
                        elif second_changing == True:
                            denominator = denominator * (m[1][2] + m[1][3])
                        
                        break
                
                denominator = denominator * potentials[o][2]
            
            for c in select_separator_potentials:
                denominator = denominator * c[2]
            
            potentials[q][2] = e / denominator
        
        convergence = True
        convergence_requirement = 0.3
        for x in select_potentials:
            for y in select_potentials:
                difference = 0
                if x == y:
                    continue
                
                difference = abs(potentials[x][2] - potentials[y][2])
                
                if difference > convergence_requirement:
                    convergence = False
        
print(junction_tree)
