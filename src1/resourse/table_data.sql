CREATE TABLE labours1(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    wages INT NOT NULL,
    role VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL

);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    labours_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NULL,
    FOREIGN KEY (labours_id) REFERENCES labours1(id)
);

CREATE TABLE skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    labours_id INT NOT NULL,
    skills VARCHAR(100),
    FOREIGN KEY (labours_id) REFERENCES labours1(id)
);