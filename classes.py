import tkinter as mtk
from functions import *


class startPage(mtk.Frame):
    def __init__(self, parent, controller):
        mtk.Frame.__init__(self, parent)
        self.controller = controller

        self.Header = Label(self, text="Voting System", width=20, font=("bold", 20))
        self.Header.place(x=80, y=53)

        self.vote = Button(self, text="Vote", width=20,
                           command=lambda: VoteButtonClicked(controller)).place(x=170, y=300)

        self.charts = Button(self, text="Results", width=20,
                             command=lambda: ChartButtonClicked(controller)).place(x=170, y=340)

        self.img = mtk.PhotoImage(file="image.png")
        self.myPic = Label(self, image=self.img)
        self.myPic.place(x=120, y=100)


class loginPage(mtk.Frame):
    def __init__(self, parent, controller):
        mtk.Frame.__init__(self, parent)
        self.controller = controller

        global login
        login = False

        self.Header = Label(self, text="Login Screen", width=20, font=("bold", 20))
        self.Header.place(x=90, y=53)

        self.label_username = Label(self, text="Username:", width=20, font=("bold", 10))
        self.label_username.place(x=80, y=130)

        self.label_password = Label(self, text="Password:", width=20, font=("bold", 10))
        self.label_password.place(x=80, y=160)

        self.entry_username = Entry(self)
        self.entry_username.place(x=240, y=130)

        self.entry_password = Entry(self, show="*")
        self.entry_password.place(x=240, y=160)

        self.login_btn = Button(self, text="Login", width=20,
                                command=lambda: LoginButtonClicked(self, controller))
        self.login_btn.place(x=90, y=300)

        self.back_btn = Button(self, text="Go back", width=20,
                               command=lambda: BackButtonClicked(controller))
        self.back_btn.place(x=250, y=300)


class resultsPage(mtk.Frame):
    def __init__(self, parent, controller):
        mtk.Frame.__init__(self, parent)
        self.controller = controller

        self.Header = Label(self, text="Voting Charts", width=20, font=("bold", 20))
        self.Header.place(x=80, y=53)

        self.goBack = mtk.Button(self, text="Go Back",
                                 command=lambda: controller.show_frame("startPage"))
        self.goBack.place(x=440, y=20)

        self.text = mtk.Text(self, width=40, heigh=20)
        self.text.place(x=150, y=120)

        list0 = ["President", "GSU Officer", "Faculty Officer"]
        self.gsuSelected = mtk.StringVar()
        self.droplist0 = OptionMenu(self, self.gsuSelected, *list0)
        self.droplist0.config(width=15)
        self.gsuSelected.set("Select")
        self.droplist0.place(x=10, y=20)

        self.searchButton = Button(self, text="Search", width=15,
                                   command=lambda: searchResults(self))
        self.searchButton.place(x=10, y=80)

        db = sqlite3.connect("VoteDatabase.db")
        cursor = db.cursor()
        # logan hackathon 001077626-5
        hackathon_qurey = "SELECT SUM(Preference1 + Preference2 + Preference3 + Preference4) FROM votes"
        cursor.execute(hackathon_qurey)
        total_amount = cursor.fetchall()
        print(total_amount)

#hackathon thanhsan 001067823-9
        charts = "SELECT * FROM votes ORDER BY Preference1 ASC, Preference2 ASC;"
        cursor.execute(charts)
#hackathon this is saying it will sort everything acording to the preference 1 and then preference 2
        records = cursor.fetchall()
        for record in records:
            self.text.insert("0.1", "\n")
            self.text.insert("0.1", record)

        self.text.delete("1.0", END)


class votePage(mtk.Frame):
    def __init__(self, parent, controller):
        mtk.Frame.__init__(self, parent)
        self.controller = controller

        self.search = Button(self, text="Search", width=20,
                             command=lambda: [DisplayEndResult(self), GatherPref(self)]).place(x=250, y=22)

        self.vote = Button(self, text="Vote", width=20,
                           command=lambda: VoteEntry(self)).place(x=250, y=280)

        self.user = Label(self, text="Voting poll")
        self.user.place(x=430, y=0)

        self.signout = Button(self, text="Sign Out",
                              command=lambda: controller.show_frame("startPage"))
        self.signout.place(x=440, y=20)

        self.label_gsu = Label(self, text="GSU:", width=20, font=("bold", 11))
        self.label_gsu.place(x=0, y=24)

        list0 = ["President", "GSU Officer", "Faculty Officer"]
        self.gsuSelected = mtk.StringVar()
        self.droplist0 = OptionMenu(self, self.gsuSelected, *list0)
        self.droplist0.config(width=15)
        self.gsuSelected.set("Select")
        self.droplist0.place(x=110, y=20)

        self.label1 = Label(self, text="Preference 1").place(x=250, y=100)
        self.entry_preference1 = Entry(self)
        self.entry_preference1.place(x=250, y=120)

        self.label1 = Label(self, text="Preference 2").place(x=250, y=140)
        self.entry_preference2 = Entry(self)
        self.entry_preference2.place(x=250, y=160)

        self.label1 = Label(self, text="Preference 3").place(x=250, y=180)
        self.entry_preference3 = Entry(self)
        self.entry_preference3.place(x=250, y=200)

        self.label1 = Label(self, text="Preference 4").place(x=250, y=220)
        self.entry_preference4 = Entry(self)
        self.entry_preference4.place(x=250, y=240)

        self.text = mtk.Text(self, width=25, heigh=20)
        self.text.place(x=20, y=120)
        self.text.config(relief="sunken")

