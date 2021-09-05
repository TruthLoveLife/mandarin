from pydantic import BaseModel
from fastapi import FastAPI, File, Form, UploadFile
from typing import List


class InputStuden(BaseModel):
    name: str
    sex: str
    minzu: str
    carttype: int
    cartnumber: str
    # cartphoto: List[UploadFile] = File(...)
    job: int
    job_address: str
    telephone: str
    birthday: str
    province: str
    city: str
    datileinfor: str

