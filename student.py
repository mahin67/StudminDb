import  sqlite3

con = sqlite3.connect('Student.db')

class Student:
    def __init__(self, std_id,name,gender,bithd,bat, lvl, dept):
        self.Std_ID=int(std_id)
        self.Name=name
        self.Gen=gender
        self.bd=bithd
        self.batch=int(bat)
        self.level=int(lvl)
        self.dept=dept


    def showAlldata(self, ):
        con = sqlite3.connect('Student.db')
        sql = "SELECT *FROM Students"
        c = con.cursor()
        c.execute(sql)
        Records = c.fetchall()
        print("Fetch DONE")
        print("Student ID, NAME,GENDER,BIRTHDATE(DDMMYYYY),Batch,LEVEL, DEPARTMENT")
        print(Records)
        con.commit()
        con.close()

    def insertStudData(self):
        con = sqlite3.connect('Student.db')
        ST_id = self.Std_ID
        NAme =self.Name
        GEN= self.Gen
        Birthd=self.bd
        Batch = self.batch
        Level=self.level
        Dept= self.dept
        print(ST_id,NAme,GEN,Birthd,Batch,Level,Dept)
        sql="INSERT INTO Students VALUES('{}','{}','{}','{}','{}','{}','{}')".format(ST_id,NAme,GEN,Birthd,Batch,Level,Dept)
        c=con.cursor()
        c.execute(sql)
        print("INSERTION DONE")
        con.commit()
        con.close()

    def Showstdinfo(self,ID):
        con = sqlite3.connect('Student.db')
        sql = "SELECT *FROM Students where Stud_ID=? "
        c=con.cursor()
        c.execute(sql,(int(ID),))
        Records =c.fetchall()
        print("Fetch DONE")
        print("Student ID, NAME,GENDER,BIRTHDATE(DDMMYYYY),Batch,LEVEL, DEPARTMENT")
        print(Records)
        con.commit()
        con.close()

    def Studinsertion(self):
        # Data Insertion
        X = []
        X = input().split(" ")

        stud = Student(X[0], X[1], X[2], X[3], X[4], X[5], X[6])
        stud.insertStudData()



