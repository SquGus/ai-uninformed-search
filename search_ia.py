# https://www.alphagrader.com/courses/6/assignments/11
import re
import time
import copy

def input_to_stacks(input_string):
	stacks = []
	for stack_string in input_string.split(';'):
		stacks.append([ box for box in re.sub(r'[ ()]','',stack_string).split(',') if box != ''])
	for i,stack in enumerate(stacks):
		if len(stack) > 0:
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


def track_moves(stacks,moves):
	print(moves.values())
	current = moves[str(stacks)]
	search_string = str(current[1])
	# print(search_string)
	while True:
		# print(moves[str(current[0])])
		# time.sleep(2)
		if str(current[0]) in moves.keys():
			if moves[str(current[0])] == 0:
				break
		current = moves[str(current[0])]
		search_string = str(current[1]) + ';' + search_string
	return search_string
	# while True:
	# 	break




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


# def bfs(max_height,stacks,goal_stacks):
# 	visited = set()
# 	initial_stacks = (stacks,0)
# 	bfs_q = [initial_stacks]
# 	queue = [stacks]
# 	moves = {str(stacks): 0}
# 	# initial_node = str(copy.deepcopy(stacks)) 
# 	# moves = {initial_node: 0}
# 	step = 0
# 	while True:
# 		if len(bfs_q) == 0:
# 			return 'No solution found'
# 		current_state = bfs_q.pop()
# 		current_stack = queue.pop()
# 		visited.add(str(current_stack))
# 		step += 1
# 		# if step%1000 == 0:
# 			# print("Step ", step)
# 		for i,box in enumerate(current_stack):
# 			for j in range(len(current_stack)):
# 				if i != j and len(current_stack[j]) < max_height and len(current_stack[i]) > 0:
# 					# copy to not change the original list
# 					current_stack_copy = copy.deepcopy(current_stack) 
# 					neu_stacks, cost = move_box(i,j,current_stack_copy)
# 					if str(neu_stacks) not in visited or not test_in_list(neu_stacks, queue):
# 						if test_goal(neu_stacks,goal_stacks):
# 							moves[str(neu_stacks)] = (str(current_stack),(i,j))
# 							return neu_stacks, cost+current_state[1], track_moves(neu_stacks,moves)
# 						if check_better_cost(neu_stacks,cost+current_state[1], bfs_q):

# 							moves[str(neu_stacks)] = (str(current_stack),(i,j))

# 							bfs_q.insert(0,(neu_stacks,cost+current_state[1]))
# 							queue.insert(0,neu_stacks)

# def bfs(max_height,stacks,goal_stacks):
# 	visited = set()
# 	initial_stacks = (stacks,0)
# 	bfs_q = [initial_stacks]
# 	queue = [stacks]
# 	moves = {str(stacks): ''}

# 	while True:
# 		if len(bfs_q) == 0:
# 			return 'No solution found'
# 		current_state = bfs_q.pop()
# 		current_stack = queue.pop()
# 		visited.add(str(current_stack))
# 		# step += 1
# 		# if step%1000 == 0:
# 			# print("Step ", step)
# 		for i,box in enumerate(current_stack):
# 			for j in range(len(current_stack)):
# 				if i != j and len(current_stack[j]) < max_height and len(current_stack[i]) > 0:
# 					# copy to not change the original list
# 					current_stack_copy = copy.deepcopy(current_stack) 
# 					neu_stacks, cost = move_box(i,j,current_stack_copy)
# 					if str(neu_stacks) not in visited or not test_in_list(neu_stacks, queue):
# 						if test_goal(neu_stacks,goal_stacks):
# 							moves[str(neu_stacks)] = (str(current_stack),(i,j))
# 							return cost+current_state[1], track_moves(neu_stacks,moves)
# 						if check_better_cost(neu_stacks,cost+current_state[1], bfs_q):
# 							state_string = str(neu_stacks)
# 							if state_string in moves.keys():
# 								if isinstance(moves[state_string],str):
# 									moves[str(neu_stacks)] = (str(current_stack),(i,j))
# 							bfs_q.insert(0,(neu_stacks,cost+current_state[1]))
# 							queue.insert(0,neu_stacks)



def bfs(max_height,stacks,goal_stacks):
	moves = {stack_to_state(stacks): [(),0,(0,0), False]}
	queue = [stack_to_state(stacks)]

	while True:
		if len(queue) == 0:
			return 'No solution found'
		current_state = queue.pop()
		moves[current_state][3] = True

		for i,box in enumerate(current_state):
			for j in range(len(current_state)):
				if i != j and len(current_state[j]) < max_height and len(current_state[i]) > 0:
					neu_stacks, cost = move_box(i,j,state_to_stack(current_state))
					#if not visitado
					neu_state = stack_to_state(neu_stacks)

					# valid = False
					# if neu_state in moves.keys():
					# 	if not moves[neu_state][3]:
					# 		valid = True
					# if neu_state not in queue:
					# 	valid = True

					# if valid:



					if not moves[neu_state][3] or neu_state not in queue:
						if test_goal(neu_stacks, goal_stacks):
							moves[str(neu_stacks)] = (str(current_state),(i,j))
							return cost+current_state[1], track_moves(neu_stacks,moves)

						if check_better_cost(neu_stacks,cost+current_state[1], moves):
							state_string = str(neu_stacks)
							if state_string in moves.keys():
								if isinstance(moves[state_string],str):
									moves[str(neu_stacks)] = (str(current_state),(i,j))
							bfs_q.insert(0,(neu_stacks,cost+current_state[1]))
							queue.insert(0,neu_stacks)




max_height = int(input())
stacks = input_to_stacks(input())
stacks_original = list(stacks)
goal_stacks = input_to_stacks(input())


# falta guardar el historial
cost, moves = bfs(max_height,stacks,goal_stacks)
print(stacks)
print(cost)
print(moves)
print(goal_stacks)
