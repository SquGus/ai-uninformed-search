# https://www.alphagrader.com/courses/6/assignments/11
import re

def input_to_stacks(input_string):
	stacks = []
	for stack_string in input_string.split(';'):
		stacks.append([ box for box in re.sub(r'[ ()]','',stack_string).split(',')])
	for i,stack in enumerate(stacks):
		if stack[0] == 'X':
			stacks[i] = 'X'
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


max_height = int(input())
stacks = input_to_stacks(input())
stacks_original = list(stacks)
goal_stacks = input_to_stacks(input())


expand_nodes(max_height,stacks,goal_stacks)

# graph = {stacks:[]}

#FALTA CREAR LA VUSQUEDA QUE PARA CADA STACK INTENTE MOVER A LOS OTROS STACKS
search = []
# actions for for
movements = []



		

print(stacks)
# print(cost)
# print(stacks)
# print(goal_stacks)
# print(test_goal(stacks,goal_stacks))
# cost = 

# append y pop