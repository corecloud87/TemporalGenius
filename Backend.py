from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {'id': 1, 'name': 'Email', 'duration': 30},
    {'id': 2, 'name': 'Meeting', 'duration': 60},
    {'id': 3, 'name': 'Coding', 'duration': 120},
]

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)
