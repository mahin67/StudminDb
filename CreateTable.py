import  sqlite3

con = sqlite3.connect('Student.db')
print("DB is connected")

def CST():
    c= con.cursor()
    c.execute("CREATE TABLE Students (Stud_ID Integer, Name text, Gender text, Birthdate text , Batch Integer, Level Integer , Dept text)")
    print("Table  Student Created")
    con.commit()
    con.close()


def CSUB():
    c= con.cursor()
    c.execute("CREATE TABLE SUB (Stud_ID Integer, SUB_CODE Integer, SUB_NAME text, CT1 Decimal  , CT2 Decimal, CT3 Decimal , MID Decimal, Final  Decimal)")
    print("Table Subject Created")
    con.commit()
    con.close()
