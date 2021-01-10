from classes import *


class MainPage(mtk.Tk):

    def __init__(self, *args, **kwargs):
        mtk.Tk.__init__(self, *args, **kwargs)

        self.title(" ")
        self.geometry("500x500")

        container = mtk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        all_frames = (startPage, loginPage, votePage, resultsPage)

        for F in all_frames:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("votePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
