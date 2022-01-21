#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector


class User():
    isRunning = False
    mySource = ''

    def __init__(self):
        return


surnames = []
chatid = {}
names = {}
categories = []
# conn = sqlite3.connect(r"Users.db")
conn = mysql.connector.connect(user='user_name', password='password', host='host', database='db_name')
cursor = conn.cursor()
mysql_select_query = "SELECT * from Users"
cursor.execute(mysql_select_query)
records = cursor.fetchall()
mysql_chats = "SELECT * from chatids"
cursor.execute(mysql_chats)
chats = cursor.fetchall()
mysql_names = "SELECT Name, Surname from Users, chatids WHERE Surname = Surnames"
cursor.execute(mysql_names)
name = cursor.fetchall()
mysql_categories = "SELECT * from Categories"
cursor.execute(mysql_categories)
category = cursor.fetchall()

for row in records:
    surnames.append(row[7])

for row in chats:
    if row[0] is not None:
        chatid[row[0]] = row[1]

for row in name:
    names[row[1]] = row[0]

for row in category:
    categories.append(row[1])


# Отправка копии на почту
def send_email(problem):
    import requests

    url = "api_url"

    headers = {
        "Content-Type": "application/json",
        'Authorization': "token"  
        }

    json = {
        "recipients": "email",
        "subject": "Проблема: " + problem[1] + "(" + problem[0] + ")",
        "body": problem[2],

    }

    response = requests.post(url, headers=headers, json=json)


# Вставка обращения в базу данных
def insert_in_db(problem):
    conn1 = mysql.connector.connect(user='user_name', password='password', host='host', database='db_name')
    cursor1 = conn1.cursor()
    cursor1.execute("INSERT INTO Requests (Surname, Category, Description) VALUES (%s,%s,%s)", problem)
    conn1.commit()

# Вставка chat_id в базу данных
def add_id(chatids):
    conn1 = mysql.connector.connect(user='user_name', password='password', host='host', database='db_name')
    cursor1 = conn1.cursor()
    cursor1.execute("INSERT INTO chatids (chatid, Surnames) VALUES (%s,%s)", chatids)
    conn1.commit()

