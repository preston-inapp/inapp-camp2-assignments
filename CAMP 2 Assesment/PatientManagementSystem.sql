CREATE TABLE patient (
	patientId INT PRIMARY KEY,
	patientName VARCHAR(20),
	gender VARCHAR(10),
	age INT,
	bloodGroup VARCHAR(4)
)

CREATE PROCEDURE addPatient (@patientId AS INT, @patientName AS VARCHAR(20), @gender AS VARCHAR(10), @age AS INT, @bloodGroup AS VARCHAR(4)) AS
BEGIN
	INSERT INTO patient VALUES (@patientId, @patientName, @gender, @age, @bloodGroup)
END

CREATE PROCEDURE updatePatient (@patientId AS INT, @patientName AS VARCHAR(20), @gender AS VARCHAR(10), @age AS INT, @bloodGroup AS VARCHAR(4)) AS
BEGIN
	DELETE FROM patient WHERE patientId = @patientId
	INSERT INTO patient VALUES (@patientId, @patientName, @gender, @age, @bloodGroup)
END

CREATE PROCEDURE deletePatient (@patientId AS INT) AS
BEGIN
	DELETE FROM patient WHERE patientId = @patientId
END

CREATE PROCEDURE listPatients AS
BEGIN
	SELECT * FROM patient
END

CREATE PROCEDURE searchPatient (@id AS INT) AS
BEGIN
	SELECT * FROM patient WHERE patientId=@id
END