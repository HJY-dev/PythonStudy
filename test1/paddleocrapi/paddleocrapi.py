# main.py
import os
import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from paddleocr import PaddleOCR, draw_ocr
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# 初始化 FastAPI 应用
app = FastAPI(
    title='PadlleOCR API',
    description='基于 PaddleOCR 的 OCR 服务 API 接口',
    version='1.0.1',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 定义 OCR 参数
params = {
    'det_model_dir': '/ppocr_img/ch_PP-OCRv4_det_server_infer',
    'rec_model_dir': '/ppocr_img/ch_PP-OCRv4_rec_server_infer',
    'cls_model_dir': '/ppocr_img/ch_ppocr_mobile_v2.0_cls_slim_infer',
    'use_gpu': False,
    'use_angle_cls': True
}

# 初始化 OCR 实例
ocr = PaddleOCR(**params)


@app.post("/image_ocr")
async def upload_image(image: UploadFile = File(...)):
    """
    接收上传的图片文件并进行 OCR 处理
    """
    try:
        img = cv2.imdecode(np.fromstring(image.file.read(), np.uint8), cv2.IMREAD_COLOR)
        # 读取保存的图片并进行 OCR
        result = ocr.ocr(img, cls=True)
        return result
    except:
        print("Error")
        # 返回HTTP错误码601
        raise HTTPException(status_code=601, detail="处理出错")


if __name__ == '__main__':
    uvicorn.run(f'{os.path.basename(__file__).split(".")[0]}:app',
                host='0.0.0.0',
                port=7860,
                reload=False,
                workers=1)