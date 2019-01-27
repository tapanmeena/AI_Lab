from Queue import PriorityQueue
import math
def GoalTest(check1,check2):
	if(check1==check2):
		return True
	else:
		return False

def hillclimb(mat,cordinatesList,curr,dest):
	final = dest
	visited = [False] * len(mat)
	parentList = [-1] * len(mat)
	qList = []
	qList.append(curr)
	found = False
	pathFollowed=[]
	PQ = PriorityQueue()
	distance = math.sqrt(pow((cordinatesList[curr][0]-cordinatesList[dest][0]),2)+pow((cordinatesList[curr][1]-cordinatesList[dest][1]),2))
	best = distance
	PQ.put((distance,curr))
	l=1
	while not PQ.empty():
		if l!=1:
			ls = heuristic1(mat,top[1],dest)
			distance = ls[0]
		l = l+1
		top = PQ.get()
		checkDistance = heuristic1(mat,top[1],dest)
		print "checkdistance",checkDistance[0],distance
		if(checkDistance[0]>distance):
			break
		while not PQ.empty():
			PQ.get()
		print "Node Searching is",top[1]+1
		qList.remove(top[1])
		while qList:
			qList.pop()
		if (top[1]+1) not in pathFollowed:
			pathFollowed.append(top[1]+1)
		visited[top[1]] = True
		for i in range(len(mat)):
			if(mat[top[1]][i] > 0):
				if(visited[i]):
					continue
				else:
					if i not in qList:
						PQ.put(heuristic1(mat,i,dest))
						print "Co-ordinates of",i+1,"is",cordinatesList[i][0],cordinatesList[i][1]
						distance = math.sqrt(pow((cordinatesList[i][0]-cordinatesList[dest][0]),2)+pow((cordinatesList[i][1]-cordinatesList[dest][1]),2))
						print "current distance and ith postion",distance,i+1
						qList.append(i)
					parentList[i] = top[1]
					if(GoalTest(i,dest)):
						visited[i] = True
						found = True
						break
		print "\n"
		# print "toSort is ",PQ.qsize()
		if(found):
			break
	if(not visited[dest]):
			print "Path not Found"
			exit(0)

	path = []
	while(True):
		dest = parentList[dest]
		path.append(dest+1)
		if(dest == curr):
			break

	fullPath=""
	for i in range(len(path)):
		fullPath = fullPath+str(path[len(path)-i-1]) +" -> "
	print "\nBest First Search:",fullPath,final+1
	print "Nodes searched in Best First Search",pathFollowed

def heuristic1(mat,i,dest):
	distance = math.sqrt(pow((cordinatesList[i][0]-cordinatesList[dest][0]),2)+pow((cordinatesList[i][1]-cordinatesList[dest][1]),2))
	return (distance,i)


nodes = int(input("Number of Nodes "))

cordinatesList = []
for i in range(0,nodes):
	print "Enter Station",i+1,"Co-ordinates"
	temp = input()
	cordinatesList.append(temp)
print cordinatesList

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

hillclimb(mat,cordinatesList,curr,dest)

# example given in PDF file
'''
22
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
'''
5
1,1
3,5
2,0
8,1
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