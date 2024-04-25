import requests
import urllib.request

def upload_image_for_ocr(file_path,save_path):
    """
    上传图片并调用OCR接口进行处理
    :param file_path: 图片文件路径
    :return: OCR处理结果或错误信息
    """
    url = "http://127.0.0.1:7860/image_ocr"  # 假设服务运行在本地的8000端口
    try:
        
        if(file_path.startswith("http")):
            urllib.request.urlretrieve(file_path, save_path)
            with open(save_path, 'rb') as file:
                files = {'image': file}
                response = requests.post(url, files=files)
        else:
            with open(file_path, 'rb') as file:
                files = {'image': file}
                response = requests.post(url, files=files)

        if response.status_code == 200:
            return response.json()  # 返回OCR处理结果
        elif response.status_code == 601:
            return "处理出错"  # 返回错误信息
        else:
            return f"未知错误，状态码：{response.status_code}"

    except Exception as e:
        return f"发生错误：{e}"

# 调用函数并传入图片路径
# file_path = "../imgs/11.jpg"  # 替换为您的图片文件路径
file_path = "https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2019%2F10%2F15%2Fe214dd8e2f1d424b94b80244f4d882cb.jpeg&thumbnail=660x2147483647&quality=80&type=jpg"
save_path = "image.jpg"  
result = upload_image_for_ocr(file_path,save_path)
# print(result)
# 数据加工
items = result[0]
txts = [line[1][0] for line in items]
print(txts)