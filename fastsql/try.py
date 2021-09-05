# def new_student(*args):
#     print("输出的内容是：%s,%s,%s"%args)
#
# # new_student("张三","李四", "王五")
# # ,%s,%s
# new_student("张三","李四", "王五")

from fastsql import CRUD

with open("./test.jpeg", "rb") as file:
    image = file.read()

CRUD.insert_image(image)