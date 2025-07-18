task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority level"

if time_bound == "yes" and priority in ["high", "medium"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["high", "medium"]:
    message += " that can be completed later."
elif time_bound == "yes" and priority == "low":
    message += " that is time-sensitive."
else:
    message += ". Consider completing it when you have free time."

print(message)

