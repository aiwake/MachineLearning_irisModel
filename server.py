# -*- coding: utf-8 -*-
"""
@author: aiwake
"""

# %%
from joblib import load

filename = "aiwakeIrisModel.joblib"
clafUploaded = load(filename)

# %%
from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# Create templates files your projets locate
templates = Jinja2Templates(directory="templates")

app = FastAPI()  # i linking this object and uvicorn


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/irisPredict/")
def iris_predict(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# i start uvicorn this server
# Anaconda Powershell Prompt open > uvicorn server:app --reload
# Anaconda Powershell Prompt open > uvicorn this_file_name:app_16_line --reload
