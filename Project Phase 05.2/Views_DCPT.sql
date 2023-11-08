CREATE VIEW v_user_info AS
SELECT UserId, FirstName, LastName, DOB, Email, PhoneNumber, Username 
FROM User;

CREATE VIEW v_bus_routes AS
SELECT RouteID, StartLocation, EndLocation
FROM BusRoute;

CREATE VIEW v_ticket_types AS  
SELECT TicketTypeID, TypeName, Price, ValidityPeriod, Description
FROM TicketType;

CREATE VIEW v_user_update AS
SELECT UserId, FirstName, LastName, Email, PhoneNumber, Username
FROM User;

CREATE VIEW v_payment_info AS
SELECT p.PaymentID, p.Amount, p.PaymentDate, 
       u.FirstName, u.LastName, u.Username,
       t.TypeName
FROM Payment p
JOIN User u ON p.User_UserId = u.UserId 
JOIN TicketType t ON p.TicketType_TicketTypeId = t.TicketTypeId;
select *from v_bus_schedule;

CREATE VIEW v_schedule AS
SELECT ScheduleID, DayFlag, ArrivalTime, DepartureTime
FROM Schedule;

CREATE VIEW v_bus_stops AS
SELECT StopID, StopName, Location 
FROM BusStop;

CREATE VIEW v_route_stop_seq AS 
SELECT rs.NumberofStops, rs.ArrivalTime,  
       bs.StopName, bs.Location
FROM RouteStopSequence rs 
JOIN BusStop bs ON rs.BusStop_StopID = bs.StopID;

CREATE VIEW v_bus_schedule AS
SELECT b.BusID, b.BusNumber, s.ScheduleID, s.DayFlag, s.ArrivalTime, s.DepartureTime
FROM Bus_has_Schedule bs
JOIN Bus b ON bs.Bus_BusID = b.BusID
JOIN Schedule s ON bs.Schedule_ScheduleID = s.ScheduleID;

CREATE VIEW v_bus_routes AS  
SELECT b.BusID, b.BusNumber, r.RouteID, r.StartLocation, r.EndLocation
FROM Bus_has_BusRoute bbr
JOIN Bus b ON bbr.Bus_BusID = b.BusID 
JOIN BusRoute r ON bbr.BusRoute_RouteID = r.RouteID;

SHOW FULL TABLES IN dutchess_county_bus_transportation_dbms_project WHERE TABLE_TYPE = 'VIEW';

CREATE VIEW BusScheduleView AS
SELECT b.BusNumber,  
       s.ArrivalTime,
       s.DepartureTime,
       rs.NumberofStops,  
       r.StartLocation,
       r.EndLocation,
       s.DayFlag
FROM Schedule s
JOIN Bus_has_Schedule bs ON s.ScheduleID = bs.Schedule_ScheduleID
JOIN Bus b ON bs.Bus_BusID = b.BusID  
JOIN Bus_has_BusRoute bbr ON b.BusID = bbr.Bus_BusID
JOIN BusRoute r ON bbr.BusRoute_RouteID = r.RouteID
JOIN BusRoute r ON bbr.BusRoute_RouteID = r.RouteID
JOIN RouteStopSequence rs ON r.RouteID = rs.BusStop_StopID;

DROP VIEW IF EXISTS BusScheduleView;
SELECT *FROM BusScheduleView;


    
SELECT * FROM BusScheduleView WHERE StartLocation = 'YourStartLocation' AND EndLocation = 'YourEndLocation' AND DayFlag = 'YourDayFlag';


