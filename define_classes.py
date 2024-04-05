import datetime
import pickle
with open('saved_dictionary.pkl', 'rb') as f:
    time_dict = pickle.load(f)

#time_dict = {"spülen": 15,"staubsaugen":15,"Wäsche sortieren": 5}

class Task:
    def __init__(self,start_time,name):
        self.start_time = start_time #datetime.strptime(start_time, "%H:%M")
        self.name = name
        self.duration = time_dict[str(name)] #timedelta(minutes=int(time_dict[str(name)]))
        self.end_time = self.start_time + self.duration

    def __str__(self):
        antwort = "Das Objekt ist eine Aufgabe."
        antwort += f"Es beginnt um {self.start_time}."
        antwort += f"Es heißt {self.name}."
        antwort += f"Es dauert {self.duration}."
        antwort += f"Es endet um {self.end_time}."
        return antwort

class Break(Task):
    def __init__(self):
        self.name = "Pause"
        self.duration = 5

class Tabel:

    def __init__(self, starttime):
        self.starttime = starttime

    def make_planer(self):
        pass
    """takes different end points and adds them to duration"""



erstes_spülen = Task(30,"fahren")
zweites_spülen = Task(erstes_spülen.end_time,"staubsaugen")
print(erstes_spülen)
print(zweites_spülen)
print(time_dict)



