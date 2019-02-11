from Queue import PriorityQueue
import math
import operator

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
print "\n"
tabusearch(mat,cordinatesList,curr,dest)
