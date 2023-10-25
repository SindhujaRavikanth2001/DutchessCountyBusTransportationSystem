use dutchess_county_bus_transportation_dbms_project;
show tables;
-- Insert schedules
INSERT INTO Schedule (DayFlag, ArrivalTime, DepartureTime) 
VALUES
  ('Monday', '06:00:00', '06:05:00'),
  ('Monday', '06:10:00', '06:15:00'),
  ('Tuesday', '07:00:00', '07:05:00'),
  ('Wednesday', '08:30:00', '08:35:00'),
  ('Thursday', '15:45:00', '15:50:00'),
  ('Friday', '13:10:00', '13:15:00'),
  ('Saturday', '11:15:00', '11:20:00'),
  ('Sunday', '09:30:00', '09:35:00');


-- Insert bus routes
INSERT INTO BusRoute (StartLocation, EndLocation)
VALUES
  ('Poughkeepsie', 'Fishkill'),
  ('Poughkeepsie', 'Beacon'), 
  ('Poughkeepsie', 'Tivoli'),
  ('Poughkeepsie', 'Wassaic'),
  ('Poughkeepsie', 'Pawling'),
  ('Beacon', 'Hopewell Junction');
  select *from busroute;


-- Insert bus stops
INSERT INTO BusStop (StopName, Location)  
VALUES
  ('Poughkeepsie Station', '1 Station Plaza, Poughkeepsie, NY'),
  ('Beacon Station', '223 Fishkill Ave, Beacon NY'),
  ('Hopewell Junction', '123 Main St, Hopewell Junction, NY'),
  ('Tivoli', '456 Broadway, Tivoli, NY'),
  ('Fishkill', '789 Main St, Fishkill, NY'),
  ('Wassaic', '234 Rail Rd, Wassaic, NY');

-- Insert bus stop arrival times
INSERT INTO RouteStopSequence (NumberofStops, ArrivalTime, BusStop_StopID)
VALUES
  (1, '06:00:00', 1), 
  (2, '06:15:00', 2),
  (3, '06:30:00', 3),
  (4, '06:45:00', 4),
  (5, '07:00:00', 5),
  (6, '07:15:00', 6);

-- Assign buses to schedules
INSERT INTO Bus_has_Schedule (Bus_BusID, Schedule_ScheduleID)  
VALUES
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5),
  (6, 6),
  (7, 7),
  (8, 8);

-- Assign buses to routes  
INSERT INTO Bus_has_BusRoute (Bus_BusID, BusRoute_RouteID)
VALUES
  (1, 1),
  (2, 2),
  (17, 3),
  (18, 4),
  (19, 5),
  (20, 6);
DESCRIBE Bus_has_BusRoute;
-- Insert ticket types
INSERT INTO TicketType (TicketTypeID, TypeName, Price, ValidityPeriod, Description)
VALUES
  (1, 'Day Pass', 5.00, 1, 'Valid for one day'),
  (2, '7-day Pass', 20.00, 7, 'Valid for 7 consecutive days'), 
  (3, '31-day Pass', 70.00, 31, 'Valid for 31 consecutive days');
-- Insert data into User table
INSERT INTO User (FirstName, LastName, DOB, Email, PhoneNumber, Username, Password)
VALUES
  ('John', 'Doe', '1990-01-01', 'john@example.com', '123-456-7890', 'johndoe', 'password123'),
  ('Jane', 'Smith', '1995-05-15', 'jane@example.com', '987-654-3210', 'janesmith', 'password456');

-- Insert data into Bus table
INSERT INTO Bus (BusNumber, Capacity, LicensePlateNumber, BusType)
VALUES
  ('A2', 50, 'ABC126','Coach'), 
  ('C', 60, 'GHI789', 'School Bus'),
  ('D', 40, 'JKL012', 'Shuttle'),
  ('E', 45, 'MNO345', 'Shuttle'),
  ('F', 35, 'PQR678', 'Mini Bus'),
  ('H', 30, 'STU901', 'Mini Bus');

-- Insert data into Department table  
INSERT INTO Department (DepartmentName, Location)
VALUES
  ('Operations', '123 Main St, Poughkeepsie, NY'),
  ('Maintenance', '456 Park Rd, Beacon, NY');

-- Insert data into Employee table
INSERT INTO Employee (FirstName, LastName, Position, Department_DepartmentID)
VALUES
  ('Sarah', 'Jones', 'Driver', 1),
  ('Mark', 'Lee', 'Mechanic', 2);

-- Insert data into Admin table
INSERT INTO Admin (Username, Password, Email, PhoneNumber, Employee_EmployeeID) 
VALUES
  ('sarahj','password123', 'sarah@example.com','123-555-1234',1),
  ('markl','password456', 'mark@example.com','987-555-4321',2);
  
-- Insert data into Payment table
INSERT INTO Payment (PaymentID, Amount, PaymentDate, User_UserID, TicketType_TicketTypeID)
VALUES
  (1, 5.00, '2023-01-01', 1, 1),
  (2, 20.00, '2023-01-10', 2, 2);
  
-- Verify all data insertion
SELECT * FROM User;
SELECT * FROM Bus;
SELECT * FROM Department; 
SELECT * FROM Employee;
SELECT * FROM Admin;
SELECT * FROM Payment;
SELECT * FROM Schedule;
SELECT * FROM BusRoute; 
SELECT * FROM BusStop;
SELECT * FROM RouteStopSequence;
SELECT * FROM Bus_has_Schedule;
SELECT * FROM Bus_has_BusRoute;
SELECT * FROM TicketType;