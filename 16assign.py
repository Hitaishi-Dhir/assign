import sqlite3

conn=sqlite3.connect('assign.db')
print("database opened successfully!")
#ques1

#conn.execute('''create table books(
#BOOKID INT PRIMARY KEY NOT NULL,
#TITLEID NOT NULL,
#LOCATION NOT NULL,
#GENRE CHAR(50)
#);
#''')

#conn.execute('''create table Titles(
#TITLEID INT PRIMARY KEY NOT NULL,
#TITLE CHAR(50) NOT NULL,
#ISBN INT NOT NULL,
#PUBLISHERID INT NOT NULL,
#PUBLISHERYEAR INT NOT NULL
#);
#''')

#conn.execute('''create table Publishers(
#PUBLISHERID INT PRIMARY KEY NOT NULL,
#NAME CHAR(50) NOT NULL,
#STREETADDRESS CHAR(50),
#SUITENUMBER INT NOT NULL,
#ZIPCODEID INT NOT NULL
#);
#''')

#conn.execute('''create table Zipcodes(
#ZIPCODEID INT PRIMARY KEY NOT NULL,
#CITY CHAR(50)NOT NULL,
#STATE CHAR(50)NOT NULL,
#ZIPCODE CHAR(50)
#);
#''')

#conn.execute('''create table Authorstitle(
#AUTHORTITLEID INT PRIMARY KEY NOT NULL,
#AUTHORID NOT NULL,
#TITLEID NOT NULL
#);
#''')

#conn.execute('''create table AUTHOR(
#AUTHORID INT PRIMARY KEY NOT NULL,
#FIRSTNAME CHAR(50) NOT NULL,
#MIDDLENAME CHAR(50) NOT NULL,
#LASTNAME CHAR(50) NOT NULL
#);
#''')

conn.commit()
print("tables created!")

#ques2
'''
conn.execute("INSERT INTO books(BOOKID,TITLEID,LOCATION,GENRE) VALUES (1,101,'DELHI','academic')")
conn.execute("INSERT INTO books(BOOKID,TITLEID,LOCATION,GENRE) VALUES (2,102,'PUNE','adventure')")
conn.execute("INSERT INTO books(BOOKID,TITLEID,LOCATION,GENRE) VALUES (3,103,'RAJISTHAN','horror')")
conn.execute("INSERT INTO books(BOOKID,TITLEID,LOCATION,GENRE) VALUES (4,104,'MUMBAI','crime')")
conn.commit()
print("data inserted in table book")

conn.execute("INSERT INTO titles(TITLEID,TITLE,ISBN,PUBLISHERID,PUBLISHERYEAR) VALUES (101,'QUANTZ',120,111,2017)")
conn.execute("INSERT INTO titles(TITLEID,TITLE,ISBN,PUBLISHERID,PUBLISHERYEAR) VALUES (102,'BIRBILLING HILLS PARAGLIDING!!',125,110,2012)")
conn.execute("INSERT INTO titles(TITLEID,TITLE,ISBN,PUBLISHERID,PUBLISHERYEAR) VALUES (103,'PARANORMAL..IS IT THAT NORMAL?',129,119,2005)")
conn.execute("INSERT INTO titles(TITLEID,TITLE,ISBN,PUBLISHERID,PUBLISHERYEAR) VALUES (104,'CASESTUDY..THE MEAN CAUSE',130,113,2018)")
conn.commit()
print("data inserted in table titles")

conn.execute("INSERT INTO Publishers(PUBLISHERID,NAME,STREETADDRESS,SUITENUMBER,ZIPCODEID) VALUES(111,'RSAGGARWAL','BLOCK-D AZADNAGAR DELHI',1120,1500)")
conn.execute("INSERT INTO Publishers VALUES(110,'RD RONALD','STREET 18 WETERNMARKT',11,1300)")
conn.execute("INSERT INTO Publishers VALUES(119,'MARKLINDER','NEAR BANGARH FORT',114,1400)")
conn.execute("INSERT INTO Publishers VALUES(113,'RASHIDDEV','56 JUHHU',116,1200)")
conn.commit()
print("data inserted in table Publishers")

conn.execute("INSERT INTO Zipcodes(ZIPCODEID,CITY,STATE,ZIPCODE) VALUES (1500,'DELHI','DELHI',0)")
conn.execute("INSERT INTO Zipcodes(ZIPCODEID,CITY,STATE,ZIPCODE) VALUES (1300,'PUNE','MAHARASHTRA',10)")
conn.execute("INSERT INTO Zipcodes(ZIPCODEID,CITY,STATE,ZIPCODE) VALUES (1400,'RAJISTHAN','BIKANAIR',20)")
conn.execute("INSERT INTO Zipcodes(ZIPCODEID,CITY,STATE,ZIPCODE) VALUES (1200,'MUMBAI','MAHARASHTRA',30)")
conn.commit()
print("data inserted in table Zipcodes")

conn.execute("INSERT INTO Authorstitle(AUTHORTITLEID,AUTHORID,TITLEID) VALUES (65,45,101)")
conn.execute("INSERT INTO Authorstitle(AUTHORTITLEID,AUTHORID,TITLEID) VALUES (75,46,102)")
conn.execute("INSERT INTO Authorstitle(AUTHORTITLEID,AUTHORID,TITLEID) VALUES (85,47,103)")
conn.execute("INSERT INTO Authorstitle(AUTHORTITLEID,AUTHORID,TITLEID) VALUES (95,48,104)")
conn.commit()
print("data inserted in table Authorstitle")

conn.execute("INSERT INTO AUTHOR(AUTHORID,FIRSTNAME,MIDDLENAME,LASTNAME) VALUES (45,'DR.R','S','AGGARWAL')")
conn.execute("INSERT INTO AUTHOR(AUTHORID,FIRSTNAME,MIDDLENAME,LASTNAME) VALUES (46,'RONALD',' ','KINGSTON')")
conn.execute("INSERT INTO AUTHOR(AUTHORID,FIRSTNAME,MIDDLENAME,LASTNAME) VALUES (47,'DHARGHRAJ','KUMAR','SHARMA')")
conn.execute("INSERT INTO AUTHOR(AUTHORID,FIRSTNAME,MIDDLENAME,LASTNAME) VALUES (48,'ANITA',' ','AWASTHI')")
conn.commit()
print("data inserted in table Author")
'''

#ques3

cursor=conn.execute("SELECT * FROM Authorstitle")
print("original values are")
for row in cursor:
    print("AUTHORTITLEID= ", row[0])
    print("AUTHORTITLE= ", row[1])
    print("TITLEID= ", row[2])
    print("")

conn.execute("UPDATE Authorstitle SET TITLEID =111 WHERE AUTHORTITLEID = 65")

print("updated values are")
cursor=conn.execute("SELECT * FROM Authorstitle")
for row in cursor:
    print("AUTHORTITLEID= ", row[0])
    print("AUTHORTITLE= ", row[1])
    print("TITLEID= ", row[2])
    print("")



