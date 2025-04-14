#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Agent(object):
	def SearchSolution(self, state):
		return []
		
class AgentSnake(Agent):    
	def SearchSolution(self, state):
		FoodX = state.FoodPosition.X
		FoodY = state.FoodPosition.Y

		HeadX = state.snake.HeadPosition.X #L
		HeadY = state.snake.HeadPosition.Y #T
		
		DR = FoodY - HeadY
		DC = FoodX - HeadX
		
		plan = []
		
		F = -1
		if(DR == 0 and state.snake.HeadDirection.X*DC < 0):
			plan.append(0)
			F = 6
			
		if(state.snake.HeadDirection.Y*DR < 0):
			plan.append(3)
			if(DC == 0):
				F = 9
			else:
				DC = DC - 1
		Di = 6
		if(DR < 0):
			Di = 0
			DR = -DR
		for i in range(0,int(DR)):
			plan.append(Di)
		Di = 3
		if(DC < 0):
			Di = 9
			DC = -DC
		for i in range(0,int(DC)):
			plan.append(Di)
		if(F > 0):
			plan.append(F)
			F = -1
			
		return plan
	
	def showAgent():
		print("A Snake Solver By MB")
		
# You code of agent goes here
# You must create three agents one using A*, second using greedy best first search and third using an uninformed algo of your choice to make a plan

class DFS_Agent(Agent):
    def SearchSolution(self, state):
        visited = set()  # To keep track of visited positions
        stack = [(state.snake.HeadPosition.X, state.snake.HeadPosition.Y, [])]  # Initialize stack with starting position and empty plan
        
        while stack:
            x, y, plan = stack.pop()  # Pop the top position and plan from the stack
            
            if (x, y) in visited:
                continue  # Skip if position is already visited
            
            # Mark current position as visited
            visited.add((x, y))
            
            # If food is found at the current position, return the plan
            if x == state.FoodPosition.X and y == state.FoodPosition.Y:
                return plan
            
            # Generate new positions and plans based on possible moves (up, down, left, right)
            for dx, dy, direction in [(0, -1, 0), (0, 1, 6), (1, 0, 3), (-1, 0, 9)]:
                nx, ny = x + dx, y + dy  # New position coordinates
                
                # Check if the new position is within bounds and not blocked
                if 0 <= nx < state.maze.WIDTH and 0 <= ny < state.maze.HEIGHT and state.maze.MAP[ny][nx] != -1:
                    stack.append((nx, ny, plan + [direction]))  # Push the new position and updated plan onto the stack
                    
        return []  # Return an empty plan if food cannot be reached

 
	


# In[ ]:




