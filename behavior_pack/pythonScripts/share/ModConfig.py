# -*- coding: utf-8 -*-
# 这个文件保存了MOD中使用的一些变量，这样做的好处很多，建议参考

# 组件名称，规定需要使用自己的域名倒装+组件名称的方式
ModName = "com.domain.Sample"
# 组件版本，暂无实际作用（可能会显示）
ModVersion = "1.0"
# 调试开关
debug = True


# 用于定义自己的模块
# 使用方式见registerServerModules或registerClientModules
# 需要加入前缀，如ModName+"ModuleName"
class Module:
    pass


# 用于定义自己的事件，
# 需要加入前缀，如ModName+"EventName"
class Event:
    pass


# 用于注册自己模块使用的配置
# 使用方式见def registerData(system):
# 需要加入前缀，如ModName+"DataName"
class Data:
    pass


# 非公共存储键，一般用于存储玩家/方块的参数，需要与其他mod进行区分
# 需要加入前缀，如ModName+"KeyName"
class Key:
    pass


def registerServerModules(system):
    """
    在这里注册服务端module，单例模块不需要写register，使用注解注入,直接初始化即可
    如果需要共存，不用写name和version，需要覆盖时需要设定name和version，相同name的模块，高版本会覆盖低版本
    :param system:
    """

    # 如果是一般mod自己新建的模块，只需要与自己同系列保持兼容，那么只需要像这样注册，注意name需要唯一，所以最好加上mod前缀
    if debug:
        from pythonScripts.server.modules.CommandsModule import CommandsModule

        system.registerModule(
            CommandsModule(), name=ModName + "EXAMPLE_COMMAND_MODULE", version=0
        )


def registerClientModules(system):
    """
    在这里注册客户端module，单例模块不需要写register，使用注解注入,直接初始化即可
    如果需要共存，不用写name和version，需要覆盖时需要设定name和version，相同name的模块，高版本会覆盖低版本
    :param system:
    """

    # 如果是一般mod自己新建的模块，只需要与自己同系列保持兼容，那么只需要像这样注册，注意name需要唯一，所以最好加上mod前缀+
    if debug:
        from pythonScripts.client.modules.KeyPressModule import KeyPressModule

        system.registerModule(
            KeyPressModule(), name=ModName + "EXAMPLE_KEY_MODULE", version=0
        )


def registerData(system):
    """
    在这里加入数据
    :param system:
    """
    system.addData("EXAMPLE", {}, version=0)
