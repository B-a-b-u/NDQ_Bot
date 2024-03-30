-- Create the database
CREATE DATABASE pc_factory;
USE pc_factory;

-- Create the pc_inventory table
CREATE TABLE pc_inventory (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL
);

-- Populate the pc_inventory table with sample data
INSERT INTO pc_inventory (name, price, stock_quantity)
VALUES
('Gaming PC - Model X', 1500.00, 10),
('Professional Workstation - Model Y', 2000.00, 8),
('Home Office PC - Model Z', 1000.00, 15),
('Media Editing PC - Model A', 2500.00, 5),
('Student Laptop - Model B', 800.00, 20),
('Ultra-Portable Laptop - Model C', 1200.00, 12),
('Gaming Laptop - Model D', 1800.00, 7),
('2-in-1 Convertible Laptop - Model E', 1500.00, 10),
('Business Laptop - Model F', 1500.00, 8),
('Chromebook - Model G', 600.00, 25);

-- Create the discounts table
CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100),
    FOREIGN KEY (product_id) REFERENCES pc_inventory(product_id)
);

-- Insert at least 5 records into the discounts table
INSERT INTO discounts (product_id, pct_discount)
VALUES
(1, 10.00),
(3, 15.00),
(5, 20.00),
(7, 5.00),
(9, 25.00);
