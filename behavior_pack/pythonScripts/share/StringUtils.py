# -*- coding: utf-8 -*-
# @Author  : Ree
"""文本工具"""


def getBar(process, number=20, icon="┃", prefix_finish="§2", prefix_undone="§c"):
    """
    生成文本进度条
    @param process: 进度，0~1
    @param number: 总进度条数
    @param icon: 图标
    @param prefix_finish: 完成颜色
    @param prefix_undone: 未完成的颜色
    @return:
    """
    result = ""
    step = 1.0 / number
    count = 0
    for i in range(number):
        count += step
        if count <= process:
            result += prefix_finish
        else:
            result += prefix_undone
        result += icon
    return result


def transformSize(total, position):
    """
    转换位置信息
    @param total: 总长度，如utils.getScreenViewInfo()
    @param position: 与total对应的长度信息，如"50%+10",当这一项是float且小于等于1时，会当作百分比处理
    @return:
    """
    import re
    result = []
    for size, t in zip(position, total):
        if isinstance(size, float) and size <= 1.0:
            size = "%.2f" % (100.0 * size) + "%"
        size = str(size)
        match = re.search("(\-|\+)?\d+(\.\d+)?%", size)
        if match:
            group = match.group(0)
            add = size.replace(group, "")
            add = 0 if len(add) == 0 else float(add)
            x = float(group[:-1]) * t / 100.0 + add
        else:
            x = float(size)
        result.append(x)
    return tuple(result)


def replaceRecursive(d, origin, replacement):
    """
    替换字典中的字符串
    :param d:
    :param origin:
    :param replacement:
    """
    for key, value in d.items():
        if isinstance(value, dict):
            replaceRecursive(value, origin, replacement)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    replaceRecursive(item, origin, replacement)
        elif isinstance(value, str):
            d[key] = value.replace(origin, str(replacement))


if __name__ == '__main__':
    print transformSize((100, 100), ("20%", "50%"))
    print transformSize((100, 100), (0.2, 0.5))
    print transformSize((100, 100), (20, 50))
    print transformSize((100, 100), ("20%+16", "50%-2"))
