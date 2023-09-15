from PIL import Image

from fun_图片处理.fun_图片水印.fun_图片蜘蛛水印 import fun_图片蜘蛛水印, fun_获取单排水印

im = Image.open(r"F:\小夕素材\7000-7999\7817\预览图\200_299\小夕素材(262).png")
im.thumbnail((1200, 1200))

fun_图片蜘蛛水印(im=im, logo_size=60, line=3, line_num=2).show()
