import csv
import json
import os
import random as rnd
import re
import sys
import pickle

from fastapi import APIRouter, Body, Depends, File, Query, UploadFile
from fastapi.responses import FileResponse, JSONResponse

from .nlp_men_ru_ber import Clussifier
test = Clussifier()

router = APIRouter (
    prefix='/api',
    tags= ['api']
)


@router.post("/zagruzka")
async def upload_file(file: UploadFile):
    folder_path = os.getcwd() + r'/src/api/INPUT_//'  # путь к папке, в которую нужно сохранить файл
    file_path = os.path.join(folder_path, file.filename)  # объединяем путь к папке и имени файла
    with open(file_path, "wb") as f:  # открываем файл на запись
        f.write(await file.read())  # записываем содержимое загруженного файла в созданный файл

    # data = test.crate_xlsx(test.main(test.parse_xlsx(file_path)))
    data_out = test.main(test.parse_xlsx(file_path))
    pickle.dump(data_out, file = open("data_out.pickle", "wb"))

    return JSONResponse(content=data_out)

@router.post("/vigruzka")
async def upload_file():
    folder_path = os.getcwd() + r'/src/api/INPUT_//'  # путь к папке, в которую нужно сохранить файл
    file_path = os.path.join(folder_path, 'answer.xlsx')  # объединяем путь к папке и имени файла

    return FileResponse(path=file_path,filename='answer.xlsx', media_type='multipart/form-data' )


@router.post("/vigruzka_for_chek")
async def upload_file():
    folder_path = os.getcwd() + r'/src/api/INPUT_//NaturaLP_ANSWER_FOR_CHECKING.xlsx'  # путь к папке, в которую нужно сохранить файл
    return FileResponse(path=folder_path,filename='NaturaLP_ANSWER_FOR_CHECKING.xlsx', media_type='multipart/form-data' )


@router.post("/for_chek")
async def upload_file():
    company1_reloaded = pickle.load(open("data_out.pickle", "rb"))
    return JSONResponse(
        content=company1_reloaded
    )

# company1_reloaded = pickle.load(open("data_out.pickle", "rb"))
