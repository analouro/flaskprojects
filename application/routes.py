from application import app, db
from application.models import Task

@app.route('/')
@app.route('/home')
def home():
    return "Welcome to TODO!"

@app.route('/todo')
def todo():
    new_task = Task(name_task = "New task entered") #status_task=False)
    db.session.add(new_task)
    db.session.commit()
    return "New task added to your todo list :)"

@app.route('/read')
def read():
    all_tasks = Task.query.all()
    tasks_string = ""
    for t in all_tasks:
        tasks_string += "<br>" + t.name_task
    return tasks_string

@app.route('/update/<content>')
def update(content):
    first_task = Task.query.get(1)
    first_task.name_task = content
    db.session.commit()
    return first_task.name_task

@app.route('/delete')
def delete():
    delete_task = Task.query.get(1)
    db.session.delete(delete_task)
    db.session.commit()
    return "Task deleted with success!"

@app.route('/done')
def done():
    done_task = Task.query.get(1)
    db.session.commit()
    return f"{done_task.name_task} completed!"

@app.route('/wip')
def wip():
    wip_task = Task.query.get(1)
    db.session.commit()
    return f"{wip_task.name_task} is still a work in progress!"

# @app.route('/status/incompleted')
# def status(completion):
#     first_task = Task.query.get(1)
#     first_task.status_task = bool(completion)
#     db.session.commit()
#     if bool(completion) == True:
#         return f"{first_task.name_task} completed"
#     else:
#         return f"{first_task.name_task} incomplete"  

