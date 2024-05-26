# 这个软件的目的是通过利用汉语、英语等自然语言的属性——改变次序和形状并不很大的影响对语言的阅读和意思，以此来反和谐、反删帖
import string
import re
import random
import numpy as np


def swap_chars(input_string, mean, variance):  # 能运行的一个函数，各方面完美，缺点是没有保留首字符位置
    if not input_string or not isinstance(input_string, str):
        raise ValueError("Input must be a non-empty string.")
    if mean < 0 or variance < 0:
        raise ValueError("Mean and variance must be non-negative.")

    length = len(input_string)
    # 生成新位置
    new_positions = np.clip(np.round(np.arange(length) + np.random.normal(mean, np.sqrt(variance), length)).astype(int),
                            0, length - 1)

    # 创建一个字符数组和输出字符串
    chars = list(input_string)
    output_string = [None] * length

    # 应用新的位置，处理冲突
    for original_position, new_position in enumerate(new_positions):
        # 如果新位置已经被占据，则寻找下一个可用的位置
        while new_position < length and output_string[new_position] is not None:
            new_position += 1
            # 如果超出字符串长度，则回绕到开始位置（可选）
        if new_position == length:
            new_position = 0
            # 寻找第一个可用的位置
            while output_string[new_position] is not None:
                new_position += 1
                # 放置字符到新位置
        output_string[new_position] = chars[original_position]

        # 将字符数组转换回字符串并返回
    return ''.join(output_string)


def is_english_char(char):
    english_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    return char in english_chars


def split_chinese_english(s):
    result = []
    current = ''
    in_english = False

    for char in s:
        # 判断字符是否为英文字符
        if is_english_char(char):
            if not in_english:
                # 如果之前不在英文中，则添加之前累积的非英文字符到结果中
                if current:
                    result.append(current)
                    current = ''
                in_english = True
        else:
            if in_english:
                # 如果之前在英文中，则添加累积的英文字符到结果中
                result.append(current)
                current = ''
                in_english = False

                # 无论是否切换状态，都添加当前字符到current中
        current += char

        # 处理最后一个累积的字符串
    if current:
        result.append(current)

    return result


def cut(s):  # 完美的cut函数
    final_text_fragments = []
    if isinstance(s, str):
        s = [s]

    for part in s:
        pattern = r'([\s。，？！；“”、".,!?;:；]+|\w+)'
        # print("FRA:")
        fragments = re.findall(pattern, part)
        # print(fragments)
        # 过滤和处理片段
        for frag in fragments:
            stripped_frag = frag
            if stripped_frag.isspace():
                final_text_fragments.append(stripped_frag)
            elif stripped_frag:
                if len(stripped_frag) > 1:
                    first_char, *remaining_chars = stripped_frag
                    final_text_fragments.extend([first_char, ''.join(remaining_chars)])
                else:
                    final_text_fragments.append(stripped_frag)

    return final_text_fragments


def replace(s, sensitive_words, replacement_words):
    # 创建一个字典，将敏感词映射到替换词
    word_map = dict(zip(sensitive_words, replacement_words))

    # 将敏感词列表转换为一个正则表达式模式，用'|'连接各个词，并加上边界'\b'以避免部分匹配
    pattern = r'\b' + r'\b|\b'.join(re.escape(word) for word in sensitive_words) + r'\b'

    # 使用正则表达式替换函数替换敏感词
    def replace_word(match):
        word = match.group()
        return word_map.get(word, word)  # 如果找到了敏感词，返回替换词；否则返回原词

    # 应用替换函数到整个字符串
    replaced_s = re.sub(pattern, replace_word, s)

    return replaced_s


def main(s):
    # 配置层
    sensitive_words = ["敏感词1", "敏感词2", "qq"]
    replacement_words = ["替换词A", "替换词B", "QQ"]
    DEBUG_mode = True  # True就开启debug模式
    usr_inter_mode = True  # 如果是True，就是以可执行程序运行的状态，False是以脚本在IDE里运行的状态
    cfg_mean = 0.1  # 均值。正态分布的元素中心距期望，越大混淆度越高
    cfg_variance = 5  # 方差。正态分布的元素中心距方差，越大混淆度越高

    if DEBUG_mode:
        usr_inter_mode = False
    if usr_inter_mode:
        s = input("(输入exit退出程序)输入要和谐的内容：")
        if s == "exit":
            return

    # 分割层
    sp1 = split_chinese_english(s)
    sp2 = cut(sp1)

    # 混淆层
    swapped_texts = [swap_chars(tmp, cfg_mean, cfg_variance) for tmp in sp2]

    # 特殊规则匹配替换层          (比如把傻逼改成别的字)
    rep = ''.join(swapped_texts)
    output = replace(rep, sensitive_words, replacement_words)

    # DEBUG层
    if DEBUG_mode:
        print("SP1:ENG:")
        print(sp1)
        print("SP2:CUT:")
        print(sp2)
        print("SWAP:")
        print(swapped_texts)
        print("OUTPUT:")

    # 输出层
    result = output
    if usr_inter_mode:
        print(result)
    return result


if __name__ == '__main__':
    s = "我操死你的吗,你是什么狗？什么jb人？"  # 以脚本程序运行时，在此输入要和谐的内容
    while True:
        main(s)
