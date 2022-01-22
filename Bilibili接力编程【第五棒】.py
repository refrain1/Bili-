# 第一棒Windows-Registry制作基础框架
# 后面的接力up写上第几棒+名字+贡献就行
# 第二棒李某软件工作室 制作计算机功能
# 第三棒 CZJ_Official改进计算器+模块化+记事本
# 第四棒 某科学的方程核显   修改语言
# 第五棒 阿門_ 优化结构 添加图片压缩
import os
from random import randint
import time
# pip install pillow
from PIL import Image, ImageFile
# pip install tqdm
from tqdm import tqdm

storage = ''


def print_welcome():
    print("欢迎使用Registry的工具箱！本应用有多名科技区UP主联合接力制作！")


def generate_validate_captcha():
    captcha = randint(10001, 99999)
    while True:
        mycaptcha = input("请输入验证码，验证码：" + str(captcha) + "请再输入一遍您刚刚输出的验证码")
        if mycaptcha == str(captcha):
            print("验证成功！欢迎！")
            return True
        else:
            print("验证失败，请重新输入验证码！")


def print_time():
    t = time.localtime()
    now_time = str(t.tm_year) + "年" + str(t.tm_mon) + "月" + str(t.tm_mday) + "日"
    print("当前日期：" + str(now_time))


def about_toolbox():
    print("Registry的工具箱 v0.1 Realase Beta 1 本应用由多名科技区UP主联合接力制作！")


def calculator(expression):
    while True:
        try:
            print(eval(expression))
            break
        except Exception:
            print("您所输入的表达式错误，请重新输入")


def notepad():
    global storage
    input_option = ['返回上层', '储存信息', '编辑信息', '清空信息']
    mes = input("请选择操作：")
    for key in range(len(input_option)):
        print('{key} {input_option}'.format(key=key, input_option=input_option[key]))
    if mes == '0':
        mainloop()
    elif mes == '1':
        storage = input("请输入要储存的信息：")
        print("储存信息完成！")
    elif mes == '2':
        print("当前储存的信息为：" + storage)
        storage = input("请重新输入：")
        print("编辑完成！")
    elif mes == '3':
        storage = ''
        print("消息已清空！")


def logout():
    import sys
    sys.exit(0)


# 创建文件夹
def make_dir(dir_path):
    path = dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


# 获取文件下下所有图片
def get_img_file(filename):
    img_list = []
    for parent, dirname, filenames in os.walk(filename):
        for filename in filenames:
            if filename.lower().endswith(('.bmp','.dib','.png','.pbm','.pgm','.ppm','.tif','tiff')):
                img_list.append(os.path.join(parent,filename))
    return img_list



# 简单压缩图片
def compress_img(path_list, out_image_path):
    image_name = os.path.basename(path_list).split('.')[0]
    image = Image.open(path_list)
    # 强制转为RGB
    image = image.convert('RGB')
    # 保持原比例大小
    image = image.resize((int(image.width), int(image.height)), Image.ANTIALIAS)
    # quality:保存图像的质量
    image.save(out_image_path + os.sep + image_name + '.jpg', quality=95)


# 压缩图片至指定大小
def compress_img_to_size(input_size, input_image_path, out_image_path):
    size = os.path.getsize(input_image_path) // 1024
    image = Image.open(input_image_path)
    # 强制转为RGB
    image = image.convert('RGB')
    img_name = os.path.basename(input_image_path).split('.')[0]
    image.save(out_image_path + os.sep + img_name + '.jpg')
    if int(size) <= int(input_size):
        return False
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    while int(size) > int(input_size):
        image = Image.open(out_image_path + os.sep + img_name + '.jpg')
        image = image.convert('RGB')
        out = image.resize((int(image.width * 0.9), int(image.height * 0.9)), Image.ANTIALIAS)
        try:
            out.save(out_image_path + os.sep + img_name + '.jpg', quality=95)
        except Exception as e:
            raise e
        size = os.path.getsize(out_image_path + os.sep + img_name + '.jpg') // 1024


def img_tool():
    input_option = ['返回上层', '简单压缩图片', '压缩图片至指定大小']
    for key in range(len(input_option)):
        print('{key} {input_option}'.format(key=key, input_option=input_option[key]))
    code = input("请选择一个选项：")
    if code == '0':
        mainloop()
    if code == '1':
        input_image_path = input('请输入图片路径')
        if os.path.isdir(input_image_path):
            out_image_path = input_image_path + os.sep + '../img_'
            make_dir(out_image_path)
            path_list = get_img_file(input_image_path)
            for i in tqdm(range(len(path_list))):
                compress_img(path_list[i], out_image_path)
        elif os.path.isfile(input_image_path):
            out_image_path = input_image_path + os.sep + '../../img_'
            make_dir(out_image_path)
            compress_img(input_image_path, out_image_path)
    elif code == '2':
        input_image_path = input('请输入图片路径')
        if os.path.isdir(input_image_path):
            print('这个路径看起来是个文件呢!')
        elif os.path.isfile(input_image_path):
            input_size = input('输入您的文件目标大小（单位KB）')
            out_image_path = input_image_path + os.sep + '../../img_'
            make_dir(out_image_path)
            compress_img_to_size(input_size=input_size, input_image_path=input_image_path,
                                 out_image_path=out_image_path)


def mainloop():
    input_option = ['退出当前程序', 'Reg关于此工具箱', 'Reg计算器', 'Reg记事本', 'Reg图片工具箱']
    for key in range(len(input_option)):
        print('{key} {input_option}'.format(key=key, input_option=input_option[key]))
    code = input("请选择一个选项：")
    if code == '0':
        print("感谢您使用Registory的工具箱，我们欢迎您的下次使用！")
        logout()
    elif code == '1':
        about_toolbox()
    elif code == '2':
        expression = input("请输入表达式：")
        calculator(expression)
    elif code == '3':
        notepad()
    elif code == '4':
        img_tool()


if __name__ == '__main__':
    print_welcome()
    if generate_validate_captcha():
        while True:
            print_time()
            mainloop()
