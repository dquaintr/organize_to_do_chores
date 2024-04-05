
from datetime import datetime, timedelta

time_dict = {"spülen": 15,"staubsaugen":15,"Wäsche sortieren": 5}

"""#def add_time_to_current(hours, minutes):
    # Get the current time
current_time = datetime.now()

    # Create a timedelta object for the specified hours and minutes
    time_delta = timedelta(hours = hours, minutes = minutes)

    # Add the timedelta to the current time
    new_time = current_time + time_delta
    return(new_time.strftime("%H:%M"))"""


#print(time_dict["Wäsche sortieren"])
# Ask the user to enter a time in HH:MM format
time_input = input("Enter a time in HH:MM format: ")
activity = input("Was musst du machen? ")
# Ask the user to enter an amount of minutes to add
def calculate_time(time_input,activity):
    minutes_input = time_dict[str(activity)]

    # Convert the time input to a datetime object
    time_object = datetime.strptime(time_input, "%H:%M")

    # Convert the minutes input to an integer
    minutes_object = int(minutes_input)

    # Add the minutes to the time using timedelta
    new_time_object = time_object + timedelta(minutes=minutes_object)

    # Convert the new time object to a string in HH:MM format
    new_time_string = new_time_object.strftime("%H:%M")

    pause = timedelta(minutes=5)
    #pause_string = pause.strftime("%H:%M")

    new_time_object_2 = new_time_object + pause + timedelta(minutes=minutes_object)
    new_time_string_2 = new_time_object_2.strftime("%H:%M")
    return new_time_string_2

new_time_string_2 = calculate_time(time_input,activity)
# Print the result
print(f"When du um {time_input} mit {activity} anfängst, bist du um {new_time_string_2} fertig.")


danach = input("Willst du danach noch etwas machen? ")
while True:
    if danach == "Ja":
        new_activity = input("Was musst du machen? ")
        calculate_time(new_time_string_2,new_activity)
        print(f"Wenn du danach noch {new_activity} machst, bist du um {new_time_string_2} fertig.")
        danach = input("Willst du danach noch etwas machen? ")
    else:
        break

