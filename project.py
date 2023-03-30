# importing MySQL Connector, in order to access the database, and tkinter to make the GUI
from tkinter import *
from tkinter import ttk
import mysql.connector


# setting up connection to the SQL database
cnx = mysql.connector.connect(user='root', host='127.0.0.1', database='ProjectDatabase')
cursor = cnx.cursor()

# QOL tables, to make some calculations more comprehensible
three_attr_tables = {'Albums', 'Songs'}
relation_tables = {'BelongsToAlbum', 'WritesAlbum', 'WritesSong'}


#####
# GUI FUNCTIONS
#####

# these functions set which table to perform tasks on, and edit the GUI accordingly.
def set_artists(*args):
    table.set("Artists")
    attr1.set("artist_id")
    attr2.set("artist_name")
    attr3.set("")
    lb3.grid_forget()
    clear_entry()
    update_confirm_text()
    select_mode()

def set_albums(*args):
    table.set("Albums")
    attr1.set("album_id")
    attr2.set("album_name")
    attr3.set("year")
    lb3.grid(column=3, row=2)
    clear_entry()
    update_confirm_text()
    select_mode()

def set_songs(*args):
    table.set("Songs")
    attr1.set("song_id")
    attr2.set("song_name")
    attr3.set("genre")
    lb3.grid(column=3, row=2)
    clear_entry()
    update_confirm_text()
    select_mode()

def set_artist_album(*args):
    table.set("WritesAlbum")
    attr1.set("artist_id")
    attr2.set("album_id")
    attr3.set("")
    lb3.grid_forget()
    clear_entry()
    update_confirm_text()
    select_mode()

def set_album_song(*args):
    table.set("BelongsToAlbum")
    attr1.set("song_id")
    attr2.set("album_id")
    attr3.set("")
    lb3.grid_forget()
    clear_entry()
    update_confirm_text()
    select_mode()

def set_song_artist(*args):
    table.set("WritesSong")
    attr1.set("artist_id")
    attr2.set("song_id")
    attr3.set("")
    lb3.grid_forget()
    clear_entry()
    update_confirm_text()
    select_mode()

# functions for selecting the various tasks

def  select_mode(*args):
    i_lab3.grid_forget()
    i_ent3.grid_forget()
    searchbutt1.grid_forget()
    searchbutt2.grid_forget()
    if mode.get() == "Insert Into":
        select_insert()
    elif mode.get() == "Delete From":
        select_delete()
    elif mode.get() == "Update":
        select_update()
    elif mode.get() == "List":
        select_list()
    else:
        select_search()

def select_insert(*args):
    if (table.get() in relation_tables):
        input_l1.set(attr1.get())
        input_l2.set(attr2.get())
        i_lab1.grid(column=1, row=1, sticky=(NE))
        i_lab2.grid(column=1, row=2, sticky=(E))
        i_ent1.grid(column=2, row=1, sticky=(NE))
        i_ent2.grid(column=2, row=2, sticky=(E))
    elif (table.get() in three_attr_tables):
        input_l1.set(attr2.get())
        input_l2.set(attr3.get())
        i_lab1.grid(column=1, row=1, sticky=(NE))
        i_lab2.grid(column=1, row=2, sticky=(E))
        i_ent1.grid(column=2, row=1, sticky=(NE))
        i_ent2.grid(column=2, row=2, sticky=(E))
    else:
        input_l1.set(attr2.get())
        i_lab1.grid(column=1, row=1, sticky=(NE))
        i_ent1.grid(column=2, row=1, sticky=(NE))
        i_lab2.grid_forget()
        i_ent2.grid_forget()

    update_confirm_text()

def select_delete(*args):
    input_l1.set(attr1.get())
    i_lab1.grid(column=1, row=1, sticky=(NE))
    i_ent1.grid(column=2, row=1, sticky=(NE))
    if table.get() in relation_tables:
        input_l2.set(attr2.get())
        i_lab2.grid(column=1, row=2, sticky=(E))
        i_ent2.grid(column=2, row=2, sticky=(E))
    else:
        i_lab2.grid_forget()
        i_ent2.grid_forget()

    update_confirm_text()

def select_update(*args):
    input_l1.set(attr1.get())
    input_l2.set(attr2.get())
    i_lab1.grid(column=1, row=1, sticky=(NE))
    i_ent1.grid(column=2, row=1, sticky=(NE))
    i_lab2.grid(column=1, row=2, sticky=(E))
    i_ent2.grid(column=2, row=2, sticky=(E))
    if table.get() in three_attr_tables:
        input_l3.set(attr3.get())
        i_lab3.grid(column=1, row=3, sticky=(SE))
        i_ent3.grid(column=2, row=3, sticky=(SE))
    else:
        i_lab3.grid_forget()
        i_ent3.grid_forget()
    update_confirm_text()

def select_list(*args):
    i_lab1.grid_forget()
    i_ent1.grid_forget()
    i_lab2.grid_forget()
    i_ent2.grid_forget()
    update_confirm_text()

def select_search(*args):
    input_l1.set(attr1.get())
    input_l2.set(attr2.get())
    i_lab1.grid(column=1, row=1, sticky=(NE))
    i_ent1.grid(column=2, row=1, sticky=(NE))
    i_lab2.grid(column=1, row=2, sticky=(E))
    i_ent2.grid(column=2, row=2, sticky=(E))
    if table.get() in three_attr_tables:
        input_l3.set(attr3.get())
        i_lab3.grid(column=1, row=3, sticky=(SE))
        i_ent3.grid(column=2, row=3, sticky=(SE))
    searchbutt1.grid(column=1, row=4)
    searchbutt2.grid(column=2, row=4)
    update_confirm_text()


#####
# QOL FUNCTIONS
#####

# clear entry boxes
def clear_entry(*args):
    i_ent1.delete(0, END)
    i_ent2.delete(0, END)
    i_ent3.delete(0, END)

# update the text of the confirmation button
def update_confirm_text(*args):
    confirm_text.set("{} {}".format(mode.get(), table.get()))

# check to see if the right entry boxes are filled in
def blank_check(*args):
    if e1_text.get() == "":
            bottom_text.set("Error. No value listed for {}.".format(input_l1.get()))
            return False
    elif table.get() != "Artists" and e2_text.get() == "":
            bottom_text.set("Error. No value listed for {}.".format(input_l2.get()))
            return False
    else: return True
    

#####
# SQL FUNCTIONS
#####

# function to perform an SQL query
def make_query(*args):
    list1 = []
    list2 = []
    list3 = []
    if mode.get() == "Insert Into":
        if blank_check():
            if table.get() == "Artists":
                sql_query = "INSERT INTO Artists (artist_name) VALUES ('{}')".format(e1_text.get())
                cursor.execute(sql_query)
                bottom_text.set("Inserted artist {}.".format(e1_text.get()))
            elif table.get() == "Albums":
                sql_query = "INSERT INTO Albums (album_name, year) VALUES ('{}',{})".format(e1_text.get(), e2_text.get())
                cursor.execute(sql_query)
                bottom_text.set("Inserted album {} from the year {}.".format(e1_text.get(), e2_text.get()))
            elif table.get() == "Songs":
                sql_query = "INSERT INTO Songs (song_name, genre) VALUES ('{}','{}')".format(e1_text.get(), e2_text.get())
                cursor.execute(sql_query)
                bottom_text.set("Inserted song {} of genre {}".format(e1_text.get(), e2_text.get()))
            else:
                sql_query = "INSERT INTO {} ({}, {}) VALUES ({}, {})".format(table.get(), attr1.get(), attr2.get(), e1_text.get(), e2_text.get())
                cursor.execute(sql_query)
                bottom_text.set("Inserted entry ({},{}) into table {}.".format(e1_text.get(),e2_text.get(), table.get()))
    elif mode.get() == "Delete From":
        if e1_text.get() == "":
            bottom_text.set("Error. No value listed for {}.".format(input_l1.get()))
            return
        elif table.get() not in relation_tables:
            sql_query = "DELETE FROM {} WHERE {} = {}".format(table.get(), attr1.get(), e1_text.get())
            cursor.execute(sql_query)
            if table.get() == "Artists":
                cursor.execute("DELETE FROM WritesAlbum WHERE artist_id = {}".format(e1_text.get()))
                cursor.execute("DELETE FROM WritesSong WHERE artist_id = {}".format(e1_text.get()))
            elif table.get() == "Albums":
                cursor.execute("DELETE FROM WritesAlbum WHERE album_id = {}".format(e1_text.get()))
                cursor.execute("DELETE FROM BelongsToAlbum WHERE album_id = {}".format(e1_text.get()))
            elif table.get() == "Songs":
                cursor.execute("DELETE FROM WritesSong WHERE song_id = {}".format(e1_text.get()))
                cursor.execute("DELETE FROM BelongsToAlbum WHERE song_id = {}".format(e1_text.get()))
            bottom_text.set("Deleted ID {} from table {}.".format(e1_text.get(), table.get()))
        else:
            if e2_text.get() == "":
                bottom_text.set("Error. No value listed for {}.".format(input_l2.get()))
                return
            else:
                sql_query = "DELETE FROM {} WHERE {} = {} AND {} = {}".format(table.get(), attr1.get(), e1_text.get(), attr2.get(), e2_text.get())
                cursor.execute(sql_query)
                bottom_text.set("Deleted entry ({},{}) from table {}.".format(e1_text.get(), e2_text.get(), table.get()))
    elif mode.get() == "Update":
        if table.get() in relation_tables:
            bottom_text.set("Update task cannot be performed on relationship tables.")
            return
        else:
            if e1_text.get() == "":
                bottom_text.set("Error. Cannot update on entry without unique ID.")
                return
            else:
                if (e2_text.get() == "") and (e3_text.get() == ""):
                    bottom_text.set("Nothing to change. Entry not updated.")
                    return
                if (e2_text.get() != ""):
                    sql_query = "UPDATE {} SET {} = '{}' WHERE {} = {}".format(table.get(), attr2.get(), e2_text.get(), attr1.get(), e1_text.get())
                    cursor.execute(sql_query)
                if (e3_text.get() != ""):
                    if table.get() == "Albums":
                        sql_query = "UPDATE {} SET {} = {} WHERE {} = {}".format(table.get(), attr3.get(), e3_text.get(), attr1.get(), e1_text.get())
                        cursor.execute(sql_query)
                    else:
                        sql_query = "UPDATE {} SET {} = '{}' WHERE {} = {}".format(table.get(), attr3.get(), e3_text.get(), attr1.get(), e1_text.get())
                        cursor.execute(sql_query)
                bottom_text.set("Updated ID number {} in table {}.".format(e1_text.get(),table.get()))
    elif mode.get() == "List":
        sql_query = "SELECT * FROM " + table.get()
        cursor.execute(sql_query)
        if table.get() in three_attr_tables:
            for (att1, att2, att3) in cursor:
                list1.append(att1)
                list2.append(att2)
                list3.append(att3)
        else:
            for (att1, att2) in cursor:
                list1.append(att1)
                list2.append(att2)
        list1var.set(list1)
        list2var.set(list2)
        list3var.set(list3)
    else: execute_search()
            


# function to perform the search task
def execute_search(*args):
    list1 = []
    list2 = []
    list3 = []
    if table.get() in relation_tables:
        if (e1_text.get() != "") and (e2_text.get() != ""):
            if search_mode.get() == 0:
                sql_query = "SELECT * FROM {} WHERE ({} = {}) OR ({} = {})".format(table.get(), attr1.get(), e1_text.get(), attr2.get(), e2_text.get())
            else:
                sql_query = "SELECT * FROM {} WHERE ({} = {}) AND ({} = {})".format(table.get(), attr1.get(), e1_text.get(), attr2.get(), e2_text.get())
        elif (e1_text.get() == "") and (e2_text.get() != ""):
            sql_query = "SELECT * FROM {} WHERE {} = {}".format(table.get(), attr2.get(), e2_text.get())
        elif (e2_text.get() == "") and (e1_text.get() != ""):
            sql_query = "SELECT * FROM {} WHERE {} = {}".format(table.get(), attr1.get(), e1_text.get())
        else:
            bottom_text.set("Cannot execute search. No parameters listed.")
            return
    elif table.get() == "Artists":
        if (e1_text.get() != "") and (e2_text.get() != ""):
            if search_mode.get() == 0:
                sql_query = "SELECT * FROM Artists WHERE (artist_id = {} OR artist_name = '{}')".format(e1_text.get(), e2_text.get())
            else:
                sql_query = "SELECT * FROM Artists WHERE (artist_id = {} AND artist_name = '{}')".format(e1_text.get(), e2_text.get())
        elif (e1_text.get() != "") and (e2_text.get() == ""):
            sql_query = "SELECT * FROM Artists WHERE artist_id = {}".format(e1_text.get())
        elif (e1_text.get() == "") and (e2_text.get() != ""):
            sql_query = "SELECT * FROM Artists WHERE artist_name = '{}'".format(e2_text.get())
        else:
            bottom_text.set("Cannot execute search. No parameters listed.")
            return
    elif table.get() == "Albums":
        if (e1_text.get() != ""):
            if (e2_text.get() != ""):
                if (e3_text.get() != ""):
                    # 123
                    if search_mode.get() == 0:
                        sql_query = "SELECT * FROM Albums WHERE (album_id = {} OR album_name = '{}' OR year = {})".format(e1_text.get(), e2_text.get(), e3_text.get())
                    else:
                        sql_query = "SELECT * FROM Albums WHERE (album_id = {} AND album_name = '{}' AND year = {})".format(e1_text.get(), e2_text.get(), e3_text.get())
                else:
                    #12
                    if search_mode.get() == 0:
                        sql_query = "SELECT * FROM Albums WHERE (album_id = {} OR album_name = '{}')".format(e1_text.get(), e2_text.get())
                    else:
                        sql_query = "SELECT * FROM Albums WHERE (album_id = {} AND album_name = '{})'".format(e1_text.get(), e2_text.get())
            else:
                if e3_text.get() != "":
                    # 13
                    if search_mode.get() == 0:
                        sql_query = "SELECT * FROM Albums WHERE (album_id = {} OR year = {})".format(e1_text.get(), e3_text.get())
                    else:
                        sql_query = "SELECT * FROM Albums WHERE (album_id = {} AND year = {})".format(e1_text.get(), e3_text.get())
                else:
                    #1
                    sql_query = "SELECT * FROM Albums WHERE album_id = {}".format(e1_text.get())
        else:
            if e2_text.get() != "":
                if e3_text.get() != "":
                    # 23
                    if search_mode.get() == 0:
                        sql_query = "SELECT * FROM Albums WHERE (album_name = '{}' OR year = {})".format(e2_text.get(), e3_text.get())
                    else:
                        sql_query = "SELECT * FROM Albums WHERE (album_name = '{}' AND year = {})".format(e2_text.get(), e3_text.get())
                else:
                    # 2
                    sql_query = "SELECT * FROM Albums WHERE album_name = '{}'".format(e2_text.get())
            else:
                if e3_text.get() != "":
                    # 3
                    sql_query = "SELECT * FROM Albums WHERE year = {}".format(e3_text.get())
                else:
                    # none
                    bottom_text.set("Cannot execute search. No parameters listed.")
                    return
    elif table.get() == "Songs":
        if (e1_text.get() != ""):
            if (e2_text.get() != ""):
                if (e3_text.get() != ""):
                    # 123
                    if search_mode.get() == 0:
                        sql_query = "SELECT * FROM Songs WHERE (song_id = {} OR song_name = '{}' OR genre = '{}')".format(e1_text.get(), e2_text.get(), e3_text.get())
                    else:
                        sql_query = "SELECT * FROM Songs WHERE (song_id = {} AND song_name = '{}' AND genre = '{}')".format(e1_text.get(), e2_text.get(), e3_text.get())
                else:
                    #12
                    if search_mode.get() == 0:
                        sql_query = "SELECT * FROM Songs WHERE (song_id = {} OR song_name = '{}')".format(e1_text.get(), e2_text.get())
                    else:
                        sql_query = "SELECT * FROM Songs WHERE (song_id = {} AND song_name = '{}')".format(e1_text.get(), e2_text.get())
            else:
                if e3_text.get() != "":
                    # 13
                    if search_mode.get() == 0:
                        sql_query = "SELECT * FROM Songs WHERE (song_id = {} OR genre = '{}')".format(e1_text.get(), e3_text.get())
                    else:
                        sql_query = "SELECT * FROM Songs WHERE (song_id = {} AND genre = '{}')".format(e1_text.get(), e3_text.get())
                else:
                    #1
                    sql_query = "SELECT * FROM Songs WHERE song_id = {}".format(e1_text.get())
        else:
            if e2_text.get() != "":
                if e3_text.get() != "":
                    # 23
                    if search_mode.get() == 0:
                        sql_query = "SELECT * FROM Songs WHERE (song_name = '{}' OR genre = '{}')".format(e2_text.get(), e3_text.get())
                    else:
                        sql_query = "SELECT * FROM Songs WHERE (song_name = '{}' AND genre = '{}')".format(e2_text.get(), e3_text.get())
                else:
                    # 2
                    sql_query = "SELECT * FROM Songs WHERE song_name = '{}'".format(e2_text.get())
            else:
                if e3_text.get() != "":
                    # 3
                    sql_query = "SELECT * FROM Songs WHERE genre = '{}'".format(e3_text.get())
                else:
                    # none
                    bottom_text.set("Cannot execute search. No parameters listed.")
                    return

    print(sql_query)
    cursor.execute(sql_query)
    
    if table.get() in three_attr_tables:
        for (att1, att2, att3) in cursor:
            list1.append(att1)
            list2.append(att2)
            list3.append(att3)
    else:
        for (att1, att2) in cursor:
            list1.append(att1)
            list2.append(att2)
        
    list1var.set(list1)
    list2var.set(list2)
    list3var.set(list3)
    bottom_text.set("Search successful.")

# ADVANCED QUERY NUMBER 1: select all artists with a higher than average number of songs
def advanced_one(*args):
    list1 = []
    list2 = []
    sql_query = "SELECT artist_name, COUNT(song_id) AS song_count FROM Artists NATURAL JOIN WritesSong GROUP BY artist_name HAVING COUNT(song_id) > (SELECT AVG(song_count) FROM (SELECT artist_name, COUNT(song_id) AS song_count FROM Artists NATURAL JOIN WritesSong GROUP BY artist_name) AS SongCountByArtist);"
    cursor.execute(sql_query)
    for (artist_name, song_count) in cursor:
        list1.append(artist_name)
        list2.append(song_count)
    list1var.set(list1)
    list2var.set(list2)
    attr1.set("artist_name")
    attr2.set("song_count")
    attr3.set("")
    lb3.grid_forget()

# ADVANCED QUERY NUMBER 2: select all albums with a lower than average number of songs
def advanced_two(*args):
    list1 = []
    list2 = []
    sql_query = "SELECT album_name, COUNT(song_id) AS song_count FROM Albums NATURAL JOIN BelongsToAlbum GROUP BY album_name HAVING COUNT(song_id) < (SELECT AVG(song_count) FROM (SELECT album_name, COUNT(song_id) AS song_count FROM Albums NATURAL JOIN BelongsToAlbum GROUP BY album_name) AS SongCountByAlbum);"
    cursor.execute(sql_query)
    for (album_name, song_count) in cursor:
        list1.append(album_name)
        list2.append(song_count)
    list1var.set(list1)
    list2var.set(list2)
    attr1.set("album_name")
    attr2.set("song_count")
    attr3.set("")
    lb3.grid_forget()


#####
# SET UP GUI
#####


# setting up the GUI window
window = Tk()
window.title("Electronic Music Database")
mainframe = ttk.Frame(window, padding='3 3 3 3')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
button_frame = ttk.Frame(mainframe, padding='10 10 10 10')
button_frame.grid(column=1, row=1, sticky=(N))
select_frame = ttk.Frame(mainframe, padding='10 10 10 10')
select_frame.grid(column=1, row=2)
input_frame = ttk.Frame(mainframe, padding='10 10 10 10')
input_frame.grid(column=1, row=3)
confirm_frame = ttk.Frame(mainframe, padding='10 10 10 10')
confirm_frame.grid(column=1, row=4)
output_frame = ttk.Frame(mainframe, padding='10 10 10 10', borderwidth=4, relief="ridge")
output_frame.grid(column=1, row=5)
bottom_frame = ttk.Frame(mainframe, padding='5 5 5 5')
bottom_frame.grid(column=1, row=6)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)


# this variable describes the table currently being edited
table = StringVar()
table.set("Artists")

# this variable describes how we edit the table: add, remove, update, list, or search
mode = StringVar()
mode.set("Insert Into")

# adding buttons to button_frame, to select which table to edit
ttk.Button(button_frame, text="Artists", command=set_artists).grid(column=1, row=1, sticky=(NW))
ttk.Button(button_frame, text="Albums", command=set_albums).grid(column=2, row=1, sticky=(N))
ttk.Button(button_frame, text="Songs", command=set_songs).grid(column=3, row=1, sticky=(NE))
ttk.Button(button_frame, text="Artist -> Album", command=set_artist_album).grid(column=1, row=2, sticky=(W))
ttk.Button(button_frame, text="Album -> Song", command=set_album_song).grid(column=2, row=2)
ttk.Button(button_frame, text="Song -> Artist", command=set_song_artist).grid(column=3, row=2, sticky=(N, E))

# adding labels and input boxes to input_frame

input_l1 = StringVar()
input_l1.set("Artist Name")
input_l2 = StringVar()
input_l2.set("Test")
input_l3 = StringVar()
input_l3.set("Test")
i_lab1 = ttk.Label(input_frame, textvariable=input_l1)
i_lab1.grid(column=1, row=1, sticky=(NE))
i_lab2 = ttk.Label(input_frame, textvariable=input_l2)
i_lab2.grid(column=1, row=2, sticky=(E))
i_lab3 = ttk.Label(input_frame, textvariable=input_l3)

e1_text = StringVar()
e2_text = StringVar()
e3_text = StringVar()
i_ent1 = ttk.Entry(input_frame, textvariable=e1_text, width=20)
i_ent1.grid(column=2, row=1, sticky=(NE))
i_ent2 = ttk.Entry(input_frame, textvariable=e2_text, width=20)
i_ent2.grid(column=2, row=2, sticky=(E))
i_ent3 = ttk.Entry(input_frame, textvariable=e3_text, width=20)

search_mode = IntVar()
search_mode.set(0)
searchbutt1 = ttk.Radiobutton(input_frame, text="Search for any of these conditions", variable=search_mode, value=0)
searchbutt2 = ttk.Radiobutton(input_frame, text="Search for all of these conditions", variable=search_mode, value=1)


# adding radio buttons to select_frame, to specify what we're doing to the table
ttk.Radiobutton(select_frame, text="Insert", variable=mode, value="Insert Into", command=select_mode).grid(column=1, row=1)
ttk.Radiobutton(select_frame, text="Delete", variable=mode, value="Delete From", command=select_mode).grid(column=1, row=2)
ttk.Radiobutton(select_frame, text="Update", variable=mode, value="Update", command=select_mode).grid(column=1, row=3)
ttk.Radiobutton(select_frame, text="List", variable=mode, value="List", command=select_mode).grid(column=1, row=4)
ttk.Radiobutton(select_frame, text="Search", variable=mode, value="Search", command=select_mode).grid(column=1, row=5)

# adding buttons to confirm_frame
confirm_text = StringVar()
update_confirm_text()
ttk.Button(confirm_frame, textvariable=confirm_text, command=make_query).grid(column=1, row=1)
ttk.Button(confirm_frame, text="List Artists With Many Songs", command=advanced_one).grid(column=1, row=2)
ttk.Button(confirm_frame, text="List Albums With Few Songs", command=advanced_two).grid(column=2, row=2)

# adding labels and output display listboxes to output_frame
list1var = StringVar()
list2var = StringVar()
list3var = StringVar()

attr1 = StringVar()
attr1.set("artist_id")
attr2 = StringVar()
attr2.set("artist_name")
attr3 = StringVar()

ttk.Label(output_frame, textvariable=attr1).grid(column=1, row=1)
ttk.Label(output_frame, textvariable=attr2).grid(column=2, row=1)
ttk.Label(output_frame, textvariable=attr3).grid(column=3, row=1)
lb1 = Listbox(output_frame, listvariable=list1var, height=15)
lb1.grid(column=1, row=2)
lb2 = Listbox(output_frame, listvariable=list2var, height=15)
lb2.grid(column=2, row=2)
lb3 = Listbox(output_frame, listvariable=list3var, height=15)

# adding some text at the bottom to communicate state
bottom_text = StringVar()
ttk.Label(bottom_frame, textvariable=bottom_text).grid(column=1, row=1)

# the default "state" of the program is Insert Into Artists
select_insert()

# run the GUI
window.mainloop()

#once the GUI is closed, close the cursor and the MySQL connection
cursor.close()
cnx.close()