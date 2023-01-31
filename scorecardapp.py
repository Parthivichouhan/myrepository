import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pa$$w0rd"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS scorecard1")
mycursor.execute("use scorecard1")
mycursor.execute("Drop Table ScoreCardList")
mycursor.execute("CREATE TABLE ScoreCardlist(ID int, USERNAME Varchar(20), TESTSCORE int, TEST_PCT int, SUBID int)")
mycursor.execute("Drop Table IF EXISTS SubjectList")
mycursor.execute("CREATE TABLE Subjectlist(ID int, SubjectName Varchar(20))")

#username = str(input("Enter username:"))
#userscore = int(input("Enter Score (between 1 to 100) :"))
#score_pct=((userscore/100)*100)

#print("username is: " + username)
#print(" Score is: ", userscore)
#print(" Score percentage is:", score_pct,"%")
#print(" record for ", username,"updated in database")
#print("INSERT INTO ScoreCardlist(ID, USERNAME, TESTSCORE, TEST_PCT, SUBID) VALUES(1,'Manohar',89,89,11)")
mycursor.execute("INSERT INTO ScoreCardlist(ID, USERNAME, TESTSCORE, TEST_PCT, SUBID) VALUES(1,'Manohar',89,78,11)")
#print("INSERT INTO ScoreCardlist(ID, USERNAME, TESTSCORE, TEST_PCT, SUBID) VALUES(1,'",username,"',", userscore, ",", score_pct, ",", "11)")