# -*- coding: utf-8 -*-
"""
@author: aiwake
"""

# %%
from joblib import load

filename = "aiwakeIrisModel.joblib"
clafUploaded = load(filename)

# %%
from sklearn.datasets import load_iris

irisSet = load_iris()

labelName = list(irisSet.target_names)

# %%
from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import numpy as np

# Create templates files your projets locate
templates = Jinja2Templates(directory="templates")

app = FastAPI()  # i linking this object and uvicorn


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/irisPredict/")
async def iris_predict(request: Request, L1: float, W1: float, L2: float, W2: float):
    testData = np.array([L1, W1, L2, W2]).reshape(-1, 4)  # we change array for numpy but 1d -> 2d
    rates = clafUploaded.predict_proba(testData)[0]
    predicted = np.argmax(rates)

    rate = rates[predicted]

    predicted = labelName[predicted]

    return templates.TemplateResponse("calculate.html", {"request": request, "rates": rates,
                                                         "predicted": predicted,
                                                         "rate": rate
                                                         }
                                      )

# i start uvicorn this server
# Anaconda Powershell Prompt open > uvicorn server:app --reload
# Anaconda Powershell Prompt open > uvicorn this_file_name:app_16_line --reload
