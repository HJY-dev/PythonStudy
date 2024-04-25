
from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def say_hello():
    return {'code': 200, 'message': 'hello, world!'}

# uvicorn api:app --reload 运行服务
# 浏览器访问 http://127.0.0.1:8000/docs 查看接口文档