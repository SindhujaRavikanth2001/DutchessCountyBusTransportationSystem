-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Dutchess_county_bus_transportation_DBMS_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Dutchess_county_bus_transportation_DBMS_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema SQl
-- -----------------------------------------------------
USE `Dutchess_county_bus_transportation_DBMS_project` ;

-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`User` (
  `UserID` INT NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(50) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `DOB` DATETIME NOT NULL,
  `Email` VARCHAR(60) NOT NULL,
  `PhoneNumber` BIGINT(14) NOT NULL,
  `Username` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE INDEX `Username_UNIQUE` (`Username` ASC) VISIBLE,
  UNIQUE INDEX `UserID_UNIQUE` (`UserID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Bus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Bus` (
  `BusID` INT NOT NULL AUTO_INCREMENT,
  `BusNumber` VARCHAR(45) NOT NULL,
  `Capacity` INT NOT NULL,
  `LicensePlateNumber` VARCHAR(45) NOT NULL,
  `BusType` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`BusID`),
  UNIQUE INDEX `BusID_UNIQUE` (`BusID` ASC) VISIBLE,
  UNIQUE INDEX `BusNumber_UNIQUE` (`BusNumber` ASC) VISIBLE,
  UNIQUE INDEX `LicensePlateNumber_UNIQUE` (`LicensePlateNumber` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Bus Route`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Bus Route` (
  `RouteID` INT NOT NULL AUTO_INCREMENT,
  `StartLocation` VARCHAR(45) NOT NULL,
  `EndLocation` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`RouteID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Ticket Type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Ticket Type` (
  `TicketTypeID` INT NOT NULL,
  `TypeName` VARCHAR(45) NOT NULL,
  `Price` DECIMAL(4) NOT NULL,
  `ValidityPeriod` INT NULL,
  `Description` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`TicketTypeID`),
  UNIQUE INDEX `TicketTypeID_UNIQUE` (`TicketTypeID` ASC) VISIBLE,
  UNIQUE INDEX `TypeName_UNIQUE` (`TypeName` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Department`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Department` (
  `DepartmentID` INT NOT NULL AUTO_INCREMENT,
  `DepartmentName` VARCHAR(45) NOT NULL,
  `Location` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`DepartmentID`),
  UNIQUE INDEX `DepartmentID_UNIQUE` (`DepartmentID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Employee` (
  `EmployeeID` INT NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `Position` VARCHAR(45) NOT NULL,
  `Department_DepartmentID` INT NOT NULL,
  PRIMARY KEY (`EmployeeID`, `Department_DepartmentID`),
  UNIQUE INDEX `EmployeeID_UNIQUE` (`EmployeeID` ASC) VISIBLE,
  INDEX `fk_Employee_Department1_idx` (`Department_DepartmentID` ASC) VISIBLE,
  CONSTRAINT `fk_Employee_Department1`
    FOREIGN KEY (`Department_DepartmentID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Department` (`DepartmentID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Admin` (
  `AdminID` INT NOT NULL AUTO_INCREMENT,
  `Username` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(155) NOT NULL,
  `PhoneNumber` BIGINT(14) NOT NULL,
  `Employee_EmployeeID` INT NOT NULL,
  PRIMARY KEY (`AdminID`, `Employee_EmployeeID`),
  UNIQUE INDEX `AdminID_UNIQUE` (`AdminID` ASC) VISIBLE,
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE,
  UNIQUE INDEX `PhoneNumber_UNIQUE` (`PhoneNumber` ASC) VISIBLE,
  INDEX `fk_Admin_Employee1_idx` (`Employee_EmployeeID` ASC) VISIBLE,
  CONSTRAINT `fk_Admin_Employee1`
    FOREIGN KEY (`Employee_EmployeeID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Employee` (`EmployeeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Bus Stop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Bus Stop` (
  `StopID` INT NOT NULL AUTO_INCREMENT,
  `StopName` VARCHAR(45) NOT NULL,
  `Location` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`StopID`),
  UNIQUE INDEX `StopID_UNIQUE` (`StopID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Notification`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Notification` (
  `NotificationID` INT NOT NULL AUTO_INCREMENT,
  `Message` VARCHAR(150) NOT NULL,
  `DateAndTime` DATETIME NOT NULL,
  `User_UserID` INT NOT NULL,
  `Admin_AdminID` INT NOT NULL,
  PRIMARY KEY (`NotificationID`, `User_UserID`, `Admin_AdminID`),
  UNIQUE INDEX `NotificationID_UNIQUE` (`NotificationID` ASC) VISIBLE,
  INDEX `fk_Notification_User1_idx` (`User_UserID` ASC) VISIBLE,
  INDEX `fk_Notification_Admin1_idx` (`Admin_AdminID` ASC) VISIBLE,
  CONSTRAINT `fk_Notification_User1`
    FOREIGN KEY (`User_UserID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`User` (`UserID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Notification_Admin1`
    FOREIGN KEY (`Admin_AdminID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Admin` (`AdminID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Holidays`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Holidays` (
  `HolidayID` INT NOT NULL AUTO_INCREMENT,
  `HolidayDate` DATETIME NOT NULL,
  `Description` VARCHAR(100) NOT NULL,
  `Notification_NotificationID` INT NOT NULL,
  PRIMARY KEY (`HolidayID`, `Notification_NotificationID`),
  INDEX `fk_Holidays_Notification1_idx` (`Notification_NotificationID` ASC) VISIBLE,
  CONSTRAINT `fk_Holidays_Notification1`
    FOREIGN KEY (`Notification_NotificationID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Notification` (`NotificationID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Route Stop Sequence`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Route Stop Sequence` (
  `StopSequenceID` INT NOT NULL AUTO_INCREMENT,
  `NumberofStops` INT NOT NULL,
  `ArrivalTime` DATETIME NOT NULL,
  `Bus Stop_StopID` INT NOT NULL,
  PRIMARY KEY (`StopSequenceID`, `Bus Stop_StopID`),
  UNIQUE INDEX `StopSequenceID_UNIQUE` (`StopSequenceID` ASC) VISIBLE,
  INDEX `fk_Route Stop Sequence_Bus Stop1_idx` (`Bus Stop_StopID` ASC) VISIBLE,
  CONSTRAINT `fk_Route Stop Sequence_Bus Stop1`
    FOREIGN KEY (`Bus Stop_StopID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Bus Stop` (`StopID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Payment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Payment` (
  `PaymentID` INT NOT NULL,
  `Amount` DECIMAL(6) NOT NULL,
  `PaymentDate` DATETIME NOT NULL,
  `User_UserID` INT NOT NULL,
  `Ticket Type_TicketTypeID` INT NOT NULL,
  PRIMARY KEY (`PaymentID`, `User_UserID`, `Ticket Type_TicketTypeID`),
  INDEX `fk_Payment_User1_idx` (`User_UserID` ASC) VISIBLE,
  INDEX `fk_Payment_Ticket Type1_idx` (`Ticket Type_TicketTypeID` ASC) VISIBLE,
  CONSTRAINT `fk_Payment_User1`
    FOREIGN KEY (`User_UserID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`User` (`UserID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Payment_Ticket Type1`
    FOREIGN KEY (`Ticket Type_TicketTypeID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Ticket Type` (`TicketTypeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Reservation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Reservation` (
  `ReservationID` INT NOT NULL AUTO_INCREMENT,
  `ReservationDate` DATETIME NOT NULL,
  `NumberOfReservations` INT NOT NULL,
  `Notification_NotificationID` INT NOT NULL,
  `Bus_BusID` INT NOT NULL,
  PRIMARY KEY (`ReservationID`, `Notification_NotificationID`, `Bus_BusID`),
  INDEX `fk_Reservation_Notification1_idx` (`Notification_NotificationID` ASC) VISIBLE,
  INDEX `fk_Reservation_Bus1_idx` (`Bus_BusID` ASC) VISIBLE,
  CONSTRAINT `fk_Reservation_Notification1`
    FOREIGN KEY (`Notification_NotificationID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Notification` (`NotificationID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reservation_Bus1`
    FOREIGN KEY (`Bus_BusID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Bus` (`BusID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Bus_has_Bus Route`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Bus_has_Bus Route` (
  `Bus_BusID` INT NOT NULL,
  `Bus Route_RouteID` INT NOT NULL,
  PRIMARY KEY (`Bus_BusID`, `Bus Route_RouteID`),
  INDEX `fk_Bus_has_Bus Route_Bus Route1_idx` (`Bus Route_RouteID` ASC) VISIBLE,
  INDEX `fk_Bus_has_Bus Route_Bus1_idx` (`Bus_BusID` ASC) VISIBLE,
  CONSTRAINT `fk_Bus_has_Bus Route_Bus1`
    FOREIGN KEY (`Bus_BusID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Bus` (`BusID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bus_has_Bus Route_Bus Route1`
    FOREIGN KEY (`Bus Route_RouteID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Bus Route` (`RouteID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Bus Route_has_Route Stop Sequence`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Bus Route_has_Route Stop Sequence` (
  `Bus Route_RouteID` INT NOT NULL,
  `Route Stop Sequence_StopSequenceID` INT NOT NULL,
  PRIMARY KEY (`Bus Route_RouteID`, `Route Stop Sequence_StopSequenceID`),
  INDEX `fk_Bus Route_has_Route Stop Sequence_Route Stop Sequence1_idx` (`Route Stop Sequence_StopSequenceID` ASC) VISIBLE,
  INDEX `fk_Bus Route_has_Route Stop Sequence_Bus Route1_idx` (`Bus Route_RouteID` ASC) VISIBLE,
  CONSTRAINT `fk_Bus Route_has_Route Stop Sequence_Bus Route1`
    FOREIGN KEY (`Bus Route_RouteID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Bus Route` (`RouteID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bus Route_has_Route Stop Sequence_Route Stop Sequence1`
    FOREIGN KEY (`Route Stop Sequence_StopSequenceID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Route Stop Sequence` (`StopSequenceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Schedule`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Schedule` (
  `ScheduleID` INT NOT NULL AUTO_INCREMENT,
  `DayFlag` VARCHAR(45) NOT NULL,
  `ArrivalTime` DATETIME NOT NULL,
  `DepartureTime` DATETIME NOT NULL,
  PRIMARY KEY (`ScheduleID`),
  UNIQUE INDEX `ScheduleID_UNIQUE` (`ScheduleID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Bus_has_Schedule`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Bus_has_Schedule` (
  `Bus_BusID` INT NOT NULL,
  `Schedule_ScheduleID` INT NOT NULL,
  PRIMARY KEY (`Bus_BusID`, `Schedule_ScheduleID`),
  INDEX `fk_Bus_has_Schedule_Schedule1_idx` (`Schedule_ScheduleID` ASC) VISIBLE,
  INDEX `fk_Bus_has_Schedule_Bus1_idx` (`Bus_BusID` ASC) VISIBLE,
  CONSTRAINT `fk_Bus_has_Schedule_Bus1`
    FOREIGN KEY (`Bus_BusID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Bus` (`BusID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bus_has_Schedule_Schedule1`
    FOREIGN KEY (`Schedule_ScheduleID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Schedule` (`ScheduleID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Bus Route_has_Schedule`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Bus Route_has_Schedule` (
  `Bus Route_RouteID` INT NOT NULL,
  `Schedule_ScheduleID` INT NOT NULL,
  PRIMARY KEY (`Bus Route_RouteID`, `Schedule_ScheduleID`),
  INDEX `fk_Bus Route_has_Schedule_Schedule1_idx` (`Schedule_ScheduleID` ASC) VISIBLE,
  INDEX `fk_Bus Route_has_Schedule_Bus Route1_idx` (`Bus Route_RouteID` ASC) VISIBLE,
  CONSTRAINT `fk_Bus Route_has_Schedule_Bus Route1`
    FOREIGN KEY (`Bus Route_RouteID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Bus Route` (`RouteID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bus Route_has_Schedule_Schedule1`
    FOREIGN KEY (`Schedule_ScheduleID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Schedule` (`ScheduleID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dutchess_county_bus_transportation_DBMS_project`.`Payment_has_Reservation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dutchess_county_bus_transportation_DBMS_project`.`Payment_has_Reservation` (
  `Payment_PaymentID` INT NOT NULL,
  `Payment_User_UserID` INT NOT NULL,
  `Payment_Ticket Type_TicketTypeID` INT NOT NULL,
  `Reservation_ReservationID` INT NOT NULL,
  `Reservation_Notification_NotificationID` INT NOT NULL,
  `Reservation_Bus_BusID` INT NOT NULL,
  PRIMARY KEY (`Payment_PaymentID`, `Payment_User_UserID`, `Payment_Ticket Type_TicketTypeID`, `Reservation_ReservationID`, `Reservation_Notification_NotificationID`, `Reservation_Bus_BusID`),
  INDEX `fk_Payment_has_Reservation_Reservation1_idx` (`Reservation_ReservationID` ASC, `Reservation_Notification_NotificationID` ASC, `Reservation_Bus_BusID` ASC) VISIBLE,
  INDEX `fk_Payment_has_Reservation_Payment1_idx` (`Payment_PaymentID` ASC, `Payment_User_UserID` ASC, `Payment_Ticket Type_TicketTypeID` ASC) VISIBLE,
  CONSTRAINT `fk_Payment_has_Reservation_Payment1`
    FOREIGN KEY (`Payment_PaymentID` , `Payment_User_UserID` , `Payment_Ticket Type_TicketTypeID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Payment` (`PaymentID` , `User_UserID` , `Ticket Type_TicketTypeID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Payment_has_Reservation_Reservation1`
    FOREIGN KEY (`Reservation_ReservationID` , `Reservation_Notification_NotificationID` , `Reservation_Bus_BusID`)
    REFERENCES `Dutchess_county_bus_transportation_DBMS_project`.`Reservation` (`ReservationID` , `Notification_NotificationID` , `Bus_BusID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
