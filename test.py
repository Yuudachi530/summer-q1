from PIL import Image, ImageDraw

import random

value_color = 80

dic_color = {}

list_color_value = []
while value_color <= 255:
    list_color_value.append(int(value_color))
    value_color = value_color * 1.1
    

def draw_scaleline(length, width):
    #绘制横向格线
    draw = ImageDraw.Draw(image)
    coordinate_x = 0
    coordinate_y = 0
    for y in range(width + 1):
        draw.line((coordinate_x, coordinate_y, length*100, coordinate_y), 0)
        coordinate_y = coordinate_y + 100
    coordinate_y = 0
    #绘制纵向格线
    for x in range(length + 1):
        draw.line((coordinate_x, coordinate_y, coordinate_x, width*100), 0)
        coordinate_x = coordinate_x + 100
    coordinate_x = 0
    
    return image

    
def fill_scale_color(image_scale, length, width):
    draw = ImageDraw.Draw(image_scale)
    constant_length = length
    counter = length * width
    for i in range(counter):
        color = random.choice(list_color_value)
        for x in range((length - 1) * 100, length * 100):
            for y in range((width - 1) * 100, width * 100):
                draw.point((x, y), color)
        dictionary_value_color(dic_color, str(length)+str(width), color)
        length = length - 1
        if length == 0:
            width = width - 1
            length = constant_length
    
    return image_scale

def dictionary_value_color(dic, name, value):
        dic[name] = value
    
        return dic

def dictionary_modify_value_color(dic, name, value):
        dic[name] = int(value * 1.1)
        
    

def modify_scale_color(image_scale, length, width):
    draw = ImageDraw.Draw(image_scale)
    constant_length = length
    counter = length * width
    for i in range(counter):
        color = dic_color[str(length)+str(width)]
        dic_color[str(length)+str(width)] = int(color * 1.1)
        color = dic_color[str(length)+str(width)]  
        if color <= 255:
            for x in range((length - 1) * 100, length * 100):
                for y in range((width - 1) * 100, width * 100):
                    draw.point((x, y), color)
            else:
                print("scale_location: (",str(length),",",str(width),"): True")
        length = length - 1
        if length == 0:
            width = width - 1
            length = constant_length
    
    return image_scale
    

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



   
            
        
    
    
        
    
    
    
    
    
    


