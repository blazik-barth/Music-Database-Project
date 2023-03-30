DELETE FROM Artists WHERE artist_id >= 1;
DELETE FROM Albums WHERE album_id >= 1;
DELETE FROM Songs WHERE song_id >= 1;
DELETE FROM BelongsToAlbum WHERE album_id >= 1 AND song_id >= 1;
DELETE FROM WritesAlbum WHERE album_id >= 1 AND artist_id >= 1;
DELETE FROM WritesSong WHERE song_id >= 1 AND artist_id >= 1;

ALTER TABLE Artists AUTO_INCREMENT = 1;
ALTER TABLE Albums AUTO_INCREMENT = 1;
ALTER TABLE Songs AUTO_INCREMENT = 1;

INSERT INTO Artists(artist_name) VALUES ('Hatsune Miku'), ('Vindata'), ('Skrillex'), ('Ekcle'), ('QVEST'), ('Rezz'), ('Convexity'), ('Bad Computer'), ('Graham Kartna'), ('Starjunk95');
INSERT INTO Albums (album_name, year) VALUES ('Re:package', 2008), ('Hatsune Miku 1st Song Album', 2007), ('With Opened Eyes', 2021), ('Scary Monsters and Nice Sprites', 2012), ('Yoja', 2019), ('Septic Souls', 2022), ('Spiral', 2022), ('.Temp', 2018);
INSERT INTO Songs (song_name, genre) VALUES ('Miku Miku ni Shite Ageru', 'Vocaloid'), ('Aoi Usagi', 'Vocaloid'), ('Tori no Uta', 'Vocaloid'), ('Ne-ni-ge de Reset!', 'Vocaloid'), ('Tsuki no Shizuku', 'Vocaloid'), ('Mirai no Eve', 'Vocaloid'), ('Platinum', 'Vocaloid'), ('Futari no Mojipittan', 'Vocaloid'), ('Uninstall', 'Vocaloid'), ('Ano Subarashii Ai o Mou Ichido', 'Vocaloid'), ('ANGEL VOICE', 'Vocaloid'), ('Ievan Polkka', 'Vocaloid'), ('True My Heart', 'Vocaloid'), ('Melodies of Life', 'Vocaloid'), ('you', 'Vocaloid'),
('Anthem', 'Vocaloid'), ('Packaged', 'Vocaloid'), ('over16bit!', 'Vocaloid'), ('Light Song', 'Vocaloid'), ('Last Night, Good Night', 'Vocaloid'), ('our music', 'vocaloid'),
('Union', 'Future Bass'), ('6 ft.', 'Pop'), ('One Time', 'Pop'), ('Good 4 Me', 'Indie Dance'), ('Odyssey', 'Trap'), ('Skin (I Give In To You)', 'Pop'), ('Already Home', 'Pop'), ('B4 Noon', 'Rap'), ('Knock On', 'Future Bass'), ('Spiritual Food (Interlude)', 'Other'), ('Amethyst', 'Trap'), ('Try Me', 'Pop'),
('Rock \'n\' Roll (Will Take You to the Mountain)', 'Complextro'), ('Scary Monsters and Nice Sprites', 'Dubstep'), ('Kill EVERYBODY', 'Dubstep'), ('All I Ask of You', 'Electro House'), ('With You, Friends (Long Drive)', 'Dubstep'),
('Within the Palms of a God', 'Halftime'), ('Totemfire', 'Other'), ('Moonstone', 'Garage'), ('Clandestine', 'Other'), ('Crafted in Ice', 'Other'),
('Walk Away', 'Future Bass'), ('Escape', 'Chillout'), ('Divinity', 'Chillout'), 
('Chemical Bond', 'Midtempo'), ('Let Me In', 'Midtempo'), ('Levitate', 'Midtempo'), ('Sacrificial', 'Midtempo'), ('Paper Walls', 'Midtempo'), ('Spun', 'Midtempo'), ('Out Of My Head', 'Midtempo'), ('Taste of You', 'Midtempo'), ('Vortex', 'Midtempo'), ('Time', 'Midtempo'), ('Breathe', 'Midtempo'), ('Menace', 'Midtempo'),
('Robotkisses.Temp', 'Pop'), ('Siliconvalleysyrup.Temp', 'Other'), ('Eternal.Temp', 'Other'), ('16fca.Temp', 'Other'),
('Entangle', 'Color Bass'), ('Network', 'Color Bass'), ('Lattice', 'Color Bass'),
('Disarray', 'House'), ('Riddle', 'Complextro'), ('Clarity', 'Breaks'), ('2U', 'House');
#in case anyone sees this: i hated typing this out manually so dang much
#i wish i lived in the alternate universe where albums only have like 8 songs ever

INSERT INTO BelongsToAlbum (SELECT song_id, 1 FROM Songs WHERE song_id >= 16 AND song_id < 22);
INSERT INTO BelongsToAlbum (SELECT song_id, 2 FROM Songs WHERE song_id >= 1 AND song_id < 16);
INSERT INTO BelongsToAlbum (SELECT song_id, 3 FROM Songs WHERE song_id >= 22 AND song_id < 34);
INSERT INTO BelongsToAlbum (SELECT song_id, 4 FROM Songs WHERE song_id >= 34 AND song_id < 39);
INSERT INTO BelongsToAlbum (SELECT song_id, 5 FROM Songs WHERE song_id >= 39 AND song_id < 44);
INSERT INTO BelongsToAlbum (SELECT song_id, 6 FROM Songs WHERE song_id = 44 OR song_id = 46);
INSERT INTO BelongsToAlbum (SELECT song_id, 7 FROM Songs WHERE song_id >= 47 AND song_id < 59);
INSERT INTO BelongsToAlbum (SELECT song_id, 8 FROM Songs WHERE song_id >= 59 AND song_id < 63);

INSERT INTO WritesAlbum VALUES (1,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (9,8);
 
INSERT INTO WritesSong (SELECT 1, song_id FROM Songs WHERE song_id >= 1 AND song_id < 22);
INSERT INTO WritesSong (SELECT 2, song_id FROM Songs WHERE song_id >= 22 AND song_id < 34);
INSERT INTO WritesSong (SELECT 3, song_id FROM Songs WHERE song_id >= 34 AND song_id < 39);
INSERT INTO WritesSong (SELECT 4, song_id FROM Songs WHERE song_id >= 39 AND song_id < 44);
INSERT INTO WritesSong (SELECT 5, song_id FROM Songs WHERE song_id >= 44 AND song_id < 47);
INSERT INTO WritesSong (SELECT 6, song_id FROM Songs WHERE song_id >= 47 AND song_id < 59);
INSERT INTO WritesSong (SELECT 9, song_id FROM Songs WHERE song_id >= 59 AND song_id < 63);
INSERT INTO WritesSong (SELECT 7, song_id FROM Songs WHERE song_id >= 63 AND song_id < 66);
INSERT INTO WritesSong (SELECT 8, song_id FROM Songs WHERE song_id >= 66 AND song_id < 70);