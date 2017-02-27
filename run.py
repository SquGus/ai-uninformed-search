import fileinput
import re
from queue import PriorityQueue

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
	cost = int(0.5 + abs(current - neu_position) + 0.5)
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

def track_moves(state,moves):
	current = moves[state]
	search_string = str(current[2])
	while True:
		if current[0] not in moves.keys():
			break
		current = moves[current[0]]
		if current[0] in moves.keys():
			search_string = str(current[2]) + '; ' + search_string
	return search_string

def cons_heuristic_cost(current_stacks,goal_stacks):
	total = 0
	for i,stack in enumerate(goal_stacks):
		if stack == 'X':
			pass
		else:
			for j,box in enumerate(stack):
				try:
					if stacks[i][j] != box:
						total += 1
				except:
					total += 1
	return total

def a_star_cons(max_height,stacks,goal_stacks):
	initial_state = stack_to_state(stacks)
	moves = {initial_state: [(),0,(0,0), False]}
	queue = PriorityQueue()
	queue.put((0, initial_state))

	while True:
		if queue.empty():
			return False
		current_state = queue.get()[1]
		moves[current_state][3] = True

		for i,box in enumerate(current_state):
			for j in range(len(current_state)):
				if i != j and len(current_state[j]) < max_height and len(current_state[i]) > 0:
					neu_stacks, cost = move_box(i,j,state_to_stack(current_state))
					#if not visitado
					neu_state = stack_to_state(neu_stacks)
					if neu_state not in moves.keys():
						moves[neu_state] = [current_state,cost+moves[current_state][1],(i,j), False]
						current_cost = cost+moves[current_state][1]
						if test_goal(neu_stacks, goal_stacks):
							return current_cost, track_moves(neu_state,moves)
						priority_cost = current_cost + cons_heuristic_cost(neu_stacks,goal_stacks)
						queue.put((priority_cost,neu_state))


max_height = int(input())
stacks = input_to_stacks(input())
stacks_original = list(stacks)
goal_stacks = input_to_stacks(input())


answer = a_star_cons(max_height,stacks,goal_stacks)
if answer:
	cost, moves = answer
	print(cost)
	print(moves,end='')
else:
	print('No solution found.',end='')