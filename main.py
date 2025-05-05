from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return "heyyy"

@app.get('/about')
def about():
    return {"data": "hi hello !!!!!"}