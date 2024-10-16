#PREDICT SCHEDULE

# Predict completion time for a new task
new_task = [[45, 2]]  # Example input: duration 45 mins, priority 2
predicted_time = model.predict(new_task)
print(f'Predicted Completion Time: {predicted_time[0]}')
