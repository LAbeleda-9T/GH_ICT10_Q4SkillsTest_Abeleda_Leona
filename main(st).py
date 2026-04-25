#ATTENDANCE TRACKER
from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

# Store data (default = 0 absences)
attendance = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0
}

def add_data(e):
    day = document.getElementById("day").value
    value = document.getElementById("absences").value

    if value == "":
        value = 0

    attendance[day] = int(value)

    document.getElementById("output").innerHTML = f"Added: {day} = {value} absences"

def show_graph(e):
    document.getElementById("output").innerHTML = ""

    days = np.array(list(attendance.keys()))
    absences = np.array(list(attendance.values()))

    plt.figure()
    plt.bar(days, absences)

    plt.title("Weekly Absences")
    plt.xlabel("Days")
    plt.ylabel("Number of Absences")

    display(plt.gcf(), target="output")