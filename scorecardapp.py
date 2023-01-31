import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="Pa$$w0rd")
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE IF NOT EXISTS scorecard")
mycursor.execute("use scorecard")
#mycursor.execute("CREATE TABLE SubjectList(ID int NOT NULL AUTO_INCREMENT,SubjectName varchar(20),PRIMARY KEY(ID))")
#mycursor.execute("CREATE TABLE ScoreList(ID int NOT NULL AUTO_INCREMENT,UserName varchar(20),ScoreValue int,ScorePct Decimal(3,2),SUB_ID int,PRIMARY KEY(ID),FOREIGN KEY (SUB_ID) REFERENCES SubjectList(ID))")
#mycursor.execute("INSERT INTO SubjectList (SubjectName) VALUES('ICT')")
#mycursor.execute("INSERT INTO SubjectList (SubjectName) VALUES('MATH')")
#mycursor.execute("INSERT INTO SubjectList (SubjectName) VALUES('CHEMISTRY')")
#mycursor.execute("select * from SubjectList")

#username = str(input("Enter username:"))
#userscore = int(input("Enter Score (between 1 to 100) :"))
#score_pct=((userscore/100)*100)

#print("username is: " + username)
#print(" Score is: ", userscore)
#print(" Score percentage is:", score_pct,"%")
#print(" record for ", username,"updated in database")
#print("INSERT INTO ScoreCardlist(ID, USERNAME, TESTSCORE, TEST_PCT, SUBID) VALUES(1,'Manohar',89,89,11)")
print("INSERT INTO ScoreList (UserName, ScoreValue, ScorePct, SUB_ID) VALUES('Manohar', 50, 15.67, 1)")
mycursor.execute("INSERT INTO ScoreList (UserName, ScoreValue, ScorePct, SUB_ID) VALUES('Manohar', 50, 15.67, 1)")
#print("INSERT INTO ScoreCardlist(ID, USERNAME, TESTSCORE, TEST_PCT, SUBID) VALUES(1,'",username,"',", userscore, ",", score_pct, ",", "11)")
mycursor.execute("commit")