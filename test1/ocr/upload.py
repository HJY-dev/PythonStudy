from fastapi import FastAPI, File, UploadFile
from typing import List
import uvicorn

app = FastAPI()

# file: UploadFile：适合大文件上传，比较常用

@app.post("/uploadFile/")
#直接对应UploadFile类型数据
async def create_upload_file(file: UploadFile):
    #打印文件名称
    print('file',file.filename)
    #将上传的文件保存到服务本地
    with open(f"{file.filename}", 'wb') as f:
        #一次读取1024字节，循环读取写入
        for chunk in iter(lambda: file.file.read(1024), b''):
            f.write(chunk)

    return {"filename": file.filename}


if __name__ == '__main__':
    #注意，run的第一个参数 必须是文件名:应用程序名
    uvicorn.run("upload:app", port=8080,  reload=True)