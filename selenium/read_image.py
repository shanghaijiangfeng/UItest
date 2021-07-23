#codinng=utf-8
import pytesseract
from PIL import Image
import sys
import os
basepath=os.getcwd()
sys.path.append(basepath)
from util.ShowapiRequest import ShowapiRequest
"打开图片"
image = Image.open(basepath+"\\Image\\image2.png")
"通过pytesseract对图片识别，返回一个字符串"
text = pytesseract.image_to_string(image)
print(text)

"调用第三方接口，传入图片地址，返回一个字符串"
r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
image = basepath+"\\Image\\image2.png"
r.addFilePara("image", r"image") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
