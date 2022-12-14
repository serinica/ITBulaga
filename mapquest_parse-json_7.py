from logging import root
import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
from tkinter.tix import COLUMN, ButtonBox
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
    outputResult = ""
    while True:

        orig = locvalue.get()

        dest = destvalue.get()

        metric = metvalue.get()

        url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

        json_data = requests.get(url).json()


        
        #outputResult += "\033[0;34;47m==================================================================================\033[0m"
        
        print("\nURL: " + (url))
        json_data = requests.get(url).json()

        json_status = json_data["info"]["statuscode"]

       
        if json_status == 0:

            print("\nAPI Status: " + str(json_status) + " = A successful route call \n")
            
            #outputResult += "\033[0;34;47m==================================================================================\033[0m"
            
            outputResult += "\nDirections from " + (orig) + " to " + (dest)
            
            outputResult += "\nTrip Duration:   " + (json_data["route"]["formattedTime"] + "\n")
            #condition for the metric system
            if metric == "Kilometer":

                outputResult += "\nKilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)) + "\n"

            elif metric == "Meter":

                
                outputResult += "\nMeters:      " + str("{:.2f}".format((json_data["route"]["distance"])*1000.61)) + "\n"


            elif metric == "Hectometer":

                
                outputResult += "\nHectometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*10.61)) + "\n"


            elif metric == "Decameter":

                
                outputResult += "\nDecameters:      " + str("{:.2f}".format((json_data["route"]["distance"])*100.61)) + "\n"

            elif metric == "Decimeter":

                
                outputResult += "\nDecimeters:      " + str("{:.2f}".format((json_data["route"]["distance"])*10000.61)) + "\n"

            elif metric == "Centimeter":

                
                outputResult += "\nCentimeters:      " + str("{:.2f}".format((json_data["route"]["distance"])*100000.61)) + "\n"

            elif metric == "Millimeter":

                
                outputResult += "\nMillimeters:      " + str("{:.2f}".format((json_data["route"]["distance"])*1000000.61))  + "\n"

            

            
            #outputResult += "\033[0;34;47m==================================================================================\033[0m"

            for each in json_data["route"]["legs"][0]["maneuvers"]:

                if metric == "Kilometer":

                    
                    outputResult += (each["narrative"]) + "\n Distance: (" + str("{:.2f}".format((each["distance"])*1.61) + " km)" + "\n")

                elif metric == "Meter":

                    
                    outputResult += (each["narrative"]) + "\n Distance: (" + str("{:.2f}".format((each["distance"])*1000.61) + " m)" + "\n")

                elif metric == "Hectometer":

                    
                    outputResult += (each["narrative"]) + "\n Distance: (" + str("{:.2f}".format((each["distance"])*10.61) + " hm)" + "\n")

                elif metric == "Decameter":

                    
                    outputResult += (each["narrative"]) + "\n Distance: (" + str("{:.2f}".format((each["distance"])*100.61) + " dam)" + "\n")

                
                elif metric == "Decimeter":

                
                    outputResult += (each["narrative"]) + "\n Distance: (" + str("{:.2f}".format((each["distance"])*10000.61) + " dm)" + "\n")

                elif metric == "Centimeter":

                    
                    outputResult += (each["narrative"]) + "\n Distance: (" + str("{:.2f}".format((each["distance"])*100000.61) + " cm)" + "\n")


                elif metric == "Millimeter":

                    
                    outputResult += (each["narrative"]) + "\n Distance: (" + str("{:.2f}".format((each["distance"])*1000000.61) + " mm)" + "\n")

            
            outputResult += (each["narrative"]) + "\n Distance: (" + str("{:.2f}".format((each["distance"])*1000000.61) + " mm)" + "\n")
            return outputResult
        elif json_status == 402:

            
            #outputResult += "\033[0;31;47m**********************************************\033[0m"
            
            outputResult += "Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations."
            
            #outputResult += "\033[0;31;47m**********************************************\033[0m"
            return outputResult
        elif json_status == 611:

            
            #outputResult += "\033[0;31;47m**********************************************\033[0m"

            
            outputResult += "Status Code: " + str(json_status) + "; Missing an entry for one or both locations."
            return outputResult
        break
    return outputResult

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


def onClick():
    global box
    box = Toplevel(app)
    box.title("Result")
    box.geometry("700x900")
    box.config(bg="white")

    boxes = Label(box, text=getResult(), bg="grey", font=("Roboto Medium", 12), fg= "black")
    boxes.pack(padx=10)
 

    Button(box,command=Close, text="Ok", highlightbackground="red", width=8, bg= "Black", fg= "White").pack(pady=y_padding, padx=15)

Button(app,command=onClick, text="Result", highlightbackground="lightgray", width=8, bg= "Grey", fg= "White").pack(pady=y_padding, padx=15)

Button(app,command=Close, text="Exit", highlightbackground="red", width=8, bg= "Black", fg= "White").pack(pady=y_padding, padx=15)

app.mainloop()