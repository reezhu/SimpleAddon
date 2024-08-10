# -*- coding: utf-8 -*-
# decompiled in 2024-04-04 03:09:27


class PlayerInventoryOpenScriptServerEvent(object):
    """某个客户端打开物品背包界面时触发"""

    def __init__(self):
        # 客户端对应的玩家entity的唯一ID
        self.playerId = None  # type: str
        # 是否是创造模式背包界面
        self.isCreative = None  # type: bool


class UrgeShipEvent(object):
    """玩家点击商城催促发货按钮时触发该事件"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str


class AchievementCompleteEvent(object):
    """玩家完成自定义成就时触发该事件"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str
        # 所属的页面的根节点成就id
        self.rootNodeId = None  # type: str
        # 达成的成就id
        self.achievementId = None  # type: str
        # 成就标题
        self.title = None  # type: str
        # 成就描述
        self.description = None  # type: str


class AddEntityServerEvent(object):
    """服务端侧创建新实体，或实体从存档加载时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str
        # 位置x
        self.posX = None  # type: float
        # 位置y
        self.posY = None  # type: float
        # 位置z
        self.posZ = None  # type: float
        # 实体维度
        self.dimensionId = None  # type: int
        # 是否为幼儿
        self.isBaby = None  # type: bool
        # 实体类型，即实体identifier
        self.engineTypeStr = None  # type: str
        # 物品identifier（仅当物品实体时存在该字段）
        self.itemName = None  # type: str
        # 物品附加值（仅当物品实体时存在该字段）
        self.auxValue = None  # type: int


class AddServerPlayerEvent(object):
    """触发时机：玩家加入时触发该事件。"""

    def __init__(self):
        # 玩家id
        self.id = None  # type: str
        # 是否是切服时进入服务器，仅用于Apollo。如果是True，则表示切服时加入服务器，若是False，则表示登录进入网络游戏
        self.isTransfer = None  # type: bool
        # 是否是断线重连，仅用于Apollo。如果是True，则表示本次登录是断线重连，若是False，则表示本次是正常登录或者转服
        self.isReconnect = None  # type: bool
        # 是否从手机端登录，仅用于Apollo。如果是True，则表示本次登录是从手机端登录，若是False，则表示本次登录是从PC端登录
        self.isPeUser = None  # type: bool
        # 切服传入参数，仅用于Apollo。调用【TransferToOtherServer】或【TransferToOtherServerById】传入的切服参数
        self.transferParam = None  # type: str
        # 仅用于Apollo，玩家的netease uid，玩家的唯一标识
        self.uid = None  # type: int
        # 仅用于Apollo，当前客户端连接的proxy服务器id
        self.proxyId = None  # type: int


class ChunkAcquireDiscardedServerEvent(object):
    """服务端区块即将被卸载时触发"""

    def __init__(self):
        # 区块所在维度
        self.dimension = None  # type: int
        # 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15]
        self.chunkPosX = None  # type: int
        # 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15]
        self.chunkPosZ = None  # type: int
        # 随区块卸载而从世界移除的实体id的列表。注意事件触发时已经无法获取到这些实体的信息，仅供脚本资源回收用。
        self.entities = None  # type: list(str)
        # 随区块卸载而从世界移除的自定义方块实体的坐标的列表，列表元素dict包含posX，posY，posZ三个int表示自定义方块实体的坐标。注意事件触发时已经无法获取到这些方块实体的信息，仅供脚本资源回收用。
        self.blockEntities = None  # type: list(dict)


class ChunkGeneratedServerEvent(object):
    """触发时机：区块创建完成时触发"""

    def __init__(self):
        # 该区块所在的维度
        self.dimension = None  # type: int
        # 该区块中的自定义方块实体列表，通常是由自定义特征生成的自定义方块，没有自定义方块实体时该值为None
        self.blockEntityData = None  # type: dict


class ChunkLoadedServerEvent(object):
    """触发时机：服务端区块加载完成时"""

    def __init__(self):
        # 区块所在维度
        self.dimension = None  # type: int
        # 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15]
        self.chunkPosX = None  # type: int
        # 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15]
        self.chunkPosZ = None  # type: int


class ClientLoadAddonsFinishServerEvent(object):
    """触发时机：客户端mod加载完成时，服务端触发此事件。服务器可以使用此事件，往客户端发送数据给其初始化。"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str


class CommandEvent(object):
    """玩家请求执行指令时触发"""

    def __init__(self):
        # 玩家ID
        self.entityId = None  # type: str
        # 指令字符串
        self.command = None  # type: str
        # 是否取消
        self.cancel = None  # type: bool


class DelServerPlayerEvent(object):
    """触发时机：删除玩家时触发该事件。"""

    def __init__(self):
        # 玩家id
        self.id = None  # type: str
        # 是否是切服时退出服务器，仅用于Apollo。如果是True，则表示切服时退出服务器；若是False，则表示退出网络游戏
        self.isTransfer = None  # type: bool
        # 玩家的netease uid，玩家的唯一标识
        self.uid = None  # type: int


class EntityRemoveEvent(object):
    """实体被删除时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str


class ExplosionServerEvent(object):
    """当发生爆炸时触发。"""

    def __init__(self):
        # 爆炸涉及到的方块坐标(x,y,z)，cancel是一个bool值
        self.blocks = None  # type: list[[x,y,z,cancel],...]
        # 受伤实体id列表，当该爆炸创建者id为None时，victims也为None
        self.victims = None  # type: list
        # 爆炸创建者id
        self.sourceId = None  # type: str
        # 爆炸位置[x,y,z]
        self.explodePos = None  # type: list
        # 维度id
        self.dimensionId = None  # type: int


class LoadServerAddonScriptsAfter(object):
    """服务器加载完mod时触发"""

    def __init__(self):
        pass


class NewOnEntityAreaEvent(object):
    """触发时机：通过RegisterEntityAOIEvent注册过AOI事件后，当有实体进入或离开注册感应区域时触发该事件。"""

    def __init__(self):
        # 注册感应区域名称
        self.name = None  # type: str
        # 进入该感应区域的实体id列表
        self.enteredEntities = None  # type: list[str]
        # 离开该感应区域的实体id列表
        self.leftEntities = None  # type: list[str]


class OnCommandOutputServerEvent(object):
    """Command命令执行成功事件"""

    def __init__(self):
        # 命令名称
        self.command = None  # type: str
        # 命令返回的消息
        self.message = None  # type: str


class OnContainerFillLoottableServerEvent(object):
    """触发时机：随机奖励箱第一次打开根据loottable生成物品时"""

    def __init__(self):
        # 奖励箱子所读取的loottable的json路径
        self.loottable = None  # type: str
        # 打开奖励箱子的玩家的playerId
        self.playerId = None  # type: str
        # 掉落物品列表，每个元素为一个itemDict，格式可参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemList = None  # type: list
        # 默认为False，如果需要修改掉落列表需将该值设为True
        self.dirty = None  # type: bool


class OnLightningLevelChangeServerEvent(object):
    """打雷强度发生改变"""

    def __init__(self):
        # 改变前的打雷强度
        self.oldLevel = None  # type: float
        # 改变后的打雷强度
        self.newLevel = None  # type: float


class OnLocalLightningLevelChangeServerEvent(object):
    """独立维度天气打雷强度发生改变时触发"""

    def __init__(self):
        # 改变前的打雷强度
        self.oldLevel = None  # type: float
        # 改变后的打雷强度
        self.newLevel = None  # type: float
        # 独立天气维度id
        self.dimensionId = None  # type: int


class OnLocalRainLevelChangeServerEvent(object):
    """独立维度天气下雨强度发生改变时触发"""

    def __init__(self):
        # 改变前的下雨强度
        self.oldLevel = None  # type: float
        # 改变后的下雨强度
        self.newLevel = None  # type: float
        # 独立天气维度id
        self.dimensionId = None  # type: int


class OnRainLevelChangeServerEvent(object):
    """下雨强度发生改变"""

    def __init__(self):
        # 改变前的下雨强度
        self.oldLevel = None  # type: float
        # 改变后的下雨强度
        self.newLevel = None  # type: float


class OnScriptTickServer(object):
    """服务器tick时触发,1秒有30个tick"""

    def __init__(self):
        pass


class PlaceNeteaseStructureFeatureEvent(object):
    """触发时机：首次生成地形时，结构特征即将生成时服务端抛出该事件。"""

    def __init__(self):
        # 结构名称
        self.structureName = None  # type: str
        # 结构坐标最小方块所在的x坐标
        self.x = None  # type: int
        # 结构坐标最小方块所在的y坐标
        self.y = None  # type: int
        # 结构坐标最小方块所在的z坐标
        self.z = None  # type: int
        # 该feature所放置区块的生物群系类型
        self.biomeType = None  # type: int
        # 该feature所放置区块的生物群系名称
        self.biomeName = None  # type: str
        # 维度id
        self.dimensionId = None  # type: int
        # 设置为True时可阻止该结构的放置
        self.cancel = None  # type: bool


class PlayerIntendLeaveServerEvent(object):
    """触发时机：即将删除玩家时触发该事件，此时可以通过各种API获取玩家的当前状态。"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str


class PlayerJoinMessageEvent(object):
    """触发时机：准备显示“xxx加入游戏”的玩家登录提示文字时服务端抛出的事件。"""

    def __init__(self):
        # 玩家实体id
        self.id = None  # type: str
        # 玩家昵称
        self.name = None  # type: str
        # 是否显示提示文字，允许修改。True：不显示提示
        self.cancel = None  # type: bool
        # 玩家加入游戏的提示文字，允许修改
        self.message = None  # type: str


class PlayerLeftMessageServerEvent(object):
    """触发时机：准备显示“xxx离开游戏”的玩家离开提示文字时服务端抛出的事件。"""

    def __init__(self):
        # 玩家实体id
        self.id = None  # type: str
        # 玩家昵称
        self.name = None  # type: str
        # 是否显示提示文字，允许修改。True：不显示提示
        self.cancel = None  # type: bool
        # 玩家离开游戏的提示文字，允许修改
        self.message = None  # type: str


class ServerChatEvent(object):
    """玩家发送聊天信息时触发"""

    def __init__(self):
        # 玩家名称
        self.username = None  # type: str
        # 玩家id
        self.playerId = None  # type: str
        # 玩家发送的聊天消息内容
        self.message = None  # type: str
        # 是否取消这个聊天事件，若取消可以设置为True
        self.cancel = None  # type: bool
        # 是否把聊天消息发送给指定在线玩家，而不是广播给所有在线玩家，若只发送某些玩家可以设置为True
        self.bChatById = None  # type: bool
        # 是否禁言，仅apollo可用。true：被禁言，玩家聊天会提示“你已被管理员禁言”。
        self.bForbid = None  # type: bool
        # 接收聊天消息的玩家id列表，bChatById为True时生效
        self.toPlayerIds = None  # type: list(str)


class ServerPostBlockPatternEvent(object):
    """触发时机：用方块组合生成生物，生成生物之后触发该事件。"""

    def __init__(self):
        # 生成生物的id
        self.entityId = None  # type: str
        # 生成生物的名字，如"minecraft:pig"
        self.entityGenerated = None  # type: str
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int


class ServerPreBlockPatternEvent(object):
    """触发时机：用方块组合生成生物，在放置最后一个组成方块时触发该事件。"""

    def __init__(self):
        # 是否允许继续生成。若设为False，可阻止生成生物
        self.enable = None  # type: bool
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int
        # 即将生成生物的名字，如"minecraft:pig"
        self.entityWillBeGenerated = None  # type: str


class ServerSpawnMobEvent(object):
    """游戏内自动生成生物，以及使用api生成生物时触发"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 生成实体的命名空间
        self.identifier = None  # type: str
        # 生成实体的类型，参考[EntityType](../枚举值/EntityType.md)
        self.type = None  # type: int
        # 生成怪物是否是幼年怪
        self.baby = None  # type: bool
        # 生成实体坐标x
        self.x = None  # type: float
        # 生成实体坐标y
        self.y = None  # type: float
        # 生成实体坐标z
        self.z = None  # type: float
        # 生成实体的维度，默认值为0（0为主世界，1为地狱，2为末地）
        self.dimensionId = None  # type: int
        # 生成实体的命名空间，通过MOD API生成的生物在这个参数也能获取到真正的命名空间，而不是以custom开头的
        self.realIdentifier = None  # type: str
        # 是否取消生成该实体
        self.cancel = None  # type: bool


class ActorHurtServerEvent(object):
    """触发时机：生物（包括玩家）受伤时触发"""

    def __init__(self):
        # 生物Id
        self.entityId = None  # type: str
        # 伤害来源，详见Minecraft枚举值文档的[ActorDamageCause](../枚举值/ActorDamageCause.md)
        self.cause = None  # type: str
        # 伤害值（被伤害吸收后的值），不可修改
        self.damage = None  # type: int
        # 被伤害吸收效果吸收的伤害值
        self.absorbedDamage = None  # type: int


class ActuallyHurtServerEvent(object):
    """实体实际受到伤害时触发，相比于DamageEvent，该伤害为经过护甲及buff计算后，实际的扣血量"""

    def __init__(self):
        # 伤害源id
        self.srcId = None  # type: str
        # 投射物id
        self.projectileId = None  # type: str
        # 被伤害id
        self.entityId = None  # type: str
        # 伤害值（被伤害吸收后的值），允许修改，设置为0则此次造成的伤害为0
        self.damage = None  # type: int
        # 伤害来源，详见Minecraft枚举值文档的[ActorDamageCause](../枚举值/ActorDamageCause.md)
        self.cause = None  # type: str


class AddEffectServerEvent(object):
    """触发时机：实体获得状态效果时"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 实体获得状态效果的名字
        self.effectName = None  # type: str
        # 状态效果的持续时间，单位秒
        self.effectDuration = None  # type: int
        # 状态效果的放大倍数
        self.effectAmplifier = None  # type: int
        # 状态造成的伤害值（真实扣除生命值的量）。只有持续时间为0时有用
        self.damage = None  # type: int


class ChangeSwimStateServerEvent(object):
    """触发时机：实体开始或者结束游泳时"""

    def __init__(self):
        # 实体的唯一ID
        self.entityId = None  # type: str
        # 事件触发前，实体是否在游泳状态
        self.formState = None  # type: bool
        # 事件触发后，实体是否在游泳状态
        self.toState = None  # type: bool


class DamageEvent(object):
    """实体受到伤害时触发"""

    def __init__(self):
        # 伤害源id
        self.srcId = None  # type: str
        # 投射物id
        self.projectileId = None  # type: str
        # 被伤害id
        self.entityId = None  # type: str
        # 伤害值（被伤害吸收前的值），允许修改，设置为0则此次造成的伤害为0
        self.damage = None  # type: int
        # 伤害吸收生命值，详见[AttrType枚举](../枚举值/AttrType.md)的ABSORPTION
        self.absorption = None  # type: int
        # 伤害来源，详见Minecraft枚举值文档的[ActorDamageCause](../枚举值/ActorDamageCause.md)
        self.cause = None  # type: str
        # 是否击退被攻击者，允许修改，设置该值为False则不产生击退
        self.knock = None  # type: bool
        # 是否点燃被伤害者，允许修改，设置该值为True产生点燃效果，反之亦然
        self.ignite = None  # type: bool


class EntityChangeDimensionServerEvent(object):
    """实体维度改变时服务端抛出"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 维度改变前的维度
        self.fromDimensionId = None  # type: int
        # 维度改变后的维度
        self.toDimensionId = None  # type: int
        # 改变前的位置x
        self.fromX = None  # type: float
        # 改变前的位置Y
        self.fromY = None  # type: float
        # 改变前的位置Z
        self.fromZ = None  # type: float
        # 改变后的位置x
        self.toX = None  # type: float
        # 改变后的位置Y
        self.toY = None  # type: float
        # 改变后的位置Z
        self.toZ = None  # type: float


class EntityDefinitionsEventServerEvent(object):
    """触发时机：生物定义json文件中设置的event触发时同时触发。生物行为变更事件"""

    def __init__(self):
        # 生物id
        self.entityId = None  # type: str
        # 触发的事件名称
        self.eventName = None  # type: str


class EntityDieLoottableServerEvent(object):
    """触发时机：生物死亡掉落物品时"""

    def __init__(self):
        # 死亡实体的entityId
        self.dieEntityId = None  # type: str
        # 伤害来源的entityId
        self.attacker = None  # type: str
        # 掉落物品列表，每个元素为一个itemDict，格式可参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemList = None  # type: list(dict)
        # 默认为False，如果需要修改掉落列表需将该值设为True
        self.dirty = None  # type: bool


class EntityDroppedItemServerEvent(object):
    """触发时机：生物扔出物品时触发"""

    def __init__(self):
        # 生物Id
        self.entityId = None  # type: str
        # 扔出的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 物品实体Id
        self.itemEntityId = None  # type: str


class EntityEffectDamageServerEvent(object):
    """生物受到状态伤害/回复事件。"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 伤害值（伤害吸收后实际扣血量），负数表示生命回复量
        self.damage = None  # type: int
        # 状态类型，参考[AttributeBuffType](../枚举值/AttributeBuffType.md)
        self.attributeBuffType = None  # type: int
        # 状态持续时间，单位秒（s）
        self.duration = None  # type: float
        # 状态生命时间，单位秒（s）
        self.lifeTimer = None  # type: float
        # 是否为立即生效状态
        self.isInstantaneous = None  # type: bool


class EntityLoadScriptEvent(object):
    """数据库加载实体自定义数据时触发"""

    def __init__(self):
        # 该事件的参数为长度为2的list，而非dict，其中list的第一个元素为实体id
        self.args = None  # type: list


class EntityMotionStartServerEvent(object):
    """实体运动器开始事件。实体（包含玩家）添加运动器后，运动器开始运行时触发"""

    def __init__(self):
        # 运动器id
        self.motionId = None  # type: int
        # 实体id
        self.entityId = None  # type: str


class EntityMotionStopServerEvent(object):
    """实体运动器停止事件。实体（包含玩家）添加运动器并开始运行后，运动器自动停止时触发"""

    def __init__(self):
        # 运动器id
        self.motionId = None  # type: int
        # 实体id
        self.entityId = None  # type: str
        # 是否移除该运动器，设置为False则保留，默认为True，即运动器停止后自动移除，该参数设置只对非玩家实体有效
        self.remove = None  # type: bool


class EntityPickupItemServerEvent(object):
    """有minecraft:behavior.pickup_items行为的生物拾取物品时触发该事件，例如村民拾取面包、猪灵拾取金锭"""

    def __init__(self):
        # 生物Id
        self.entityId = None  # type: str
        # 拾取的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 物品给予者id（一般是玩家），如果不存在给予者的话，这里为空字符串
        self.secondaryActor = None  # type: str


class EntityStartRidingEvent(object):
    """当实体骑乘上另一个实体时触发"""

    def __init__(self):
        # 乘骑者实体id
        self.id = None  # type: str
        # 被乘骑者实体id
        self.rideId = None  # type: str


class EntityStopRidingEvent(object):
    """触发时机：当实体停止骑乘时"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str
        # 坐骑id
        self.rideId = None  # type: str
        # 是否下坐骑
        self.exitFromRider = None  # type: bool
        # 坐骑是否将要销毁
        self.entityIsBeingDestroyed = None  # type: bool
        # 是否换乘坐骑
        self.switchingRides = None  # type: bool
        # 设置为True可以取消（需要与客户端事件一同取消）
        self.cancel = None  # type: bool


class HealthChangeBeforeServerEvent(object):
    """生物生命值发生变化之前触发"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 变化前的生命值
        self.from_ = None  # type: float
        # 将要变化到的生命值，cancel设置为True时可以取消该变化，但是此参数不变
        self.to = None  # type: float
        # 是否通过SetAttrValue或SetAttrMaxValue调用产生的变化
        self.byScript = None  # type: bool
        # 是否取消该变化
        self.cancel = None  # type: bool

    def __getattr__(self, item):
        if item == "from_":
            return self.__dict__.get("from")
        else:
            return self.__dict__.get(item)


class HealthChangeServerEvent(object):
    """生物生命值发生变化时触发"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 变化前的生命值
        self.from_ = None  # type: float
        # 变化后的生命值
        self.to = None  # type: float
        # 是否通过SetAttrValue或SetAttrMaxValue调用产生的变化
        self.byScript = None  # type: bool

    def __getattr__(self, item):
        if item == "from_":
            return self.__dict__.get("from")
        else:
            return self.__dict__.get(item)


class MobDieEvent(object):
    """实体被玩家杀死时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str
        # 伤害来源id
        self.attacker = None  # type: str


class MobGriefingBlockServerEvent(object):
    """环境生物改变方块时触发，触发的时机与mobgriefing游戏规则影响的行为相同"""

    def __init__(self):
        # 是否允许触发，默认为False，若设为True，可阻止触发后续物理交互事件
        self.cancel = None  # type: bool
        # 方块x坐标
        self.blockX = None  # type: int
        # 方块y坐标
        self.blockY = None  # type: int
        # 方块z坐标
        self.blockZ = None  # type: int
        # 触发的entity的唯一ID
        self.entityId = None  # type: str
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 维度id
        self.dimensionId = None  # type: int


class OnFireHurtEvent(object):
    """生物受到火焰伤害时触发"""

    def __init__(self):
        # 受伤实体id
        self.victim = None  # type: str
        # 火焰创建者id
        self.src = None  # type: str
        # 着火时间，单位秒
        self.fireTime = None  # type: float
        # 是否取消此处火焰伤害
        self.cancel = None  # type: bool


class OnGroundServerEvent(object):
    """实体着地事件。实体，掉落的物品，点燃的TNT掉落地面时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str


class OnKnockBackServerEvent(object):
    """实体被击退时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str


class OnMobHitBlockServerEvent(object):
    """触发时机：通过OpenMobHitBlockDetection打开方块碰撞检测后，当生物（不包括玩家）碰撞到方块时触发该事件。"""

    def __init__(self):
        # 碰撞到方块的生物Id
        self.entityId = None  # type: str
        # 碰撞方块x坐标
        self.posX = None  # type: int
        # 碰撞方块y坐标
        self.posY = None  # type: int
        # 碰撞方块z坐标
        self.posZ = None  # type: int
        # 碰撞方块的identifier
        self.blockId = None  # type: str
        # 碰撞方块的附加值
        self.auxValue = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int


class RefreshEffectServerEvent(object):
    """触发时机：实体身上状态效果更新时触发，更新条件1、新增状态等级较高，更新状态等级及时间；2、新增状态等级不变，时间较长，更新状态持续时间"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 更新状态效果的名字
        self.effectName = None  # type: str
        # 更新后状态效果剩余持续时间，单位秒
        self.effectDuration = None  # type: int
        # 更新后的状态效果放大倍数
        self.effectAmplifier = None  # type: int
        # 状态造成的伤害值，如药水
        self.damage = None  # type: int


class RemoveEffectServerEvent(object):
    """触发时机：实体身上状态效果被移除时"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 被移除状态效果的名字
        self.effectName = None  # type: str
        # 被移除状态效果的剩余持续时间，单位秒
        self.effectDuration = None  # type: int
        # 被移除状态效果的放大倍数
        self.effectAmplifier = None  # type: int


class SpawnProjectileServerEvent(object):
    """触发时机：抛射物生成时触发"""

    def __init__(self):
        # 抛射物的实体id
        self.projectileId = None  # type: str
        # 抛射物的identifier
        self.projectileIdentifier = None  # type: str
        # 发射者的实体id，没有发射者时为-1
        self.spawnerId = None  # type: str


class StartRidingServerEvent(object):
    """触发时机：一个实体即将骑乘另外一个实体"""

    def __init__(self):
        # 是否允许触发，默认为False，若设为True，可阻止触发后续的实体交互事件
        self.cancel = None  # type: bool
        # 骑乘者的唯一ID
        self.actorId = None  # type: str
        # 被骑乘实体的唯一ID
        self.victimId = None  # type: str


class WillAddEffectServerEvent(object):
    """触发时机：实体即将获得状态效果前"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 实体获得状态效果的名字
        self.effectName = None  # type: str
        # 状态效果的持续时间，单位秒
        self.effectDuration = None  # type: int
        # 状态效果的放大倍数
        self.effectAmplifier = None  # type: int
        # 设置为True可以取消
        self.cancel = None  # type: bool
        # 状态将会造成的伤害值，如药水；需要注意，该值不一定是最终的伤害值，例如被伤害吸收效果扣除。只有持续时间为0时有用
        self.damage = None  # type: int


class WillTeleportToServerEvent(object):
    """实体即将传送或切换维度"""

    def __init__(self):
        # 是否允许触发，默认为False，若设为True，可阻止触发后续的传送
        self.cancel = None  # type: bool
        # 实体的唯一ID
        self.entityId = None  # type: str
        # 传送前所在的维度
        self.fromDimensionId = None  # type: int
        # 传送后的目标维度
        self.toDimensionId = None  # type: int
        # 传送前所在的x坐标
        self.fromX = None  # type: int
        # 传送前所在的y坐标
        self.fromY = None  # type: int
        # 传送前所在的z坐标
        self.fromZ = None  # type: int
        # 传送目标地点的x坐标
        self.toX = None  # type: int
        # 传送目标地点的y坐标
        self.toY = None  # type: int
        # 传送目标地点的z坐标
        self.toZ = None  # type: int
        # 传送理由，详情见MinecraftEnum.EntityTeleportCause
        self.cause = None  # type: str


class BlockDestroyByLiquidServerEvent(object):
    """触发时机：方块被水流破坏的事件"""

    def __init__(self):
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 流体方块id
        self.liquidName = None  # type: str
        # 方块id
        self.blockName = None  # type: str
        # 方块附加值
        self.auxValue = None  # type: int


class BlockLiquidStateChangeAfterServerEvent(object):
    """触发时机：方块转为含水或者脱离含水(流体)后触发"""

    def __init__(self):
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 方块附加值
        self.auxValue = None  # type: int
        # 方块维度
        self.dimension = None  # type: int
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 是否转为含水，true则转为含水，false则脱离含水
        self.turnLiquid = None  # type: bool


class BlockLiquidStateChangeServerEvent(object):
    """触发时机：方块转为含水或者脱离含水(流体)前触发"""

    def __init__(self):
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 方块附加值
        self.auxValue = None  # type: int
        # 方块维度
        self.dimension = None  # type: int
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 是否转为含水，true则转为含水，false则脱离含水
        self.turnLiquid = None  # type: bool


class BlockNeighborChangedServerEvent(object):
    """触发时机：自定义方块周围的方块发生变化时，需要配置netease:neighborchanged_sendto_script，详情请查阅《自定义农作物》文档"""

    def __init__(self):
        # 维度
        self.dimensionId = None  # type: int
        # 方块x坐标
        self.posX = None  # type: int
        # 方块y坐标
        self.posY = None  # type: int
        # 方块z坐标
        self.posZ = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 方块附加值
        self.auxValue = None  # type: int
        # 变化方块x坐标
        self.neighborPosX = None  # type: int
        # 变化方块y坐标
        self.neighborPosY = None  # type: int
        # 变化方块z坐标
        self.neighborPosZ = None  # type: int
        # 方块变化前的identifier，包含命名空间及名称
        self.fromBlockName = None  # type: str
        # 方块变化前附加值
        self.fromBlockAuxValue = None  # type: int
        # 方块变化后的identifier，包含命名空间及名称
        self.toBlockName = None  # type: str
        # 方块变化后附加值
        self.toAuxValue = None  # type: int


class BlockRandomTickServerEvent(object):
    """触发时机：自定义方块配置<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-random-tick">netease:random_tick</a>随机tick时"""

    def __init__(self):
        # 方块x坐标
        self.posX = None  # type: int
        # 方块y坐标
        self.posY = None  # type: int
        # 方块z坐标
        self.posZ = None  # type: int
        # 方块名称
        self.blockName = None  # type: str
        # 方块的identifier，包含命名空间及名称
        self.fullName = None  # type: str
        # 方块附加值
        self.auxValue = None  # type: int
        # 实体维度
        self.dimensionId = None  # type: int


class BlockRemoveServerEvent(object):
    """触发时机：监听该事件的方块在销毁时触发，可以通过[ListenOnBlockRemoveEvent](#listenonblockremoveevent)方法进行监听，或者通过json组件<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-listen-block-remove">netease:listen_block_remove</a>进行配置"""

    def __init__(self):
        # 方块位置x
        self.x = None  # type: int
        # 方块位置y
        self.y = None  # type: int
        # 方块位置z
        self.z = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.fullName = None  # type: str
        # 方块的附加值
        self.auxValue = None  # type: int
        # 该方块所在的维度
        self.dimension = None  # type: int


class BlockSnowStateChangeAfterServerEvent(object):
    """触发时机：方块转为含雪或者脱离含雪后触发"""

    def __init__(self):
        # 方块维度
        self.dimension = None  # type: int
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 是否转为含雪，true则转为含雪，false则脱离含雪
        self.turnSnow = None  # type: bool
        # 方块进入脱离含雪的原因，参考[SetBlockType](../枚举值/SetBlockType.md)
        self.setBlockType = None  # type: int


class BlockSnowStateChangeServerEvent(object):
    """触发时机：方块转为含雪或者脱离含雪前触发"""

    def __init__(self):
        # 方块维度
        self.dimension = None  # type: int
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 是否转为含雪，true则转为含雪，false则脱离含雪
        self.turnSnow = None  # type: bool
        # 方块进入脱离含雪的原因，参考[SetBlockType](../枚举值/SetBlockType.md)
        self.setBlockType = None  # type: int


class BlockStrengthChangedServerEvent(object):
    """触发时机：自定义机械元件方块红石信号量发生变化时触发"""

    def __init__(self):
        # 方块x坐标
        self.posX = None  # type: int
        # 方块y坐标
        self.posY = None  # type: int
        # 方块z坐标
        self.posZ = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 方块附加值
        self.auxValue = None  # type: int
        # 变化后的红石信号量
        self.newStrength = None  # type: int
        # 维度
        self.dimensionId = None  # type: int


class ChestBlockTryPairWithServerEvent(object):
    """触发时机：两个并排的小箱子方块准备组合为一个大箱子方块时"""

    def __init__(self):
        # 是否允许触发，默认为False，若设为True，可阻止小箱子组合成为一个大箱子
        self.cancel = None  # type: bool
        # 小箱子方块x坐标
        self.blockX = None  # type: int
        # 小箱子方块y坐标
        self.blockY = None  # type: int
        # 小箱子方块z坐标
        self.blockZ = None  # type: int
        # 将要与之组合的另外一个小箱子方块x坐标
        self.otherBlockX = None  # type: int
        # 将要与之组合的另外一个小箱子方块y坐标
        self.otherBlockY = None  # type: int
        # 将要与之组合的另外一个小箱子方块z坐标
        self.otherBlockZ = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int


class CommandBlockContainerOpenEvent(object):
    """触发时机：玩家点击命令方块，尝试打开命令方块的设置界面"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str
        # 是否以方块坐标的形式定位命令方块，当为True时下述的blockX/blockY/blockZ有意义，当为False时，下述的victimId有意义
        self.isBlock = None  # type: bool
        # 命令方块位置x，当isBlock为True时有效
        self.blockX = None  # type: int
        # 命令方块位置y，当isBlock为True时有效
        self.blockY = None  # type: int
        # 命令方块位置z，当isBlock为True时有效
        self.blockZ = None  # type: int
        # 命令方块对应的逻辑实体的唯一id，当isBlock为False时有效
        self.victimId = None  # type: str
        # 修改为True时，可以阻止玩家打开命令方块的设置界面
        self.cancel = None  # type: bool


class CommandBlockUpdateEvent(object):
    """触发时机：玩家尝试修改命令方块的内置命令时"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str
        # 玩家的uid
        self.playerUid = None  # type: int
        # 企图修改的命令方块中的命令内容字符串
        self.command = None  # type: str
        # 是否以方块坐标的形式定位命令方块，当为True时下述的blockX/blockY/blockZ有意义，当为False时，下述的victimId有意义
        self.isBlock = None  # type: bool
        # 命令方块位置x，当isBlock为True时有效
        self.blockX = None  # type: int
        # 命令方块位置y，当isBlock为True时有效
        self.blockY = None  # type: int
        # 命令方块位置z，当isBlock为True时有效
        self.blockZ = None  # type: int
        # 命令方块对应的逻辑实体的唯一id，当isBlock为False时有效
        self.victimId = None  # type: str
        # 修改为True时，可以阻止玩家修改命令方块的内置命令
        self.cancel = None  # type: bool


class DestroyBlockEvent(object):
    """触发时机：当方块已经被玩家破坏时触发该事件。"""

    def __init__(self):
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 方块被敲击的面向id，参考[Facing枚举](../枚举值/Facing.md)
        self.face = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.fullName = None  # type: str
        # 方块附加值
        self.auxData = None  # type: int
        # 破坏方块的玩家ID
        self.playerId = None  # type: str
        # 维度id
        self.dimensionId = None  # type: int


class DirtBlockToGrassBlockServerEvent(object):
    """触发时机：泥土方块变成草方块时触发"""

    def __init__(self):
        # 方块维度
        self.dimension = None  # type: int
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int


class EntityPlaceBlockAfterServerEvent(object):
    """触发时机：当生物成功放置方块后触发"""

    def __init__(self):
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.fullName = None  # type: str
        # 方块附加值
        self.auxData = None  # type: int
        # 试图放置方块的生物ID
        self.entityId = None  # type: str
        # 维度id
        self.dimensionId = None  # type: int
        # 点击方块的面，参考[Facing枚举](../枚举值/Facing.md)
        self.face = None  # type: int


class FallingBlockBreakServerEvent(object):
    """触发时机：当下落的方块实体被破坏时，服务端触发该事件"""

    def __init__(self):
        # 下落的方块实体id
        self.fallingBlockId = None  # type: str
        # 下落的方块实体位置x
        self.fallingBlockX = None  # type: float
        # 下落的方块实体位置y
        self.fallingBlockY = None  # type: float
        # 下落的方块实体位置z
        self.fallingBlockZ = None  # type: float
        # 重力方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 下落的方块实体持续下落了多少tick
        self.fallTickAmount = None  # type: int
        # 下落的方块实体维度id
        self.dimensionId = None  # type: int
        # 是否取消方块物品掉落，可以在脚本层中设置
        self.cancelDrop = None  # type: bool


class FallingBlockCauseDamageBeforeServerEvent(object):
    """触发时机：当下落的方块开始计算砸到实体的伤害时，服务端触发该事件"""

    def __init__(self):
        # 下落的方块实体id
        self.fallingBlockId = None  # type: str
        # 下落的方块实体位置x
        self.fallingBlockX = None  # type: float
        # 下落的方块实体位置y
        self.fallingBlockY = None  # type: float
        # 下落的方块实体位置z
        self.fallingBlockZ = None  # type: float
        # 重力方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 下落的方块实体维度id
        self.dimensionId = None  # type: int
        # 当前碰撞到的实体列表id，如果没有的话是None
        self.collidingEntitys = None  # type: list(str)
        # 下落的方块实体持续下落了多少tick
        self.fallTickAmount = None  # type: int
        # 下落的方块实体持续下落了多少距离
        self.fallDistance = None  # type: float
        # 是否计算对实体的伤害，引擎传来的值由json配置和伤害是否大于0决定，可在脚本层修改传回引擎
        self.isHarmful = None  # type: bool
        # 对实体的伤害，引擎传来的值距离和json配置决定，可在脚本层修改传回引擎
        self.fallDamage = None  # type: int


class FallingBlockReturnHeavyBlockServerEvent(object):
    """触发时机：当下落的方块实体变回普通重力方块时，服务端触发该事件"""

    def __init__(self):
        # 下落的方块实体id
        self.fallingBlockId = None  # type: int
        # 方块位置x
        self.blockX = None  # type: int
        # 方块位置y
        self.blockY = None  # type: int
        # 方块位置z
        self.blockZ = None  # type: int
        # 重力方块的identifier，包含命名空间及名称
        self.heavyBlockName = None  # type: str
        # 变回重力方块时，原本方块位置的identifier，包含命名空间及名称
        self.prevHereBlockName = None  # type: str
        # 下落的方块实体维度id
        self.dimensionId = None  # type: int
        # 下落的方块实体持续下落了多少tick
        self.fallTickAmount = None  # type: int


class FarmBlockToDirtBlockServerEvent(object):
    """触发时机：耕地退化为泥土时触发"""

    def __init__(self):
        # 方块维度
        self.dimension = None  # type: int
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 耕地退化为泥土的原因，参考[SetBlockType](../枚举值/SetBlockType.md)
        self.setBlockType = None  # type: int


class GrassBlockToDirtBlockServerEvent(object):
    """触发时机：草方块变成泥土方块时触发"""

    def __init__(self):
        # 方块维度
        self.dimension = None  # type: int
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int


class HeavyBlockStartFallingServerEvent(object):
    """触发时机：当重力方块变为下落的方块实体后，服务端触发该事件"""

    def __init__(self):
        # 下落的方块实体id
        self.fallingBlockId = None  # type: str
        # 方块位置x
        self.blockX = None  # type: int
        # 方块位置y
        self.blockY = None  # type: int
        # 方块位置z
        self.blockZ = None  # type: int
        # 重力方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 下落的方块实体维度id
        self.dimensionId = None  # type: int


class HopperTryPullInServerEvent(object):
    """触发时机：当漏斗上方连接容器后，容器往漏斗开始输入物品时触发，事件仅触发一次"""

    def __init__(self):
        # 漏斗位置x
        self.x = None  # type: int
        # 漏斗位置y
        self.y = None  # type: int
        # 漏斗位置z
        self.z = None  # type: int
        # 交互的容器位置x
        self.abovePosX = None  # type: int
        # 交互的容器位置y
        self.abovePosY = None  # type: int
        # 交互的容器位置z
        self.abovePosZ = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int
        # 是否允许容器往漏斗加东西(要关闭此交互，需先监听此事件再放置容器)
        self.canHopper = None  # type: bool


class HopperTryPullOutServerEvent(object):
    """触发时机：当漏斗以毗邻的方式连接容器时，即从旁边连接容器时，漏斗向容器开始输出物品时触发，事件仅触发一次"""

    def __init__(self):
        # 漏斗位置x
        self.x = None  # type: int
        # 漏斗位置y
        self.y = None  # type: int
        # 漏斗位置z
        self.z = None  # type: int
        # 交互的容器位置x
        self.attachedPosX = None  # type: int
        # 交互的容器位置y
        self.attachedPosY = None  # type: int
        # 交互的容器位置z
        self.attachedPosZ = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int
        # 是否允许漏斗往容器加东西(要关闭此交互，需先监听此事件再放置容器)
        self.canHopper = None  # type: bool


class OnAfterFallOnBlockServerEvent(object):
    """触发时机：当实体降落到方块后服务端触发，主要用于力的计算"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 实体位置x
        self.posX = None  # type: float
        # 实体位置y
        self.posY = None  # type: float
        # 实体位置z
        self.posZ = None  # type: float
        # 瞬时移动X方向的力
        self.motionX = None  # type: float
        # 瞬时移动Y方向的力
        self.motionY = None  # type: float
        # 瞬时移动Z方向的力
        self.motionZ = None  # type: float
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 是否按脚本层传值计算力
        self.calculate = None  # type: bool


class OnBeforeFallOnBlockServerEvent(object):
    """触发时机：当实体刚降落到方块上时服务端触发，主要用于伤害计算"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str
        # 方块位置x
        self.blockX = None  # type: int
        # 方块位置y
        self.blockY = None  # type: int
        # 方块位置z
        self.blockZ = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 实体下降距离，可在脚本层传给引擎
        self.fallDistance = None  # type: float
        # 是否取消引擎对实体下降伤害的计算
        self.cancel = None  # type: bool


class ServerBlockEntityTickEvent(object):
    """触发时机：自定义方块配置了netease:block_entity组件并设tick为true，方块在玩家的模拟距离（新建存档时可以设置，默认为4个区块）内，或者在tickingarea内的时候触发"""

    def __init__(self):
        # 该方块名称
        self.blockName = None  # type: str
        # 该方块所在的维度
        self.dimension = None  # type: int
        # 该方块的x坐标
        self.posX = None  # type: int
        # 该方块的y坐标
        self.posY = None  # type: int
        # 该方块的z坐标
        self.posZ = None  # type: int


class ServerBlockUseEvent(object):
    """触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时服务端抛出该事件（该事件tick执行，需要注意效率问题）。"""

    def __init__(self):
        # 玩家Id
        self.playerId = None  # type: str
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 方块附加值
        self.aux = None  # type: int
        # 设置为True可拦截与方块交互的逻辑。
        self.cancel = None  # type: bool
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int


class ServerEntityTryPlaceBlockEvent(object):
    """触发时机：当生物试图放置方块时触发该事件。"""

    def __init__(self):
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.fullName = None  # type: str
        # 方块附加值
        self.auxData = None  # type: int
        # 试图放置方块的生物ID
        self.entityId = None  # type: str
        # 维度id
        self.dimensionId = None  # type: int
        # 点击方块的面，参考[Facing枚举](../枚举值/Facing.md)
        self.face = None  # type: int
        # 默认为False，在脚本层设置为True就能取消该方块的放置
        self.cancel = None  # type: bool


class ServerPlaceBlockEntityEvent(object):
    """触发时机：手动放置或通过接口创建含自定义方块实体的方块时触发，此时可向该方块实体中存放数据"""

    def __init__(self):
        # 该方块名称
        self.blockName = None  # type: str
        # 该方块所在的维度
        self.dimension = None  # type: int
        # 该方块的x坐标
        self.posX = None  # type: int
        # 该方块的y坐标
        self.posY = None  # type: int
        # 该方块的z坐标
        self.posZ = None  # type: int


class ServerPlayerTryDestroyBlockEvent(object):
    """当玩家即将破坏方块时，服务端线程触发该事件。"""

    def __init__(self):
        # 方块x坐标
        self.x = None  # type: int
        # 方块y坐标
        self.y = None  # type: int
        # 方块z坐标
        self.z = None  # type: int
        # 方块被敲击的面向id，参考[Facing枚举](../枚举值/Facing.md)
        self.face = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.fullName = None  # type: str
        # 方块附加值
        self.auxData = None  # type: int
        # 试图破坏方块的玩家ID
        self.playerId = None  # type: str
        # 维度id
        self.dimensionId = None  # type: int
        # 默认为False，在脚本层设置为True就能取消该方块的破坏
        self.cancel = None  # type: bool
        # 是否生成掉落物，默认为True，在脚本层设置为False就能取消生成掉落物
        self.spawnResources = None  # type: bool


class ShearsDestoryBlockBeforeServerEvent(object):
    """触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在服务端线程触发该事件"""

    def __init__(self):
        # 方块位置x
        self.blockX = None  # type: int
        # 方块位置y
        self.blockY = None  # type: int
        # 方块位置z
        self.blockZ = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 方块附加值
        self.auxData = None  # type: int
        # 触发剪刀效果的掉落物identifier，包含命名空间及名称
        self.dropName = None  # type: str
        # 触发剪刀效果的掉落物数量
        self.dropCount = None  # type: int
        # 触发剪刀效果的玩家id
        self.playerId = None  # type: str
        # 玩家触发时的维度id
        self.dimensionId = None  # type: int
        # 是否取消剪刀效果
        self.cancelShears = None  # type: bool


class StartDestroyBlockServerEvent(object):
    """玩家开始挖方块时触发。创造模式下不触发。"""

    def __init__(self):
        # 方块的坐标
        self.pos = None  # type: tuple(float,float,float)
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 方块的附加值
        self.auxValue = None  # type: int
        # 玩家id
        self.playerId = None  # type: str
        # 维度id
        self.dimensionId = None  # type: int
        # 修改为True时，可阻止玩家进入挖方块的状态。需要与StartDestroyBlockClientEvent一起修改。
        self.cancel = None  # type: bool


class AttackAnimBeginServerEvent(object):
    """当攻击动作开始时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str


class AttackAnimEndServerEvent(object):
    """当攻击动作结束时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str


class JumpAnimBeginServerEvent(object):
    """当跳跃动作开始时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str


class WalkAnimBeginServerEvent(object):
    """当走路动作开始时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str


class WalkAnimEndServerEvent(object):
    """当走路动作结束时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str


class ActorAcquiredItemServerEvent(object):
    """触发时机：玩家获得物品时服务端抛出的事件（有些获取物品方式只会触发客户端事件，有些获取物品方式只会触发服务端事件，在使用时注意一点。）"""

    def __init__(self):
        # 获得物品玩家实体id
        self.actor = None  # type: str
        # 物品给予者玩家实体id，如果不存在给予者的话，这里为空字符串
        self.secondaryActor = None  # type: str
        # 获得的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 获得物品的方法，详见[ItemAcquisitionMethod枚举](../枚举值/ItemAcquisitionMethod.md)
        self.acquireMethod = None  # type: int


class ActorUseItemServerEvent(object):
    """触发时机：玩家使用物品生效之前服务端抛出的事件（比较特殊不走该事件的例子：1）喝牛奶；2）染料对有水的炼药锅使用；3）盔甲架装备盔甲）"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 使用物品的方法，详见[ItemUseMethodEnum枚举](../枚举值/ItemUseMethodEnum.md)
        self.useMethod = None  # type: int


class ContainerItemChangedServerEvent(object):
    """容器物品变化事件"""

    def __init__(self):
        # 容器坐标
        self.pos = None  # type: tuple(int,int,int)
        # 容器类型，类型含义见：[容器类型枚举](../枚举值/ContainerType.md)
        self.containerType = None  # type: int
        # 容器槽位
        self.slot = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int
        # 旧物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.oldItemDict = None  # type: dict
        # 新物品物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.newItemDict = None  # type: dict


class CraftItemOutputChangeServerEvent(object):
    """玩家从容器拿出生成物品时触发"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str
        # 生成的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 当前界面类型,类型含义见：[容器类型枚举](../枚举值/ContainerType.md)
        self.screenContainerType = None  # type: int
        # 是否取消生成物品
        self.cancel = None  # type: bool


class FurnaceBurnFinishedServerEvent(object):
    """服务端熔炉烧制触发事件。熔炉, 高炉，烟熏炉烧出物品时触发"""

    def __init__(self):
        # 维度id
        self.dimensionId = None  # type: int
        # 位置x
        self.posX = None  # type: float
        # 位置y
        self.posY = None  # type: float
        # 位置z
        self.posZ = None  # type: float
        # 物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当新物品为空时，此项属性为None
        self.itemDict = None  # type: dict


class InventoryItemChangedServerEvent(object):
    """玩家背包物品变化时服务端抛出的事件。"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str
        # 背包槽位
        self.slot = None  # type: int
        # 变化前槽位中的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.oldItemDict = None  # type: dict
        # 变化后槽位中的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.newItemDict = None  # type: dict


class ItemReleaseUsingServerEvent(object):
    """触发时机：释放正在使用的物品时"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str
        # 蓄力剩余时间(当物品缺少"minecraft:maxduration"组件时,蓄力剩余时间为负数)
        self.durationLeft = None  # type: float
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 最大蓄力时长
        self.maxUseDuration = None  # type: int
        # 设置为True可以取消，需要同时取消客户端事件[ItemReleaseUsingClientEvent](#itemreleaseusingclientevent)
        self.cancel = None  # type: bool


class ItemUseAfterServerEvent(object):
    """玩家在使用物品之后服务端抛出的事件。"""

    def __init__(self):
        # 玩家实体id
        self.entityId = None  # type: str
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict


class ItemUseOnAfterServerEvent(object):
    """玩家在对方块使用物品之后服务端抛出的事件。"""

    def __init__(self):
        # 玩家实体id
        self.entityId = None  # type: str
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 方块 x 坐标值
        self.x = None  # type: int
        # 方块 y 坐标值
        self.y = None  # type: int
        # 方块 z 坐标值
        self.z = None  # type: int
        # 点击方块的面，参考[Facing枚举](../枚举值/Facing.md)
        self.face = None  # type: int
        # 点击点的x比例位置
        self.clickX = None  # type: float
        # 点击点的y比例位置
        self.clickY = None  # type: float
        # 点击点的z比例位置
        self.clickZ = None  # type: float
        # 方块的identifier
        self.blockName = None  # type: str
        # 方块的附加值
        self.blockAuxValue = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int


class OnCarriedNewItemChangedServerEvent(object):
    """触发时机：玩家切换主手物品时触发该事件"""

    def __init__(self):
        # 旧物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当旧物品为空时，此项属性为None
        self.oldItemDict = None  # type: dict
        # 新物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当新物品为空时，此项属性为None
        self.newItemDict = None  # type: dict
        # 玩家 entityId
        self.playerId = None  # type: str


class OnItemPutInEnchantingModelServerEvent(object):
    """触发时机：玩家将可附魔物品放到附魔台上时"""

    def __init__(self):
        # 玩家id，参数类型为str
        self.playerId = None  # type: str
        # 玩家放入物品的EnchantSlotType
        self.slotType = None  # type: int
        # 附魔台选项
        self.options = None  # type: list
        # 传入True时，附魔台选项会被新传入的options覆盖
        self.change = None  # type: bool


class OnNewArmorExchangeServerEvent(object):
    """触发时机：玩家切换盔甲时触发该事件"""

    def __init__(self):
        # 槽位id
        self.slot = None  # type: int
        # 旧装备的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当旧物品为空时，此项属性为None
        self.oldArmorDict = None  # type: dict
        # 新装备的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当新物品为空时，此项属性为None
        self.newArmorDict = None  # type: dict
        # 玩家 entityId
        self.playerId = None  # type: str


class OnOffhandItemChangedServerEvent(object):
    """触发时机：玩家切换副手物品时触发该事件"""

    def __init__(self):
        # 旧物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当旧物品为空时，此项属性为None
        self.oldItemDict = None  # type: dict
        # 新物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当新物品为空时，此项属性为None
        self.newItemDict = None  # type: dict
        # 玩家 entityId
        self.playerId = None  # type: str


class OnPlayerActiveShieldServerEvent(object):
    """触发时机：玩家激活/取消激活盾牌触发的事件。包括玩家持盾进入潜行状态，以及在潜行状态切换盾牌（切换耐久度不同的相同盾牌不会触发）"""

    def __init__(self):
        # 玩家Id
        self.playerId = None  # type: str
        # True:尝试激活,False:尝试取消激活
        self.isActive = None  # type: bool
        # 盾牌物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 是否可以取消。如果玩家在潜行状态切换盾牌，则无法取消
        self.cancelable = None  # type: bool
        # 是否取消这次激活
        self.cancel = None  # type: bool


class OnPlayerBlockedByShieldAfterServerEvent(object):
    """触发时机：玩家使用盾牌抵挡伤害之后触发"""

    def __init__(self):
        # 玩家Id
        self.playerId = None  # type: str
        # 伤害来源实体Id，没有实体返回"-1"
        self.sourceId = None  # type: str
        # 盾牌物品字典<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 抵挡的伤害数值
        self.damage = None  # type: float


class OnPlayerBlockedByShieldBeforeServerEvent(object):
    """触发时机：玩家使用盾牌抵挡伤害之前触发"""

    def __init__(self):
        # 玩家Id
        self.playerId = None  # type: str
        # 伤害来源实体Id，没有实体返回"-1"
        self.sourceId = None  # type: str
        # 盾牌物品字典<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 抵挡的伤害数值
        self.damage = None  # type: float


class PlayerDropItemServerEvent(object):
    """触发时机：玩家丢弃物品时触发"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str
        # 物品entityId
        self.itemEntityId = None  # type: str


class ServerItemTryUseEvent(object):
    """玩家点击右键尝试使用物品时服务端抛出的事件。注：如果需要取消物品的使用需要同时在ClientItemTryUseEvent和ServerItemTryUseEvent中将cancel设置为True才能正确取消。"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 设为True可取消物品的使用
        self.cancel = None  # type: bool


class ServerItemUseOnEvent(object):
    """玩家在对方块使用物品之前服务端抛出的事件。注：如果需要取消物品的使用需要同时在ClientItemUseOnEvent和ServerItemUseOnEvent中将ret设置为True才能正确取消。"""

    def __init__(self):
        # 玩家实体id
        self.entityId = None  # type: str
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 方块 x 坐标值
        self.x = None  # type: int
        # 方块 y 坐标值
        self.y = None  # type: int
        # 方块 z 坐标值
        self.z = None  # type: int
        # 方块的identifier
        self.blockName = None  # type: str
        # 方块的附加值
        self.blockAuxValue = None  # type: int
        # 点击方块的面，参考[Facing枚举](../枚举值/Facing.md)
        self.face = None  # type: int
        # 维度id
        self.dimensionId = None  # type: int
        # 点击点的x比例位置
        self.clickX = None  # type: float
        # 点击点的y比例位置
        self.clickY = None  # type: float
        # 点击点的z比例位置
        self.clickZ = None  # type: float
        # 设为True可取消物品的使用
        self.ret = None  # type: bool


class ServerPlayerTryTouchEvent(object):
    """玩家即将捡起物品时触发"""

    def __init__(self):
        # 玩家Id
        self.playerId = None  # type: str
        # 物品实体的Id
        self.entityId = None  # type: str
        # 触碰的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 设置为True时将取消本次拾取
        self.cancel = None  # type: bool
        # 取消拾取后重新设置该物品的拾取cd，小于15帧将视作15帧，大于等于97813帧将视作无法拾取
        self.pickupDelay = None  # type: int


class ShearsUseToBlockBeforeServerEvent(object):
    """触发时机：实体手持剪刀对方块使用时，有剪刀特殊效果的方块会在服务端线程触发该事件"""

    def __init__(self):
        # 方块位置x
        self.blockX = None  # type: int
        # 方块位置y
        self.blockY = None  # type: int
        # 方块位置z
        self.blockZ = None  # type: int
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str
        # 方块附加值
        self.auxData = None  # type: int
        # 触发剪刀效果的掉落物identifier，包含命名空间及名称
        self.dropName = None  # type: str
        # 触发剪刀效果的掉落物数量
        self.dropCount = None  # type: int
        # 触发剪刀效果的实体id，目前仅玩家会触发
        self.entityId = None  # type: str
        # 玩家触发时的维度id
        self.dimensionId = None  # type: int
        # 是否取消剪刀效果
        self.cancelShears = None  # type: bool


class UIContainerItemChangedServerEvent(object):
    """合成容器物品发生变化时触发"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str
        # 容器槽位，含义见：[容器类型枚举](../枚举值/PlayerUISlot.md)
        self.slot = None  # type: int
        # 旧物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.oldItemDict = None  # type: dict
        # 生成的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.newItemDict = None  # type: dict


class AddExpEvent(object):
    """触发时机：当玩家增加经验时触发该事件。"""

    def __init__(self):
        # 玩家id
        self.id = None  # type: str
        # 增加的经验值
        self.addExp = None  # type: int


class AddLevelEvent(object):
    """触发时机：当玩家升级时触发该事件。"""

    def __init__(self):
        # 玩家id
        self.id = None  # type: str
        # 增加的等级值
        self.addLevel = None  # type: int
        # 新的等级
        self.newLevel = None  # type: int


class ChangeLevelUpCostServerEvent(object):
    """触发时机：获取玩家下一个等级升级经验时，用于重载玩家的升级经验，每个等级在重置之前都只会触发一次"""

    def __init__(self):
        # 玩家当前等级
        self.level = None  # type: int
        # 当前等级升级到下个等级需要的经验值，当设置升级经验小于1时会被强制调整到1
        self.levelUpCostExp = None  # type: int
        # 设置为True，重载玩家升级经验才会生效
        self.changed = None  # type: bool


class DimensionChangeFinishServerEvent(object):
    """玩家维度改变完成后服务端抛出"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str
        # 维度改变前的维度
        self.fromDimensionId = None  # type: int
        # 维度改变后的维度
        self.toDimensionId = None  # type: int
        # 改变后的位置x,y,z,其中y值为脚底加上角色的身高值
        self.toPos = None  # type: tuple(float,float,float)


class DimensionChangeServerEvent(object):
    """玩家维度改变时服务端抛出"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str
        # 维度改变前的维度
        self.fromDimensionId = None  # type: int
        # 维度改变后的维度
        self.toDimensionId = None  # type: int
        # 改变前的位置x
        self.fromX = None  # type: float
        # 改变前的位置Y
        self.fromY = None  # type: float
        # 改变前的位置Z
        self.fromZ = None  # type: float
        # 改变后的位置x
        self.toX = None  # type: float
        # 改变后的位置Y
        self.toY = None  # type: float
        # 改变后的位置Z
        self.toZ = None  # type: float


class ExtinguishFireServerEvent(object):
    """玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。"""

    def __init__(self):
        # 火焰方块的坐标
        self.pos = None  # type: tuple(float,float,float)
        # 玩家id
        self.playerId = None  # type: str
        # 修改为True时，可阻止玩家扑灭火焰。需要与ExtinguishFireClientEvent一起修改。
        self.cancel = None  # type: bool


class GameTypeChangedServerEvent(object):
    """个人游戏模式发生变化时服务端触发。"""

    def __init__(self):
        # 玩家Id，[SetDefaultGameType](../接口/世界/游戏规则.md#SetDefaultGameType)接口改变游戏模式时该参数为空字符串
        self.playerId = None  # type: str
        # 切换前的游戏模式
        self.oldGameType = None  # type: int
        # 切换后的游戏模式
        self.newGameType = None  # type: int


class PlayerAttackEntityEvent(object):
    """触发时机：当玩家攻击时触发该事件。"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str
        # 受击者id
        self.victimId = None  # type: str
        # 伤害值：引擎传过来的值是0 允许脚本层修改为其他数
        self.damage = None  # type: int
        # 脚本是否设置伤害值：1表示是；0 表示否
        self.isValid = None  # type: int
        # 是否取消该次攻击，默认不取消
        self.cancel = None  # type: bool
        # 是否支持击退效果，默认支持，当不支持时将屏蔽武器击退附魔效果
        self.isKnockBack = None  # type: bool


class PlayerDieEvent(object):
    """触发时机：当玩家死亡时触发该事件。"""

    def __init__(self):
        # 玩家id
        self.id = None  # type: str
        # 伤害来源id
        self.attacker = None  # type: str


class PlayerDoInteractServerEvent(object):
    """玩家与有minecraft:interact组件的生物交互时触发该事件，例如玩家手持空桶对牛挤奶、玩家手持打火石点燃苦力怕"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str
        # 交互时使用物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 交互的生物entityId
        self.interactEntityId = None  # type: str


class PlayerEatFoodServerEvent(object):
    """触发时机：玩家吃下食物时触发"""

    def __init__(self):
        # 玩家Id
        self.playerId = None  # type: str
        # 食物物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 食物增加的饥饿值，可修改
        self.hunger = None  # type: int
        # 食物的营养价值，回复饱和度 = 食物增加的饥饿值 * 食物的营养价值 * 2，饱和度最大不超过当前饥饿值，可修改
        self.nutrition = None  # type: float


class PlayerHurtEvent(object):
    """触发时机：当玩家受伤害前触发该事件。"""

    def __init__(self):
        # 受击玩家id
        self.id = None  # type: str
        # 伤害来源实体id，若没有实体攻击，例如高空坠落，id为-1
        self.attacker = None  # type: str


class PlayerInteractServerEvent(object):
    """触发时机：玩家可以与实体交互时。如果是鼠标控制模式，则当准心对着实体时触发。如果是触屏模式，则触发时机与屏幕下方的交互按钮显示的时机相同。玩家真正与实体发生交互的事件见[PlayerDoInteractServerEvent](#playerdointeractserverevent)"""

    def __init__(self):
        # 是否取消触发，默认为False，若设为True，可阻止触发后续的实体交互事件
        self.cancel = None  # type: bool
        # 主动与实体互动的玩家的唯一ID
        self.playerId = None  # type: str
        # 当前玩家手持物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict
        # 被动的实体的唯一ID
        self.victimId = None  # type: str


class PlayerRespawnEvent(object):
    """触发时机：玩家复活时触发该事件。"""

    def __init__(self):
        # 玩家id
        self.id = None  # type: str


class PlayerRespawnFinishServerEvent(object):
    """触发时机：玩家复活完毕时触发"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str


class PlayerSleepServerEvent(object):
    """玩家使用床睡觉成功"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str


class PlayerStopSleepServerEvent(object):
    """玩家停止睡觉"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str


class PlayerTeleportEvent(object):
    """触发时机：当玩家传送时触发该事件，如：玩家使用末影珍珠或tp指令时。"""

    def __init__(self):
        # 玩家id
        self.id = None  # type: str


class PlayerTrySleepServerEvent(object):
    """玩家尝试使用床睡觉"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str
        # 是否取消（开发者传入）
        self.cancel = None  # type: bool


class ServerPlayerGetExperienceOrbEvent(object):
    """触发时机：玩家获取经验球时触发的事件"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str
        # 经验球经验值
        self.experienceValue = None  # type: int
        # 是否取消（开发者传入）
        self.cancel = None  # type: bool


class StoreBuySuccServerEvent(object):
    """触发时机:玩家游戏内购买商品时服务端抛出的事件"""

    def __init__(self):
        # 购买商品的玩家实体id
        self.playerId = None  # type: str


class lobbyGoodBuySucServerEvent(object):
    """玩家登录联机大厅服务器，或者联机大厅游戏内购买商品时触发。如果是玩家登录，触发时玩家客户端已经触发了UiInitFinished事件"""

    def __init__(self):
        # 购买商品的玩家实体id
        self.eid = None  # type: str
        # 玩家登录时为False，玩家购买了商品时为True
        self.buyItem = None  # type: bool
