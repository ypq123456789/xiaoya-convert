import re

def convert_urls(input_file, output_file):
    # 第一种模式匹配规则
    pattern1 = re.compile(r'https://www\.alipan\.com/s/(\w+)/folder/(\w+)')
    # 第二种模式匹配规则
    pattern2 = re.compile(r'(.+) https://www\.alipan\.com/s/(\w+)/folder/(\w+) (\d+)')
    # 新增的模式匹配规则 1
    pattern3 = re.compile(r'(\w+) https://www\.aliyundrive\.com/s/(\w+)/folder/(\w+)')
    # 新增的模式匹配规则 2
    pattern4 = re.compile(r'https://www\.aliyundrive\.com/s/(\w+)/folder/(\w+)(.*)')

    try:
        # 读取输入文件，指定使用 utf-8 编码，并确保行结束符为 Unix 格式
        with open(input_file, 'r', encoding='utf-8', newline='') as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"无法找到输入文件：{input_file}")
        return
    except UnicodeDecodeError as e:
        print(f"文件编码错误：{e}")
        return

    # 准备转换后的 URL 列表
    converted_urls = []

    # 转换每个 URL
    for url in urls:
        # 尝试第一种规则匹配和转换
        if pattern1.search(url):
            converted = pattern1.sub(r'\1 \2', url)
        # 尝试第二种规则匹配和转换
        elif pattern2.search(url):
            converted = pattern2.sub(r'\1 \2 \3 \4', url)
        # 尝试新增的规则 1 匹配和转换
        elif pattern3.search(url):
            converted = pattern3.sub(r'\1 \2 \3', url)
        # 尝试新增的规则 2 匹配和转换
        elif pattern4.search(url):
            converted = pattern4.sub(r'\1 \2 \3', url)
        else:
            # 如果都不匹配，保留原始 URL
            converted = url
        # 将转换后的 URL 添加到列表，并在每个 URL 后添加换行符
        converted_urls.append(converted + '\n')

    # 输出结果到指定的输出文件
    try:
        with open(output_file, 'w', encoding='utf-8', newline='\n') as file:
            file.writelines(converted_urls)
    except IOError as e:
        print(f"文件写入错误：{e}")
        return

    print(f'转换完成，转换后的 URLs 已保存在 "{output_file}" 文件中，转换后的内容为：\n{"".join(converted_urls)}')  # 添加转换后的内容，并分行显示
    # 等待用户按任意键退出
    any_key = input("项目地址：https://github.com/ypq123456789/xiaoya-convert，如果使用满意请给个star，按ENTER键退出...")


# 输入文件和输出文件的路径
input_file_path = 'input_urls.txt'
output_file_path = 'alishare_list.txt'

# 调用转换函数
convert_urls(input_file_path, output_file_path)
