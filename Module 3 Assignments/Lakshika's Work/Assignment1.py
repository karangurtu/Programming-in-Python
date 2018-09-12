'''1) Connect to Oracle Database '''
import sqlite3
connection_object = sqlite3.connect("ass.db") #Connection IP
cursor_object = connection_object.cursor()
cursor_object.execute("CREATE TABLE Employer(CompanyID varchar2(5) PRIMARY KEY, CompanyName Varchar2(50) NOT NULL,EmailID Varchar2(30),Mobile Number(10) CHECK (length(Mobile)=10),City Varchar2(15),IndustryType Varchar2(20),FunctionalArea Varchar2(20),MembershipPlan Varchar2(20) CHECK (MembershipPlan IN('Trial','Monthly','Yearly')),DateofSignup Date,DateofRenewal Date,RenewalStatus varchar2(10) CHECK (RenewalStatus IN ('Active','Expired')))")
cursor_object.execute("INSERT INTO Employer (CompanyID,CompanyName,EmailID,Mobile,City,IndustryType,FunctionalArea,MembershipPlan,DateofSignup,DateofRenewal,RenewalStatus) VALUES ('C1000','Infosys Limited','jobs@infosys.com',7896579875,'Chennai','IT', 'Accounting','Yearly','07/01/2016','06/30/2017','Active')")
cursor_object.execute("INSERT INTO Employer (CompanyID,CompanyName,EmailID,Mobile,City,IndustryType,FunctionalArea,MembershipPlan,DateofSignup,DateofRenewal,RenewalStatus) VALUES ('C1001','Accenture','careers@accenture.com',9878776567,'Bangalore','IT', 'Marketing','Monthly','06/02/2016','07/01/2017','Active')")
cursor_object.execute("INSERT INTO Employer (CompanyID,CompanyName,EmailID,Mobile,City,IndustryType,FunctionalArea,MembershipPlan,DateofSignup,DateofRenewal,RenewalStatus) VALUES ('C1002','HP','openings@hp.com',8789878750,'Mumbai','IT', 'Marketing','Monthly', '07/12/2016','07/11/2017','Active')")
cursor_object.execute("INSERT INTO Employer (CompanyID,CompanyName,EmailID,Mobile,City,IndustryType,FunctionalArea,MembershipPlan,DateofSignup,DateofRenewal,RenewalStatus) VALUES ('C1003','NewGen','jobs@newgen.com',8877643228,'Bangalore','Manufacturing', 'Marketing','Yearly', '09/02/2016','09/01/2017','Expired')")
'''2) Fetch all rows from Table Employee '''

'''2) Fetch all rows from Table Employee '''
cursor_object.execute("select * from Employer")

'''3) Display all the rows '''
i=1
for row in cursor_object:
    print("Row number",i,"is:",row)
    i = i+1

'''4) Display count of rows fetched '''
cursor_object.fetchall() #Without fetchall() the rowcount attribute does not works
print("The number of rows fetched are:",cursor_object.rowcount)

'''5) Display the description of all the columns of the table'''
print("The table has following Schema:")
print(cursor_object.description)

#Close the Database connection
connection_object.close()
