# -*- coding: utf-8 -*-
"""
@author: aiwake
"""

# %%
from joblib import load
filename="aiwakeIrisModel.joblib"
clafServ = load(filename)


# %%
from typing import Union
from fastapi import FastAPI

app = FastAPI() # i linking this object and uvicorn


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#i start uvicorn this server
#Anaconda Powershell Prompt open > uvicorn server:app --reload
#Anaconda Powershell Prompt open > uvicorn this_file_name:app_16_line --reload
