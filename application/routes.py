from application import app, db
from application.models import Task
from flask import Flask, render_template
from flask_wtf import FlaskForm
from application.forms import TaskForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')

@app.route('/add_todo', methods=["GET", "POST"])
def add_todo():
    form = TaskForm()

    if request.method == "POST":
        new_task = form.new_task

        if form.validate_on_submit():
            task = Task(new_task = form.name_task.data)
            db.session.add(task)
            db.session.commit()
            return redirect(url_for("read"))
    return render_template('add_todo.html', form=form)

@app.route('/read')
def read():
    all_tasks = Task.query.all()
    return render_template('read.html', tasks=all_tasks)


@app.route('/update/<content>')
def update(content):
    first_task = Task.query.get(6)
    first_task.name_task = content
    db.session.commit()
    return first_task.name_task

@app.route('/status/<situation>')
def status(situation):
    a_task = Task.query.get(7)
    a_task.status_task = situation
    db.session.commit()
    return a_task.status_task

@app.route('/delete')
def delete():
    delete_task = Task.query.get(1)
    db.session.delete(delete_task)
    db.session.commit()
    return "Task deleted with success!"


#### Code added in the first stages of development: ####

# @app.route('/')
# @app.route('/home')
# def home():
#     return "Welcome to TODO!"

# First way to add a new task - GET
# @app.route('/todo')
# def todo():
#     new_task = Task(name_task = "New task entered") #status_task=False)
#     db.session.add(new_task)
#     db.session.commit()
#     return "New task added to your todo list :)"


# @app.route('/read')
# def read():
#     all_tasks = Task.query.all()
#     tasks_string = ""
#     for t in all_tasks:
#         tasks_string += "<br>" + t.name_task
#     return tasks_string

# Day 2 Task: Page to update/delete tasks
# @app.route('/updatetask')
# def updatetask():
#     return render_template('update.html')

# @app.route('/deletetask')
# def deletetask():
#     return render_template('delete.html')

# @app.route('/done')
# def done():
#     done_task = Task.query.get(1)
#     db.session.commit()
#     return f"{done_task.name_task} completed!"

# @app.route('/wip')
# def wip():
#     wip_task = Task.query.get(1)
#     db.session.commit()
#     return f"{wip_task.name_task} is still a work in progress!"

# Other option that did not work:
# @app.route('/status/incompleted')
# def status(completion):
#     first_task = Task.query.get(1)
#     first_task.status_task = bool(completion)
#     db.session.commit()
#     if bool(completion) == True:
#         return f"{first_task.name_task} completed"
#     else:
#         return f"{first_task.name_task} incomplete"  

