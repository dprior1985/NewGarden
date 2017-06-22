CREATE DATABASE NEWGARDEN;

create user 'danny'@'localhost' IDENTIFIED BY 'danny123';
GRANT ALL ON NEWGARDEN.* TO 'danny'@'localhost';
--Metadata for action
-- i.e run yes/no 

USE NEWGARDEN;

CREATE TABLE CONTROL 
(
  ControlId int(11) NOT NULL AUTO_INCREMENT,
  ActionName varchar(100) DEFAULT NULL,
  Active varchar(10) DEFAULT NULL,
  PRIMARY KEY (ControlId)
) 
;

INSERT INTO CONTROL(ActionName,Active)
VALUES ('WeatherAPI','N'); 
INSERT INTO CONTROL(ActionName,Active)
VALUES ('WaterLevel','N'); 
INSERT INTO CONTROL(ActionName,Active)
VALUES ('CurrentTemp','N'); 
INSERT INTO CONTROL(ActionName,Active)
VALUES ('CurrentLight','N'); 
INSERT INTO CONTROL(ActionName,Active)
VALUES ('Rain','N'); 


-- Log of run
-- details
-- time
-- action
--Results from action
CREATE TABLE ControlLog
 (
  ControlLogId int(11) NOT NULL AUTO_INCREMENT,
  LogDescription varchar(100) DEFAULT NULL,
  ControlId int(11) DEFAULT NULL,
  ActionName varchar(100) DEFAULT NULL,
  SaveData varchar(1000) DEFAULT NULL,
  DateNow datetime DEFAULT NULL,
  Active bit(1) DEFAULT NULL,
  RunNumberId int(11) DEFAULT NULL,
  SavedDataInt decimal(16,2) DEFAULT NULL,
  PRIMARY KEY (ControlLogId)
) ;


 CREATE TABLE RunNumber
 (
  RunNumberId int(11) NOT NULL AUTO_INCREMENT,
  DateNow datetime DEFAULT NULL,
  Water int(11) DEFAULT NULL,
  PRIMARY KEY (RunNumberId)
) ;

CREATE TABLE SenorLog 
(
  SenorLogId int(11) NOT NULL AUTO_INCREMENT,
  SensorName varchar(50) DEFAULT NULL,
  Data varchar(10) DEFAULT NULL,
  DateNow datetime DEFAULT NULL,
  PRIMARY KEY (SenorLogId)
) ;



CREATE TABLE Schedule 
(
  ScheduleId int(11) NOT NULL AUTO_INCREMENT,
  ScheduleName varchar(50) DEFAULT NULL,
  Time int DEFAULT NULL,
  PRIMARY KEY (ScheduleId)
) ;




INSERT INTO Schedule(ScheduleName,Time)
VALUES ('Morning',6);

INSERT INTO Schedule(ScheduleName,Time)
VALUES ('Night',18);


 

