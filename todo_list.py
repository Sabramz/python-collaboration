
# tasks are stored as a dict
tasks = {}
# a task is a str: boolean
# where str is the task name, and the boolean indicates the task's level of completeness

def add_task(name):
	tasks[name] = False

def delete_task(name):
	del tasks[name]

def view_tasks():
	for key, value in tasks.items():
		state = ""
		if value:
			state = "complete"
		else:
			state = "uncomplete"
		print("Task: " + key + ", " + state)

def mark_completed(name):
	tasks[name] = True

def save_to_file():
	out_file = open("./output.txt", "w")
	for key, value in tasks.items():
		state = ""
		if value:
			state = "complete"
		else:
			state = "uncomplete"
		out_file.write("Task: " + key + ", " + state + "\n")

def main():
	print("Welcome to the to-do list")
	while True:
		inp = input("Enter 1 to add a task, 2 to delete a task, 3 to view tasks, and 4 to mark a task as completed, \
5 to save tasks to a file e to exit: ")
		if inp == "1":
			inp = input("Enter the name of the task: ")
			add_task(inp)
		elif inp == "2":
			inp = input("Enter the name of the task: ")
			delete_task(inp)
		elif inp == "3":
			view_tasks()
		elif inp == "4":
			inp = input("Enter the name of the task: ")
			mark_completed(inp)
		elif inp == "5":
			save_to_file()
		elif inp == "e":
			print("Terminating...")
			return

main()