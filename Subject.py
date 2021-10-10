import  sqlite3

con = sqlite3.connect('Student.db')

class subject:
    def __init__(self, std_id,sb_code,sub_name,ct1,ct2,ct3,mid,fin,dept):
        self.Std_ID=int(std_id)
        self.sub_cd=sb_code
        self.sub_nm = sub_name
        self.ct1 = float(ct1)
        self.ct2 = float(ct2)
        self.ct3 = float(ct3)
        self.mid = float(mid)
        self.Fin = float(fin)
        self.dept=dept
        self.Grade= None

    def showAlldata(self, ):
        con = sqlite3.connect('Student.db')
        sql = "SELECT *FROM SUB"
        c = con.cursor()
        c.execute(sql)
        Records = c.fetchall()
        print("Fetch DONE")
        print("Student ID, Sub_Code,Sub_Name,CT1,CT2,CT3,MID,FINAl,DEPARTMENT,GRADE")
        print(Records)
        con.commit()
        con.close()

    def grade(self):

        CT = (self.ct1 + self.ct2 + self.ct3)
        Final = (self.Fin + CT + self.mid) * 100 / 300

        if Final >= 50.0 and Final <= 59.9:
            return "D"
        elif Final >= 60.0 and Final <= 65.9:
            return "C"
        elif Final >= 66 and Final <= 69.9:
            return "B"
        elif Final >= 70 and Final <= 75.9:
            return "A-"
        elif Final >= 76 and Final <= 79.9:
            return "A"
        elif Final >= 80 and Final <= 100.00:
            return "A+"

    def insertSubData(self):
        con = sqlite3.connect('Student.db')
        print(self.Std_ID,self.sub_cd,self.sub_nm,self.ct1,self.ct2,self.ct3,self.mid,self.Fin,self.dept,self.Grade)
        grd=self.grade()
        sql="INSERT INTO SUB VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(self.Std_ID,self.sub_cd,self.sub_nm,self.ct1,self.ct2,self.ct3,self.mid,self.Fin,self.dept,grd)
        c=con.cursor()
        c.execute(sql)
        print("INSERTION DONE")
        con.commit()
        con.close()


