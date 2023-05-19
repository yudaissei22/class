#todo list manager

#add a new to do item
#see all todo items
#check a todo items
#新規登録でき、一覧でき、削除もできる。

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Create a list to store the tasks
data = []

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Define the route to handle task submission
@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect('/')

# Define the route to handle task deletion
@app.route('/delete_task', methods=['POST'])
def delete_task():
    task = request.form['task']
    tasks.remove(task)
    return redirect('/')

if __name__ == '__main__':

app.run(port=8080, debug=True)
