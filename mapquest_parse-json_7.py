import tkinter.ttk as ttk
import tkinter
import tkinter.messagebox
from tkinter import *
import urllib.parse
import requests
app = tkinter.Tk()
app.geometry("450x400")
app.title("MapQuest API")

main_api = "https://www.mapquestapi.com/directions/v2/route?"

key = "sBTGRt94bHSZB37vjW7bKvZFLSGaVHSd"


def button_function():
    print("button pressed")

def getResult():
    while True:

        orig = locvalue.get()

        dest = destvalue.get()

        metric = metvalue.get()

        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

        json_data = requests.get(url).json()

        print("URL: " + (url))

        json_data = requests.get(url).json()

        json_status = json_data["info"]["statuscode"]

        if json_status == 0:

            print("API Status: " + str(json_status) + " = A successful route call.\n")

            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))

            print("Trip Duration:   " + (json_data["route"]["formattedTime"]))

            if metric == "Kilometer":

                print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))

            elif metric == "Meter":

                print("Meters:      " + str("{:.2f}".format((json_data["route"]["distance"])*10.61)))

            elif metric == "Millimeter":

                print("Millimeters:      " + str("{:.2f}".format((json_data["route"]["distance"])*10000.61)))

            print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

            print("=============================================")

            for each in json_data["route"]["legs"][0]["maneuvers"]:

                if metric == "Kilometer":

                    print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

                elif metric == "Meter":

                    print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " m)"))

                elif metric == "Millimeter":

                    print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " mm)"))
            print("=============================================\n")

        elif json_status == 402:

            print("**********************************************")

            print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

            print("**********************************************\n")

        elif json_status == 611:

            print("**********************************************")

            print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        break

def Close():
    print("**********************Thank You for Using MapQuest************************\n")
    app.destroy()

s = ttk.Style()
s.configure("TRadiobutton", fg="red")

app.configure(bg='Navy')

y_padding = 6

frame = tkinter.Frame(master=app, width=300, height=290, bg="Teal")
frame.pack(padx=60, pady=20, fill="both", expand=True)

label_map = tkinter.Label(frame, text="MapQuest API", bg="Teal", font=("Roboto Medium", -30), fg= "white")
label_map.pack(pady=y_padding, padx=10)

loc = Label(frame, text="Starting Location")
dest = Label(frame, text="Destination")
met = Label(frame, text="Metric")

locvalue = StringVar()
destvalue = StringVar()
metvalue = StringVar()

#Entries for our form
locentry = Entry(frame, textvariable=locvalue)
destentry = Entry(frame, textvariable=destvalue)
metentry = Entry(frame, textvariable=metvalue)

# Tkinter variable for storing entries
locvalue = StringVar()
destvalue = StringVar()
metvalue = StringVar()

#Label & Entries for our form
label_loc = tkinter.Label(frame, text="Starting Location:", bg="Teal", font="comicsansms 9 bold")
label_loc.pack(pady=y_padding, padx=10)

entry_loc = tkinter.Entry(frame, textvariable=locvalue, highlightbackground="lightgray", width=25)
entry_loc.pack(pady=y_padding, padx=10)

label_dest = tkinter.Label(frame, text="Destination:", bg="Teal", font="comicsansms 9 bold")
label_dest.pack(pady=y_padding, padx=10)

entry_dest = tkinter.Entry(frame, textvariable=destvalue, highlightbackground="lightgray", width=25)
entry_dest.pack(pady=y_padding, padx=10)

label_met = tkinter.Label(frame, text="Metric: (Kilometer/Meter/Millimeter)", bg="Teal", font="comicsansms 9 bold")
label_met.pack(pady=y_padding, padx=10)

entry_met = tkinter.Entry(frame, textvariable=metvalue, highlightbackground="lightgray", width=25)
entry_met.pack(pady=y_padding, padx=10)

button_res = tkinter.Button(frame, command=getResult, text="Result", highlightbackground="lightgray", width=8, bg= "Grey", fg= "White")
button_res.pack(pady=y_padding, padx=15)

button_ex = tkinter.Button(frame, command=Close, text="Exit", highlightbackground="red", width=8, bg= "Black", fg= "White")
button_ex.pack(pady=y_padding, padx=15)

label_out = tkinter.Label(frame, text="+Check result in terminal after clicking result button+", bg="Teal", font="comicsansms 8 italic")
label_out.pack(pady=y_padding, padx=10)

app.mainloop()