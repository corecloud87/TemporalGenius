import React, { useState, useEffect } from 'react';

const Schedule = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    // Fetch tasks from backend
    fetch('/api/tasks')
      .then(response => response.json())
      .then(data => setTasks(data));
  }, []);

  return (
    <div>
      <h1>Schedule</h1>
      <ul>
        {tasks.map(task => (
          <li key={task.id}>{task.name} - {task.duration} mins</li>
        ))}
      </ul>
    </div>
  );
};

export default Schedule;
