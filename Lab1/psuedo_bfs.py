import Queue as queue

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def bfs(mat,curr,dest,visited,lst):
	q = queue.Queue(maxsize = 10000)
	neigh = []
	size = len(mat)
	q.put(curr)
	visited.append(curr)
	count = 1
	while(not q.empty()):
		top = q.get()
		visited.append(top)
		count = count + 1
		for i in range(size):
			if( mat[top][i] == 1 and (i not in visited)):
				q.put(i)
				visited.append(i)
				count=count+1
				lst[i] = curr
	path = ""
	print(lst)
	print(count)
	while(True):
		dest = lst[dest]
		path = path + str(dest+1)
		if dest == start:
			break
	path = reverse(path)
	print(path)

nodes = int(input("Number of Nodes "))
mat = [[int(j) for j in raw_input().split()] for i in range(nodes)]
for i in range(nodes):
	if (len(mat[i])!=nodes):
		print(" Invalid Input! Terminating...")
		exit(0)
lst = [-1] * nodes
print(lst)
visited=[]
curr=input("Starting Position ")-1
if((curr+1)>nodes):
	print "Invalid Start State"
	exit()
start = curr
dest=input("Destination ")-1
finalDest = dest +1
if(finalDest>nodes):
	print "Invalid Goal State"
	exit()

bfs(mat,curr,dest,visited,lst)