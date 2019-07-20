from PIL import Image, ImageDraw

import random
#设定初始颜色值
value_color = 80
#创建空白字典，字典将填入表格坐标以及对应颜色值
dic_color = {}
#创建颜色值列表
list_color_value = []
while value_color <= 255:
    list_color_value.append(int(value_color))
    value_color = value_color * 1.1
    

def draw_scaleline(length, width):
    #绘制横向表格框线
    draw = ImageDraw.Draw(image)
    coordinate_x = 0
    coordinate_y = 0
    for y in range(width + 1):
        draw.line((coordinate_x, coordinate_y, length*100, coordinate_y), 0)
        coordinate_y = coordinate_y + 100
    coordinate_y = 0
    #绘制纵向表格框线
    for x in range(length + 1):
        draw.line((coordinate_x, coordinate_y, coordinate_x, width*100), 0)
        coordinate_x = coordinate_x + 100
    coordinate_x = 0
    
    return image

#单元格颜色填充函数
#length为横向单元格数目，width为纵向单元格数目    
def fill_scale_color(image_scale, length, width):
    draw = ImageDraw.Draw(image_scale)
    constant_length = length #设置常量，方便调用
    counter = length * width #单元格总数目
    for i in range(counter):
        color = random.choice(list_color_value) #从颜色值列表里随机选择颜色值生成初始表格
        #填色
        for x in range((length - 1) * 100, length * 100):
            for y in range((width - 1) * 100, width * 100):
                draw.point((x, y), color)
        #向字典中添加元素，将每个单元格的颜色值记录在字典内
        dictionary_value_color(dic_color, str(length)+str(width), color)
        #转移填色目标单元格
        length = length - 1
        if length == 0:
            width = width - 1
            length = constant_length
    
    return image_scale #输出表格

#定义函数写入各单元格颜色值
def dictionary_value_color(dic, name, value):
        dic[name] = value
    
        return dic

#定义函数改变各单元颜色值
def dictionary_modify_value_color(dic, name, value):
        dic[name] = int(value * 1.1)
        
    
#定义函数改变各单元格颜色
#length为横向单元格数目，width为纵向单元格数目
def modify_scale_color(image_scale, length, width):
    draw = ImageDraw.Draw(image_scale)
    constant_length = length #设置常量，方便调用
    counter = length * width #单元格总数目
    for i in range(counter):
        color = dic_color[str(length)+str(width)] #调用单元格坐标为(length, width)的单元格的颜色值
        dic_color[str(length)+str(width)] = int(color * 1.1) #改变颜色值，并将其写入字典对应元素
        color = dic_color[str(length)+str(width)]  #重新调用坐标为(length, width)的单元格的颜色值
        if color <= 255: #如果颜色值没有超出范围(颜色值 <= 255)
            #填色
            for x in range((length - 1) * 100, length * 100):
                for y in range((width - 1) * 100, width * 100):
                    draw.point((x, y), color)
            else:
                #输出对应单元格的坐标和结果
                print("scale_location: (",str(length),",",str(width),"): True")
        ##转移填色目标单元格
        length = length - 1
        if length == 0:
            width = width - 1
            length = constant_length
    
    return image_scale #输出表格
    
#创建新
image = Image.new("L", (800, 500), None)
image = fill_scale_color(image , 8, 5)
image = draw_scaleline(8, 5)
image.save("test.jpg", "jpeg")
image.show()
print("enter 'y' if you want to modify the square, else enter 'n' ")
judge = str(input("please give your answer: "))
image = modify_scale_color(image, 8, 5)
image = draw_scaleline(8, 5)
image.show()
while judge == "y" :
    print("enter 'y' if you want to modify the square, else enter 'n' ")
    judge = str(input("please give your answer: "))
    image = modify_scale_color(image, 8, 5)
    image = draw_scaleline(8, 5)
    image.save("test.jpg", "jpeg")
    image.show()



   
            
        
    
    
        
    
    
    
    
    
    


