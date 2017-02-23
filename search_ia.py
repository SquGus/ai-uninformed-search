# https://www.alphagrader.com/courses/6/assignments/11
import re

def input_to_state(input_string):
	stacks = ()
	for stack_string in input_string.split('; '):
		stacks += (stack_string, )
	return stacks

def input_to_stacks(state_array):
	stacks = []
	for i, box in enumerate(state_array):
		stacks.append([])
		box = box.replace("(", "")
		box = box.replace(")", "")
		box = box.replace(" ", "")
		for item in box.split(","):
			stacks[i].append(item)
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
	visited = {}
	initial_stacks = (stacks, 0)
	dfs_stack = [initial_stacks]

	while True:
		if len(dfs_stack) == 0:
			return False #por el momento
		current_state = dfs_stack.pop()
		print(current_state)

		current_stack = current_state[0]
		print(current_stack)
		
		if test_goal(current_stack, goal_stacks):
			return True
		visited[current_state] = current_stack

		for i,box in enumerate(current_stack):
			for j in len(current_stack):
				if i != j and len(current_stack[j]) < max_height:
					neu_stacks, cost = move_box(i,j,current_stack)
					visited[(neu_stacks, cost)] = (neu_stacks)
					dfs_stack.append((neu_stacks,cost+current_state[1]))


max_height = int(input())
initial_state = input_to_state(input())
goal_state = input_to_state(input())
stacks = input_to_stacks(goal_state)

print(initial_state)
print(goal_state)

for stack in goal_state:
	print(stack)
# stacks_original = list(stacks)

# expand_nodes(max_height, stacks, goal_stacks)

# graph = {stacks:[]}

#FALTA CREAR LA BUSQUEDA QUE PARA CADA STACK INTENTE MOVER A LOS OTROS STACKS
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