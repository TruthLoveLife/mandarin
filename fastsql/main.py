from typing import List
from faker import Faker
from fastapi import APIRouter, UploadFile, File, Form
from pymysql.converters import escape_string

from fastsql import schemas,CRUD
app01 = APIRouter()
f = Faker(locale='zh-CN')

@app01.post("/getstudent/")
async def sign_up(
        name: str,
        sex: str,
        minzu: str,
        carttype: int,
        cartnumber: str,
        job: int,
        telephone: str,
        birthday: str,
        province: str,
        city: str,
        datileinfor: str,
        cartphoto: UploadFile = File(...)
):
    image = cartphoto.file.read()
    CRUD.new_student(f.random_number(5), name, sex, minzu,carttype,cartnumber, image, job,
                     telephone,birthday,province,city,datileinfor)

