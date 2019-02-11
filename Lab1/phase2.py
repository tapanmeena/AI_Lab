import Queue as queue

def bfs(mat,curr,dest):
	final = dest
	visited = [False] * len(mat)
	lst = [-1] * len(mat)
	q = queue.Queue(maxsize = 10000)
	q.put(curr)
	found = False
	pathFollowed=[]
	while(not q.empty()):
		top = q.get()
		if (top+1) not in pathFollowed:
			pathFollowed.append(top+1)
		visited[top] = True
		for i in range(len(mat)):
			if(mat[top][i] == 1):
				if(visited[i]):
					continue
				else:
					q.put(i)
					lst[i] = top
					if(i == dest):
						visited[i] = True
						found = True
						break
		if(found):
			break
	if(not visited[dest]):
			print "Path not Found"
			exit(0)
	path = []
	while(True):
		dest = lst[dest]
		path.append(dest+1)
		if(dest == curr):
			break
	fullPath=""
	for i in range(len(path)):
		fullPath = fullPath+str(path[len(path)-i-1]) +" -> "
	print "BFS: ",fullPath,final+1
	print "Nodes searched during BFS ",pathFollowed

def dfs(mat,curr,dest):
	final = dest
	visited = [False] * len(mat)
	lst = [-1] * len(mat)
	q=[]
	q.append(curr)
	found = False
	pathFollowed=[]
	while(q):
		top = q.pop()
		if (top+1) not in pathFollowed:
			pathFollowed.append(top+1)
		visited[top] = True
		for i in range(len(mat)):
			if(mat[top][i] == 1):
				if(visited[i]):
					continue
				else:
					if i not in q:
						q.append(i)
					lst[i] = top
					if(i == dest):
						visited[i] = True
						found = True
						break
		if(found):
			break
	if(not visited[dest]):
			print "Path not Found"
			exit(0)
	path = []
	while(True):
		dest = lst[dest]
		path.append(dest+1)
		if(dest == curr):
			break
	fullPath=""
	for i in range(len(path)):
		fullPath = fullPath+str(path[len(path)-i-1]) +" -> "
	print "DFS: ",fullPath,final+1
	print "Nodes searched in DFS ",pathFollowed

dfidNodesSearched=[]

def dfid(mat,curr,dest,depth):
	final = dest
	visited = [False] * len(mat)
	lst = [-1] * len(mat)
	q=[]
	q.append(curr)
	found = False
	level = 0
	pathFollowed=[]
	while(q):
		top = q.pop()
		level = level+1
		dfidNodesSearched.append(top+1)
		if((top+1) not in pathFollowed):
			pathFollowed.append(top+1)
		visited[top] = True
		for i in range(len(mat)):
			if(mat[top][i] == 1):
				if(visited[i]):
					continue
				else:
					if(i not in q):
						if (level<=depth):
							q.append(i)
					lst[i] = top
					if(i == dest):
						visited[i] = True
						found = True
						break
		if(found):
			break
	if(not visited[dest]):
			#print "Path not Found at Depth",depth
			return False
	path = []
	while(True):
		dest = lst[dest]
		path.append(dest+1)
		if(dest == curr):
			break
	fullPath=""
	for i in range(len(path)):
		fullPath = fullPath+str(path[len(path)-i-1]) +" -> "
	print "DFID: ",fullPath,final+1
#	print "Nodes searched during DFID",pathFollowed
	return True

nodes = int(input("Number of Nodes "))
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

bfs(mat,curr,dest)
dfs(mat,curr,dest)
for i in range(nodes):
	#print "Trying at Depth ",i
	if(dfid(mat,curr,dest,i)):
		print "Found at Depth",i+2
		break
print "Nodes searched during DFID",dfidNodesSearched

# example given in PDF file
'''
22
0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
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
