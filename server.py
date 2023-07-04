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
from fastapi import FastAPI

app = FastAPI() # i linking this object and uvicorn


@app.get("/")
def read_root():
    return {"Work": "Worked"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#i start uvicorn this server
#Anaconda Powershell Prompt open > cd YOUR_USER_NAME\anaconda3\envs\YOUR_ENV_NAME\YOUR_PROJECT_FILE
#Anaconda Powershell Prompt open > uvicorn server:app --reload
#Anaconda Powershell Prompt open > uvicorn this_file_name:app_16_line --reload
