-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER //

CREATE PROCEDURE Addbonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
IF EXISTS(SELECT * FROM projects WHERE name = project_name LIMIT 1)
THEN SET @projectid = (SELECT id FROM projects WHERE name = project_name LIMIT 1);
INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, @projectid, score);
ELSE 
INSERT INTO projects (name) VALUES (project_name);
END IF;
END//
DELIMITER ;
