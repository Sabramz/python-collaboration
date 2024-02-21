
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