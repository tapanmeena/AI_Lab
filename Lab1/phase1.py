def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def GoalTest(curr,dest):
	if curr == dest:
		return True
	else:
		return False

def MoveGen(mat,visited,curr,dest,Todo,lst):
	neigh = []
	size = len(mat)
	visited.append(curr)
	for i in range(size):
		if(mat[curr][i] == 1):
			if(i in visited):
				continue
			else:
				if i in Todo:
					continue
				else:
					neigh.append(i)
					lst[i]=curr
	return neigh,visited,lst

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
Todo =[curr]
found = False
while(Todo):
	curr = Todo[0]
	print curr," -> "
	if(GoalTest(curr,dest)):
		print("Goal Reached")
		found = True
		break
	neigh, visited,lst = MoveGen(mat,visited,curr,dest,Todo,lst)
	if dest in neigh:
		lst[dest] = curr
	Todo.extend(neigh)
	Todo.remove(curr)
	if(not Todo):
		found = False
		print(" Path not Found")
		exit()

print " Path Followed is "
path = ""
p=" >- "
while(True):
	dest = lst[dest]
	path = path + str(dest+1)+p
	if dest == start:
		break
path = reverse(path)+" -> "+str(finalDest)

print path
# 1 1 1 1
# 1 1 0 1
# 1 0 1 0
# 1 1 0 1