################################################################
#Dijkstra's Algorithm to Find the shortest from any Source
################################################################
#Written by
#Avinash Shanker
#NetID: AXS8570
#ID: 1001668570
################################################################
#Usage: Run in any Python IDE and Enter inputs as below example
#Number of Nodes: 3
#Number of Connections: 3
#Node-1,Node-2,Weight: A,B,1
#Node-1,Node-2,Weight: B,C,3
#Node-1,Node-2,Weight: C,A,9
#Intermediate Output (Adjacency Matrix):
#[0, 1, 9]
#[1, 0, 3]
#[9, 3, 0]
#Enter Source Node: A
#Output from Source Node 'A':
#A-->B (A,B,1)
#A-->C (A,B,C,4)
################################################################

import ast
import os

#import ast is imported to covert input file to List type in python
#import os for file write operations and remove

#This class is used to create adjacency matrix
class Adjacency_Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    #Add new edges to graph
    def addEdge(self, v1, v2,w1):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = w1
        self.adjMatrix[v2][v1] = w1

    #Print Adjacency matrix        
    def print_adj_string(self):
        f=open("adjacency.txt", "w+")
        print("\nIntermediate Output (Adjacency Matrix):")
        for row in self.adjMatrix:
            print(row)
        f.write(str(self.adjMatrix))
        print('\n')

#Converting Input Alphabet to Numeric value        
def alplha_num(key_value):
    if key_value=='A' or key_value=='a' : return 0
    if key_value=='B' or key_value=='b' : return 1
    if key_value=='C' or key_value=='c' : return 2
    if key_value=='D' or key_value=='d' : return 3
    if key_value=='E' or key_value=='e' : return 4
    if key_value=='F' or key_value=='f' : return 5
    if key_value=='G' or key_value=='g' : return 6
    if key_value=='H' or key_value=='h' : return 7
    if key_value=='I' or key_value=='i' : return 8     
        
def main():
        node=input("Number of Nodes: ")
        g = Adjacency_Graph(int(node))
        connections =input("Number of Connections: ")
        #input Node details from user
        #It must be in format A,B,Weight(eg: A,B,4)
        for x in range(0,int(connections)):
            a,b,w1 = input('Node-1,Node-2,Weight: ').split(",")
			#Converting Input alplhabets to number
            a = alplha_num(a)
            b = alplha_num(b)
            g.addEdge(int(a),int(b),int(w1));
        g.print_adj_string()


#This Class represents a Graph format and pasrsing
class Spanning_Graph: 
    #Function to find the vertex with minimum distance
    def minimum_distance(self,dist,queue): 
        #Initialising minimum value to minus one 
        minimum = float("Inf") 
        min_index = -1
        # from the dist array,pick one which 
        # has min value and is till in queue 
        for i in range(len(dist)): 
            if dist[i] < minimum and i in queue: 
                minimum = dist[i] 
                min_index = i 
        return min_index 

    #Fucntion to return Alphabet value for Integer values		
    def alplhabets(self,key_value):
        if key_value==0: return 'A'
        if key_value==1: return 'B'
        if key_value==2: return 'C'
        if key_value==3: return 'D'
        if key_value==4: return 'E'
        if key_value==5: return 'F'
        if key_value==6: return 'G'
        if key_value==7: return 'H'
        if key_value==8: return 'I'

    #Function to print shortest path  from source input from user to j
    def Display_Path(self, parent, j): 
        if parent[j] == -1 : 
            j_alpha = self.alplhabets(j)
			#used flush and end to keep output in same line
            print (j_alpha + ',', sep=' ', end='', flush=True),
            return  
        self.Display_Path(parent , parent[j])
        j_alpha = self.alplhabets(j) 
        print (j_alpha + ',', sep=' ', end='', flush=True),
                        

    #Function is used to display the complete solution from Source Node to Destination Node
	 #Also the route and the shortest path from source to destination
    def Display_Solution(self, dist, parent,src): 
        src = src
        src_alpha = self.alplhabets(src)
        print("Output from Source Node \'%s\':" % (src_alpha)) 
        for i in range(0, len(dist)):
            i_alpha = self.alplhabets(i)
            src_alpha = self.alplhabets(src)
            if i_alpha != src_alpha:
                print("%s-->%s (" % (src_alpha, i_alpha), sep=' ', end='', flush=True)
                self.Display_Path(parent,i)
                print("%d)" % (dist[i]))


    #This is key function which performs Dijkstra Shortest Path computation
	#Function obtains a List from a TXT file format
	#We also pass the Source Node as SRC from which shortest path is obtained for each subsequent node
    def dijkstra(self, graph, src): 
        row = len(graph) 
        col = len(graph[0])
        src = src 
        # Initialize all distances as INFINITE initailly
        dist = [float("Inf")] * row 
        #Parent array to store 
        # shortest path tree 
        parent = [-1] * row
        #Distance from Source to Source is Assigned to Zero		
        dist[src] = 0
    
        queue = [] 
        for i in range(row): 
            queue.append(i) 
        
		#While loop will parse the entire List to find the minimum distance vertex
        while queue: 
            u = self.minimum_distance(dist,queue) 
            # remove min element     
            queue.remove(u) 
            
			#Checks the shortest path in given list for each iteration
            for i in range(col): 
                if graph[u][i] and i in queue: 
                    if dist[u] + graph[u][i] < dist[i]: 
                        dist[i] = dist[u] + graph[u][i] 
                        parent[i] = u 
        #At the end of while loop calling print to display that path
        self.Display_Solution(dist,parent,src) 

#Main Function call           
if __name__ == '__main__':
   main()
   
g= Spanning_Graph() 

#Reading the Adjacency Matrix written in the file as list and using it as input
#Direct Input can be given in the form of a file
with open('adjacency.txt', 'r') as f:
    mylist = ast.literal_eval(f.read())

graph = mylist
g.dijkstra(graph,0)   
source = input("\nEnter Different Source Node: ")
source1 = alplha_num(source)
g.dijkstra(graph,int(source1))    

#To Removed the file created, can be commented if you wish to view the file
#os.remove("adjacency.txt")