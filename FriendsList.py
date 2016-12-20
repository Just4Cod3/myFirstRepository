import sqlite3 #polączenie z DB
import random #pozwala używać generatora liczb pseudolosowych
import time #pozwala użyć time.sleep()
import os #czyści konsole?
import sys

conn = sqlite3.connect("FriendsList.db")
c = conn.cursor()
id = 0
play = True

def create_table():
     c.execute("CREATE TABLE IF NOT EXISTS friendList(id INTEGER primary key autoincrement, name TEXT, last_name TEXT)")
     
def load_id_from_DB():
     pass
     #????????????????
     
def dynamic_data_entry():
     global id
     id = id + 1
     name = input("Enter your name: ")
     last_name = input("Enter your last name: ")
     c.execute("INSERT INTO friendList (id, name, last_name) VALUES (?, ?, ?)",
     (id, name, last_name))
     conn.commit()

def show_only_specific_last_name(): #write last_name = search only that persons
     last_name = input("Search by last name: ")
     c.execute("SELECT * FROM friendList WHERE last_name==(last_name)")
     for row in c.fetchall():
          print(row)
     
     
def show_full_list():
     c.execute("SELECT * FROM  friendList")
     for row in c.fetchall():
          print(row)
          
create_table()
while(play == True):
     print("-----------------")
     print("1.Add new friend")
     print("2.Show List")
     print("3.Search by last name")
     print("0.Exit")
     print("-----------------")
     choice = int(input("Choice: "))

     if choice == 1:
          dynamic_data_entry()
          print("Adding new friend!")
          time.sleep(1)
     elif choice == 2:
          show_full_list()
          time.sleep(1)
     elif choice == 3:
          show_only_specific_last_name()
          time.sleep(1)
     elif choice == 0:
          play = False
     else:
          print("Wrong choice!")
          time.sleep(2)
