# Dataset for inserting
# Customer_table's columns_info : customer_id, phone, country, address, level_royalty
customer_data = [
    ('CUS001', '010-1111-1111', 'Korea', 'Seoul, Gangnam-gu', 'Gold'),
    ('CUS002', '010-2222-2222', 'USA', 'New York, Manhattan', 'Silver'),
    ('CUS003', '010-3333-3333', 'Japan', 'Tokyo, Shibuya', 'Platinum'),
    ('CUS004', '010-4444-4444', 'UK', 'London, Soho', 'Gold'),
    ('CUS005', '010-5555-5555', 'France', 'Paris, Champs-Elysees', 'Silver'),
    ('CUS006', '010-6666-6666', 'Germany', 'Berlin, Mitte', 'Bronze'),
    ('CUS007', '010-7777-7777', 'Canada', 'Toronto, Downtown', 'Gold'),
    ('CUS008', '010-8888-8888', 'Australia', 'Sydney, CBD', 'Silver'),
    ('CUS009', '010-9999-9999', 'Vietnam', 'Ho Chi Minh', 'Bronze'),
    ('CUS010', '010-1010-1010', 'Singapore', 'Orchard Road', 'Platinum')
]

# Product_table's columns_info : product_id, product_name, price, weight_kg, seller_company 
product_data = [
    ('PRD001', 'Wireless Earbuds', 120.00, 0.2, 'Samsung'),
    ('PRD002', 'Smartphone Case', 25.00, 0.05, 'LG'),
    ('PRD003', 'Portable Charger', 50.00, 0.3, 'Anker'),
    ('PRD004', 'Bluetooth Speaker', 85.00, 1.2, 'Sony'),
    ('PRD005', 'Smartwatch', 250.00, 0.5, 'Apple'),
    ('PRD006', 'Laptop Sleeve', 30.00, 0.4, 'Logitech'),
    ('PRD007', 'Mechanical Keyboard', 100.00, 1.5, 'Keychron'),
    ('PRD008', 'Gaming Mouse', 60.00, 0.25, 'Razer'),
    ('PRD009', 'Noise Cancelling Headphones', 300.00, 0.8, 'Bose'),
    ('PRD010', 'Webcam', 90.00, 0.35, 'Logitech')
]


# order_table's columns_info: order_id, customer_id, product_id, delivery_id, delivery_fee, order_date, shipping_date, request 
order_data = [
    ('ORD001', 'CUS001', 'PRD001', 101, 15.00, '2024-04-25 10:00:00', '2024-04-26 12:00:00', 'Handle with care'),
    ('ORD002', 'CUS002', 'PRD002', 102, 20.00, '2024-04-25 11:00:00', '2024-04-27 15:00:00', ''),
    ('ORD003', 'CUS003', 'PRD003', 103, 18.00, '2024-04-25 12:30:00', '2024-04-28 10:00:00', 'Gift wrap'),
    ('ORD004', 'CUS004', 'PRD004', 104, 25.00, '2024-04-25 14:00:00', '2024-04-29 09:00:00', ''),
    ('ORD005', 'CUS005', 'PRD005', 105, 22.00, '2024-04-25 15:00:00', '2024-04-30 13:00:00', 'Urgent delivery'),
    ('ORD006', 'CUS006', 'PRD006', 106, 17.00, '2024-04-25 16:00:00', '2024-04-27 10:00:00', ''),
    ('ORD007', 'CUS007', 'PRD007', 107, 19.00, '2024-04-25 17:00:00', '2024-04-28 11:00:00', ''),
    ('ORD008', 'CUS008', 'PRD008', 108, 16.00, '2024-04-25 18:00:00', '2024-04-29 08:00:00', ''),
    ('ORD009', 'CUS009', 'PRD009', 109, 21.00, '2024-04-25 19:00:00', '2024-04-30 14:00:00', ''),
    ('ORD010', 'CUS010', 'PRD010', 110, 23.00, '2024-04-25 20:00:00', '2024-05-01 16:00:00', 'Fragile item')
]

# addition1
customer_data_additional = [
    ('CUS011', '010-1111-2222', 'Korea', 'Seoul, Seocho-gu', 'Gold'),
    ('CUS012', '010-2222-3333', 'USA', 'Los Angeles, Downtown', 'Silver'),
    ('CUS013', '010-3333-4444', 'Japan', 'Osaka, Umeda', 'Bronze'),
    ('CUS014', '010-4444-5555', 'UK', 'Manchester, City Centre', 'Gold'),
    ('CUS015', '010-5555-6666', 'France', 'Lyon, La Croix-Rousse', 'Silver'),
    ('CUS016', '010-6666-7777', 'Germany', 'Munich, Marienplatz', 'Platinum'),
    ('CUS017', '010-7777-8888', 'Canada', 'Vancouver, Downtown', 'Bronze'),
    ('CUS018', '010-8888-9999', 'Australia', 'Melbourne, CBD', 'Gold'),
    ('CUS019', '010-9999-0000', 'Vietnam', 'Hanoi, Old Quarter', 'Silver'),
    ('CUS020', '010-0000-1111', 'Singapore', 'Sentosa Island', 'Platinum')
]

product_data_additional = [
    ('PRD011', 'Tablet PC', 450.00, 0.7, 'Apple'),
    ('PRD012', 'Smart TV Remote', 45.00, 0.2, 'Samsung'),
    ('PRD013', 'Gaming Headset', 120.00, 0.6, 'Razer'),
    ('PRD014', 'Portable Hard Drive', 95.00, 0.4, 'Seagate'),
    ('PRD015', 'Fitness Tracker', 80.00, 0.2, 'Fitbit'),
    ('PRD016', 'Wireless Keyboard', 70.00, 0.9, 'Logitech'),
    ('PRD017', 'e-Book Reader', 130.00, 0.5, 'Amazon'),
    ('PRD018', 'Drone Mini', 600.00, 1.1, 'DJI'),
    ('PRD019', 'Smart Lighting Kit', 200.00, 1.8, 'Philips Hue'),
    ('PRD020', '4K Webcam', 150.00, 0.3, 'Logitech')
]

order_data_additional = [
    ('ORD011', 'CUS011', 'PRD011', 111, 20.00, '2024-04-27 09:00:00', '2024-04-28 10:00:00', 'Fragile item'),
    ('ORD012', 'CUS012', 'PRD012', 112, 18.00, '2024-04-27 10:30:00', '2024-04-29 12:00:00', ''),
    ('ORD013', 'CUS013', 'PRD013', 113, 22.00, '2024-04-27 12:00:00', '2024-04-30 14:00:00', 'Gift pack'),
    ('ORD014', 'CUS014', 'PRD014', 114, 25.00, '2024-04-27 13:00:00', '2024-04-30 16:00:00', ''),
    ('ORD015', 'CUS015', 'PRD015', 115, 17.00, '2024-04-27 14:30:00', '2024-05-01 10:00:00', ''),
    ('ORD016', 'CUS016', 'PRD016', 116, 23.00, '2024-04-27 15:00:00', '2024-05-01 12:00:00', ''),
    ('ORD017', 'CUS017', 'PRD017', 117, 20.00, '2024-04-27 16:30:00', '2024-05-01 14:00:00', 'Quick shipping'),
    ('ORD018', 'CUS018', 'PRD018', 118, 28.00, '2024-04-27 17:00:00', '2024-05-02 16:00:00', ''),
    ('ORD019', 'CUS019', 'PRD019', 119, 24.00, '2024-04-27 18:00:00', '2024-05-02 18:00:00', ''),
    ('ORD020', 'CUS020', 'PRD020', 120, 26.00, '2024-04-27 19:30:00', '2024-05-03 10:00:00', 'Urgent delivery')
]
