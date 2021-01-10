import sqlite3
import tkinter.messagebox as tm
from tkinter import *


def VoteButtonClicked(controller):
    controller.show_frame("loginPage")


def ChartButtonClicked(controller):
    controller.show_frame("resultsPage")


def LoginButtonClicked(self, controller):
    global login
    login = False

    db = sqlite3.connect("VoteDatabase.db")
    cursor = db.cursor()

    username_txt = getattr(self, "entry_username")
    username = username_txt.get()
    password_txt = getattr(self, "entry_password")
    password = password_txt.get()

    query = "SELECT * FROM account WHERE studentid = '{}' AND password = '{}' AND ID".format(username, password)

    cursor.execute(query)
    rows = cursor.fetchall()

    if len(rows) == 1:
        login = True
    if login:
        tm.showinfo("Login info", "Welcome")
        temp_file = open("temp.txt", "w")
        print(rows[0])
        temp_file.write(str(rows[0][0]))
        temp_file.close()
        controller.show_frame("votePage")
    else:
        tm.showerror("Login error", "Incorrect Username/Password")


def BackButtonClicked(controller):
    controller.show_frame("startPage")


def VoteEntry(self):
    pref1 = getattr(self, "entry_preference1")
    get_pref1 = pref1.get()
    print(get_pref1)

    pref2 = getattr(self, "entry_preference2")
    get_pref2 = pref2.get()
    print(get_pref2)

    pref3 = getattr(self, "entry_preference3")
    get_pref3 = pref3.get()
    print(get_pref3)

    pref4 = getattr(self, "entry_preference4")
    get_pref4 = pref4.get()
    print(get_pref4)

    temp_file = open("temp.txt", "r")
    account_id = temp_file.read()

    db = sqlite3.connect("VoteDatabase.db")
    cursor = db.cursor()

    query = "SELECT CandidateName FROM votes"
    cursor.execute(query)
    candidates = cursor.fetchall()

    for name in candidates:
        for position in name:
            if get_pref1 == position:
                cursor.execute("update votes set Preference1 = Preference1 + 1 where CandidateName = ?;",[position])
            elif get_pref2 == position:
                cursor.execute("update votes set Preference2 = Preference2 + 1 where CandidateName = ?;", [position])
            elif get_pref3 == position:
                cursor.execute("update votes set Preference3 = Preference3 + 1 where CandidateName = ?;", [position])
            elif get_pref4 == position:
                cursor.execute("update votes set Preference4 = Preference4 + 1 where CandidateName = ?;", [position])

    db.commit()


def GatherPref(self):
    db = sqlite3.connect("VoteDatabase.db")
    cursor = db.cursor()
    temp_file = open("temp2.txt", "r")
    gsu_type = temp_file.read()
    temp_file.close()

    if gsu_type == "President":
        list_president = "SELECT firstname, surname FROM account WHERE candidate_type = 'President'"
        cursor.execute(list_president)
        listA = cursor.fetchall()
        names = listA
        nodes = []
        for row in names:
            nodes.append(row)
        return nodes

    if gsu_type == "GSU Officer":
        list_gsu_officer = "SELECT firstname, surname FROM account WHERE candidate_type = 'GSU Officer'"
        cursor.execute(list_gsu_officer)
        listA = cursor.fetchall()
        names = listA
        nodes = []
        for row in names:
            nodes.append(row)
        return nodes

    if gsu_type == "Faculty Officer":
        list_faculty_officer = "SELECT firstname, surname FROM account WHERE candidate_type = 'Faculty Officer'"
        cursor.execute(list_faculty_officer)
        listA = cursor.fetchall()
        names = listA
        nodes = []
        for row in names:
            nodes.append(row)
        return nodes


def DisplayEndResult(self):
    get_gsu = getattr(self, "gsuSelected")
    gsu_type = get_gsu.get()

    db = sqlite3.connect("VoteDatabase.db")
    cursor = db.cursor()

    if gsu_type == "President":
        self.text.config(state=NORMAL)
        self.text.delete("1.0", END)
        get_president = "SELECT firstname, surname FROM account WHERE candidate_type = 'President'"
        cursor.execute(get_president)
        show_presidents = cursor.fetchall()
        for record in show_presidents:
            self.text.insert("0.3", "\n")
            self.text.insert("0.3", record)
        self.text.config(state=DISABLED)

        temp_file = open("temp2.txt", "w")
        temp_file.write("President")
        temp_file.close()

    if gsu_type == "GSU Officer":
        self.text.config(state=NORMAL)
        self.text.delete("1.0", END)
        get_gsu_officers = "SELECT firstname, surname FROM account WHERE candidate_type = 'GSU Officer'"
        cursor.execute(get_gsu_officers)
        show_gsu_officers = cursor.fetchall()
        for record in show_gsu_officers:
            self.text.insert("0.3", "\n")
            self.text.insert("0.3", record)
        self.text.config(state=DISABLED)

        temp_file = open("temp2.txt", "w")
        temp_file.write("GSU Officer")
        temp_file.close()

    if gsu_type == "Faculty Officer":
        self.text.config(state=NORMAL)
        self.text.delete("1.0", END)
        get_faculty_officers = "SELECT firstname, surname FROM account WHERE candidate_type = 'Faculty Officer'"
        cursor.execute(get_faculty_officers)
        show_faculty_officers = cursor.fetchall()
        for record in show_faculty_officers:
            self.text.insert("0.3", "\n")
            self.text.insert("0.3", record)
        self.text.config(state=DISABLED)

        temp_file = open("temp2.txt", "w")
        temp_file.write("Faculty Officer")
        temp_file.close()

def searchResults(self):
    db = sqlite3.connect("VoteDatabase.db")
    cursor = db.cursor()
    get_gsu = getattr(self, "gsuSelected")
    gsu_type = get_gsu.get()

    self.text.config(state=NORMAL)
    self.text.delete("1.0", END)

    if gsu_type == "President":
        list_president = "SELECT CandidateName, Preference1, Preference2, Preference3, Preference4 " \
                         "FROM votes WHERE GSUType = 'President' ORDER BY Preference1 ASC, Preference2 ASC;"
        cursor.execute(list_president)
        list_x = cursor.fetchall()
        for record in list_x:
            self.text.insert("0.3", "\n")
            self.text.insert("0.3", record)
        self.text.config(state=DISABLED)

    if gsu_type == "GSU Officer":
        list_gsu_officer = "SELECT CandidateName, Preference1, Preference2, Preference3, Preference4 " \
                         "FROM votes WHERE GSUType = 'GSU Officer' ORDER BY Preference1 ASC, Preference2 ASC;"
        cursor.execute(list_gsu_officer)
        list_x = cursor.fetchall()
        for record in list_x:
            self.text.insert("0.3", "\n")
            self.text.insert("0.3", record)
        self.text.config(state=DISABLED)

    if gsu_type == "Faculty Officer":
        list_faculty_officer = "SELECT CandidateName, Preference1, Preference2, Preference3, Preference4 " \
                         "FROM votes WHERE GSUType = 'Faculty Officer' ORDER BY Preference1 ASC, Preference2 ASC;"
        cursor.execute(list_faculty_officer)
        list_x = cursor.fetchall()
        for record in list_x:
            self.text.insert("0.3", "\n")
            self.text.insert("0.3", record)
        self.text.config(state=DISABLED)