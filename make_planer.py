from datetime import datetime, timedelta

task_time_dict = {}
time_dict = {"spülen": 15,"staubsaugen":15,"Wäsche sortieren": 5}

time_input = input("Enter a time in HH:MM format: ")
activity = input("Was musst du machen? ")

def first_task(time_input,activity):
    minutes_input = time_dict[str(activity)]
    # Convert the time input to a datetime object
    time_object = datetime.strptime(time_input, "%H:%M")

    new_time_object = time_object + timedelta(minutes=int(minutes_input))
    # Convert the new time object to a string in HH:MM format
    #new_time_string = new_time_object.strftime("%H:%M")
    #return new_time_string
    return new_time_object

def second_task(new_time_object, activity):
    minutes_input = time_dict[str(activity)]

    # Convert the time input to a datetime object
    new_time_object = datetime.strptime(new_time_object, "%H:%M")


    # Add the minutes to the time using timedelta
    new_time_object = new_time_object + timedelta(minutes=int(minutes_input))

    # Convert the new time object to a string in HH:MM format
    #other_new_time_string = new_time_object.strftime("%H:%M")
    # other_new_time_string
    return new_time_object

def more_tasks(other_new_time_object, new_activity):
    minutes_input = time_dict[str(new_activity)]

    # Convert the time input to a datetime object
    other_new_time_object = datetime.strptime(str(other_new_time_object), "%H:%M")

    # Convert the minutes input to an integer
    minutes_object = int(minutes_input)

    # Add the minutes to the time using timedelta
    new_other_new_time_object = other_new_time_object + timedelta(minutes=minutes_object)

    # Convert the new time object to a string in HH:MM format
    #other_new_time_string = other_new_time_object.strftime("%H:%M")
    other_new_time_object = new_other_new_time_object
    return other_new_time_string
    return other_new_time_object


new_time_string = first_task(time_input,activity)
new_time_object = first_task(time_input,activity)

print(f"When du um {time_input} mit {activity} anfängst, bist du um {new_time_object.strftime('%H:%M')} fertig.")
danach = input("Musst du danach noch etwas machen? ")
x = 1
if danach == "Ja" and x == 1:
    new_activity = input("Was musst du machen? ")
    other_new_time_string = more_tasks(new_time_object, new_activity)
    x +=1
    print(f"Wenn du danach noch {new_activity} willst, bist du um {new_time_object.strftime('%H:%M')} fertig. ")
elif danach == "Ja" and x > 1:
    new_activity = input("Was musst du machen? ")
    other_new_time_string = more_tasks(new_time_object, new_activity)
    print(f"Wenn du danach noch {new_activity} willst, bist du um {other_new_time_string} fertig. ")
else:
    pass
