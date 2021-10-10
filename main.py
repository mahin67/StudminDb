import student
import  Subject
import CreateTable

Z=CreateTable.con
#y=CreateTable.c (Student Table)
#x=CreateTable.CSUB() (Subject Table)



#Subject Insertion

print("WELCOME TO MY MINI STUDENT DATABASE")
print("1.Insert Students 2. Show All Students info  3. Show a specific student info 4.Insert Subject 5.Assigned students subject")

x=" "
x=input()
while x!="quit":

    if int(x)==1:
        student.Student.Studinsertion(0)
        break
    elif int(x)==2:
        student.Student.showAlldata(0)
        break
    elif int(x) == 3:
        q=input("Enter Student ID :")
        student.Student.Showstdinfo(0, int(q))
        break
    elif int(x) == 4:
        #q=input("Enter Subject for a student ID :\n" )
        Y = []
        Y = input().split(" ")
        SUB = Subject.subject(Y[0], Y[1], Y[2], Y[3], Y[4], Y[5], Y[6], Y[7], Y[8])

        print("Data insert")
        SUB.insertSubData()
        break

    elif int(x)==5:
        Subject.subject.showAlldata(0)
        break
