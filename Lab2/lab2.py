from Queue import PriorityQueue
import math

def GoalTest(check1,check2):
	if(check1==check2):
		return True
	else:
		return False

def MoveGen(mat,start):
	neigh = []
	for i in range(len(mat)):
		if(mat[start][i] > 0):
			neigh.append(i)
	return neigh

def bestfs(mat,cordinatesList,curr,dest):
	print "Best First Search Start:"
	final = dest
	visited = [False] * len(mat)	#visited list
	parentList = [-1] * len(mat)	#contains child's parent
	qList = []
	qList.append(curr)				#list contains element to iterate through
	found = False					#True if destination is found
	NodesSearched=[]				#path followed during traversing
	PQ = PriorityQueue()
	temp = heuristic(mat,curr,dest)		
	PQ.put((temp[0],curr))      	#contains (distance, node)
	while not PQ.empty():
		top = PQ.get()				#Node to search
#		print "Node Searching is",top[1]+1
		qList.remove(top[1])

		if (top[1]+1) not in NodesSearched:
			NodesSearched.append(top[1]+1)
		visited[top[1]] = True		#mark node as visited

		neighbours = MoveGen(mat,top[1])			#Ask neighbours from MoveGen Function

		for i in range(len(neighbours)):			#iterate through all neighbours
			if(visited[neighbours[i]]):
				continue
			else:
				if neighbours[i] not in qList:
					PQ.put(heuristic(mat,neighbours[i],dest))   #adding element in Priority Queue(heuristic,node)
					qList.append(neighbours[i])
				parentList[neighbours[i]] = top[1]
				if(GoalTest(neighbours[i],dest)):				#check GoalTest
					visited[neighbours[i]] = True
					found = True
					break
		if(found):			#if destination found
			break
	if(not visited[dest]):
			print "Path not Found"
			exit(0)

	path = []
	while(True):					#iterate through parentlist to found path followed
		dest = parentList[dest]
		path.append(dest+1)
		if(dest == curr):
			break

	fullPath=""
	for i in range(len(path)):			#creating path
		fullPath = fullPath+str(path[len(path)-i-1]) +" -> "
	print "Best First Search:",fullPath,final+1
	print "Nodes searched in Best First Search",NodesSearched

def hillclimb(mat,cordinatesList,curr,dest):
	print "Hill Climbing Start:"
	final = dest
	visited = [False] * len(mat)	#visited list
	parentList = [-1] * len(mat)	#contains child's parent
	qList = []
	qList.append(curr)				#list contains element to iterate through
	found = False					#True if destination is found
	NodesSearched=[]				#path followed during traversing
	PQ = PriorityQueue()			
	temp = heuristic(mat,curr,dest)
	PQ.put((temp[0],curr))
	distance = temp[0]
	l=1
	while not PQ.empty():
		if l!=1:
			temp = heuristic(mat,top[1],dest)
			distance = temp[0]
		l = l+1
		top = PQ.get()							#Node to search
		checkDistance = heuristic(mat,top[1],dest) #check its distance from destination

		if(checkDistance[0]>distance):			#check if current distance is best or not
			break

		while not PQ.empty():					#clearing Priority Queue
			PQ.get()

		print "Node Searching is",top[1]+1
		qList.remove(top[1])

		while qList:							#clearing main list
			qList.pop()

		if (top[1]+1) not in NodesSearched:
			NodesSearched.append(top[1]+1)		#adding current Station to nodes Searched
		visited[top[1]] = True					#marking it visited
		neighbours = MoveGen(mat,top[1])		#asking neighbours from movegen

		for i in range(len(neighbours)):		#iterate through neighbours
			if(visited[neighbours[i]]):
				continue
			else:
				if neighbours[i] not in qList:
					PQ.put(heuristic(mat,neighbours[i],dest))	#calculating heuristic vallue
					qList.append(neighbours[i])
				parentList[neighbours[i]] = top[1]				
				if(GoalTest(neighbours[i],dest)):				#checking GoalTest
					visited[neighbours[i]] = True
					found = True
					break
		if(found):
			break
	if(not visited[dest]):
			print "Path not Found"
			exit(0)

	path = []
	while(True):				#iterate through parentlist to found path followed
		dest = parentList[dest]
		path.append(dest+1)
		if(dest == curr):
			break

	fullPath=""
	for i in range(len(path)):    	#creating path
		fullPath = fullPath+str(path[len(path)-i-1]) +" -> "
	print "Hill Climbing:",fullPath,final+1
	print "Nodes searched in Hill Climb",NodesSearched

def heuristic(mat,i,dest): #calculate Eucleadin Distance between given and Destination cordinates
	distance = math.sqrt(pow((cordinatesList[i][0]-cordinatesList[dest][0]),2)+pow((cordinatesList[i][1]-cordinatesList[dest][1]),2))
	return (distance,i)




nodes = int(input("Number of Nodes "))

cordinatesList = []
for i in range(0,nodes):
	print "Enter Station",i+1,"Co-ordinates"
	temp = input()
	cordinatesList.append(temp)
#print cordinatesList

print "Enter Adjancy Matrix: "
mat = [[int(j) for j in raw_input().split()] for i in range(nodes)]
for i in range(nodes):
	if (len(mat[i])!=nodes):
		print(" Invalid Input! Terminating...")
		exit(0)

curr=input("Starting Position ")-1
if((curr+1)>nodes):
	print "Invalid Start State"
	exit()

dest=input("Destination ")-1
if((dest+1)>nodes):
	print "Invalid Goal State"
	exit()

if(curr == dest):
	print("Start State and Goal State is same")
	exit()

bestfs(mat,cordinatesList,curr,dest)
print "\n"
hillclimb(mat,cordinatesList,curr,dest)


# example given in PDF file

'''
5
1,1
3,5
8,1
2,1
8,5
0 1 1 1 0
1 0 0 0 1
1 0 0 1 1
1 0 1 0 0
0 1 1 0 1

22
0,2
6,0
9,1
7,5
1,5
3,9
9,14
8,8
12,9
14,5
13,1
16,4
18,0
21,1
19,6
17,9
22,8
15,11
7,13
8,17
20,15
15,18
0 1 0 0 8 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
8 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0
0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0
'''
