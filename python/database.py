import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database="MRDCENTER")
c = mydb.cursor()
def viewTables(tableName):
    command = 'SELECT * FROM ' + tableName +';'
    print(command)
    c.execute(command)
    data = c.fetchall()
    return data

def add_member(p_MembershipType, p_MembershipDuration, p_StartDate, p_TrainerService, p_FirstName, p_LastName,p_Email, p_PhoneNumber):
    command = 'CALL InsertMember("'+p_MembershipType+'","'+p_MembershipDuration+'", "'+p_StartDate+'", "'+p_TrainerService+'","'+p_FirstName+'","'+p_LastName+'","'+p_Email+'","'+p_PhoneNumber+'");'
    print(command)
    c.execute(command)
    mydb.commit()
def add_trainer(p_FirstName, p_LastName, p_Email, p_PhoneNumber):
    command = 'CALL InsertTrainer("'+p_FirstName+'","'+p_LastName+'", "'+p_Email+'", "'+p_PhoneNumber+'");'
    print(command)
    c.execute(command)
    mydb.commit()
def ScheduleTrainingSession(p_TrainerID, p_MembershipID, p_TrainingDate):
    command = 'CALL ScheduleTrainingSession("'+p_TrainerID+'","'+p_MembershipID+'", "'+p_TrainingDate+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def InsertMembershipFacility(p_MembershipID, p_FacilityID, p_BookingDate):
    command = 'CALL InsertMembershipFacility("'+p_MembershipID+'","'+p_FacilityID+'", "'+p_BookingDate+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def delRecMember(memberid):
    command1 = 'DELETE FROM memberemail where MembershipID = "' + memberid + '"'
    command2 = 'DELETE FROM memberphone where MembershipID = "' + memberid + '"'
    command3 = 'DELETE FROM payment where MembershipID = "' + memberid + '"'
    command4 = 'DELETE FROM trainerschedule where MembershipID = "' + memberid + '"'
    command5 = 'DELETE FROM MembershipFacility WHERE MembershipID = "' + memberid + '"'
    command6 = 'DELETE FROM member where MembershipID = "' + memberid + '"'
    print(command1)
    print(command6)
    c.execute(command1)
    c.execute(command2)
    c.execute(command3)
    c.execute(command4)
    c.execute(command5)
    c.execute(command6)
    mydb.commit()
def delRecTrainer(trainerid):
    command1 = 'DELETE FROM traineremail where TrainerID = "' + trainerid + '"'
    command2 = 'DELETE FROM trainerphone where TrainerID = "' + trainerid + '"'
    command3 = 'DELETE FROM trainerschedule where TrainerID = "' + trainerid + '"'
    command4 = 'DELETE FROM trainer where TrainerID = "' + trainerid + '"'
    print(command1)
    print(command4)
    c.execute(command1)
    c.execute(command2)
    c.execute(command3)
    c.execute(command4)
    mydb.commit()

def get_membershipid():
    c.execute('SELECT MEMBERSHIPID FROM MEMBER')
    data = c.fetchall()
    return data
def get_membershipid_for_trainer():
    c.execute("SELECT MembershipID FROM Member WHERE MembershipType IN ('Gym', 'Combination')")
    data = c.fetchall()
    return data
def get_membershipid_for_facility():
    c.execute("SELECT MembershipID FROM Member WHERE MembershipType IN ('Sports', 'Combination')")
    data = c.fetchall()
    return data

def get_trainerid():
    c.execute('SELECT TRAINERID FROM TRAINER')
    data = c.fetchall()
    return data

def updateStatus(p_MemberID, p_NewFirstName, p_NewLastName):
    command = 'UPDATE Member SET FirstName = "'+ p_NewFirstName +'", LastName = "'+ p_NewLastName +'" WHERE MembershipID = "'+ p_MemberID +'"'

    print(command)
    c.execute(command)
    mydb.commit()

def AddMemberPhoneNumber(p_MembershipID, p_NewNumber):
    command = 'CALL AddMemberPhoneNumber("'+p_MembershipID+'","'+p_NewNumber+'");'
    print(command)
    c.execute(command)
    mydb.commit()
def AddTrainerEmailAddress(p_TrainerID, p_NewEmail):
    command = 'CALL AddTrainerEmailAddress("'+p_TrainerID+'","'+p_NewEmail+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def AddMemberEmailAddress(p_MembershipID, p_NewEmail):
    command = 'CALL AddMemberEmailAddress("'+p_MembershipID+'","'+p_NewEmail+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def AddTrainerPhoneNumber(p_TrainerID, p_NewNumber):
    command = 'CALL AddTrainerPhoneNumber("'+p_TrainerID+'","'+p_NewNumber+'");'
    print(command)
    c.execute(command)
    mydb.commit()

def execQuery(command):
    c.execute(command)
    data = c.fetchall()
    return data

def viewQueryResult(choice):
    command=""
    if choice==1:
        command = "SELECT M.MembershipID, M.FirstName, M.LastName, P.Amount FROM Member M JOIN Payment P ON M.MembershipID = P.MembershipID WHERE M.MembershipType = 'Gym';"
    elif choice==2:
        command = "SELECT M.MembershipID, M.FirstName, M.LastName, P.Amount FROM Member M JOIN Payment P ON M.MembershipID = P.MembershipID WHERE M.MembershipType = 'Sports';"
    elif choice==3:
        command = "SELECT M.MembershipID, M.FirstName, M.LastName, P.Amount FROM Member M JOIN Payment P ON M.MembershipID = P.MembershipID WHERE M.MembershipType = 'Combination';"
    elif choice==4:
        command = "SELECT T.FirstName, T.LastName, COUNT(TS.TrainerScheduleID) AS TrainingSessionsCount FROM Trainer T JOIN TrainerSchedule TS ON T.TrainerID = TS.TrainerID GROUP BY T.FirstName, T.LastName;"
    elif choice == 5:
        command = "SELECT M.MembershipID, CONCAT(M.FirstName, ' ', M.LastName) AS FullName, GROUP_CONCAT(DISTINCT ME.Email SEPARATOR ', ') AS Emails, GROUP_CONCAT(DISTINCT MP.PhoneNumber SEPARATOR ', ') AS PhoneNumbers FROM Member M LEFT JOIN MemberEmail ME ON M.MembershipID = ME.MembershipID LEFT JOIN MemberPhone MP ON M.MembershipID = MP.MembershipID GROUP BY M.MembershipID, FullName;"
    c.execute(command)
    data = c.fetchall()
    return data