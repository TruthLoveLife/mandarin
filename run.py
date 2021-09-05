import uvicorn
from fastapi import FastAPI
from fastsql import app01

app = FastAPI(
    title='FastAPI Tutorial and Coronavirus Tracker API Docs',
    description='模拟普通话考试系统',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs'
    )

app.include_router(app01, prefix='/fastsql', tags=['考生报名系统接口'])
# app.include_router(app02, prefix='/fastsql', tags=['管理员操作系统接口'])


if __name__ == '__main__':
    uvicorn.run('run:app', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)