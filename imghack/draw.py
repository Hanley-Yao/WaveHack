from PIL import Image

# 设置图像的宽度和高度
width = 1200
height = 256

# 先刷这个图像
# 创建一个白色图像
img_0 = Image.new('RGB', (width, height), color='white')

for i in range(0,16):
    for y in range(i*16,i*16+16):
        for x in range(img_0.width):
            img_0.putpixel((x, y), (255-i*16, 255-i*16, 255-i*16))

# 保存图像
img_0.save("img_0.bmp")

# 再刷这个图像
# 创建一个白色图像
img_1 = Image.new('RGB', (width, height), color='white')

for u in range(0,16):
    for i in range(u*16,u*16+16):
        for y in range(i,i+1):
            for x in range(img_1.width):
                img_1.putpixel((x, y), (255-(i-u*16)*16, 255-(i-u*16)*16, 255-(i-u*16)*16))

# 保存图像
img_1.save("img_1.bmp")
