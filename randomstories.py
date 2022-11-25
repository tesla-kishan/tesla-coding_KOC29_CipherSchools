import random
print("Hello Reader")
readername=input("What is your name?:")
print("Hello"+" "+readername)

adjective_t=["LAZY","CARELESS","DULL","LETHARGIC","INATTENTIVE"]
who_t=["BOY","YOUNG MAN","CHILD","KID"]
print("TITLE OF THE STORY:-  "+random.choice(adjective_t)+" "+random.choice(who_t))

when = ['A few years ago', 'A long time ago','About 30 years ago', 'Once upon a time']
who=["boy","young man","child","kid"]
names=["Ujjwal","Anurag","Hritik","Ayush","Priyanshu"]
characteristics=["so lazy","so careless","so dull","so lethargic","inattentive","procastinating guy","too sleepy","unenergetic"]
first_line=["couldn't even bother to change his clothes","couldn't even bother to do his work","couldn't even bother to take intrest in any activity","couldn't even bother to do work or make any effort to do anything","always depends on others for getting his work done","always delay the schedule of completing the work","always postponed the work"]

randomwhen=random.choice(when)
randomwho=random.choice(who)
randomname=random.choice(names)
randomcharacteristic=random.choice(characteristics)
randomfirst_line=random.choice(first_line)

first_line_story= randomwhen + " there was a "  + randomwho +" " + " named " + randomname + " who was " + randomcharacteristic + " " + ", he " + randomfirst_line + " " + "."
print(first_line_story)


when2=["One day","After some day","Next day"]
time=["in evening time","in morning time","in afternoon time"]
tree=["apple tree","mango treee","lichi tree","guava tree"]
place=["their yard","their garden"]

randomwhen2=random.choice(when2)
randomtime=random.choice(time)
randomtree=random.choice(tree)
randomplace=random.choice(place)

second_line= randomwhen2 + ", " + randomtime +  " he saw that the " + randomtree + " in " + randomplace + " was " + "full of fruits."
print(second_line)

characteristics3=["too lazy","so lethargic","unenergetic"]
randomcharacteristics3=random.choice(characteristics3)
third_line="He wanted to eat some fruits from the tree but he was " + randomcharacteristics3 + " " + "to climb the tree and take the fruits."
print(third_line)


next4=["So he lay down underneath the tree and waited for the fruits to fall off","So he go near the tree and waiting for the yummy fruits to fall of","Then he go towards the tree and waiting for the fruits to fall of on the ground"]
randomnext4=random.choice(next4)
fourth_line = randomnext4 + "."
print(fourth_line)

next5=["He waited and waited until he was very hungry but the fruits never fell.","He waited for almost 5-6 hours without doing anything."]
randomnext5=random.choice(next5)
fifth_line= randomnext5 
print(fifth_line)







moral=["LAZINESS CAN GET YOU NOWHERE. IF YOU WANT SOMETHING, YOU NEED TO WORK HARD FOR IT","WORK WITH HONESTY AND SINCERITY BECAUSE LAZINESS WILL RUIN YOU.","WE SHOULD GET UP AND WORK HARD"]
print("MORAL OF THE STORY:-  "+random.choice(moral))
print("THE END")