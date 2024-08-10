# -*- coding: utf-8 -*-
# @Author  : Ree
# 请勿修改此配置！！！！！！！
# 如需增加配置，可以写在ModConfig中，已提前导入各个模块，别名为config

ServerSystemName = "MasterServerServiceProvider"
ClientSystemName = "MasterClientServiceProvider"
ServiceDomain = "org.xjcraft.MasterSystem."


# 模块名
class Module:
    Achievement = ServiceDomain + "AchievementModule"
    Armor = ServiceDomain + "ArmorModule"
    Barrage = ServiceDomain + "BarrageModule"
    Broadcast = ServiceDomain + "BroadcastModule"
    Buff = ServiceDomain + "BuffModule"
    BossSummon = ServiceDomain + "BossSummonModule"
    BossSkillServer = ServiceDomain + "BossSkillServerModule"
    BossSkillClient = ServiceDomain + "BossSkillClientModule"
    Chest = ServiceDomain + "Chest"
    Confirm = ServiceDomain + "Confirm"
    DamageDisplay = ServiceDomain + "DamageDisplayModule"
    DecoratorModule = ServiceDomain + "DecoratorModule"
    DecoratorMainModule = ServiceDomain + "DecoratorMainModule"
    LootModule = ServiceDomain + "LootModule"
    DynamicUiModule = ServiceDomain + "DynamicUiModule"
    DoubleJump = ServiceDomain + "DoubleJumpModule"
    ElasticityProjectile = ServiceDomain + "ElasticityProjectileModule"
    EquipmentDisplay = ServiceDomain + "EquipmentDisplayModule"
    EquipmentInteract = ServiceDomain + "EquipmentInteractModule"
    FbxClient = ServiceDomain + "FbxClientCommonModule"
    FlyClient = ServiceDomain + "FlyClientModule"
    HealthBar = ServiceDomain + "HealthBarModule"
    InventorySelector = ServiceDomain + "InventorySelectorModule"
    ItemDispatch = ServiceDomain + "ItemDispatchModule"
    PlaceHolder = ServiceDomain + "PlaceHolderModule"
    Plant = ServiceDomain + "PlanetModule"
    Portal = ServiceDomain + "PortalModule"
    Projectile = ServiceDomain + "ProjectileModule"
    RaffleBox = ServiceDomain + "RaffleBoxModule"
    Rpc = ServiceDomain + "RpcModule"
    Scheduler = ServiceDomain + "SchedulerModule"
    SFXClient = ServiceDomain + "SFXClientModule"
    Skill = ServiceDomain + "SkillModule"
    Slab = ServiceDomain + "SlabModule"
    Sound = ServiceDomain + "SoundModule"
    Stand = ServiceDomain + "StandModule"
    StandAnimation = ServiceDomain + "StandAnimationModule"
    Status = ServiceDomain + "StatusModule"
    Sync = ServiceDomain + "SyncModule"
    TextFloat = ServiceDomain + "ClientTextFloatModule"
    Tool = ServiceDomain + "ToolModule"
    Weapon = ServiceDomain + "WeaponModule"
    ProjectileHit = ServiceDomain + "ProjectileHitModule"


# 单例模块的数据
class Data:
    # 盔甲攻击特效
    ARMOR_EFFECT = "armor:Effect"
    # 盔甲穿戴的buff
    ARMOR_BUFF = "armor:Buff"
    # 盔甲穿戴时的粒子
    ARMOR_PARTICLE = "armor:Particle"
    # 盔甲可以免疫的buff
    ARMOR_IMMUNITY_BUFF = "armor:immunityBuff"
    # 盔甲可以免疫的伤换
    ARMOR_IMMUNITY_DAMAGE = "armor:immunityDamage"
    # 武器吸血
    ARMOR_SUCK_BLOOD = "armor:suckBlood"
    # 武器伤害加成
    ARMOR_DAMAGE_BOOST = "armor:damageBoost"
    # 盔甲反伤
    ARMOR_THRONE = "armor:throne"
    # 盔甲属性修改
    ARMOR_ATTR = "armor:attrChange"
    # 武器必杀
    ARMOR_KILL = "armor:kill"
    # 重置别的生物的攻击目标
    ARMOR_RESET_TARGET = "armor:reset_target"
    # 受到伤害执行指令
    ARMOR_SET_COMMAND = "armor:set_command"
    # 减少伤害
    ARMOR_REDUCE_DAMAGE = "armor:reduce_damage"
    # 增加耐久
    ARMOR_ADD_DURABILITY = "armor:add_durability"
    # 怪物死后掉落
    BLOCK_LOOT = "blockloot:drop"
    # 任意怪物死后掉落
    BLOCK_LOOT_GLOBAL = "blockloot:drop_global"
    # 用于
    BROADCAST_QUERY = "boarcast:query"
    # buff结合配置
    BUFF_COMBO = "buff:combo"
    # buff优先度配置
    BUFF_PRIORITY = "buff:priority"
    # 奖励箱中增加物品
    CHEST_LOOT = "chest:loot"
    # 饰品配置
    DECORATOR = "decorator:status"
    # 精英怪配置
    ELITEBOSS = "elite:boss"
    # 显示血条的配置
    HEALTHBAR = "health:bar"
    # 熔炼配方，格式name:name或者(name,aux):(name,aux)
    RECIPE_SMELTING = "recipe:smelting"
    # 自定义弓
    WEAPON_BOW = "weapon:custom_bow"
    WEAPON_CUSTOM = "customWeaponData"
    # 怪物死后掉落
    MOB_LOOT = "mobloot:drop"
    # 任意怪物死后掉落
    MOB_LOOT_GLOBAL = "mobloot:drop_global"
    PLACEHOLDER = "placeholder:processer"
    # 植物超范围检测
    PLANT_EXPAND = "plant:expand"
    # 是否可被骨粉催熟
    PLANT_GROW = "plant:grow"
    # 是否可被骨粉扩散（类似花
    PLANT_SPREAD = "plant:spread"
    # 树类植物生长功能
    PLANT_TREE = "plant:tree"
    # 方块产生掉落物的功能
    PLANT_CORP = "plant:corp"
    # 草方块破坏后产生掉落物的功能
    PLANT_DROP = "plant:drop"
    # 破坏非草方块后产生掉落物的功能，根据方块id索引，用于掉无法配置loottable的部分
    PLANT_DROP_BLOCK = "plant:drop_block"
    # 植物种植的方块被破坏掉落
    PLANT_DEPEND = "plant:depend"
    # 传送门定义
    PORTAL_DEFINE = "portal:define"
    # 传送门触发
    PORTAL_ACTIVE = "portal:active"
    # 抽奖池UI
    RAFFLE_UI = "raffle:ui"
    # 总抽奖池
    RAFFLE_POOLS = "raffle:pools"
    # 抽奖池内物品
    RAFFLE_POOL_ITEMS = "raffle:items"
    # 彈性拋射物
    Elasticity_Projectile = "elasticity:projectile"
    # 彈性拋射物特效
    Elasticity_Projectile_Particle = "elasticity:projectileParticle"
    # 自动发放物品
    ITEM_DISPATCH = "dispatch:item"
    # 物品变实体
    ITEM_PLACE_ENTITY = "dispatch:place_entity"
    # 自动生成lore
    ITEM_Lore_Replace = "dispatch:lore_replace"
    # 物品自动生成操作键
    ITEM_BUTTON = "item:button"
    # 上半砖
    SLAB_UPPER = "slab:upper"
    # 技能配置
    SKILL_STAGES = "skill:stages"
    # 攻击音效
    SOUND_ATTACK = "sound:attack"
    # 数值系统
    STATUS_DETAIL = "status:detail"
    # 快速挖掘
    TOOL_FAST = "tool:fastbreak"
    # 连锁挖掘
    TOOL_CHAIN = "tool:chain"
    # 爆炸挖掘
    TOOL_EXPLODE = "tool:explode"
    # 范围耕地
    TOOL_AREA_FARM = "tool:farm"
    # 用于保存位置的数据前缀
    UI_POSITION_PREFIX = "UiPosition:"
    # 動態UI設定
    DYNAMIC_UI = "dynamic:ui"
    # 拋射物命中後效果 ui
    PROJECTILE_ANIMATION_UI = "projectile_animation:ui"


# 用于标记玩家的tag(计分板术语)
class Tag:
    # 用于免疫kill指令
    IMMUNITY_KILL = "xjcraft:immunity_kill"


# 公共事件
class Event:
    # 解锁成就
    AchieveUnlockEvent = ServiceDomain + "AchieveUnlockEvent"
    # 奖励成就
    AchieveRewardEvent = ServiceDomain + "AchieveRewardEvent"
    # 生物技能
    BossSkillEvent = ServiceDomain + "BossSkillEvent"
    # 转发事件
    RpcForwardEvent = ServiceDomain + "RpcForwardEvent"
    # 查询玩家信息
    RpcPlayerInfoGetEvent = ServiceDomain + "RpcPlayerInfoGetEvent"
    # 设置玩家信息
    RpcPlayerInfoSetEvent = ServiceDomain + "RpcPlayerInfoSetEvent"
    # 查询玩家信息回复
    RpcPlayerInfoAnswerEvent = ServiceDomain + "RpcPlayerInfoAnswerEvent"
    # 删除玩家信息
    RpcPlayerInfoDelEvent = ServiceDomain + "RpcPlayerInfoDelEvent"
    # 获取方块信息
    RpcBlockInfoGetEvent = ServiceDomain + "RpcBlockInfoGetEvent"
    # 获取方块信息回复
    RpcBlockInfoAnswerEvent = ServiceDomain + "RpcBlockInfoAnswerEvent"
    # 远程调用查询
    RpcFunctionEvent = ServiceDomain + "RpcFunctionEvent"
    # 调整饰品镜头
    SetCamera = ServiceDomain + "SetCamera"
    # 飘文字
    ClientTextEvent = ServiceDomain + "ClientTextEvent"
    # 弹出确认窗口
    ConfirmPopEvent = ServiceDomain + "ConfirmPopEvent"
    # 创建弹幕
    CreateBarrageEvent = ServiceDomain + "CreateBarrageEvent"
    # 交换装饰品
    DecoratorExchangeEvent = ServiceDomain + "DecoratorExchangeEvent"
    # 广播饰品同步
    DecoratorSyncEvent = ServiceDomain + "DecoratorSyncEvent"
    # 广播饰品更新
    DecoratorUpdateEvent = ServiceDomain + "DecoratorUpdateEvent"
    # 自定义装备穿上
    EquipCustomWeaponEvent = ServiceDomain + "CustomWeaponEquipped"
    # 减少装备冷却时间
    EquipmentCooldownReduceEvent = ServiceDomain + "EquipCustomWeapon"
    # 通用交互按钮的服务端交互
    EquipmentDynamicButtonStatusEvent = ServiceDomain + "EquipmentDynamicButtonStatus"
    # 装备的状态更新
    EquipmentSwitchStatusEvent = ServiceDomain + "EquipmentSwitchStatusEvent"
    # 通知服务端进行了飞行（内部功能）
    FlyEnabledEvent = ServiceDomain + "FlyEnabledEvent"
    # 转发原版事件
    ForwardOnCarriedNewItemChangedServerEvent = (
        ServiceDomain + "F:OnCarriedNewItemChangedServerEvent"
    )
    ForwardOnNewArmorExchangeServerEvent = (
        ServiceDomain + "F:OnNewArmorExchangeServerEvent"
    )
    # 冻结玩家操作
    LockPlayerOperationEvent = ServiceDomain + "LockPlayerOperationEvent"
    # 播放粒子
    ParticleEvent = ServiceDomain + "ParticleEvent"
    # 玩家收到伤害
    PlayerActuallyHurtClientEvent = ServiceDomain + "ActuallyHurtClientEvent"
    # 玩家加载完成
    PlayerLoadedEvent = ServiceDomain + "PlayerLoadedEvent"
    # 玩家退出(自定义武器用)
    PlayerLeaveEvent = ServiceDomain + "PlayerLeaveEvent"
    # 玩家加入（通用）
    PlayerJoinEvent = ServiceDomain + "PlayerJoinServerEvent"
    # 玩家退出（通用）
    PlayerQuitEvent = ServiceDomain + "PlayerQuitServerEvent"
    # 玩家技能按钮通知
    PlayerSkillButtonNotifyEvent = ServiceDomain + "PlayerSkillButtonNotifyEvent"
    # 查询状态
    PlayerStatusQueryEvent = "PlayerStatusQueryEvent"
    # 回复状态
    PlayerStatusAnswerEvent = "PlayerStatusAnswerEvent"
    # 释放技能
    PlaySkillEvent = ServiceDomain + "PlaySkillEvent"
    # 技能释放完成
    PlaySkillEndEvent = ServiceDomain + "PlaySkillEndEvent"
    # 显示抽奖箱UI
    RaffleBoxUiEvent = ServiceDomain + "RaffleBoxUiEvent"
    # 播放序列帧
    SFXEvent = ServiceDomain + "SFXEvent"
    # 播放編輯器序列帧
    SFXEditorEvent = ServiceDomain + "SFXEditorEvent"
    # 变身模块重新渲染时触发，仅广播本地客户端
    StandRenderEvent = ServiceDomain + "StandRenderEvent"
    # 会在客户端与服务端同步更新的事件，可以用于监听操作
    # 注意服务端监听服务端事件，客户端监听客户端事件
    SyncInfoChangeEvent = ServiceDomain + "SyncInfoChangeEvent"
    # 同步数据功能，内部使用
    SyncInfoInnerEvent = ServiceDomain + "SyncInfoInnerEvent"
    # ui刷新时触发，一般是客户端帧率，仅广播本地客户端
    DynamicTickEvent = ServiceDomain + "DynamicTickEvent"
    # 设置飞行
    UpdateFlyEvent = ServiceDomain + "UpdateFlyEvent"
    # 设置双跳
    UpdateDoubleJumpEvent = ServiceDomain + "UpdateDoubleJump"
    # 自定义装备卸下 todo 废弃
    UnequipCustomWeaponEvent = ServiceDomain + "UnequipCustomWeapon"
    # 根據條件顯示動態 UI
    ConditionDynamicUiEvent = ServiceDomain + "ConditionDynamicUiEvent"


# 用于广播模块区分不同来源的请求id
class RequestId:
    CustomWeapon = "custom_weapon"
    Decorator = "decorator"


class Entity:
    EmptyProjectile = "common:empty_projectile"
