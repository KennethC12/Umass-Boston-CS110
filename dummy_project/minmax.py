import stdio
#This is our List and we use stdio.readallints to read the list that we are going to put in the terminal
list = stdio.readAllInts()
#Create a min and max 
min = min(list)
max = max(list)
#Use len() to return the list in the for loop, so the loop can be evaluated.
for i in range(len(list)):
    #We are running a for loop where If list[i] is > than max.
    if list[i] > max:
        #This will mean max is equal to list[i] 
        max = list[i]
    elif list[i] < min:
        min = list[i]
    
print("Minimum =" ,min)
print("Maximum =" ,max)