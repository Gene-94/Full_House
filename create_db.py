import mysql.connector

# If you get access denied for root you may want to sudo into you mysql cli and run the following query
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '$anewpasswordhere';

db_user = input("Insert your mysql username, with database creation privileges: ")
db_pass = input("insert the password for the inserted user: ")

db = mysql.connector.connect(
    host = 'localhost',
    user = db_user,
    passwd = db_pass,
    )

curs = db.cursor()

curs.execute( 
    """CREATE DATABASE Full_House_db;

    CREATE TABLE artists(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250) NOT NULL);
    CREATE TABLE bands(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250) NOT NULL, created_date DATE, music_genre VARCHAR(100));
    CREATE TABLE venues(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), address VARCHAR(255) NOT NULL);
    CREATE TABLE colabs(artist_id INT NOT NULL, band_id INT NOT NULL, joined_date DATE, left_date DATE, FOREIGN KEY (artist_id) REFERENCES artists(id), FOREIGN KEY (band_id) REFERENCES bands(ID), PRIMARY KEY (artist_id, band_id));
    CREATE TABLE event(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250),  venue_id INT NOT NULL, event_date DATE NOT NULL, FOREIGN KEY(venue_id) REFERENCES venues(id));
    CREATE TABLE confirmed_bands(band_id INT NOT NULL, event_id INT NOT NULL, PRIMARY KEY (band_id, event_id));

    INSERT INTO `artists` (`id`, `name`) VALUES (1, 'Dorcas Halvorson');
    INSERT INTO `artists` (`id`, `name`) VALUES (2, 'Mr. Jordan Klocko');
    INSERT INTO `artists` (`id`, `name`) VALUES (3, 'Dorris Davis PhD');
    INSERT INTO `artists` (`id`, `name`) VALUES (4, 'Josefa Johnson V');
    INSERT INTO `artists` (`id`, `name`) VALUES (5, 'Prof. Una Labadie');
    INSERT INTO `artists` (`id`, `name`) VALUES (6, 'Mr. Amari Bogisich MD');
    INSERT INTO `artists` (`id`, `name`) VALUES (7, 'Jeramy Davis');
    INSERT INTO `artists` (`id`, `name`) VALUES (8, 'Chase Parisian IV');
    INSERT INTO `artists` (`id`, `name`) VALUES (9, 'Caesar Hackett MD');
    INSERT INTO `artists` (`id`, `name`) VALUES (10, 'Alexander Lindgren');
    INSERT INTO `artists` (`id`, `name`) VALUES (11, 'Tomas Balistreri');
    INSERT INTO `artists` (`id`, `name`) VALUES (12, 'Ted Christiansen');
    INSERT INTO `artists` (`id`, `name`) VALUES (13, 'Dr. Monserrate Wolf');
    INSERT INTO `artists` (`id`, `name`) VALUES (14, 'Ocie Waelchi');
    INSERT INTO `artists` (`id`, `name`) VALUES (15, 'Mrs. Elva Bednar');
    INSERT INTO `artists` (`id`, `name`) VALUES (16, 'Destiny Heidenreich');
    INSERT INTO `artists` (`id`, `name`) VALUES (17, 'Lindsay Ferry');
    INSERT INTO `artists` (`id`, `name`) VALUES (18, 'Gust Bogisich II');
    INSERT INTO `artists` (`id`, `name`) VALUES (19, 'Cara McDermott');
    INSERT INTO `artists` (`id`, `name`) VALUES (20, 'Ms. Eula Schultz');
    INSERT INTO `artists` (`id`, `name`) VALUES (21, 'Ericka Predovic');
    INSERT INTO `artists` (`id`, `name`) VALUES (22, 'Francisco Mante');
    INSERT INTO `artists` (`id`, `name`) VALUES (23, 'Mr. Elwin Greenfelder');
    INSERT INTO `artists` (`id`, `name`) VALUES (24, 'Bret Brakus');
    INSERT INTO `artists` (`id`, `name`) VALUES (25, 'Tremaine Medhurst I');
    INSERT INTO `artists` (`id`, `name`) VALUES (26, 'Armand Lemke');
    INSERT INTO `artists` (`id`, `name`) VALUES (27, 'Lavada Witting');
    INSERT INTO `artists` (`id`, `name`) VALUES (28, 'Noelia Stehr MD');
    INSERT INTO `artists` (`id`, `name`) VALUES (29, 'Richie Stokes');
    INSERT INTO `artists` (`id`, `name`) VALUES (30, 'Ona Quigley');
    INSERT INTO `artists` (`id`, `name`) VALUES (31, 'Ardella Treutel');
    INSERT INTO `artists` (`id`, `name`) VALUES (32, 'Prof. Jabari Toy');
    INSERT INTO `artists` (`id`, `name`) VALUES (33, 'Prof. Jairo Flatley');
    INSERT INTO `artists` (`id`, `name`) VALUES (34, 'Lempi Jerde');
    INSERT INTO `artists` (`id`, `name`) VALUES (35, 'Thalia Legros');
    INSERT INTO `artists` (`id`, `name`) VALUES (36, 'Cary DAmore');
    INSERT INTO `artists` (`id`, `name`) VALUES (37, 'Alexanne Fadel');
    INSERT INTO `artists` (`id`, `name`) VALUES (38, 'Sharon Hackett');
    INSERT INTO `artists` (`id`, `name`) VALUES (39, 'Meredith Farrell');
    INSERT INTO `artists` (`id`, `name`) VALUES (40, 'Mr. Olin Dach');
    INSERT INTO `artists` (`id`, `name`) VALUES (41, 'Lauryn Ankunding');
    INSERT INTO `artists` (`id`, `name`) VALUES (42, 'Alexandra Mitchell');
    INSERT INTO `artists` (`id`, `name`) VALUES (43, 'Prof. Marcella Rohan DDS');
    INSERT INTO `artists` (`id`, `name`) VALUES (44, 'Leola Oberbrunner');
    INSERT INTO `artists` (`id`, `name`) VALUES (45, 'Molly Hyatt');
    INSERT INTO `artists` (`id`, `name`) VALUES (46, 'Dr. Howell Stoltenberg');
    INSERT INTO `artists` (`id`, `name`) VALUES (47, 'Ervin Sipes');
    INSERT INTO `artists` (`id`, `name`) VALUES (48, 'Brooks Terry III');
    INSERT INTO `artists` (`id`, `name`) VALUES (49, 'Dr. Sean Hudson');
    INSERT INTO `artists` (`id`, `name`) VALUES (50, 'Alexander O Connell II');


    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (1, 'Balanced zerodefect forecast', '1994-01-08', 'nihil');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (2, 'Multi-channelled 4thgeneration encoding', '2018-06-30', 'quia');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (3, 'Operative grid-enabled archive', '1978-05-28', 'numquam');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (4, 'Monitored human-resource approach', '2001-12-02', 'iusto');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (5, 'Right-sized national securedline', '1974-12-10', 'animi');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (6, 'Streamlined logistical conglomeration', '1995-12-17', 'doloribus');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (7, 'Triple-buffered client-server success', '1989-01-20', 'architecto');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (8, 'Future-proofed optimizing software', '2015-05-17', 'nesciunt');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (9, 'Grass-roots empowering hierarchy', '1992-01-17', 'laboriosam');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (10, 'Seamless disintermediate encoding', '1988-11-11', 'et');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (11, 'Enterprise-wide hybrid installation', '1998-04-01', 'non');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (12, 'Sharable fresh-thinking GraphicInterface', '2015-02-12', 'occaecati');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (13, 'Quality-focused even-keeled software', '1994-08-28', 'placeat');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (14, 'User-friendly maximized GraphicInterface', '1997-08-16', 'exercitationem');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (15, 'Optional even-keeled processimprovement', '2013-06-29', 'alias');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (16, 'Customer-focused fresh-thinking model', '1982-09-27', 'at');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (17, 'Enhanced global support', '1971-10-27', 'sed');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (18, 'Profound incremental architecture', '2008-03-20', 'eius');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (19, 'Sharable bottom-line architecture', '1994-09-11', 'debitis');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (20, 'Focused 5thgeneration moderator', '2006-11-08', 'porro');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (21, 'Reactive incremental extranet', '2021-05-04', 'reiciendis');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (22, 'Team-oriented actuating customerloyalty', '2021-12-29', 'perspiciatis');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (23, 'Adaptive fault-tolerant moderator', '2002-06-14', 'earum');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (24, 'Public-key full-range ability', '1974-03-15', 'est');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (25, 'Customizable 6thgeneration intranet', '1979-08-14', 'accusamus');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (26, 'Secured context-sensitive function', '1988-11-02', 'quidem');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (27, 'De-engineered systemic data-warehouse', '2008-02-28', 'error');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (28, 'Optional clear-thinking array', '2020-10-20', 'voluptates');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (29, 'Virtual client-server customerloyalty', '2012-12-09', 'aut');
    INSERT INTO `bands` (`id`, `name`, `created_date`, `music_genre`) VALUES (30, 'Proactive 6thgeneration matrices', '2012-04-10', 'qui');


    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (1, 1, '1990-01-24', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (2, 2, '1989-06-20', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (3, 3, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (4, 4, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (5, 5, '2012-06-13', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (6, 6, '2004-08-15', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (7, 7, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (8, 8, '1989-09-10', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (9, 9, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (10, 10, '1980-09-01', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (11, 11, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (12, 12, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (13, 13, '2014-07-21', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (14, 14, '1994-11-21', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (15, 15, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (16, 16, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (17, 17, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (18, 18, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (19, 19, '1980-09-15', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (20, 20, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (21, 21, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (22, 22, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (23, 23, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (24, 24, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (25, 25, '2008-01-14', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (26, 26, '2003-11-08', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (27, 27, '2001-09-03', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (28, 28, '1973-08-19', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (29, 29, '1977-01-15', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (30, 30, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (31, 1, '1999-12-14', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (32, 2, '1983-07-14', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (33, 3, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (34, 4, '2012-10-17', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (35, 5, '1994-03-07', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (36, 6, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (37, 7, '2021-01-28', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (38, 8, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (39, 9, '2012-02-27', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (40, 10, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (41, 11, '2000-01-09', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (42, 12, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (43, 13, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (44, 14, '1993-04-21', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (45, 15, '2015-12-05', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (46, 16, '1993-05-10', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (47, 17, '0000-00-00', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (48, 18, '2004-04-06', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (49, 19, '1971-05-29', NULL);
    INSERT INTO `colabs` (`artist_id`, `band_id`, `joined_date`, `left_date`) VALUES (50, 20, '0000-00-00', NULL);


    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (1, 'temporibus', '054 Hermann Terrace Apt. 024\nHamillhaven, KY 77407-5944');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (2, 'aspernatur', '7823 Davin Garden Apt. 823\nNew Lennyville, TX 18482');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (3, 'ut', '09142 Ebert Cove Apt. 824\nFadelborough, UT 75831-4627');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (4, 'est', '823 Alessandra Mall Suite 849\nPort Creola, TN 91280-7765');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (5, 'nobis', '04169 Stehr Lake Suite 089\nKesslerport, IL 86383');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (6, 'porro', '59485 McKenzie Stream\nVirginiaville, SC 45698-3463');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (7, 'blanditiis', '821 Valentina Run Suite 729\nAlyssonberg, NE 90164-1960');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (8, 'harum', '9849 Lesch Course Apt. 196\nNorth Johnathanstad, AZ 76180-6613');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (9, 'est', '898 Powlowski Haven Suite 303\nNew Cathrineview, AK 96541');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (10, 'earum', '18280 Bruen Ford\nHickleside, GA 04718-5295');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (11, 'ea', '91951 Sid Skyway\nNew Whitneyburgh, MS 63106-7991');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (12, 'soluta', '79655 Velva Radial\nBeierbury, DE 53660-7856');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (13, 'est', '60012 Uriah Ports Suite 043\nNorth Zaria, NH 61288');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (14, 'deserunt', '66275 Lisette Estate Suite 101\nSouth Kaylee, IN 45710');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (15, 'sit', '67734 Willms Plains\nCarterchester, MT 35112-5050');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (16, 'alias', '2296 Shanahan Street\nStarkside, WV 43106-8716');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (17, 'eius', '85118 Green Ridges Apt. 058\nHalvorsonburgh, FL 81521');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (18, 'aut', '64473 Considine Greens\nLake Brandy, KS 32344');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (19, 'iste', '4441 Hills Ridges Apt. 231\nNew Asiaport, ID 27720');
    INSERT INTO `venues` (`id`, `name`, `address`) VALUES (20, 'quibusdam', '3808 Mills Ville Suite 922\nOpheliabury, WI 52761-4866');


    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (1, 'Beahan Group', 1, '1977-05-18');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (2, 'Murphy Inc', 2, '1972-03-07');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (3, 'Rolfson LLC', 3, '1998-01-16');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (4, 'Olson-Hayes', 4, '1977-05-06');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (5, 'Dibbert, Dach and Corwin', 5, '1993-04-02');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (6, 'Dooley, Mayert and Kemmer', 6, '1983-04-13');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (7, 'Bashirian-Schultz', 7, '2018-12-30');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (8, 'Corwin, Lockman and Bauch', 8, '1987-06-18');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (9, 'Miller, Reichert and Strosin', 9, '1994-06-14');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (10, 'Paucek and Sons', 10, '1994-06-29');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (11, 'Pagac-Greenfelder', 11, '2005-01-18');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (12, 'Hoppe, Hamill and McDermott', 12, '2013-04-04');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (13, 'Gulgowski, Hettinger and Lehner', 13, '1980-06-27');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (14, 'Beier, O Reilly and Ebert', 14, '1989-01-20');
    INSERT INTO `event` (`id`, `name`, `venue_id`, `event_date`) VALUES (15, 'Hansen, Lang and Bednar', 15, '1991-06-09');

    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (1, 1);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (2, 2);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (3, 3);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (4, 4);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (5, 5);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (6, 6);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (7, 7);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (8, 8);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (9, 9);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (10, 10);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (11, 11);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (12, 12);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (13, 13);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (14, 14);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (15, 15);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (16, 1);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (17, 2);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (18, 3);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (19, 4);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (20, 5);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (21, 6);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (22, 7);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (23, 8);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (24, 9);
    INSERT INTO `confirmed_bands` (`band_id`, `event_id`) VALUES (25, 10);""", multi=True)

db.close()

