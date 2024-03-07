DROP DATABASE IF EXISTS planning;
CREATE DATABASE planning;
USE planning;
CREATE TABLE entreprise (
    id INT PRIMARY KEY NOT NULL,
    nom VARCHAR(100),
    adresse VARCHAR(255),
    ville VARCHAR(255),
    code_postal VARCHAR(5),
    pays VARCHAR(255)
);

CREATE TABLE user (
    id INT PRIMARY KEY NOT NULL,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(50),
    entreprise_id INT,
    secret VARCHAR(255),
    FOREIGN KEY (entreprise_id) REFERENCES entreprise(id)
);

CREATE TABLE planning (
    id INT PRIMARY KEY NOT NULL,
    nom VARCHAR(255),
    entreprise_id INT,
    FOREIGN KEY (entreprise_id) REFERENCES entreprise(id)
);
CREATE TABLE task (
    id INT PRIMARY KEY NOT NULL,
    nom VARCHAR(255),
    description TEXT,
    date_start DATETIME,
    date_end DATETIME,
    planning_id INT,
    FOREIGN KEY (planning_id) REFERENCES planning(id)
);
CREATE TABLE user_task (
    id INT PRIMARY KEY NOT NULL,
    user_id INT,
    task_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (task_id) REFERENCES task(id)
);

CREATE TABLE notification (
    id INT PRIMARY KEY NOT NULL,
    id_user INT,
    id_planning INT,
    title VARCHAR(255),
    details TEXT,
    FOREIGN KEY (id_user) REFERENCES user(id),
    FOREIGN KEY (id_planning) REFERENCES planning(id)
);

CREATE TABLE notification_vue (
    id INT PRIMARY KEY NOT NULL,
    user_id INT,
    notif_id INT,
    date DATETIME,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (notif_id) REFERENCES notification(id)
);

ALTER TABLE entreprise MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE user MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE planning MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE task MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE user_task MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE notification MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE notification_vue MODIFY COLUMN id INT AUTO_INCREMENT;


-- TRIGGERS
DELIMITER $$
CREATE TRIGGER `notify_users_on_join` AFTER INSERT ON `user_task`
FOR EACH ROW BEGIN
    INSERT INTO notification (id_user, id_planning, title, details)
    SELECT ut.user_id, t.planning_id, 'Nouvel utilisateur assigné à la tâche', CONCAT(NEW.user_id, ' a rejoint la tâche ', t.nom)
    FROM user_task ut
    JOIN task t ON ut.task_id = t.id
    WHERE t.id = NEW.task_id AND ut.user_id != NEW.user_id;
END$$

CREATE TRIGGER `notify_users_on_leave` BEFORE DELETE ON `user_task`
FOR EACH ROW BEGIN
    INSERT INTO notification (id_user, id_planning, title, details)
    SELECT ut.user_id, t.planning_id, 'Utilisateur désassigné de la tâche', CONCAT(OLD.user_id, ' a quitté la tâche ', t.nom)
    FROM user_task ut
    JOIN task t ON ut.task_id = t.id
    WHERE t.id = OLD.task_id AND ut.user_id != OLD.user_id;
END$$
DELIMITER ;
