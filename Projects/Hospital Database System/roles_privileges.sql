
-- create roles in database
CREATE ROLE admin_it;
CREATE ROLE administration;
CREATE ROLE medical_team;
CREATE ROLE cleaning_service;
CREATE ROLE technical_staff;


-- grant privilages to admin_it role
GRANT ALL PRIVILEGES ON hospital_db.* TO admin_it;

  
-- create admin_it users
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password1' PASSWORD EXPIRE;
CREATE USER 'user2'@'localhost' IDENTIFIED BY 'password2' PASSWORD EXPIRE;
CREATE USER 'user3'@'localhost' IDENTIFIED BY 'password3' PASSWORD EXPIRE;

ALTER USER 'user1'@'localhost' PASSWORD EXPIRE INTERVAL 180 DAY;
ALTER USER 'user2'@'localhost' PASSWORD EXPIRE INTERVAL 180 DAY;
ALTER USER 'user3'@'localhost' PASSWORD EXPIRE INTERVAL 180 DAY;

ALTER USER 'user1'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'user2'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'user3'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;

GRANT admin_it TO 'user1'@'localhost';
GRANT admin_it TO 'user2'@'localhost';
GRANT admin_it TO 'user3'@'localhost';


-- grant privilages to administration role
GRANT SELECT, INSERT, DELETE ON hospital_db.workers TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.specializations TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.workers_type TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.workers_responsibilities TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.workers_address TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.responsibilities TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.cities TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.countries TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.examinations TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.room_type TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.equipment TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.equipment_type TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.equipment_producent TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.department TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.wing_name TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.surgeries TO administration;
GRANT SELECT, INSERT, DELETE ON hospital_db.medications TO administration;


-- create administration users
CREATE USER 'admin1'@'localhost' IDENTIFIED BY 'adminpass1' PASSWORD EXPIRE;
CREATE USER 'admin2'@'localhost' IDENTIFIED BY 'adminpass2' PASSWORD EXPIRE;
CREATE USER 'admin3'@'localhost' IDENTIFIED BY 'adminpass3' PASSWORD EXPIRE;
CREATE USER 'admin4'@'localhost' IDENTIFIED BY 'adminpass4' PASSWORD EXPIRE;
CREATE USER 'admin5'@'localhost' IDENTIFIED BY 'adminpass5' PASSWORD EXPIRE;

ALTER USER 'admin1'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'admin2'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'admin3'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'admin4'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'admin5'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;

GRANT administration TO 'admin1'@'localhost';
GRANT administration TO 'admin2'@'localhost';
GRANT administration TO 'admin3'@'localhost';
GRANT administration TO 'admin4'@'localhost';
GRANT administration TO 'admin5'@'localhost';



-- grant privilages to medical_team role
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.patients_discharge TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.patient_examinations TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.appointments_schedule TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.examinations_schedule TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.room_equipment TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.patients TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.patients_nurses TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.patients_doctors TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.patients_address TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.surgeries_schedule TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.patient_surgeries TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.patient_medications TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.patients_rooms TO medical_team;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.rooms_to_clean TO medical_team;


-- create medical_team users
CREATE USER 'med1'@'localhost' IDENTIFIED BY 'medpass1' PASSWORD EXPIRE;
CREATE USER 'med2'@'localhost' IDENTIFIED BY 'medpass2' PASSWORD EXPIRE;
CREATE USER 'med3'@'localhost' IDENTIFIED BY 'medpass3' PASSWORD EXPIRE;

ALTER USER 'med1'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'med2'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'med3'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;

GRANT medical_team TO 'med1'@'localhost';
GRANT medical_team TO 'med2'@'localhost';
GRANT medical_team TO 'med3'@'localhost';


-- grant privilages to cleaning_service role
GRANT SELECT ON hospital_db.rooms_to_clean TO cleaning_service;


-- create cleaning_service users
CREATE USER 'clean1'@'localhost' IDENTIFIED BY 'cleanpass1' PASSWORD EXPIRE;
CREATE USER 'clean2'@'localhost' IDENTIFIED BY 'cleanpass2' PASSWORD EXPIRE;
CREATE USER 'clean3'@'localhost' IDENTIFIED BY 'cleanpass3' PASSWORD EXPIRE;

ALTER USER 'clean1'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'clean2'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'clean3'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;

GRANT cleaning_service TO 'clean1'@'localhost';
GRANT cleaning_service TO 'clean2'@'localhost';
GRANT cleaning_service TO 'clean3'@'localhost';


-- grant privilages to technical_staff role
GRANT SELECT ON hospital_db.equipment TO technical_staff;
GRANT SELECT ON hospital_db.equipment_producent TO technical_staff;
GRANT SELECT ON hospital_db.equipment_type TO technical_staff;
GRANT SELECT ON hospital_db.room_equipment TO technical_staff;
GRANT SELECT ON hospital_db.rooms TO technical_staff;
GRANT SELECT ON hospital_db.department TO technical_staff;
GRANT SELECT, INSERT, DELETE, UPDATE ON hospital_db.equipment_repairs TO technical_staff;


-- create technical_staff users
CREATE USER 'tech1'@'localhost' IDENTIFIED BY 'techpass1' PASSWORD EXPIRE;
CREATE USER 'tech2'@'localhost' IDENTIFIED BY 'techpass2' PASSWORD EXPIRE;

ALTER USER 'tech1'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;
ALTER USER 'tech2'@'localhost' FAILED_LOGIN_ATTEMPTS 3 PASSWORD_LOCK_TIME 2;

GRANT technical_staff TO 'tech1'@'localhost';
GRANT technical_staff TO 'tech2'@'localhost';


