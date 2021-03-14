# Sorry for weak English. Run this program  on pc .
# this project had wroted by Mahin Shahriar . Duration almost five hours !!
import datetime
def getdate():
    return datetime.datetime.now()
inp = int(input("What do you want to do:\n 1. Show files.\n 2. log \n"))
if inp == 2:
   client_name = int(input("For whom do you want to log?\n1. Alex\n2. Adam\n3. Alan\n"))
   if client_name == 1:
      activity_name = int(input("For Alex, what do you want to log?\n1. Exercise\n2. Diet\n"))
      if activity_name == 1:
        exercise_name = str(input("Input Exercise name : \n"))
        with open("alexexer.txt", "a") as ff:
         ff.write(str([getdate()])+" " + exercise_name + "\n")
        print("Exercise name is Successfully written !")
      elif activity_name==2:
        food_or_fruit_name = str(input("Input what he ate: \n"))
        with open("alexff.txt","a") as ff :
          ff.write(str([getdate()])+" "+food_or_fruit_name+"\n")
          print("Eating data is Successfully written !")
      else:
        print("Incorrect Input!")
   elif client_name == 2:
     activity_name = int(input("For Adam, what do you want to log?\n1. Exercise\n2. Diet\n"))
     if activity_name== 1:
        exercise_name = str(input("Input Exercise name : \n"))
        with open("adamexer.txt","a") as am :
          am.write(str([getdate()])+" "+exercise_name+"\n")
        print("Exercise name is Successfully written !")
     elif activity_name==2:
        food_or_fruit_name = str(input("Input what he ate: \n"))
        with open("adamff.txt","a") as af :
          af.write(str([getdate()])+" "+food_or_fruit_name+"\n")
        print("Eating data is Successfully written !")
     else:
        print("Incorrect Input!")
   elif client_name == 3:
     activity_name = int(input("For Alan, what do you want to log?\n1. Exercise\n2. Diet\n"))
     if activity_name== 1:
        exercise_name = str(input("Input Exercise name : \n"))
        with open("alanexer.txt","a") as an :
          an.write(str([getdate()])+" "+exercise_name+"\n")
        print("Exercise name is Successfully written !")
     elif activity_name==2:
        food_or_fruit_name = str(input("Input what he ate: \n"))
        with open("alanff.txt","a") as af :
          af.write(str([getdate()])+" "+food_or_fruit_name+"\n")
        print("Eating data is Successfully written !")
     else:
        print("Incorrect Input!") #  Wow I've Done this project in 2.5 hours.
elif inp == 1:
    client_nameone = int(input("Whose file do you want to see?\n1. Alex\n2. Adam\n3. Alan\n"))
    if client_nameone == 1:
       activity_file = int(input("What do you want to see?\n 1. Alex's Exercises.\n 2. Alex's Diets.\n "))
       if activity_file == 1:
            try :
                with open("alexexer.txt") as ax:
                 print(ax.read())
            except FileNotFoundError:
                print("Nothing in file.")
       elif activity_file == 2:
            try:
                with open("alexff.txt") as ff:
                 print(ff.read())
            except FileNotFoundError :
                print("Nothing in file.")
       else:
           print("Error . Input Under Options !")
    elif client_nameone == 2:
        activity_file = int(input("What do you want to see?\n 1. Adam's Exercises.\n 2. Adam's Diets.\n "))
        if activity_file == 1:
            try:
                with open("adamexer.txt") as am:
                 print(am.read())
            except FileNotFoundError:
                print("Nothing in file.")
        elif activity_file == 2:
            try:
                with open("adamff.txt") as af:
                 print(af.read())
            except FileNotFoundError:
                print("Nothing in file.")
        else:
             print("Error . Input Under Options !")
    elif client_nameone == 3:
        activity_file = int(input("What do you want to see?\n 1. Alan's Exercises.\n 2. Alan's Diets.\n "))
        if activity_file == 1:
            try:
                with open("alanexer.txt") as an:
                 print(an.read())
            except FileNotFoundError:
                print("Nothing in file.")
        elif activity_file == 2:
            try:
                with open("alanff.txt") as af:
                 print(af.read())
            except FileNotFoundError:
                 print("Nothing in file.")
        else:
         print("Error. Input Under Options !")
else:
    print("Input Under Options !")