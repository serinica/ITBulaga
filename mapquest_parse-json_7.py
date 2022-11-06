import tkinter
import tkinter.messagebox
from tkinter import *
import urllib.parse
import requests
app = tkinter.Tk()
app.geometry("600x400")
app.title("MapQuest API")

main_api = "https://www.mapquestapi.com/directions/v2/route?"
#MY API KEY
key = "oASyGZH5MQmlsOhOhOwI2xo6yvP2wSq3"

#function to compute & display the result
def getResult():
    while True:

        orig = locvalue.get()

        dest = destvalue.get()

        metric = metvalue.get()

        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

        json_data = requests.get(url).json()

        print("\033[0;34;47m==================================================================================\033[0m")
        print("\033[1;31;40mURL: " + (url) + "\033[0m")
        json_data = requests.get(url).json()

        json_status = json_data["info"]["statuscode"]

        if json_status == 0:

            print("\033[1;31;40mAPI Status: " + str(json_status) + " = A successful route call \033[0m.\n")

            print("\033[0;34;47m==================================================================================\033[0m")
            print("\033[2;36;40mDirections from " + (orig) + " to " + (dest))

            print("Trip Duration:   " + (json_data["route"]["formattedTime"]))

            #condition for the metric system
            if metric == "Kilometer":

                print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
                

            elif metric == "Meter":

                print("Meters:      " + str("{:.2f}".format((json_data["route"]["distance"])*1000.61)))

            elif metric == "Hectometer":

                print("Hectometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*10.61)))

            elif metric == "Decameter":

                print("Decameters:      " + str("{:.2f}".format((json_data["route"]["distance"])*100.61)))

            elif metric == "Decimeter":

                print("Decimeters:      " + str("{:.2f}".format((json_data["route"]["distance"])*10000.61)))

            elif metric == "Centimeter":

                print("Centimeters:      " + str("{:.2f}".format((json_data["route"]["distance"])*100000.61)))

            elif metric == "Millimeter":

                print("Millimeters:      " + str("{:.2f}".format((json_data["route"]["distance"])*1000000.61)))


            #print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))+ "\033[0m")

            print("\033[0;34;47m==================================================================================\033[0m")

            for each in json_data["route"]["legs"][0]["maneuvers"]:

                if metric == "Kilometer":

                    print((each["narrative"]) + "\n \033[2;36;40mComputed Distance: (" + str("{:.2f}".format((each["distance"])*1.61) + " km)\033[0m"))
                   

                elif metric == "Meter":

                    print((each["narrative"]) + "\n Computed Distance: (" + str("{:.2f}".format((each["distance"])*1000.61) + " m)"))
                    

                elif metric == "Hectometer":

                    print((each["narrative"]) + "\n Computed Distance: (" + str("{:.2f}".format((each["distance"])*10.61) + " hm)"))
                    

                elif metric == "Decameter":

                    print((each["narrative"]) + "\n Computed Distance: (" + str("{:.2f}".format((each["distance"])*100.61) + " dam)"))
                    
                
                elif metric == "Decimeter":

                    print((each["narrative"]) + "\n Computed Distance: (" + str("{:.2f}".format((each["distance"])*10000.61) + " dm)"))
                    

                elif metric == "Centimeter":

                    print((each["narrative"]) + "\n Computed Distance: (" + str("{:.2f}".format((each["distance"])*100000.61) + " cm)"))
                    

                elif metric == "Millimeter":

                    print((each["narrative"]) + "\n Computed Distance: (" + str("{:.2f}".format((each["distance"])*1000000.61) + " mm)"))
                    
            print("\033[0;34;47m==================================================================================\033[0m")

        elif json_status == 402:

            print("\033[0;31;47m**********************************************\033[0m")

            print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")

            print("\033[0;31;47m**********************************************\033[0m")

        elif json_status == 611:

            print("\033[0;31;47m**********************************************\033[0m")

            print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        break

def Close():
    print("\033[1;31;40m**********************Thank You for Using MapQuest************************\033[0m\n")
    app.destroy()

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

label_met = tkinter.Label(frame, text="Metric: \n(Kilometer/Meter/Hectometer/Decameter/Decimeter/Centimeter/Millimeter)", bg="Teal", font="comicsansms 9 bold")
label_met.pack(pady=y_padding, padx=10)

entry_met = tkinter.Entry(frame, textvariable=metvalue, highlightbackground="lightgray", width=25)
entry_met.pack(pady=y_padding, padx=10)

button_res = tkinter.Button(frame, command=getResult, text="Result", highlightbackground="lightgray", width=8, bg= "Grey", fg= "White")
button_res.pack(pady=y_padding, padx=15)



#label_out = tkinter.Label(frame, text="+Check result in terminal after clicking result button+", bg="Teal", font="comicsansms 8 italic")
#label_out.pack(pady=y_padding, padx=10)

#try lang
def myfunction():
    emptylabel.config(text="Result: " + getResult.get())

emptylabel = Label(app,fg='green',font=('Arial',14))
emptylabel.pack(pady=y_padding, padx=10)

button_ex = tkinter.Button(frame, command=Close, text="Exit", highlightbackground="red", width=8, bg= "Black", fg= "White")
button_ex.pack(pady=y_padding, padx=15)

app.mainloop()
