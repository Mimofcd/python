import random
global score
def grid_def():
    global grid
    grid=[]
    for row in range(4):
        grid.append([])
        for col in range(4):
            dice=random.randint(1,6)
            grid[row].append(dice)
def display_grid():
    global grid
    for row in range(4):
        st="| "
        for col in range(4):
            st = st+str(grid[row][col])+" |"
        print(st)
def is_even(number):
    if number%2==0:
        return True
    else:
        return False

def is_odd(number):
    if number%2==1:
        return True
    else:
        return False
score=0
grid_def()
display_grid()
# grid=[[2,2,2,4],[1,1,1,1],[1,2,2,1],[6,7,3,5]]
if is_even(grid[0][0]) and is_even(grid[0][3]) and is_even(grid[3][0]) and is_even(grid[3][3]):
    score=score+20
if is_odd(grid[0][0]) and is_odd(grid[0][3]) and is_odd(grid[3][0]) and is_odd(grid[3][3]):
    score=score+20
if is_even(grid[0][0]) and is_even(grid[1][1]) and is_even(grid[2][2]) and is_even(grid[3][3]):
    score=score+20
if is_odd(grid[0][0]) and is_odd(grid[1][1]) and is_odd(grid[2][2]) and is_odd(grid[3][3]):
    score=score+20
count=0
for i in range(4):
    for item in grid[i]:
        if is_even(item):
            count=count+1
    if count==4:
        score=score+20
    count=0        
for i in range(4):
    for item in grid[i]:
        if is_odd(item):
            count=count+1
    if count==4:
        score=score+20
    count=0 
print(score)