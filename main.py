# An algorithm to implement a heuristic search that find the best combination of students that are
# able to attend a particular time slot

# MODULES
import random
import pygame
from text import Text

RES = 192
RATIO_H_W = 0.35
DIMS = (6,9) #the dimensions of the screen are based on the width and height + headers and times
SCREEN = (DIMS[0]*RES,DIMS[1]*int(RES*RATIO_H_W))
TOTAL_DAYS = 8 * 5  #the total number of days in a week
# DD
# DD. STUDENT
# student = Student()
# interp. a student assigned to a classroom
class Student:
    def __init__(self,name,times):
        self.name = name 
        self.times = self.getTimes(times)

    def getTimes(self,times):
        timesAvail = []
        for time in times:
            try:
                timesAvail.append(int(time.split("_")[0])*8 + int(time[2:]))
            except:
                pass
        return (timesAvail)


# DD. LIST_OF_STUDENTS
# los = [STUDENT, ...]
# interp. the total number of students in the course
los = []
with open("schedules.txt","r",encoding="utf-8") as file:
    file = file.readlines()
    for line in file:
        line = line.strip()
        line = line.split("\t")
        student = Student(line[0],line[1:])
        los.append(student)



# DD. FINALLIST
# finalList = [{"NAME":str,"DAY":str, "TIME":int}, ...]
# interp. the collection of student metadata with scheduling times
finalList = []


# variables related to pygame
display = pygame.display.set_mode(SCREEN)

# DD. TILE
# tile = Tile()
# interp. a rectangular space in the screen representing a cell
class Tile:
    def __init__(self,c,r):
        self.c = c 
        self.r = r 
        self.w = RES 
        self.h = int(RES*RATIO_H_W)
        self.x = self.c * RES
        self.y = self.r * self.h
        self.color = "#1e1e1e"
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.text = Text(self.x+self.w//2, self.y+self.h//2,"",24)
    
    def drawCell(self):
        pygame.draw.rect(display,self.color,self.rect)

    def drawText(self,display):
        self.text.draw(display)

    def drawOutline(self):
        pygame.draw.rect(display,"white",self.rect,2)



# DD. GRID
# grid = [[TILE, ..., n=DIMS[0]], ..., n=DIMS[1]]
# interp. a 2D array of tiles
grid = []
for r in range(DIMS[1]):
    row = []
    for c in range(DIMS[0]):
        tile = Tile(c,r)
        row.append(tile)
    grid.append(row)


# DD. DAYS
# days = [str, ..., n=5]
# interp. the total number of days in a working week
days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

# DD. HOURS
# hours = [str, ...]
# interp. the list of hours of activity
hours = ["12:00 pm"," 1:00 pm"," 2:00 pm"," 3:00 pm"," 4:00 pm"," 5:00 pm"," 6:00 pm"," 7:00 pm"]


########################################### CODE #######################################################
# Update colors in the grid's first column and row
for r in range(DIMS[1]):
    grid[r][0].color = "#6e6e6e"
for c in range(DIMS[0]):
    grid[0][c].color = "#6e6e6e"

# Update the text to match that of the days of the week, for the first row (header) in the grid
for i,day in enumerate(days):
    grid[0][i+1].text.updateText(day)

for i,hour in enumerate(hours):
    grid[i+1][0].text.updateText(hour)



# FOR 1000 iterations:
    # While tries are less than 100
        # create random copy of original student LIST
        # pick a student at random from student LIST:
            # create random copy of STUDENT times
            # for every time available:
                # is time available?
                #   T: assign time, then append student and its time to finalLIst, then break
        # tries += 1
        # erase student from clone students LIST once it's done


bestFinal = []
bestScore = 0
conflictedStudents = []
for i in range(1000):
    tries = 0
    cloneLos = list(los)
    random.shuffle(cloneLos)
    localScore = 0
    candidateFinal = []
    while tries < 100 and len(cloneLos)>0:
        chosen = random.choice(cloneLos)
        cloneTimesStudent = list(chosen.times); random.shuffle(cloneTimesStudent)
        # assigned = False
        for time in cloneTimesStudent:
            # if the time is not assigned already, do so
            if time not in [st["TIME"] for st in candidateFinal]:
                st = {"NAME":chosen.name,"TIME":time,"DAY":""}
                candidateFinal.append(st)
                break
        tries += 1
        cloneLos.remove(chosen)
    if len(bestFinal)<= len(candidateFinal):
        bestFinal = candidateFinal
        conflictedStudents = list(cloneLos)




# Process the final list of students, assigned to their schedules
listToExport = list(bestFinal)
# for st in listToExport:
#     for i,day in enumerate(days):
#         if st["TIME"] - (i*8) <8 and i*8 <= st["TIME"]:
#             st["DAY"] = day
#             st["TIME"] = st["TIME"]%8

# [print(st["NAME"],st["DAY"],st["TIME"]) for st in bestFinal]
# print("\nConflicted students:")
# print("All students were assigned!") if len(conflictedStudents)==0 else [print(student["NAME"]) for student in conflictedStudents]

def findStudentByIndex_d(d):
    for st in bestFinal:
        if d == st["TIME"]:
            return st

[print(st["TIME"],st["NAME"]) for st in bestFinal]
r = 0
c = 0
for d in range(TOTAL_DAYS):
    if d%8 == 0 and d != 0: c+=1
    r = d%8
    st = findStudentByIndex_d(d)
    if isinstance(st,dict):
        grid[r+1][c+1].text.resize(24)
        grid[r+1][c+1].text.updateText(st["NAME"])
        grid[r+1][c+1].color = (random.randint(50,140),random.randint(50,140),random.randint(50,140))




def draw():
    display.fill("#1e1e1e")
    for row in grid:
        for tile in row:
            tile.drawCell()
    for row in grid:
        for tile in row:
            tile.drawOutline()
    for row in grid:
        for tile in row:
            tile.drawText(display)
    pygame.display.flip()


def update():
    [pygame.quit() for event in pygame.event.get() if event.type == pygame.QUIT]

while True:
    draw();update()