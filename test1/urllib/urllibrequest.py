import urllib.request

def print_response(url,save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        print("图片已成功下载到:", save_path)
    except Exception as e:
        print("下载失败:", e)

def main():
    # 远程资源地址
    remote_url = "https://nimg.ws.126.net/?url=http%3A%2F%2Fdingyue.ws.126.net%2F2019%2F10%2F15%2Fe214dd8e2f1d424b94b80244f4d882cb.jpeg&thumbnail=660x2147483647&quality=80&type=jpg"
    save_path = "image.jpg"
    # 发送请求并输出响应内容
    print_response(remote_url,save_path)

if __name__ == "__main__":
    main()