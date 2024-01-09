-- Create the database if not exists
CREATE DATABASE IF NOT EXISTS MRDCENTER;
USE MRDCENTER;

-- Fees Table
CREATE TABLE Fees (
    FeeType VARCHAR(50) PRIMARY KEY,
    FeePerMonth DECIMAL(10, 2)
);

-- Member Table
CREATE TABLE Member (
    MembershipID INT AUTO_INCREMENT PRIMARY KEY,
    MembershipType VARCHAR(255),
    MembershipDuration INT,
    StartDate DATE,
    EndDate DATE, -- EndDate column is not automatically generated
    TrainerService BOOLEAN,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    CONSTRAINT chk_enddate CHECK (EndDate > StartDate)
);

CREATE TABLE MemberEmail (
    MemberEmailID INT AUTO_INCREMENT PRIMARY KEY,
    MembershipID INT,
    Email VARCHAR(255),
    FOREIGN KEY (MembershipID) REFERENCES Member(MembershipID)
);

CREATE TABLE MemberPhone (
    MemberPhoneID INT AUTO_INCREMENT PRIMARY KEY,
    MembershipID INT,
    PhoneNumber VARCHAR(20),
    FOREIGN KEY (MembershipID) REFERENCES Member(MembershipID)
);

-- Payment Table
CREATE TABLE Payment (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    MembershipID INT,
    PaymentDate DATE,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (MembershipID) REFERENCES Member(MembershipID)
);

-- Facility Table
CREATE TABLE Facility (
    FacilityID INT AUTO_INCREMENT PRIMARY KEY,
    FacilityName VARCHAR(255)
);

-- MembershipFacility Table
CREATE TABLE MembershipFacility (
    MembershipFacilityID INT AUTO_INCREMENT PRIMARY KEY,
    MembershipID INT,
    FacilityID INT,
    BookingDate DATE,
    FOREIGN KEY (MembershipID) REFERENCES Member(MembershipID),
    FOREIGN KEY (FacilityID) REFERENCES Facility(FacilityID)
);

-- Trainer Table
CREATE TABLE Trainer (
    TrainerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255)
);

-- TrainerPhone Table
CREATE TABLE TrainerPhone (
    TrainerPhoneID INT AUTO_INCREMENT PRIMARY KEY,
    TrainerID INT,
    PhoneNumber VARCHAR(20),
    FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID)
);

-- TrainerEmail Table
CREATE TABLE TrainerEmail (
    TrainerEmailID INT AUTO_INCREMENT PRIMARY KEY,
    TrainerID INT,
    Email VARCHAR(255),
    FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID)
);

-- TrainerSchedule Table
CREATE TABLE TrainerSchedule (
    TrainerScheduleID INT AUTO_INCREMENT PRIMARY KEY,
    TrainerID INT,
    MembershipID INT,
    TrainingDate DATE,
    FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID),
    FOREIGN KEY (MembershipID) REFERENCES Member(MembershipID)
);
-- Stored Procedure: Insert Member
DELIMITER //
CREATE PROCEDURE InsertMember(
    IN p_MembershipType VARCHAR(255),
    IN p_MembershipDuration INT,
    IN p_StartDate DATE,
    IN p_TrainerService BOOLEAN,
    IN p_FirstName VARCHAR(255),
    IN p_LastName VARCHAR(255),
    IN p_Email VARCHAR(255),
    IN p_PhoneNumber VARCHAR(20)
)
BEGIN
    -- Insert into Member table
    INSERT INTO Member (MembershipType, MembershipDuration, StartDate, TrainerService, FirstName, LastName)
    VALUES (p_MembershipType, p_MembershipDuration, p_StartDate, p_TrainerService, p_FirstName, p_LastName);

    -- Get the MembershipID of the newly inserted member
    SET @MemberID = LAST_INSERT_ID();

    -- Insert into MemberEmail table
    INSERT INTO MemberEmail (MembershipID, Email)
    VALUES (@MemberID, p_Email);

    -- Insert into MemberPhone table
    INSERT INTO MemberPhone (MembershipID, PhoneNumber)
    VALUES (@MemberID, p_PhoneNumber);

    -- Calculate and insert payment details into Payment table
    IF p_TrainerService = 1 THEN
        SET @TrainerFeePerMonth = (SELECT FeePerMonth FROM Fees WHERE FeeType = 'TrainerFee');
        SET @TrainerFee = @TrainerFeePerMonth * p_MembershipDuration;
    ELSE
        SET @TrainerFee = 0; -- No trainer fee if trainer service is not selected
    END IF;

    INSERT INTO Payment (MembershipID, PaymentDate, Amount)
    VALUES (@MemberID, p_StartDate, ((SELECT FeePerMonth FROM Fees WHERE FeeType = p_MembershipType) * p_MembershipDuration) + @TrainerFee);
END //
DELIMITER ;


-- Stored Procedure: Insert Trainer
DELIMITER //
CREATE PROCEDURE InsertTrainer(
    IN p_FirstName VARCHAR(255),
    IN p_LastName VARCHAR(255),
    IN p_Email VARCHAR(255),
    IN p_PhoneNumber VARCHAR(20)
)
BEGIN
    -- Insert into Trainer table
    INSERT INTO Trainer (FirstName, LastName)
    VALUES (p_FirstName, p_LastName);

    -- Get the TrainerID of the newly inserted trainer
    SET @TrainerID = LAST_INSERT_ID();

    -- Insert into TrainerEmail table
    INSERT INTO TrainerEmail (TrainerID, Email)
    VALUES (@TrainerID, p_Email);

    -- Insert into TrainerPhone table
    INSERT INTO TrainerPhone (TrainerID, PhoneNumber)
    VALUES (@TrainerID, p_PhoneNumber);
END //
DELIMITER ;

-- Stored Procedure: ScheduleTrainingSession
DELIMITER //
CREATE PROCEDURE ScheduleTrainingSession(
    IN p_TrainerID INT,
    IN p_MembershipID INT,
    IN p_TrainingDate DATE
)
BEGIN
    -- Insert a new record into TrainerSchedule table
    INSERT INTO TrainerSchedule (TrainerID, MembershipID, TrainingDate)
    VALUES (p_TrainerID, p_MembershipID, p_TrainingDate);
END //
DELIMITER ;

-- Stored Procedure: Insert into MembershipFacility Table
DELIMITER //
CREATE PROCEDURE InsertMembershipFacility(
    IN p_MembershipID INT,
    IN p_FacilityID INT,
    IN p_BookingDate DATE
)
BEGIN
    -- Insert into MembershipFacility table
    INSERT INTO MembershipFacility (MembershipID, FacilityID, BookingDate)
    VALUES (p_MembershipID, p_FacilityID, p_BookingDate);
END //
DELIMITER ;

-- Stored Procedure: Add Trainer Phone Number
DELIMITER //
CREATE PROCEDURE AddTrainerPhoneNumber(
    IN p_TrainerID INT,
    IN p_PhoneNumber VARCHAR(20)
)
BEGIN
    -- Insert Trainer's Phone Number
    INSERT INTO TrainerPhone (TrainerID, PhoneNumber)
    VALUES (p_TrainerID, p_PhoneNumber);
END //
DELIMITER ;

-- Stored Procedure: Add Trainer Email Address
DELIMITER //
CREATE PROCEDURE AddTrainerEmailAddress(
    IN p_TrainerID INT,
    IN p_Email VARCHAR(255)
)
BEGIN
    -- Insert Trainer's Email Address
    INSERT INTO TrainerEmail (TrainerID, Email)
    VALUES (p_TrainerID, p_Email);
END //
DELIMITER ;

-- Stored Procedure: Add Member Phone Number
DELIMITER //
CREATE PROCEDURE AddMemberPhoneNumber(
    IN p_MembershipID INT,
    IN p_PhoneNumber VARCHAR(20)
)
BEGIN
    -- Insert member's Phone Number
    INSERT INTO MemberPhone (MembershipID, PhoneNumber)
    VALUES (p_MembershipID, p_PhoneNumber);
END //
DELIMITER ;

-- Stored Procedure: Add Member Email Address
DELIMITER //
CREATE PROCEDURE AddMemberEmailAddress(
    IN p_MembershipID INT,
    IN p_Email VARCHAR(255)
)
BEGIN
    -- Insert member's Email Address
    INSERT INTO MemberEmail (MembershipID, Email)
    VALUES (p_MembershipID, p_Email);
END //
DELIMITER ;

-- Insert default membership fees into Fees table
INSERT INTO Fees (FeeType, FeePerMonth) VALUES ('Gym', 1000), ('Sports', 500), ('Combination', 1300), ('TrainerFee', 300);
-- Insert Badminton to Facility Table
INSERT INTO Facility (FacilityName)
VALUES ('Badminton');
-- Insert Table Tennis to Facility Table
INSERT INTO Facility (FacilityName)
VALUES ('Table Tennis');

-- Trigger to calculate and update EndDate
DELIMITER //
CREATE TRIGGER CalculateEndDate
BEFORE INSERT ON Member
FOR EACH ROW
BEGIN
    SET NEW.EndDate = DATE_ADD(NEW.StartDate, INTERVAL NEW.MembershipDuration MONTH);
END //
DELIMITER ;

CALL InsertMember('Gym', 12, '2023-11-05', 1, 'Sean', 'Sougaijam', 'sean@example.com', '+1234567890');
CALL InsertMember('Gym', 6, '2023-11-05', 0, 'Saakshi', 'BK', 'sbk@example.com', '+1234999890');
CALL InsertMember('Sports', 12, '2023-11-05', 0, 'Afnaan', 'M', 'afnaan@example.com', '+1111111111');
CALL InsertMember('Combination', 12, '2023-11-05', 1, 'Tejas', 'B', 'tejas@example.com', '+1223334444');
CALL InsertMember('Combination', 6, '2023-11-05', 0, 'Kriti', 'Jain', 'kjain@example.com', '+1234566778');

CALL InsertTrainer('Arnold', 'S', 'arnold@example.com', '+1234567890');
CALL InsertTrainer('David', 'L', 'david@example.com', '+1234367890');
CALL InsertTrainer('Bupendra', 'Jogi', 'bupendrajogi@example.com', '+0987654321');
CALL InsertTrainer('Sushma', 'Patil', 'david@example.com', '+1234509876');

CALL InsertMembershipFacility(3, 1, '2023-11-12');
CALL InsertMembershipFacility(4, 2, '2023-11-13');
CALL InsertMembershipFacility(5, 2, '2023-11-13');
CALL InsertMembershipFacility(4, 1, '2023-11-14');
CALL InsertMembershipFacility(3, 1, '2023-11-14');

CALL ScheduleTrainingSession(1,1, '2023-11-20');
CALL ScheduleTrainingSession(2,2, '2023-11-21');
CALL ScheduleTrainingSession(2,4, '2023-11-22');
CALL ScheduleTrainingSession(3,5, '2023-11-23');
CALL ScheduleTrainingSession(4,1, '2023-11-23');
CALL ScheduleTrainingSession(3,2, '2023-11-24');

CALL AddMemberPhoneNumber(1,'+1111111111');
CALL AddTrainerEmailAddress(2,'NewEmail+');
CALL AddMemberEmailAddress(2,'qwerty');
CALL AddTrainerPhoneNumber(3,'+122333444444');
CALL AddMemberPhoneNumber(3,'+1111111111');
CALL AddTrainerEmailAddress(1,'NewEmail');
CALL AddMemberEmailAddress(3,'xxxx@email.com');
CALL AddTrainerPhoneNumber(4,'+00000000000');