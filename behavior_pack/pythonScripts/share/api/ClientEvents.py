# -*- coding: utf-8 -*- 
# decompiled in 2024-04-04 03:09:27 


class ClientChestCloseEvent(object):
    """关闭箱子界面时触发，包括小箱子，合并后大箱子和末影龙箱子"""

    def __init__(self):
        pass


class ClientChestOpenEvent(object):
    """打开箱子界面时触发，包括小箱子，合并后大箱子和末影龙箱子"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 箱子位置x值
        self.x = None  # type: int  
        # 箱子位置y值
        self.y = None  # type: int  
        # 箱子位置z值
        self.z = None  # type: int  


class ClientPlayerInventoryCloseEvent(object):
    """关闭物品背包界面时触发"""

    def __init__(self):
        pass


class ClientPlayerInventoryOpenEvent(object):
    """打开物品背包界面时触发"""

    def __init__(self):
        # 是否是创造模式背包界面
        self.isCreative = None  # type: bool  
        # 取消打开物品背包界面
        self.cancel = None  # type: bool  


class GridComponentSizeChangedClientEvent(object):
    """触发时机：UI grid组件里格子数目发生变化时触发"""

    def __init__(self):
        pass


class OnItemSlotButtonClickedEvent(object):
    """点击快捷栏和背包栏的物品槽时触发"""

    def __init__(self):
        # 点击的物品槽的编号
        self.slotIndex = None  # type: int  


class PlayerChatButtonClickClientEvent(object):
    """玩家点击聊天按钮或回车键触发呼出聊天窗口时客户端抛出的事件"""

    def __init__(self):
        pass


class PopScreenEvent(object):
    """screen移除触发"""

    def __init__(self):
        # UI名字
        self.screenName = None  # type: str  


class PushScreenEvent(object):
    """screen创建触发"""

    def __init__(self):
        # UI名字
        self.screenName = None  # type: str  


class UiInitFinished(object):
    """UI初始化框架完成,此时可以创建UI"""

    def __init__(self):
        pass


class AddEntityClientEvent(object):
    """客户端侧创建新实体时触发"""

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
        # 实体类型
        self.engineTypeStr = None  # type: str  
        # 物品identifier（仅当物品实体时存在该字段）
        self.itemName = None  # type: str  
        # 物品附加值（仅当物品实体时存在该字段）
        self.auxValue = None  # type: int  


class AddPlayerAOIClientEvent(object):
    """玩家加入游戏或者其余玩家进入当前玩家所在的区块时触发的AOI事件，替换AddPlayerEvent"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str  


class AddPlayerCreatedClientEvent(object):
    """玩家进入当前玩家所在的区块AOI后，玩家皮肤数据异步加载完成后触发的事件"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str  


class ChunkAcquireDiscardedClientEvent(object):
    """触发时机：客户端区块即将被卸载时"""

    def __init__(self):
        # 区块所在维度
        self.dimension = None  # type: int  
        # 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15]
        self.chunkPosX = None  # type: int  
        # 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15]
        self.chunkPosZ = None  # type: int  


class ChunkLoadedClientEvent(object):
    """触发时机：客户端区块加载完成时"""

    def __init__(self):
        # 区块所在维度
        self.dimension = None  # type: int  
        # 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15]
        self.chunkPosX = None  # type: int  
        # 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15]
        self.chunkPosZ = None  # type: int  


class LoadClientAddonScriptsAfter(object):
    """客户端加载mod完成事件"""

    def __init__(self):
        pass


class OnLocalPlayerStopLoading(object):
    """触发时机：玩家进入存档，出生点地形加载完成时触发。该事件触发时可以进行切换维度的操作。"""

    def __init__(self):
        # 加载完成的玩家id
        self.playerId = None  # type: str  


class OnScriptTickClient(object):
    """客户端tick事件,1秒30次"""

    def __init__(self):
        pass


class RemoveEntityClientEvent(object):
    """客户端侧实体被移除时触发"""

    def __init__(self):
        # 移除的实体id
        self.id = None  # type: str  


class RemovePlayerAOIClientEvent(object):
    """玩家离开当前玩家同一个区块时触发AOI事件"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str  


class UnLoadClientAddonScriptsBefore(object):
    """客户端卸载mod之前触发"""

    def __init__(self):
        pass


class ApproachEntityClientEvent(object):
    """玩家靠近生物时触发"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 靠近的生物实体id
        self.entityId = None  # type: str  


class EntityModelChangedClientEvent(object):
    """触发时机：实体模型切换时触发"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str  
        # 新的模型名字
        self.newModel = None  # type: str  
        # 原来的模型名字
        self.oldModel = None  # type: str  


class HealthChangeClientEvent(object):
    """生物生命值发生变化时触发"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str  
        # 变化前的生命值
        self.from_ = None  # type: float  
        # 变化后的生命值
        self.to = None  # type: float  

    def __getattr__(self, item):
        if item == 'from_':
            return self.__dict__.get('from')
        else:
            return self.__dict__.get(item)


class LeaveEntityClientEvent(object):
    """玩家远离生物时触发"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 远离的生物实体id
        self.entityId = None  # type: str  


class OnGroundClientEvent(object):
    """实体着地事件。玩家，沙子，铁砧，掉落的物品，点燃的TNT掉落地面时触发，其余实体着地不触发。"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str  


class StartRidingClientEvent(object):
    """触发时机：一个实体即将骑乘另外一个实体"""

    def __init__(self):
        # 骑乘者的唯一ID
        self.actorId = None  # type: str  
        # 被骑乘实体的唯一ID
        self.victimId = None  # type: str  


class ClientJumpButtonPressDownEvent(object):
    """跳跃按钮按下事件，返回值设置参数只对当次按下事件起作用"""

    def __init__(self):
        # 设置是否执行跳跃逻辑
        self.continueJump = None  # type: bool  


class ClientJumpButtonReleaseEvent(object):
    """跳跃按钮按下释放事件"""

    def __init__(self):
        pass


class GetEntityByCoordEvent(object):
    """玩家点击屏幕时触发，多个手指点在屏幕上时，只有第一个会触发。"""

    def __init__(self):
        pass


class GetEntityByCoordReleaseClientEvent(object):
    """玩家点击屏幕后松开时触发，多个手指点在屏幕上时，只有最后一个手指松开时触发。"""

    def __init__(self):
        pass


class HoldBeforeClientEvent(object):
    """玩家长按屏幕，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用RightClickBeforeClientEvent事件监听鼠标右键"""

    def __init__(self):
        # 设置为True可拦截原版的挖方块/使用物品/与实体交互响应
        self.cancel = None  # type: bool  


class LeftClickBeforeClientEvent(object):
    """玩家按下鼠标左键时触发。仅在pc的普通控制模式（即非F11模式）下触发。"""

    def __init__(self):
        # 设置为True可拦截原版的挖方块或攻击响应
        self.cancel = None  # type: bool  


class LeftClickReleaseClientEvent(object):
    """玩家松开鼠标左键时触发。仅在pc的普通控制模式（即非F11模式）下触发。"""

    def __init__(self):
        pass


class OnBackButtonReleaseClientEvent(object):
    """返回按钮（目前特指安卓系统导航中的返回按钮）松开时触发"""

    def __init__(self):
        pass


class OnClientPlayerStartMove(object):
    """移动按钮按下触发事件，在按住一个方向键的同时，去按另外一个方向键，不会触发第二次"""

    def __init__(self):
        pass


class OnClientPlayerStopMove(object):
    """移动按钮按下释放时触发事件，同时按下多个方向键，需要释放所有的方向键才会触发事件"""

    def __init__(self):
        pass


class OnKeyPressInGame(object):
    """按键按下或按键释放时触发"""

    def __init__(self):
        # 当前screenName
        self.screenName = None  # type: str  
        # 键码（注：这里的int型被转成了str型，比如"1"对应的就是枚举值文档中的1），详见[KeyBoardType枚举](../枚举值/KeyBoardType.md)
        self.key = None  # type: str
        # 是否按下，按下为1，弹起为0
        self.isDown = None  # type: str


class RightClickBeforeClientEvent(object):
    """玩家按下鼠标右键时触发。仅在pc下触发（普通控制模式及F11模式都会触发）。"""

    def __init__(self):
        # 设置为True可拦截原版的物品使用/实体交互响应
        self.cancel = None  # type: bool  


class RightClickReleaseClientEvent(object):
    """玩家松开鼠标右键时触发。仅在pc的普通控制模式（即非F11模式）下触发。在F11下右键，按下会触发RightClickBeforeClientEvent，松开时会触发TapOrHoldReleaseClientEvent"""

    def __init__(self):
        pass


class TapBeforeClientEvent(object):
    """玩家点击屏幕并松手，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用LeftClickBeforeClientEvent事件监听鼠标左键"""

    def __init__(self):
        # 设置为True可拦截原版的攻击或放置响应
        self.cancel = None  # type: bool  


class TapOrHoldReleaseClientEvent(object):
    """玩家点击屏幕后松手时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用LeftClickReleaseClientEvent与RightClickReleaseClientEvent事件监听鼠标松开"""

    def __init__(self):
        pass


class ClientBlockUseEvent(object):
    """触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时客户端抛出该事件（该事件tick执行，需要注意效率问题）。"""

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


class FallingBlockCauseDamageBeforeClientEvent(object):
    """触发时机：当下落的方块开始计算砸到实体的伤害时，客户端触发该事件"""

    def __init__(self):
        # 下落的方块实体id
        self.fallingBlockId = None  # type: int  
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
        # 当前碰撞到的实体列表id（客户端只能获取到玩家），如果没有的话是None
        self.collidingEntitys = None  # type: list(str)  
        # 下落的方块实体持续下落了多少tick
        self.fallTickAmount = None  # type: int  
        # 下落的方块实体持续下落了多少距离
        self.fallDistance = None  # type: float  
        # 客户端始终为false，因为客户端不会计算伤害值
        self.isHarmful = None  # type: bool  
        # 对实体的伤害
        self.fallDamage = None  # type: int  


class OnAfterFallOnBlockClientEvent(object):
    """触发时机：当实体降落到方块后客户端触发，主要用于力的计算"""

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


class OnEntityInsideBlockClientEvent(object):
    """触发时机：当实体碰撞盒所在区域有方块时，客户端持续触发"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str  
        # 实体所在维度id
        self.dimensionId = None  # type: int  
        # 实体移速X方向的减速比例
        self.slowdownMultiX = None  # type: float  
        # 实体移速Y方向的减速比例
        self.slowdownMultiY = None  # type: float  
        # 实体移速Z方向的减速比例
        self.slowdownMultiZ = None  # type: float  
        # 方块位置x
        self.blockX = None  # type: int  
        # 方块位置y
        self.blockY = None  # type: int  
        # 方块位置z
        self.blockZ = None  # type: int  
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str  
        # 可由脚本层回传True给引擎，阻止触发后续原版逻辑
        self.cancel = None  # type: bool  


class OnStandOnBlockClientEvent(object):
    """触发时机：当实体站立到方块上时客户端持续触发"""

    def __init__(self):
        # 实体id
        self.entityId = None  # type: str  
        # 实体所在维度id
        self.dimensionId = None  # type: int  
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
        # 方块位置x
        self.blockX = None  # type: int  
        # 方块位置y
        self.blockY = None  # type: int  
        # 方块位置z
        self.blockZ = None  # type: int  
        # 方块的identifier，包含命名空间及名称
        self.blockName = None  # type: str  
        # 可由脚本层回传True给引擎，阻止触发后续原版逻辑
        self.cancel = None  # type: bool  


class PlayerTryDestroyBlockClientEvent(object):
    """当玩家即将破坏方块时，客户端线程触发该事件。主要用于床，旗帜，箱子这些根据方块实体数据进行渲染的方块，一般情况下请使用ServerPlayerTryDestroyBlockEvent"""

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
        self.blockName = None  # type: str  
        # 方块附加值
        self.auxData = None  # type: int  
        # 试图破坏方块的玩家ID
        self.playerId = None  # type: str  
        # 默认为False，在脚本层设置为True就能取消该方块的破坏
        self.cancel = None  # type: bool  


class ShearsDestoryBlockBeforeClientEvent(object):
    """触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在客户端线程触发该事件"""

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


class StartDestroyBlockClientEvent(object):
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
        # 修改为True时，可阻止玩家进入挖方块的状态。需要与StartDestroyBlockServerEvent一起修改。
        self.cancel = None  # type: bool  


class StepOffBlockClientEvent(object):
    """触发时机：实体移动离开一个实心方块时触发"""

    def __init__(self):
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


class AttackAnimBeginClientEvent(object):
    """攻击动作开始时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str  


class AttackAnimEndClientEvent(object):
    """攻击动作结束时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str  


class WalkAnimBeginClientEvent(object):
    """走路动作开始时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str  


class WalkAnimEndClientEvent(object):
    """走路动作结束时触发"""

    def __init__(self):
        # 实体id
        self.id = None  # type: str  


class ActorAcquiredItemClientEvent(object):
    """触发时机：玩家获得物品时客户端抛出的事件（有些获取物品方式只会触发客户端事件，有些获取物品方式只会触发服务端事件，在使用时注意一点。）"""

    def __init__(self):
        # 获得物品玩家实体id
        self.actor = None  # type: str  
        # 物品给予者玩家实体id，如果不存在给予者的话，这里为空字符串
        self.secondaryActor = None  # type: str  
        # 获取到的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict  
        # 获得物品的方法，详见[ItemAcquisitionMethod](../枚举值/ItemAcquisitionMethod.md)
        self.acquireMethod = None  # type: int  


class ActorUseItemClientEvent(object):
    """触发时机：玩家使用物品时客户端抛出的事件（比较特殊不走该事件的例子：1）喝牛奶；2）染料对有水的炼药锅使用；3）盔甲架装备盔甲）"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict  
        # 使用物品的方法，详见[ItemUseMethodEnum枚举](../枚举值/ItemUseMethodEnum.md)
        self.useMethod = None  # type: int  


class AnvilCreateResultItemAfterClientEvent(object):
    """玩家点击铁砧合成得到的物品时抛出的事件。"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 合成后的物品显示名称
        self.itemShowName = None  # type: str  
        # 合成后的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict  
        # 合成前的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>（铁砧内第一个物品）
        self.oldItemDict = None  # type: dict  
        # 合成所使用材料的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>（铁砧内第二个物品）
        self.materialItemDict = None  # type: dict  


class ClientItemTryUseEvent(object):
    """玩家点击右键尝试使用物品时客户端抛出的事件，可以通过设置cancel为True取消使用物品。注：如果需要取消物品的使用需要同时在ClientItemTryUseEvent和ServerItemTryUseEvent中将cancel设置为True才能正确取消。"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str  
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict  
        # 取消使用物品
        self.cancel = None  # type: bool  


class ClientItemUseOnEvent(object):
    """玩家在对方块使用物品时客户端抛出的事件。注：如果需要取消物品的使用需要同时在ClientItemUseOnEvent和ServerItemUseOnEvent中将ret设置为True才能正确取消。"""

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
        # 点击点的x比例位置
        self.clickX = None  # type: float  
        # 点击点的y比例位置
        self.clickY = None  # type: float  
        # 点击点的z比例位置
        self.clickZ = None  # type: float  
        # 设为True可取消物品的使用
        self.ret = None  # type: bool  


class ClientShapedRecipeTriggeredEvent(object):
    """玩家合成物品时触发"""

    def __init__(self):
        # 配方id，对应配方json文件中的identifier字段
        self.recipeId = None  # type: str  


class GrindStoneRemovedEnchantClientEvent(object):
    """玩家点击砂轮合成得到的物品时抛出的事件"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 合成前的物品<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>（砂轮内第一个物品）
        self.oldItemDict = None  # type: dict  
        # 作为合成材料的物品<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>（砂轮内第二个物品）
        self.additionalItemDict = None  # type: dict  
        # 合成后的物品<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.newItemDict = None  # type: dict  
        # 本次合成返还的经验
        self.exp = None  # type: int  


class InventoryItemChangedClientEvent(object):
    """玩家背包物品变化时客户端抛出的事件。"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 背包槽位
        self.slot = None  # type: int  
        # 变化前槽位中的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.oldItemDict = None  # type: dict  
        # 变化后槽位中的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.newItemDict = None  # type: dict  


class ItemReleaseUsingClientEvent(object):
    """触发时机：释放正在使用的物品"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str  
        # 蓄力剩余时间(当物品缺少"minecraft:maxduration"组件时,蓄力剩余时间为负数)
        self.durationLeft = None  # type: float  
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict  
        # 最大蓄力时长
        self.maxUseDuration = None  # type: int  
        # 设置为True可以取消，需要同时取消服务端事件[ItemReleaseUsingServerEvent](#itemreleaseusingserverevent)
        self.cancel = None  # type: bool  


class OnCarriedNewItemChangedClientEvent(object):
    """手持物品发生变化时，触发该事件；数量改变不会通知"""

    def __init__(self):
        # 切换后物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict  


class PlayerTryDropItemClientEvent(object):
    """触发时机：玩家丢弃物品时触发"""

    def __init__(self):
        # 玩家id
        self.playerId = None  # type: str  
        # 物品dict
        self.itemDict = None  # type: dict  
        # 是否取消此次操作
        self.cancel = None  # type: bool  


class StartUsingItemClientEvent(object):
    """玩家使用物品（目前仅支持Bucket、Trident、RangedWeapon、Medicine、Food、Potion、Crossbow、ChemistryStick）时抛出"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict  


class StopUsingItemClientEvent(object):
    """玩家停止使用物品（目前仅支持Bucket、Trident、RangedWeapon、Medicine、Food、Potion、Crossbow、ChemistryStick）时抛出"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>
        self.itemDict = None  # type: dict  


class DimensionChangeClientEvent(object):
    """玩家维度改变时客户端抛出"""

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


class DimensionChangeFinishClientEvent(object):
    """玩家维度改变完成后客户端抛出"""

    def __init__(self):
        # 玩家实体id
        self.playerId = None  # type: str  
        # 维度改变前的维度
        self.fromDimensionId = None  # type: int  
        # 维度改变后的维度
        self.toDimensionId = None  # type: int  
        # 改变后的位置x,y,z,其中y值为脚底加上角色的身高值
        self.toPos = None  # type: tuple(float,float,float)  


class ExtinguishFireClientEvent(object):
    """玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。"""

    def __init__(self):
        # 火焰方块的坐标
        self.pos = None  # type: tuple(float,float,float)  
        # 玩家id
        self.playerId = None  # type: str  
        # 修改为True时，可阻止玩家扑灭火焰。需要与ExtinguishFireServerEvent一起修改。
        self.cancel = None  # type: bool  


class GameTypeChangedClientEvent(object):
    """个人游戏模式发生变化时客户端触发。"""

    def __init__(self):
        # 玩家Id
        self.playerId = None  # type: str  
        # 切换前的游戏模式
        self.oldGameType = None  # type: int  
        # 切换后的游戏模式
        self.newGameType = None  # type: int  


class OnPlayerHitBlockClientEvent(object):
    """触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。玩家着地时会触发OnGroundClientEvent，而不是该事件。客户端和服务端分别作碰撞检测，可能两个事件返回的结果略有差异。"""

    def __init__(self):
        # 碰撞到方块的玩家Id
        self.playerId = None  # type: str  
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


class OnMusicStopClientEvent(object):
    """音乐停止时，当玩家调用StopCustomMusic来停止自定义背景音乐时，会触发该事件"""

    def __init__(self):
        # 音乐名称
        self.musicName = None  # type: str  


class PlayMusicClientEvent(object):
    """播放背景音乐时触发"""

    def __init__(self):
        # 即资源包中sounds/music_definitions.json中的event_name，并且对应sounds/sound_definitions.json中的key
        self.name = None  # type: str  
        # 设为True可屏蔽该次音效播放
        self.cancel = None  # type: bool  


class PlaySoundClientEvent(object):
    """播放场景音效或UI音效时触发"""

    def __init__(self):
        # 即资源包中sounds/sound_definitions.json中的key
        self.name = None  # type: str  
        # 音效播放的位置。UI音效为(0,0,0)
        self.pos = None  # type: tuple(float,float,float)  
        # 音量，范围为0-1
        self.volume = None  # type: float  
        # 播放速度，正常速度为1
        self.pitch = None  # type: float  
        # 设为True可屏蔽该次音效播放
        self.cancel = None  # type: bool
