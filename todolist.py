from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
tasks=[]
@app.get("/")
def home():
    return {"message":"hello"}
@app.get("/tasks/")
def get_tasks():
    return tasks
class Task(BaseModel):
    title:str
    id:int | None=None
    completed: bool = False
@app.post("/tasks/")
def creat_task(title:Task):
    new_id=len(tasks)+1
    title.id=new_id
    tasks.append(title)
    return title
@app.get("/Task/{task_id}")
def get_task(task_id:int):
    for task in tasks:
        if task.id==task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
@app.delete("/Task/{task_id}")
def delete_task(task_id:int):
    for task in tasks:
        if task_id==task.id:
            tasks.remove(task)
            return "task deleted"
    raise HTTPException(status_code=404,detail="task not found")
@app.put("/Task/{task_id}")
def update_task(task_id:int,title:Task):
    for task in tasks:
        if task.id==task_id:
            task.title=title.title
            return task
    raise HTTPException(status_code=404, detail="Task not found")
@app.patch("/Task/{task_id}")
def patch_task(task_id:int,title:Task):
    for task in tasks:
        if task.id==task_id:
            task.title = title.title
            return task
    raise HTTPException(status_code=404, detail="Task not found")
class TaskUpdate(BaseModel):
    completed: bool





