CREATE TABLE train (
	train_no INT PRIMARY KEY,
	train_name VARCHAR(20),
	avlbl_seats INT,
	avlbl_wl INT
)

CREATE TABLE station (
	station_no VARCHAR(20) PRIMARY KEY,
	station_name VARCHAR(20)
)

CREATE TABLE stops (
	train_no INT,
	station_no VARCHAR(20),
	stop_no INT
)

CREATE TABLE booking (
	booking_id INT PRIMARY KEY IDENTITY,
	passenger_name VARCHAR(20),
	train_no INT,
	dest_station_no VARCHAR(20),
	booking_status VARCHAR(10)
)

INSERT INTO train VALUES
	(1, 'TVM-ALP', 5, 2),
	(2, 'TVM-EKM', 5, 2),
	(3, 'TVM-KZK', 5, 2)

INSERT INTO station VALUES
	(1, 'TVM'),
	(2, 'ALP'),
	(3, 'EKM'),
	(4, 'KZK')

INSERT INTO stops VALUES
	(1, 2, 1),
	(2, 2, 1),
	(2, 3, 2),
	(3, 2, 1),
	(3, 3, 2),
	(3, 4, 3)


CREATE VIEW DESTINATIONS AS SELECT DISTINCT station_name, station.station_no FROM station INNER JOIN stops ON station.station_no = stops.station_no

-- SELECT * FROM DESTINATIONS

CREATE PROCEDURE getTrainsToDest (@stationno AS INT)
AS 
SELECT train.train_no, train.train_name , train.avlbl_seats, train.avlbl_wl
FROM stops inner join train on train.train_no = stops.train_no 
WHERE stops.station_no = @stationno

--EXEC getTrainsToDest 3

CREATE PROCEDURE makeBookingOnCNFM (@name as varchar(10), @trno as int, @dest as int)
AS
BEGIN
	INSERT INTO booking (passenger_name, train_no, dest_station_no, booking_status) VALUES (@name, @trno, @dest, 'CNFM')
	UPDATE train SET [avlbl_seats] = [avlbl_seats] - 1 WHERE train_no = @trno
END

-- EXEC makeBooking Preston, 2, 3, CNFM

CREATE PROCEDURE makeBookingOnWL (@name as varchar(10), @trno as int, @dest as int)
AS
BEGIN
	INSERT INTO booking (passenger_name, train_no, dest_station_no, booking_status) VALUES (@name, @trno, @dest, 'WL')
	UPDATE train SET [avlbl_wl] = [avlbl_wl] - 1 WHERE train_no = @trno
END


CREATE VIEW BookingDetails AS
	SELECT booking_id, passenger_name, station_name, train_name, booking_status 
	FROM 
		booking
		inner join train on booking.train_no = train.train_no
		inner join station on booking.dest_station_no = station.station_no


--SELECT * FROM BookingDetails