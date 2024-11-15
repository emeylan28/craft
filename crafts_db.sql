CREATE DATABASE crafts;
USE crafts;

CREATE TABLE craft_type
	(craft VARCHAR(50) NOT NULL PRIMARY KEY);
    
CREATE TABLE dressmaking
	(item VARCHAR(50) NOT NULL, item_type VARCHAR(50));
    
CREATE TABLE knitting
	(item VARCHAR(50) NOT NULL, item_type VARCHAR(50));
    
CREATE TABLE paper_flower_making
	(item VARCHAR(50) NOT NULL, item_type VARCHAR(50));
    
CREATE TABLE embroidery
	(item VARCHAR(50) NOT NULL, item_type VARCHAR(50));
    
CREATE TABLE card_making
	(item VARCHAR(50) NOT NULL, item_type VARCHAR(50));
    
CREATE TABLE craft_items
	(item VARCHAR(50) NOT NULL PRIMARY KEY, _table_name VARCHAR(50));
    
CREATE TABLE wool
	(item_id INT NOT NULL PRIMARY KEY, item VARCHAR(50) NOT NULL, item_type VARCHAR(50) NOT NULL, material VARCHAR(50), colour VARCHAR(50), weight_g INT, item_use VARCHAR(150));
    
CREATE TABLE thread
	(item_id INT NOT NULL PRIMARY KEY, item VARCHAR(50) NOT NULL, item_type VARCHAR(50), colour VARCHAR(50));
    
CREATE TABLE paper
	(item_id INT NOT NULL PRIMARY KEY, item VARCHAR(50) NOT NULL, item_size VARCHAR(2), colour VARCHAR(50), weight_gsm INT);
    
CREATE TABLE card
	(item_id INT NOT NULL PRIMARY KEY, item VARCHAR(50) NOT NULL, item_size VARCHAR(2), colour VARCHAR(50), weight_gsm INT);
    
CREATE TABLE hand_sewing_needle
	(item_id INT NOT NULL PRIMARY KEY, item VARCHAR(50) NOT NULL, item_type VARCHAR(50) NOT NULL);
    
CREATE TABLE machine_sewing_needle
	(item_id INT NOT NULL PRIMARY KEY, item VARCHAR(50) NOT NULL, item_type VARCHAR(50) NOT NULL);
    
CREATE TABLE knitting_needle
	(item_id INT NOT NULL PRIMARY KEY, item VARCHAR(50) NOT NULL, item_type VARCHAR(50) NOT NULL, size_mm DECIMAL, item_use VARCHAR(150));
    
CREATE TABLE fabric
	(item_id INT NOT NULL PRIMARY KEY, item VARCHAR(50) NOT NULL, item_type VARCHAR(50) NOT NULL, pattern VARCHAR(50), colour VARCHAR(50), item_use VARCHAR(150));
    
CREATE TABLE other
	(item_id INT NOT NULL PRIMARY KEY, item VARCHAR(50) NOT NULL, item_type VARCHAR(50) NOT NULL, colour VARCHAR(50), item_use VARCHAR(150));

INSERT INTO craft_type
	(craft)
VALUES
	("Dressmaking"),
	("Knitting"),
	("Paper flower making"),
	("Embroidery"),
	("Card making");
    
INSERT INTO dressmaking
	(item, item_type)
VALUES
	("Fabric", "Your choice"),
	("Sewing Machine", "Your choice"),
	("Machine Sewing Needle", "Your choice"),
	("Thread", "Machine"),
	("Overlocker Machine", "Your choice");
    
INSERT INTO knitting
	(item, item_type)
VALUES
	("Wool", "Your choice"),
	("Knitting Needle", "Your choice"),
	("Stitch markers", "Your choice");
	
INSERT INTO paper_flower_making
	(item, item_type)
VALUES
	("Paper", "Paper"),
	("Card", "Card"),
	("Glue", "Hot glue gun"),
	("Glue", "Hot glue sticks"),
	("Tape", "Floral"),
	("Wire", "Floral");

INSERT INTO embroidery
	(item, item_type)
VALUES
	("Thread", "Embroidery"),
	("Fabric", "Your choice"),
	("Embroidery hoop",	"Hoop"),
	("Hand sewing Needle", "Your choice");

INSERT INTO card_making
	(item, item_type)
VALUES
	("Paper", "Paper"),
	("Glue", "Glue stick"),
	("Glue", "Glue tape"),
	("Tape", "Selotape");

INSERT INTO craft_items
	(item, _table_name)
VALUES
	("Wool", "wool"), 
    ("Card", "Card"), 
    ("Paper", "Paper"), 
    ("Fabric", "Fabric"), 
    ("Thread", "Thread"), 
    ("Hand sewing needle", "hand_sewing_needle"), 
    ("Machine sewing needle", "machine_sewing_needle"),
    ("Knitting needle", "knitting_needle"),
    ("Glue", "other"),
    ("Tape", "other"),
    ("Floral wire", "other"),
    ("Stitch markers", "other"),
    ("Sewing Machine", "other"),
    ("Overlocker Machine", "other"),
    ("Embroidery hoop", "other");
    

INSERT INTO wool
	(item_id, item, item_type, material, colour, weight_g, item_use)
VALUES
	(101, "Wool", "Super chunky", "100% wool", "Midnight Blue", 200, "Scarves, blankets, anything beginner!"),
	(102, "Wool", "Super chunky", "100% wool", "Rainbow Green", 200, "Scarves, blankets, anything beginner!"),
	(103, "Wool", "Chunky", "100% wool", "Lilac Powder", 100, "Hats, jumpers, cardigans, anything beginner!"),
	(104, "Wool", "Chunky", "100% wool", "Duck Egg Blue", 100, "Hats, jumpers, cardigans, anything beginner!"),
	(105, "Wool", "Chunky", "60% Merino, 40% Baby Alpaca", "Iced Coffee", 100, "Accessories, jumpers, cardigans, blankets (anything!)"),
	(106, "Wool", "Chunky", "60% Merino, 40% Baby Alpaca", "Chestnut Brown", 100, "Accessories, jumpers, cardigans, blankets (anything!)"),
	(107, "Wool", "Aran/Worsted", "70% Baby Alpaca, 7% Merino, 23% Recycled Nylon", "Forest Green", 50, "Jumpers, cardigans, hats"),
	(108, "Wool", "Aran/Worsted", "70% Baby Alpaca, 7% Merino, 23% Recycled Nylon", "Margaux Red", 50, "Jumpers, cardigans, hats"),
	(109, "Wool", "Aran/Worsted", "78% Kid Mohair, 13% Wool, 9% Polyamide", "Neon Pink", 50, "Jumpers, cardigans"),
	(110, "Wool", "Aran/Worsted", "78% Kid Mohair, 13% Wool, 9% Polyamide", "Chocolate Brown", 50, "Jumpers, cardigans"),
	(111, "Wool", "Aran/Worsted", "100% Merino Wool", "Slate blue", 50, "Core knitwear, babies, pets"),
	(112, "Wool", "Aran/Worsted", "100% Merino Wool", "Mustard Sally", 50, "Core knitwear, babies, pets"),
	(113, "Wool", "Chunky", "100% organic cotton", "Olive green", 100, "Jumpers, cardigans, tank tops"),
	(114, "Wool", "Chunky", "100% organic cotton", "Cornflower blue", 100, "Jumpers, cardigans, tank tops"),
	(115, "Wool", "Super chunky", "100% upcycled wool", "Sunset Orange", 200, "Scarves, blankets"),
	(116, "Wool", "Super chunky", "100% upcycled wool", "Cloud Blue", 200, "Scarves, blankets"),
	(119, "Wool", "Aran/Worsted", "97% recycled cashmere, 3% recycled wool", "Blush pink", 50, "Winter accessories"),
	(120, "Wool", "Aran/Worsted", "97% recycled cashmere, 3% recycled wool", "Eucalyptus Green", 50, "Winter accessories");
    
INSERT INTO thread
	(item_id, item, item_type, colour)
VALUES
	(201, "Thread", "Embroidery", "DMC 19"),
	(202, "Thread", "Embroidery", "DMC 21"),
	(203, "Thread", "Embroidery", "DMC 22"),
	(204, "Thread", "Embroidery", "DMC 29"),
	(205, "Thread", "Embroidery", "DMC 35"),
	(206, "Thread", "Embroidery", "DMC 108"),
	(207, "Thread", "Embroidery", "DMC 221"),
	(208, "Thread", "Machine", "Duck Egg Blue"),
	(209, "Thread", "Machine", "Natural"),
	(210, "Thread", "Machine", "Dark Red Brown"),
	(211, "Thread", "Machine", "Yellow"),
	(212, "Thread", "Machine", "Very Dark Forest Green");

INSERT INTO paper
	(item_id, item, item_size, colour, weight_gsm)
VALUES
	(301, "Paper", "A4", "Dusky Pink", 120),
	(302, "Paper", "A4", "Moss Green", 120),
	(303, "Paper", "A4", "Dusty Blue", 120),
	(304, "Paper", "A4", "Almond", 140),
	(305, "Paper", "A4", "Burgundy", 120),
	(306, "Paper", "A4", "Rose Gold", 140);


INSERT INTO card
	(item_id, item, item_size, colour, weight_gsm)
VALUES
	(401, "Card", "A4", "Cherry Red", 290),
	(402, "Card", "A4", "Pale Blue", 250),
	(403, "Card", "A4", "Rose Gold", 260),
	(404, "Card", "A4", "Dusky Pink", 250),
	(405, "Card", "A5", "White Hammer", 260),
	(406, "Card", "A5", "Recycled Ivory Fleck", 260),
    (407, "Card", "A5", "White linen", 250),
    (408, "Card", "A6", "Pearl, Gold", 230);


INSERT INTO hand_sewing_needle
	(item_id, item, item_type)
VALUES
	(501, "Hand sewing needle", "ballpoint"),
	(502, "Hand sewing needle", "beading"),
	(503, "Hand sewing needle", "quilting"),
	(504, "Hand sewing needle", "chenille"),
	(505, "Hand sewing needle", "darning"),
	(506, "Hand sewing needle", "doll"),
	(507, "Hand sewing needle", "embroidery"),
	(508, "Hand sewing needle", "leather"),
	(509, "Hand sewing needle", "upholstery"),
	(510, "Hand sewing needle", "straight point"),
	(511, "Hand sewing needle", "Tapestry"),
	(512, "Hand sewing needle", "yarn");
    
    
INSERT INTO machine_sewing_needle
	(item_id, item, item_type)
VALUES
	(601, "Machine sewing needle", "ballpoint"),
	(602, "Machine sewing needle", "quilting"),
	(603, "Machine sewing needle", "embroidery"),
	(604, "Machine sewing needle", "hemstitch"),
	(605, "Machine sewing needle", "leather"),
	(606, "Machine sewing needle", "universal"),
	(607, "Machine sewing needle", "straight point"),
	(608, "Machine sewing needle", "Topstitchting"),
	(609, "Machine sewing needle", "twin"),
	(610, "Machine sewing needle", "triple");


INSERT INTO knitting_needle
	(item_id, item, item_type, size_mm, item_use)
VALUES
	(701, "Knitting needle", "straight", 5, "lightweight wool"),
	(702, "Knitting needle", "Straight", 6.5, "lightweight wool"),
	(703, "Knitting needle", "Straight", 8, "medium-weight wool"),
	(704, "Knitting needle", "Straight", 10, "medium-weight wool"),
	(705, "Knitting needle", "Straight", 12, "medium-weight wool"),
	(706, "Knitting needle", "Straight", 15, "heavy-weight wool"),
	(707, "Knitting needle", "Straight", 25, "heavy-weight wool"),
	(708, "Knitting needle", "Circular", 3.5, "lightweight wool"),
	(709, "Knitting needle", "Circular", 4, "medium-weight wool"),
	(710, "Knitting needle", "Circular", 5, "medium-weight wool"),
	(711, "Knitting needle", "Circular", 6, "medium-weight wool");


INSERT INTO fabric
	(item_id, item, item_type, pattern, colour, item_use)
VALUES
	(801, "Fabric", "Cotton", "Willow Boughs", "Navy, White", "Quilting, dressmaking, anything"),
    (802, "Fabric", "Cotton", "Gingham", "Yellow", "Quilting, dressmaking, anything"),
	(803, "Fabric", "Cotton", "Sweet Cream", "multi", "Quilting, dressmaking, anything"),
	(804, "Fabric", "Cotton", "Painted Butterflies", "Blue", "Quilting, dressmaking, anything"),
	(805, "Fabric", "Jersey", "Graphic dots", "Blue", "Dresses, tops, children's clothes"),
	(806, "Fabric", "Jersey", "Big Flowers", "Multi", "Dresses, tops, children's clothes"),
	(807, "Fabric", "Jersey", "Digital Flowers", "Green	", "Dresses, tops, children's clothes"),
	(808, "Fabric", "Viscose", "Windy Night", "Blue", "Dressmaking"),
	(809, "Fabric", "Viscose", "Palmetto Off White", "White", "Dressmaking"),
	(810, "Fabric", "Viscose", "Bold and Bloom", "Green", "Dressmaking");


INSERT INTO other
	(item_id, item, item_type, colour, item_use)
VALUES
	(901, "Glue", "Hot glue gun", NULL, "Paper flowers"),
	(902, "Glue", "Hot glue stick", "Clear", "Paper flowers"),
	(903, "Glue", "glue stick",	"Clear", "Card making"),
	(904, "Glue", "glue tape", "Clear",	"Card making"),
	(905, "Tape", "selotape", "Clear", "Card making"),
	(906, "Tape", "floral tape", "Green", "Paper flowers"),
	(907, "Tape", "floral tape", "Brown", "Paper flowers"),
	(908, "Tape", "floral tape", "White	",	"Paper flowers"),
	(909, "Floral wire", "20guage",	"Green", "Paper flowers"),
	(910, "Floral wire", "22guage", "Brown", "Paper flowers"),
	(911, "Floral wire", "24guage",	"White", "Paper flowers"),
	(912, "Stitch markers", "Ring",	"Multi", "Knitting"),
	(913, "Stitch markers", "Clip", "Multi", "Knitting"),
	(914, "Sewing Machine", "Bernina", NULL	, "Dressmaking"),
	(915, "Overlocker Machine", "Bernina", NULL	, "Dressmaking"),
	(916, "Embroidery hoop", "7inch", NULL, "Embroidery"),
	(917, "Embroidery hoop", "8inch", NULL,	"Embroidery"),
	(918, "Embroidery hoop", "9inch", NULL,	"Embroidery"),
	(919, "Embroidery hoop", "10inch", NULL, "Embroidery");
