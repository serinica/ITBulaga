from tkinter import *
import urllib.parse
import requests

root = Tk()

main_api = "https://www.mapquestapi.com/directions/v2/route?"

key = "sBTGRt94bHSZB37vjW7bKvZFLSGaVHSd"

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

            elif metric == "MIllimeter":

                print("MIllimeters:      " + str("{:.2f}".format((json_data["route"]["distance"])*10000.61)))

            print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))

            print("=============================================")

            for each in json_data["route"]["legs"][0]["maneuvers"]:

                if metric == "Kilometer":

                    print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

                elif metric == "Meter":

                    print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " m)"))

                elif metric == "MIllimeter":

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
    root.destroy()


root.geometry("644x344")
#Heading
Label(root, text="MAPQUEST API", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
loc = Label(root, text="Starting Location")
dest = Label(root, text="Destination")
met = Label(root, text="Metric")

#Pack text for our form
loc.grid(row=1, column=2)
dest.grid(row=2, column=2)
met.grid(row=3, column=2)

# Tkinter variable for storing entries
locvalue = StringVar()
destvalue = StringVar()
metvalue = StringVar()

#Entries for our form
locentry = Entry(root, textvariable=locvalue)
destentry = Entry(root, textvariable=destvalue)
metentry = Entry(root, textvariable=metvalue)
# Packing the Entries
locentry.grid(row=1, column=3)
destentry.grid(row=2, column=3)
metentry.grid(row=3, column=3)

#Button & packing it and assigning it a command
Button(text="Submit", command=getResult).grid(row=7, column=3)

Button(root, text="Exit", command=Close).grid(row=8, column=3)

root.mainloop()