from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def printed():
    word= "Hello world"
    return word