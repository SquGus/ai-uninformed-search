# https://www.alphagrader.com/courses/6/assignments/11
import re
import time
import copy

def input_to_stacks(input_string):
	stacks = []
	for stack_string in input_string.split(';'):
		stacks.append([ box for box in re.sub(r'[ ()]','',stack_string).split(',')])
	for i,stack in enumerate(stacks):
		if stack[0] == 'X':
			stacks[i] = 'X'
	return stacks

def move_box(current,neu_position,stacks):
	neu_stacks = stacks[:]
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

def test_in_list(stack,stacks):
	for x in stacks:
		if test_goal(stack,x):
			return True
	return False


def check_better_cost(stacks, cost, queue):
	valid = False
	not_in_list = True
	for state in queue:
		if test_goal(stacks,state[0]):
			not_in_list = False
			if cost < state[1]:
				valid = True

	if not_in_list:
		return True
	else:
		return valid



def dfs(max_height,stacks,goal_stacks):
	visited = set()
	initial_stacks = (stacks,0)
	dfs_stack = [initial_stacks]
	stacks = [stacks]
	while True:
		if len(dfs_stack) == 0:
			return 'No solution found'
		current_state = dfs_stack.pop()
		current_stack = stacks.pop()
		visited.add(str(current_stack))
		for i,box in enumerate(current_stack):
			for j in range(len(current_stack)):
				if i != j and len(current_stack[j]) < max_height and len(current_stack[i]) > 0:
					current_stack_copy = copy.deepcopy(current_stack)
					neu_stacks, cost = move_box(i,j,current_stack_copy)
					if str(neu_stacks) not in visited or not test_in_list(neu_stacks, stacks):
						if test_goal(neu_stacks,goal_stacks):
							return neu_stacks, cost+current_state[1]
						if check_better_cost(neu_stacks,cost+current_state[1], dfs_stack):
							dfs_stack.append((neu_stacks,cost+current_state[1]))
							stacks.append(neu_stacks)


def bfs(max_height,stacks,goal_stacks):
	visited = set()
	initial_stacks = (stacks,0)
	bfs_q = [initial_stacks]
	queue = [stacks]
	while True:
		if len(bfs_q) == 0:
			return 'No solution found'
		current_state = bfs_q.pop()
		current_stack = queue.pop()
		visited.add(str(current_stack))
		for i,box in enumerate(current_stack):
			for j in range(len(current_stack)):
				if i != j and len(current_stack[j]) < max_height and len(current_stack[i]) > 0:
					# copy to not change the original list
					current_stack_copy = copy.deepcopy(current_stack) 
					neu_stacks, cost = move_box(i,j,current_stack_copy)
					if str(neu_stacks) not in visited or not test_in_list(neu_stacks, queue):
						if test_goal(neu_stacks,goal_stacks):
							return neu_stacks, cost+current_state[1]
						if check_better_cost(neu_stacks,cost+current_state[1], bfs_q):




							#############################################################################
							#############################################################################
							# Agregar el padre del stack, para hacer una lista de estados como historia #
							#############################################################################
							#############################################################################
							bfs_q.insert(0,(neu_stacks,cost+current_state[1]))
							queue.insert(0,neu_stacks)


max_height = int(input())
stacks = input_to_stacks(input())
stacks_original = list(stacks)
goal_stacks = input_to_stacks(input())


# falta guardar el historial
print(bfs(max_height,stacks,goal_stacks))
