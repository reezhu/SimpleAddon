# -*- coding: utf-8 -*-
# @Author  : Ree
import mod.client.extraClientApi as clientApi
from mod.client.ui.screenNode import ScreenNode

from pythonScripts.client import ClientUtils as utils


class ModularScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        # ui初始化标记
        self.__inited = False
        self._compList = []
        self.__pressed = None
        self.__lastPos = None
        self._movable = True
        self.sx, self.sy = utils.getScreenViewInfo()
        # print "screen view", ClientUtils.getScreenViewInfo()
        self.scale = float(min(int(self.sx / 320), int(self.sy / 210)))
        self.sx = self.sx / self.scale
        self.sy = self.sy / self.scale
        self._positions = {}
        self.__tick = 0
        self.__tickMove = 0
        self._tickAble = False

    def _setButtonMovable(self, enable):
        self._movable = enable

    def _getButtonMovable(self):
        return self._movable

    def Create(self):
        pass

    def OnActive(self):
        pass

    def OnDeactive(self):
        pass

    def OnUpdatePosition(self, data):
        # print "update position", data
        if data is not None:
            import json
            obj = json.loads(data)
            for k, v in obj.items():
                v = tuple(v)
                self._positions[k] = v
                self.SetPosition(k, (v[0] * self.sx, v[1] * self.sy))

    def OnUploadPosition(self):
        import json
        s = json.dumps(self._positions)
        # print "upload position", s
        return s

    def Update(self):
        if not self.__inited:
            self.__inited = True
            self.UpdateInit()
        if self._tickAble:
            self.__tick += 1
            if self.__tick % 30 == 0:
                self.UpdatePerSecond()
        if self.__pressed and self._movable:
            self.__tickMove += 1
            posX, posY = clientApi.GetTouchPos()
            # print "touch", posX, posY
            if posX == 0 and posY == 0:
                self.__pressed = None
                self.__tickMove = 0
                return
            if self.__lastPos is not None and self.__tickMove > 30:
                lastX, lastY = self.__lastPos
                x, y = self.GetPosition(self.__pressed)
                sx, sy = self.GetSize(self.__pressed)
                # print "self", self.sx, sx, self.sx - sx
                position = (max(0, min(x + posX - lastX, self.sx - sx)), (max(0, min(y + posY - lastY, self.sy - sy))))
                self.SetPosition(self.__pressed, position)
                self._positions[self.__pressed] = float(position[0]) / self.sx, float(position[1]) / self.sy

            self.__lastPos = (posX, posY)

    def _onClickMovableButton(self, args):
        # print "click", args
        if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
            if self._movable:
                tickMove = self.__tickMove
                self.__pressed = None
                self.__tickMove = 0
                self.OnUploadPosition()
                return tickMove < 30
            return True
        elif args.get("TouchEvent") == clientApi.GetMinecraftEnum().TouchEvent.TouchDown:
            if self._movable:
                self.__pressed = args["ButtonPath"]
                self.__lastPos = clientApi.GetTouchPos()
        return False

    def _isTouchUpEvent(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        touchEvent = args["TouchEvent"]

        return touchEvent == touchEventEnum.TouchUp

    def _isTouchDownEvent(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        touchEvent = args["TouchEvent"]

        return touchEvent == touchEventEnum.TouchDown

    def UpdateInit(self):
        pass

    def UpdatePerSecond(self):
        pass

    def UpdateGrid(self):
        """
        这个接口只是方便补全，需要自己监听相关api触发
        """
        pass


class ModularComponent:
    _screenNode = None  # type: ScreenNode

    def __init__(self, screenNode, path):
        self._screenNode = screenNode
        self._path = path
        self._visible = None
        self.__alpha = 1

    def _registerComponent(self, comp):
        for key in dir(comp):
            func = getattr(comp, key)
            if hasattr(func, 'collection_name') or hasattr(func, 'binding_flags'):
                if hasattr(self, key):
                    raise Exception("%s in %s has been defined as %s" % (key, comp, getattr(self, key)))
                else:
                    setattr(self, key, func)

    def getCompPath(self):
        return self._path

    def getSubCompPath(self, subPath):
        return self._path + subPath

    def setVisible(self, visible):
        if self._visible is None or self._visible != visible:
            self._screenNode.SetVisible(self._path, visible)
            self._visible = visible

    def isVisible(self):
        return self._visible

    def setText(self, text):
        self._screenNode.SetText(self._path, text)

    def setPosition(self, pos):
        # type: (tuple(x,y)) -> None
        self._screenNode.SetPosition(self._path, pos)

    def getPosition(self):
        return self._screenNode.GetPosition(self._path)

    def getPositionFrom(self, path):
        if not self._path.startswith(path): return None
        position = (0, 0)
        p = self._path
        from pythonScripts.share import VectorUtils
        while len(p) > 0 and p != path:
            position = VectorUtils.add(position, self._screenNode.GetPosition(p))
            p = p[:p.rfind("/")]
        return position

    def setSize(self, size):
        self._screenNode.SetSize(self._path, size, resizeChildren=True)

    def getSize(self):
        return self._screenNode.GetSize(self._path)

    def setAlpha(self, alpha):
        if self.__alpha == alpha:
            return
        if alpha < 0:
            self.setVisible(False)
        else:
            self._screenNode.SetAlpha(self._path, alpha)
            self.setVisible(True)
        self.__alpha = alpha

    def getAlpha(self):
        return self.__alpha

    def setLayer(self, layer):
        self._screenNode.GetBaseUIControl(self._path).SetLayer(layer)

    def setRemove(self):
        self._screenNode.RemoveComponent(self._path, self._path[:self._path.rindex("/")])


class Label(ModularComponent):
    def __init__(self, screenNode, path):
        ModularComponent.__init__(self, screenNode, path)
        self.__screenNode = screenNode
        self.__path = path
        self.__scale = 1.0
        self.__color = (1, 1, 1, 1)

    def setTextColor(self, color):
        if color == self.__color: return
        self.__color = color
        self.__screenNode.SetTextColor(self.__path, color)

    def setFontSize(self, scale):
        if self.__scale == scale:
            return
        self.__screenNode.SetTextFontSize(self.__path, scale)
        self.__scale = scale

    def getTextColor(self):
        return self.__color

    def getTextSize(self):
        return self.__scale


class Image(ModularComponent):
    def __init__(self, screenNode, path):
        ModularComponent.__init__(self, screenNode, path)
        self.__screenNode = screenNode
        self.__path = path
        self.__imagePath = None

    def setImage(self, texturePath):
        if self.__imagePath == texturePath:
            return
        self.__screenNode.SetSprite(self.__path, texturePath)
        self.__imagePath = texturePath

    def setUV(self, size, start=(0, 0)):
        comp = self.__screenNode.GetBaseUIControl(self.__path).asImage()
        comp.SetSpriteUVSize(size)
        comp.SetSpriteUV(start)

    def setColor(self, color):
        comp = self.__screenNode.GetBaseUIControl(self.__path).asImage()
        comp.SetSpriteColor(color)

    def setGray(self, isGray):
        comp = self.__screenNode.GetBaseUIControl(self.__path).asImage()
        comp.SetSpriteGray(isGray)

    def setRot(self, rot):
        self.__screenNode.SetSpriteRot(int(rot))


class ClipImage(Image):
    def __init__(self, screenNode, path, uv):
        Image.__init__(self, screenNode, path)
        self.__u, self.__v = uv
        self.__size = None

    def clip(self, x=1.0, y=1.0, fromLeft=True, fromTop=True, clipUV=True):
        """
        切uv
        @param x: 横向比例
        @param y: 纵向比例
        @return:
        """
        if self.__size is None:
            self.__size = self.getSize()
        if self.__size is None: return
        sx, sy = self.__size
        size = x * sx, y * sy
        self.setSize(size)
        if clipUV:
            uvSize = x * self.__u, y * self.__v
            start = 0 if fromLeft else (self.__u - uvSize[0]), 0 if fromTop else (self.__v - uvSize[1])
            self.setUV(uvSize, start)
            # print "clip", start, uvSize, size


class ItemStackButton(ModularComponent):
    def __init__(self, screenNode, path):
        ModularComponent.__init__(self, screenNode, path)
        self.__screenNode = screenNode
        self.__path = path
        self.__item = None
        self.__pressed = False

    def setItem(self, itemDict):
        if self.__item == itemDict: return
        self.__item = itemDict
        if itemDict is not None:
            self.__screenNode.SetUiItem(self.__path + "/item_render", itemDict["itemName"], itemDict["auxValue"], isEnchanted=len(itemDict.get("enchantData", [])) > 0)
            self._screenNode.SetVisible(self._path + "/item_render", True)
            self.__screenNode.SetText(self.__path + "/item_amount", str(itemDict["count"] if itemDict["count"] > 1 else ""))
            durability = itemDict.get("durability", 0)
            maxDurability = utils.getItemBasicInfo(itemDict).get("maxDurability", 0)
            if durability > 0 and durability != maxDurability:
                # print "item", itemDict
                self._screenNode.SetVisible(self._path + "/durability", True)
                x, y = self.__screenNode.GetSize(self._path + "/durability")
                percent = float(durability) / maxDurability
                self.__screenNode.SetSize(self._path + "/durability", (x, 3), resizeChildren=True)
                self.__screenNode.SetSize(self._path + "/durability/filled_progress_bar", (x * percent, 3), resizeChildren=False)
                self._screenNode.SetSpriteColor(self.__path + "/durability/filled_progress_bar", (1 - percent, percent, 0))
            else:
                self._screenNode.SetVisible(self._path + "/durability", False)

        else:
            self._screenNode.SetVisible(self._path + "/item_render", False)
            self.__screenNode.SetText(self.__path + "/item_amount", "")
            x, y = self.__screenNode.GetSize(self._path + "/durability")
            self.__screenNode.SetVisible(self._path + "/durability", False)

    def getItem(self):
        return self.__item

    def setChoose(self, enable):
        self.__pressed = enable
        self.__screenNode.SetVisible(self.__path + "/item_pressed", enable)

    def getChoose(self):
        return self.__pressed

    def setContentVisible(self, visible):
        if self._visible is None or self._visible != visible:
            self._screenNode.SetVisible(self._path + "/item_render", visible)
            self._screenNode.SetVisible(self._path + "/item_amount", visible)
            if not visible:
                self._screenNode.SetVisible(self._path + "/item_pressed", visible)
            self._visible = visible

    def setBoarderColor(self, color):
        self._screenNode.SetSpriteColor(self.__path + "/item_pressed", color)

    def addTouchHandler(self, callback, param={"isSwallow": True}):
        # print "add handler", self.__path + "/item_button"
        self._screenNode.AddTouchEventHandler(self.__path + "/item_button", callback, param)


class ImageButton(ModularComponent):

    def __init__(self, screenNode, buttonPath):
        ModularComponent.__init__(self, screenNode, buttonPath)
        self.__screenNode = screenNode
        self.__path = buttonPath
        self.__defaultImagePath = None
        self.__hoverImagePath = None
        self.__pressedImagePath = None
        self.__text = None
        self.__text_scale = 1.0

    def setText(self, text):
        path = self.__path + "/button_label"
        self.__screenNode.SetText(path, text)
        self.__text = text

    def getText(self):
        return self.__text

    def setTextSize(self, scale):
        path = self.__path + "/button_label"
        self.__screenNode.SetTextFontSize(path, scale)
        self.__text_scale = scale

    def getTextSize(self):
        return self.__text_scale

    def setDefaultImage(self, texturePath):
        if self.__defaultImagePath == texturePath:
            return

        defaultPath = self.__path + "/default"
        self.__screenNode.SetSprite(defaultPath, texturePath)
        self.__defaultImagePath = texturePath

    def setHoverImage(self, texturePath):
        if self.__hoverImagePath == texturePath:
            return

        hoverPath = self.__path + "/hover"
        self.__screenNode.SetSprite(hoverPath, texturePath)
        self.__hoverImagePath = texturePath

    def setPressedImage(self, texturePath):
        if self.__pressedImagePath == texturePath:
            return

        pressedPath = self.__path + "/pressed"
        self.__screenNode.SetSprite(pressedPath, texturePath)
        self.__pressedImagePath = texturePath

    def setAllStateImages(self, texturePath):
        # type: (str) -> None
        self.setDefaultImage(texturePath)
        self.setHoverImage(texturePath)
        self.setPressedImage(texturePath)

    def setImageBright(self, value):
        # type: (int) -> None
        defaultPath = self.__path + "/default"
        self.__screenNode.SetSpriteBright(defaultPath, value)
        hoverPath = self.__path + "/hover"
        self.__screenNode.SetSpriteBright(hoverPath, value)
        pressedPath = self.__path + "/pressed"
        self.__screenNode.SetSpriteBright(pressedPath, value)

    def setImageGray(self, gray):
        # type: (bool) -> None
        defaultPath = self.__path + "/default"
        self.__screenNode.SetSpriteGray(defaultPath, gray)
        hoverPath = self.__path + "/hover"
        self.__screenNode.SetSpriteGray(hoverPath, gray)
        pressedPath = self.__path + "/pressed"
        self.__screenNode.SetSpriteGray(pressedPath, gray)

    def setEnable(self, enable):
        # type: (bool) -> None
        self.__screenNode.SetTouchEnable(self.__path, enable)

    def getPath(self):
        return self.__path

    def addTouchHandler(self, callback, param={"isSwallow": True}):
        self._screenNode.AddTouchEventHandler(self.__path, callback, param)


class PapperDoll(ModularComponent):
    def __init__(self, screenNode, path):
        ModularComponent.__init__(self, screenNode, path)
        self.__screenNode = screenNode
        self.__path = path
        self.__instance = screenNode.GetBaseUIControl(path).asNeteasePaperDoll()  # type:NeteasePaperDollUIControl

    def setEntity(self, entityId, scale=1.0, init_rot=0, molang={}):
        param = {
            "entity_id": entityId,
            "scale": scale,
            "render_depth": -50,
            "init_rot_y": init_rot,
            "molang_dict": molang
        }
        # print "param", param
        self.__instance.RenderEntity(param)

    def setVanillaEntityByIdentifier(self, identifier):
        self.__screenNode.SetUiEntity(self.__path, identifier)

    def getSkeletonModelId(self):
        return self.__instance.GetModelId()

    def setSkeletonModel(self, identifier, animation="idle", animation_looped=True, scale=1.0, init_rot_y=0, molang={}):
        param = {
            "skeleton_model_name": identifier,
            "animation": animation,
            "animation_looped": animation_looped,
            "render_depth": -50,
            "scale": scale,
            "init_rot_y": init_rot_y,
            "molang_dict": molang,
        }
        self.__instance.RenderSkeletonModel(param)


class ScrollingPanel(ModularComponent):
    __MOUSE_PATH = "/scroll_mouse/scroll_view/stack_panel/background_and_viewport" \
                   "/scrolling_view_port/scrolling_content"

    __TOUCH_PATH = "/scroll_touch/scroll_view/panel/background_and_viewport" \
                   "/scrolling_view_port/scrolling_content"

    def __init__(self, screenNode, path):
        ModularComponent.__init__(self, screenNode, path)
        self.__contentPath = None

    def getContentPath(self):
        if self.__contentPath is not None:
            return self.__contentPath

        contentPath = self._path + ScrollingPanel.__MOUSE_PATH
        if self._screenNode.GetPosition(contentPath) is not None:
            self.__contentPath = contentPath
            return self.__contentPath
        else:
            self.__contentPath = self._path + ScrollingPanel.__TOUCH_PATH
            return self.__contentPath

    def setContentSize(self, size):
        self._screenNode.SetSize(self.getContentPath(), size, True)


class GridPanel(ModularComponent):

    def __init__(self, screenNode, path):
        ModularComponent.__init__(self, screenNode, path)

    def setDimension(self, col, line):
        # print "set dimension", self._path, (col, line), self._screenNode.GetAllChildrenPath(self._path)
        self._screenNode.SetGridDimension(self._path, (col, line))


class ItemRender(ModularComponent):
    def __init__(self, screenNode, path):
        ModularComponent.__init__(self, screenNode, path)
        self.__item = None
        self.__aux = None

    def setItem(self, itemName, auxValue):
        self.__item = itemName
        self.__aux = auxValue
        self._screenNode.SetUiItem(self._path, itemName, auxValue)


class InputPanel(ModularComponent):
    def __init__(self, screenNode, path):
        ModularComponent.__init__(self, screenNode, path)
        self.text = None
        self.mode = None
        self.id = -1


class ProgressBar(ModularComponent):
    # 注意，这个使用产品的progressbar配合一个增加_text后缀的文本来实现
    def __init__(self, screenNode, path):
        ModularComponent.__init__(self, screenNode, path)

    def setProcess(self, now, max):
        ModularComponent(self._screenNode, self._path + "_text").setText(("%d/%d" % (now, max)) if max != 0 else "0/0")
        self._screenNode.GetBaseUIControl(self._path).asProgressBar().SetValue((float(now) / max) if max != 0 else 1.0)
