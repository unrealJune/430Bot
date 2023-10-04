from canvasapi import Canvas
import requests
from datetime import datetime
import os

# Canvas API URL
API_URL = os.environ['CANVAS_API_URL']
API_KEY = os.environ['CANVAS_API_KEY']
COURSE = 1350066

pwd = os.getcwd()

ASSIGNMENT_FILE = pwd + "/assignments.txt"
LOG_FILE = pwd + "/log.txt"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

#get list of assignments from file
#save list of assignments to a file
f = open(ASSIGNMENT_FILE, "r")
parse = f.read()
f.close()
#split parse into list of assignments
assignments = parse.split(",")

# #print assignments
# for ass in assignments:
#     print(ass)


CSClass =  canvas.get_course(COURSE)
assList = CSClass.get_assignments()


for assignment in assList:
    if str(assignment) not in assignments:
        data =  '{"text": " ' + "New Assignment: " + str(assignment) + " " + str(assignment.html_url) + ' ","bot_id": "' + "a07c779ea9ac416e6601387688" + '"}'


        #curl GroupMe
        r = requests.post("https://api.groupme.com/v3/bots/post", data=data)
        print(r)



        f = open(ASSIGNMENT_FILE, "a")
        f.write(str(assignment) + ",")
        f.close()


#write log
f = open(LOG_FILE, "a")
f.write("SCRIPT RUN :" + str(datetime.now()) + "\n")
f.close()
    
