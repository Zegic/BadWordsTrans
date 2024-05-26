import re


# r'([\s。，？！；“”、".,!?;:；]+|\w+)'
# def cut(string_list):
#     truncated_list = []
#     for s in string_list:
#         matches = re.split(r'(\W.*?)(?=\W|$)', s)
#         truncated_list.extend(matches)
#     parts = [part for part in truncated_list if part]
#     return parts




# def cut(s):  # 完美的cut函数
#     final_text_fragments = []
#     if isinstance(s, str):
#         s = [s]
#
#     for part in s:
#         pattern = r'([\s。，？！；“”、".,!?;:；]+|\w+)'
#         fragments = re.findall(pattern, part)
#         for frag in fragments:
#             stripped_frag = frag
#             # if stripped_frag.isspace():
#             #     final_text_fragments.append(stripped_frag)
#
#             final_text_fragments.append(stripped_frag)
#
#     return final_text_fragments
# def cut(s):  # 最初的cut
#     final_text_fragments = []
#
#     # 遍历 text2 中的每个元素
#     for part in s:
#         pattern = r'((?:\s*)[。，？！；“”、".,!?;:；]+(?:\s*)|(?:\s*)\w+(?:\s*))'
#         # 使用 re.findall 查找所有匹配的片段
#         fragments = re.findall(pattern, part)
#         # 过滤掉只包含空格的片段
#         fragments = [frag for frag in fragments if frag.strip()]
#         # 将找到的片段添加到最终列表中
#         final_text_fragments.extend(fragments)
#         # 打印最终的文本片段列表
#     # print(final_text_fragments)
#     return final_text_fragments

# pattern = r'[。，？！；“”、\".,!?;:\s]+'，还有什么符号都可以加进去
# text = re.split(r'(?<=[。，？！；“”、\".,!?;:])\s*?', text2)

# def split_string_by_punctuation(text):
#     # 使用正则表达式定义标点符号
#     punctuation =  r'([\s。，？！；“”、".,!?;:；]+|\w+)'
#     # 使用re.split进行截断，但保留分隔符
#     parts = re.split(f'({punctuation})', text)
#     return parts
# def cut(text):
#     result = [split_string_by_punctuation(s) for s in test]
#     return result

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


# def cut(input_string):
#     # punctuation_pattern = r'([\s。，？！；“”、".,!?;:；]+|\w+)'
#     punctuation_pattern = r'[，。！？；：“”‘’";:,.?!()《》〈〉【】（）【】{}]'
#     truncated_parts = re.split(punctuation_pattern, input_string)
#     return [part for part in truncated_parts if part]


def cut(input_string, max_length):
    punctuation_pattern = r'[，。！？；：“”‘’";:,.?!()《》〈〉【】（）【】{}]'
    truncated_parts = re.split(punctuation_pattern, input_string)
    final_parts = []
    for part in truncated_parts:
        if part:  # 忽略空字符串
            if len(part) > max_length:
                part = part[:max_length]  # 截断字符串
            final_parts.append(part)
    return final_parts

# def cut(input_string): # 在cut里再加一个int，超过int的长度的字符串将被截断，防止字符串过长
#     punctuation_pattern = r'[，。！？；：“”‘’";:,.?!()《》〈〉【】（）【】{}]'
#     truncated_list = re.split(punctuation_pattern, input_string)
#     final_list = []
#     i = 0
#     while i < len(truncated_list):
#         if i < len(truncated_list) - 1:
#             final_list.append(truncated_list[i] + truncated_list[i + 1])
#             i += 2  # 跳过一个元素（标点符号）
#         else:
#             final_list.append(truncated_list[i])
#             i += 1
#     return [part for part in final_list if part]

# def cut(input_string, max_length):
#     punctuation_pattern = r'[，。！？；：“”‘’";:,.?!()《》〈〉【】（）【】{}]'
#     # punctuation_pattern = r'([\s。，？！；“”、".,!?;:；]+|\w+)'
#     truncated_list = re.split(punctuation_pattern, input_string)
#     final_list = []
#     i = 0
#     while i < len(truncated_list):
#         if i < len(truncated_list) - 1:
#             # 合并两个字符串，并检查长度
#             combined_part = truncated_list[i] + truncated_list[i + 1]
#             if len(combined_part) > max_length:
#                 # 如果超过最大长度，则截断字符串
#                 combined_part = combined_part[:max_length]
#             final_list.append(combined_part)
#             i += 2  # 跳过一个元素（标点符号）
#         else:
#             # 如果是最后一个元素，直接添加到列表
#             final_list.append(truncated_list[i])
#             i += 1
#     return [part for part in final_list if part]

# def add(string, string_list):
#     result_list = string_list.copy()
#     index = 0
#     for char in string:
#         result_list[index] = char + result_list[index]
#         index = (index + 1) % len(string_list)
#
#     return result_list


# def add(string, string_list):  # 这个函数可以用来排竖式
#     result_list = string_list.copy()
#     char_index = 0  # 字符串字符的索引
#     sub_index = 0  # 列表子字符串的索引
#     while char_index < len(string):
#         result_list[sub_index] = string[char_index] + result_list[sub_index]
#         char_index += 1
#         sub_index = (sub_index + 1) % len(string_list)
#     return result_list

def add(string, string_list):
    result_list = []
    char_index = 0  # 字符串中字符的当前索引
    sub_index = -1  # 子字符串列表的当前索引

    # 循环遍历字符串的每个字符
    while char_index < len(string):
        sub_index = (sub_index + 1) % len(string_list)
        result_list.append(string[char_index] + string_list[sub_index]+ "，")
        char_index += 1

    return result_list



# r'([\s。，？！；“”、".,!?;:；]+|\w+)'
header = "..有些话发不出来，你竖着看："
payload = """这几天心里颇不宁静。。。今晚在院子里坐着乘凉。。。忽然想起日日走过的荷塘，在这满月的光里，总该另有一番样子吧。月亮渐渐地升高了，墙外马路上孩子们的欢笑，已经听不见了；妻在屋里拍着闰儿⑴，迷迷糊糊地哼着眠歌。我悄悄地披了大衫，带上门出去。沿着荷塘，是一条曲折的小煤屑路。这是一条幽僻的路；白天也少人走，夜晚更加寂寞。荷塘四面，长着许多树，蓊蓊郁郁⑵的。路的一旁，是些杨柳，和一些不知道名字的树。没有月光的晚上，这路上阴森森的，有些怕人。今晚却很好，虽然月光也还是淡淡的。"""
payload2 = """豫章故郡，洪都新府。星分翼轸，地接衡庐。襟三江而带五湖，控蛮荆而引瓯越。物华天宝，龙光射牛斗之墟；人杰地灵，徐孺下陈蕃之榻。雄州雾列，俊采星驰。台隍枕夷夏之交，宾主尽东南之美。都督阎公之雅望，棨戟遥临；宇文新州之懿范，襜帷暂驻。十旬休假，胜友如云；千里逢迎，高朋满座。腾蛟起凤，孟学士之词宗；紫电青霜，王将军之武库。家君作宰，路出名区；童子何知，躬逢胜饯。时维九月，序属三秋。潦水尽而寒潭清，烟光凝而暮山紫。俨骖騑于上路，访风景于崇阿。临帝子之长洲，得天人之旧馆。层峦耸翠，上出重霄；飞阁流丹，下临无地。鹤汀凫渚，穷岛屿之萦回；桂殿兰宫，即冈峦之体势。披绣闼，俯雕甍，山原旷其盈视，川泽纡其骇瞩。闾阎扑地，钟鸣鼎食之家；舸舰弥津，青雀黄龙之舳。云销雨霁，彩彻区明。落霞与孤鹜齐飞，秋水共长天一色。渔舟唱晚，响穷彭蠡之滨，雁阵惊寒，声断衡阳之浦。遥襟甫畅，逸兴遄飞。爽籁发而清风生，纤歌凝而白云遏。睢园绿竹，气凌彭泽之樽；邺水朱华，光照临川之笔。四美具，二难并。穷睇眄于中天，极娱游于暇日。天高地迥，觉宇宙之无穷；兴尽悲来，识盈虚之有数。望长安于日下，目吴会于云间。地势极而南溟深，天柱高而北辰远。关山难越，谁悲失路之人；萍水相逢，尽是他乡之客。怀帝阍而不见，奉宣室以何年？嗟乎！时运不齐，命途多舛。冯唐易老，李广难封。屈贾谊于长沙，非无圣主；窜梁鸿于海曲，岂乏明时？所赖君子见机，达人知命。老当益壮，宁移白首之心？穷且益坚，不坠青云之志。酌贪泉而觉爽，处涸辙以犹欢。北海虽赊，扶摇可接；东隅已逝，桑榆非晚。孟尝高洁，空余报国之情；阮籍猖狂，岂效穷途之哭！勃，三尺微命，一介书生。无路请缨，等终军之弱冠；有怀投笔，慕宗悫之长风。舍簪笏于百龄，奉晨昏于万里。非谢家之宝树，接孟氏之芳邻。他日趋庭，叨陪鲤对；今兹捧袂，喜托龙门。杨意不逢，抚凌云而自惜；钟期既遇，奏流水以何惭？呜呼！胜地不常，盛筵难再；兰亭已矣，梓泽丘墟。临别赠言，幸承恩于伟饯；登高作赋，是所望于群公。敢竭鄙怀，恭疏短引；一言均赋，四韵俱成。请洒潘江，各倾陆海云尔"""
payloadt = "啊啊啊啊d,啊啊啊啊j.啊啊啊啊hd，啊啊啊啊hj。啊啊啊啊kg 啊啊啊啊wh？啊啊啊啊gt！啊"
# test = "A,B,C,D,E"
# plain = "草你妈的臭傻逼，你妈什么时候死啊，我去给你妈坟头蹦个迪"
# plain = "123456789012345678901234567890"
plain = "测试一下我的牛逼和谐软件三点零最终形态，能不能在逼站发出去？我先来陈瑞你妈死了，你妈什么时候死啊，草你血吗"
max = 99  # 可以控制payload字符串的最大长度
sp1 = cut(payload,max)
sp2 = add(plain,sp1)
result = sp2

# print(sp1)
# print(sp2)
# print(result)
print(header)
for s in result:
    # print()
    print(s)

# if "__name__" == "__main__" :
#     s1 = input("输入你想要和谐的内容")
#     s2 = cut(test)
#     s3 = add (s1,s2)
#     for a in s3 :
#         print (a)