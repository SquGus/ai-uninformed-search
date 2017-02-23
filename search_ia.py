# https://www.alphagrader.com/courses/6/assignments/11
import re

# takes input and returns a list of lists
def input_to_stacks(input_string):
	stacks = []
	for stack_string in input_string.split(';'):
		stacks.append([ box for box in re.sub(r'[ ()]','',stack_string).split(',')])
	for i,stack in enumerate(stacks):
		if stack[0] == 'X':
			stacks[i] = 'X'
	return stacks

# takes list of lists and returns a tuple of tuples
def stack_to_state(stacks):
	state = ()
	for stack in stacks:
		column = ()
		for box in stack:
			column += (box, )
		state += (column, )

	return state

# takes tuple of tuples and returns a list of lists
def state_to_stack(state):
	stacks = []
	for i,column in enumerate(state):
		stacks.append([])
		for j in column:
			stacks[i].append(j)
	return stacks


def move_box(current,neu_position,stacks):
	neu_stacks = list(stacks)
	cost = 0.5 + abs(current - neu_position) + 0.5
	box = neu_stacks[current].pop()
	neu_stacks[neu_position].append(box)
	return neu_stacks, cost

def test_goal(stacks,goal_stacks):
	valid = True
	for i,stack in enumerate(goal_stacks):
		if stack == 'X':
			pass
		else:
			for j,box in enumerate(stack):
				try:
					if stacks[i][j] != box:
						valid = False
						break
				except:
					valid = False
	return valid

def expand_nodes(max_height,stacks,goal_stacks):
	visited = set()
	initial_stacks = (stacks,0)
	dfs_stack = [initial_stacks]

	while True:
		if len(dfs_stack) == 0:
			return False #por elmomento
		current_state = dfs_stack.pop()
		current_stack = current_state[0]
		if test_goal(current_stack,goal_stacks):
			return True
		visited.add(current_stack)

		for i,box in enumerate(current_stack):
			for j in len(current_stack):
				if i != j and len(current_stack[j]) < max_height:
					neu_stacks, cost = move_box(i,j,current_stack)
					visited.add(neu_stacks)
					dfs_stack.append((neu_stacks,cost+current_state[1]))

def bfs_search(max_height, current_state, goal_state):
	visited_states = set()
	node = (current_state, 0)
	if (test_goal(current_state, goal_state)):
		return True
	bfs_frontier = [node]

	while True:
		if len(bfs_frontier) == 0:
			return False
		node = bfs_frontier.pop()
		visited_states.add(node[0])
		for i,box in enumerate(node[0]):
			print(i)
			print(box)
			# for j in len(node[0]):
			# 	if i != j and len(node[0][j]) < max_height:
			# 		child_node = move(i, j, node[0][j]) 



max_height = int(input())
stacks = input_to_stacks(input())
goal_stacks = input_to_stacks(input())

initial_state = stack_to_state(stacks)
goal_state = stack_to_state(goal_stacks)

# expand_nodes(max_height,stacks,goal_stacks)
bfs_search(max_height, initial_state, goal_state)

# graph = {stacks:[]}

#FALTA CREAR LA VUSQUEDA QUE PARA CADA STACK INTENTE MOVER A LOS OTROS STACKS
# search = []
# actions for for
# movements = []



		

# print(stacks)
# print(cost)
# print(stacks)
# print(goal_stacks)
# print(test_goal(stacks,goal_stacks))
# cost = 

# append y pop