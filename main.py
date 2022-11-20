from fastapi import FastAPI
from fastapi.responses import HTMLResponse,JSONResponse,PlainTextResponse,FileResponse

app=FastAPI()


@app.get("/")
async def home():
    return HTMLResponse("<h1>loh</h1>")


@app.get("/haha")
async def home():
    return {"massage": "bezdari"}


    
@app.get("/a")
async def home():
    return PlainTextResponse("hahahahaahahahhahahhahhahaaahahaha")