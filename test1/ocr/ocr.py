from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = 'imgs/11.jpg'
result = ocr.ocr(img_path, cls=True)

# 显示结果
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]

scores = [line[1][1] for line in result]
print('姓名:'+txts[2],'性别:'+txts[6],txts[7],'出生年月:'+txts[12],'住址:'+txts[15]+txts[16],'身份证号:'+txts[20])

# 保存结果
im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('imgs/result.jpg')