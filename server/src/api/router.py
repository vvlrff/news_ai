import csv
import json
import os
import random as rnd
import re
import sys

from fastapi import APIRouter, Body, Depends, File, Query, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, distinct, insert, select,  func

from .nlp_men import Clussifier

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
    test = Clussifier()
    data = test.crate_xlsx(test.main(test.parse_xlsx(file_path)))
    data_out = test.main(test.parse_xlsx(file_path))
    return JSONResponse(content=data_out)

@router.post("/vigruzka")
async def upload_file(file: str):
    folder_path = os.getcwd() + r'/src/api/INPUT_//'  # путь к папке, в которую нужно сохранить файл
    file_path = os.path.join(folder_path, file)  # объединяем путь к папке и имени файла

    return FileResponse(path=file_path,filename=file, media_type='multipart/form-data' )



# @router.get("/answer_to_draw")
# async def upload_file(path_to_input_data: str):
#     test = Clussifier()
#     folder_path = os.getcwd() + r'\src\api\INPUT_\\'+path_to_input_data
#     test.crate_xlsx(test.main(test.parse_xlsx(folder_path)))

#     return FileResponse(path=file_path,filename=file, media_type='multipart/form-data' )
