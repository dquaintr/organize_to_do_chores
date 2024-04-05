#From "C:\Users\ar-daniel.quaintrell\Documents\get_stuff_done\make_planer.py" import task_time_dict
import pickle
with open('saved_dictionary.pkl', 'rb') as f:
    task_time_dict = pickle.load(f)

if task_time_dict is True:
    task_time_dict = task_time_dict
else:
    task_time_dict = {}


#input_name = input("Please enter the name of the task: ")
#input_length = input("Please enter the amount of time (in whole minutes) the task will take: ")
def add_to_dictionry(name,length):
    #new_dict = task_time_dict
    key = str(name)
    value = int(length)
    task_time_dict[key] = value
    return task_time_dict

#print(add_to_dictionry("spülen",10))

while True:
    input_name = input("Please enter the name of the task: ")
    input_length = input("Please enter the amount of time (in whole minutes) the task will take: ")
    input_continue = input("Do you want to add a new task? ")
    if input_continue == "no":

        print(add_to_dictionry(input_name, input_length))
        with open('saved_dictionary.pkl', 'wb') as f:
            pickle.dump(task_time_dict, f)
        break
    add_to_dictionry(input_name,input_length)



