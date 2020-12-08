# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:56:31 2020

@author: Grant
"""

num_variables = 9

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
			node = Belief_Node(e.dest, e.source_state, e.destination_state)
			self.adj[e.src].append(node)

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
belief_data = [Belief_Edge(0, 1, True, True), Belief_Edge(0, 2, True, True), Belief_Edge(0, 3, True, True),
               Belief_Edge(1, 4, True, True),
               Belief_Edge(2, 6, True, True),
               Belief_Edge(3, 4, True, True), Belief_Edge(3, 5, True, True), Belief_Edge(3, 6, True, True),
               Belief_Edge(4, 7, True, True),
               Belief_Edge(5, 7, True, True), Belief_Edge(5, 8, True, True),
               Belief_Edge(6, 8, True, True)]

belief_network = Belief_Graph(belief_data)

for i in range(len(belief_network.adj)):
    for j in range(len(belief_network.adj[i])):
        print(i)
        print(belief_network.adj[i][j].value)
        print(belief_network.adj[i][j].source_state)
        print(belief_network.adj[i][j].destination_state)
        print()

print()
print()
print()

new_edges = []
for m in range(len(belief_network.adj)):
    for n in range(len(belief_network.adj[m])):
        new_edges.append(Edge(m, belief_network.adj[m][n].value, belief_network.adj[m][n].source_state, belief_network.adj[m][n].destination_state))

#moralisation
moralised_pairs = []
for a in range(num_variables):
    count = 0
    temp_pairs = []
    for b in range(len(belief_network.adj)):
        for c in range(len(belief_network.adj[b])):
            if belief_network.adj[b][c].value == a:
                count += 1
                temp_pairs.append(b)
                temp_pairs.append(belief_network.adj[b][c].source_state)
    if count == 2:
        new_edges.append(Edge(temp_pairs[0], temp_pairs[2], temp_pairs[1], temp_pairs[3]))

print(new_edges)
print()
print()
print()

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
                """
                for j in range(len(temp_network.adj[r[1]])):
                    for k in range(len(temp_network.adj[r[2]])):
                        if temp_network.adj[r[1]][j].value == temp_network.adj[r[2]][k].value:
                            links = True
                """     
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


