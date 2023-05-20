#todo list manager

#add a new to do item
#see all todo items
#check a todo items
#新規登録でき、一覧でき、削除もできる。


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = []

@app.route('/')
def index():
        return render_template('index.html', todos=todos)

@app.route('/todos')
def todo_list():
        return render_template('todos.html', todos=todos)
    

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    todos.append(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>', methods=['GET'])
def delete(index):
        if index < len(todos):
        del todos[index]
        return redirect(url_for('index'))



if __name__ == '__main__':

app.run(port=8080, debug=True)
