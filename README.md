# CS-480-Project
 Music database project for an intro to databases class. Database created with MySQL; interface created with Python using tkinter.

This application is a small project that allows you to manipulate a database intended primarily to catalog music.
The database consists of six tables, each of which can be independently manipulated:

- ARTIST: Each entry in the Artists table consists of the artist's name and their unique artist ID, which is necessary in the case of multiple artists sharing the same name.

- ALBUM: Each entry in the Albums table consists of the name of the album, the year in which it was released, and its unique album ID.

- SONG: Each entry in the Songs table consists of the name of the song, its genre, and its unique song ID.

- ARTIST-ALBUM: Each entry in the WritesAlbum table represents a relation between an album and an artist who created the album. For the purpose of this project, any given artist can write any number of albums, and any given album can belong to any number of artists; therefore, the relationship between artists and albums is many-to-many, and requires a separate table.
   Each entry in the WritesAlbum table consists of two columns: an artist ID and an album ID, where the album referred to by the album ID was written at least in part by the artist referred to by the artist ID.

- ALBUM-SONG: Each entry in the BelongsToAlbum table represents a relation between a song and an album to which the song belongs. Any given album can have any number of songs, and any given song can belong to any number of albums; thus, the album-song relationship is many-to-many and requires a separate table.
   Each entry in the BelongsToAlbum table consists of two columns: a song ID and an album ID, where the song referred to by the song ID belongs to the album referred to by the album ID.

- SONG-ARTIST: Each entry in the WritesSong table represents a relation between a song and an artist who created the song. Any given artist can write any number of songs, and any given song can belong to any number of artists; thus, the song-artist relationship is many-to-many and requires a separate table.
   Each entry in the WritesSong table consists of two columns: an artist ID and a song ID, where the artist referred to by the artist ID writes the song referred to by the song ID.

In addition to these six tables, this application has five generic operations that can each be applied to multiple tables, as well as two specific functions created to satisfy project requirements for the class.

- INSERT: Inserts a new entry into a given table. 
   For the Artists, Albums, and Songs tables, this only requires the name of the new entry (and, in the case of Albums and Songs, its given release year and genre, respectively). Upon insertion, a unique ID will be assigned to the entry. New IDs are assigned sequentially, so ID 1 will be assigned first, then 2, 3, and so on.
   For the three relational tables, rather than give names, IDs are required instead, so as not to cause confusion if multiple entries in the first three tables have identical names.

- DELETE: Delete a given entry from a given table.
   For the data tables (Artists, Albums, and Songs), deleting an entry also deletes any corresponding entries from the relational tables. In addition, in all tables, IDs are used in lieu of names in case multiple entries in a table have the same name. The data tables only require the ID of the specific entry to be deleted, while the relational tables require both the IDs in the given entry to delete.

- UPDATE: Change data about a given entry.
   Unlike the other operations, updating is only supported for the data tables and not the relational tables. This is because the operation requires the primary key of the table, followed by the information to change; in the case of the relational tables, the primary key consists entirely of the two columns of data in the table, so there is no additional information that can be changed.
   Unlike Insert and Delete, certain pieces of data can be left blank, leaving them unchanged.

- LIST: List out the contents of a given table.

- SEARCH: Search a table for entries matching one or more pieces of information.
   Unlike Insert and Delete, one or more fields can be left blank.
   The Search operation functions on one of two modes: "search for any of these conditions", which acts as an "or" operator on each piece of data (e.g. search for artists named "Hatsune Miku" OR with an artist ID of 5), or "search for all of these conditions", which instead acts as an "and" operator (e.g. search for artists named "Hatsune Miku" AND with an artist ID of 5).

- LIST ARTISTS WITH MANY SONGS: This function uses a complex nested SQL query to find the average number of songs per artist in the full database, then lists all artist whose songs-per-artist count is higher than the database average. If running using the default database (i.e. after running RESET_SETUP.sql), this will return three artists: Hatsune Miku, Vindata, and Rezz.

- LIST ALBUMS WITH FEW SONGS: In a contrast to the previous function, this uses an SQL query to first find the average number of songs per album in the database, then lists any albums with a lower-than-average number of songs. In the default database, this function returns five albums: Re:package, Scary Monsters and Nice Sprites, Yoja, Septic Souls, and .Temp.

This project was created for the class CS 480: Database Systems, at the University of Illinois at Chicago during the Summer 2022 semester. All code used in the project was created by myself, Barth Blazik.

To run the application, simply open any given terminal to the project folder and run the following command:
python project.py