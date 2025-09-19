CREATE DATABASE IF NOT EXISTS food_redistribution;
USE food_redistribution;

CREATE TABLE IF NOT EXISTS donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(50),
    location VARCHAR(100),
    donor_type ENUM('Restaurant', 'Wedding', 'Individual') NOT NULL
);

CREATE TABLE IF NOT EXISTS receivers (
    receiver_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(50),
    location VARCHAR(100),
    receiver_type ENUM('NGO', 'Shelter', 'Individual') NOT NULL
);

CREATE TABLE IF NOT EXISTS donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT,
    food_details VARCHAR(255),
    quantity INT,
    donation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
);

CREATE TABLE IF NOT EXISTS distributions (
    distribution_id INT AUTO_INCREMENT PRIMARY KEY,
    donation_id INT,
    receiver_id INT,
    distribution_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (donation_id) REFERENCES donations(donation_id),
    FOREIGN KEY (receiver_id) REFERENCES receivers(receiver_id)
);

