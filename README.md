![Example Image](resource_pack/pack_icon.jpg)

## SimpleAddon 小鸡万能模板

### 注意事项

导出时，在mcstudio中，打开设置——作品，勾选自 “过滤指定文件与文件夹”，并在下方的输入框中输入以下内容：
```*.svn,*.git,*.idea,*.gitignore,*.md,*.mcgui,venv,*.pyc,pack_icon.jpg,tool_offline*```

### 一般开发流程

-
  1. fork本项目到一个新的路径下
-
  2. 右键标记(Mark Directory As)behavior_pack文件夹为sources root（根路径）
-
  3. 暂无
-
  4. 在pythonScripts/share/modConfig.py中修改自己的组件名
-
  5. 在modMain.py中，注册服务端或者客户端，不需要写system.registerModule,只写import和类本身的构造即可
-
  6. 在类中找到配置的example或者找技术问到配置的格式，复制到modMain.py内的registerData下，根据对应格式进行配置
-
  7. （可选）使用generator工具生成json配置(即将开源)
-
  8. （程序可选）使用linkTemplate与本地的Template项目进行文件同步
-
  9. 开发完成后，运行behavior_pack/pythonScripts/tool_offline/OfflineToolBeforeRelease.py （点击文件内的三角标志）进行发布前的清理
-
  10.

当清理完成后，提交后重新下载项目（防止修改template文件内容）使用shift+f6（rename）把behavior_pack/pythonScripts目录修改为behavior_pack/<
域名>_<
  项目英文名>_pythonScripts，注意保持两个search勾选
-
  11. 点击左下角Do Refactor确认进行更名操作，重命名pythonScripts为<域名>_<组件名称>_
      Scripts,其中<域名>是与其他团队区分的团队名，组件名称为防止冲突的组件名，Scripts为用于识别代码部分的标记
-
  12. 进行上架操作（10与11严禁省略，会造成不同mod之间的冲突）
-
  13. 检查template同步到的接口修改，并提交

### 即将发布时，推荐进行以下修改（可选）：

- 修改pack_icon.jpg
- 修改pack_manifest.json中的描述
- 重命名behavior_pack为behavior_pack_<任意代码>（官方推荐，但是暂未发现有什么作用）
- 重命名resource_pack为resource_pack_<任意代码>（官方推荐，但是暂未发现有什么作用）

### 一些这个项目中的规则，你可以自由选择是否遵守，但是如果你想要向主分支提交pr，你必须遵守

- 除了modMain以外，所有文件名大写开头，驼峰规则
- 所有服务端内容写在server，客户端内容写在client，共享内容写在share，仅仅模块使用的bean对象，卸载server或client目录下的bean文件夹中，按照模块建立子文件夹
- 方法名除了监听，都以java相同的驼峰形式书写
- 监听的方法与监听的事件同名，如监听ServerChatEvent的方法使用ServerChatEvent方法进行监听
- 所有的工具方法以静态方法写在工具类中，除非极端情况下考虑性能优化，不得直接调用网易提供的接口
- 所有的工具方法不得使用未公开的接口，即无法通过代码检查的接口，如os、eval等
- 所有的工具方法必须写注释
- 所有的工具方法必须使用pycharm的注释标记调用及返回类型

### 多mod兼容与通讯框架

#### 为了利于组件之间形成“联动”，并且降低加载多个mod时重复代码带来的性能消耗，我们需要打通所有的组件，对代码与配置进行统一的代码管理

模组中注册了唯一性的服务端system与客户端system注册名写在StaticConfig中，正常不应该修改，mod只需要使用registerServerModules与registerClientModules将自己的module注册进去即可

- 注册

  使用system.registerModule进行注册，无需多版本兼容的模块可以自动生成name与version，需要多版本覆盖的模块请手工定义名字，手工维护版本，system会自动使用最新版本。system名建议使用域名+项目名，如 "com.netease.ArmorMod"，也可不填让系统自动使用类的路径

  系统模块使用注解进行注册，注册时不需要写system.registerModule,只用初始化即可，如果需要对系统模块进行升级，必须在模块中对其注解中的version增加1，以避免被其他mod覆盖

- 数据

  有时候你需要使用多版本合并的数据，这个时候你可以使用system.addData在启动阶段注入数据，在mod完成加载后使用getData进行查询，会按照版本从小到大进行覆盖，数据建议也使用域名作为开头

- 特殊模块

  由于性能考虑，原来的scheduler从静态工具变成了module，需要使用StaticConfig中的模块名字来获取，如ClientUtils.getModule(StaticConfig.schedulerModule)

  camera模块的调用方式不变

- 与模板的同步

  为了形成技术积累，所以在开发过程中请尽可能使用系统模块，如果有什么你觉得能够通用的功能，也要写成系统模块，并提交到模板中来，为了方便这一操作，你可以在从模板fork到新项目时运行linkTemplate.py文件，将新项目与模板项目进行软连接，这时你修改新项目中的系统文件，会同时修改模板中的对应文件，当你完成一个组件的开发后，记得看一遍模板项目并提交哦

- 文件路径

  在测试中如果两个不同mod有两个路径相同的文件，会在游戏组装过程中相互覆盖，因此为了

这个框架在不同版本间只能更新module部分，所以system部分禁止修改，如需修改需要所有mod更新才能保证正确加载

如有bug请及时反馈
