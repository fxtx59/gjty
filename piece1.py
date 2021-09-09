import pygame
import time

pygame.init()

setting = {"model": None, "map": None, "zt": False}
openm = {}
xianshi = [False, False]
yxz = []
xslb_bx_1 = []
xslb_bx_2 = []
kaizhan = False
_r_b_shezhi = [False,False]


xxsz_all = {"弹药": None, "粮草": None, "进攻": None, "防御": None, "训练": None, "技能": None, "纪律": None}
xxsz = None
xxsz_bh = None
xxsz_pos = {"弹药": (825, 125), "粮草": (825, 215), "进攻": (925, 295), "防御": (925, 375), "训练": (825, 435), "技能": (825, 525),
            "纪律": (825, 615)}

qdd = False

class jishi:
    def __init__(self):
        self.min1 = 0
        self.sec1 = 0
        self.hour1 = 0

    def js(self):
        self.a = time.localtime(time.time())[5] - self.sec1 > 0.5 or \
                 time.localtime(time.time())[4] - self.min1 > 1 or \
                 time.localtime(time.time())[3] - self.hour1 > 1

        self.min1, self.sec1, self.hour1 = time.localtime(time.time())[4], \
                                           time.localtime(time.time())[5], \
                                           time.localtime(time.time())[3]

        return self.a


class shiji(pygame.sprite.Sprite):
    """师级部队"""

    def __init__(self, image_name, speed, call_name,sz, *group):
        super(shiji, self).__init__(*group)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        print(call_name[0:5])
        if call_name[0:5] == "alpha":
            self.rect.center = (40,30+int(call_name[5:])*50)
            print(self.rect.center)
        elif call_name[0:4] == "beta":
            self.rect.center = (1240,30+int(call_name[4:])*50)
            print(self.rect.center)

        self.speed = speed
        self.call_name = call_name
        self.sz = sz
        print(sz)

    def update(self, *args):
        pass


class ui(pygame.sprite.Sprite):
    def __init__(self, image_name, rect, lx, *group, bh=None):

        """lx类型 1为普通"""
        super(ui, self).__init__(*group)
        self.name = image_name
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.center = rect
        self.oldrect = self.rect.center
        self.lx = lx
        self.bh = bh
        if self.name not in xslb_bx_1:
            xslb_bx_1.append(self.name)
            xslb_bx_2.append(jishi())
        else:
            pass

    def update(self, background, mouse, zt, *args):
        if pygame.sprite.collide_rect(self, background):

            if self.rect.center == self.oldrect and not zt:
                self.rect[1] -= 10

            openm[self.name] = self.name

            self.js = xslb_bx_1.index(self.name)

            if mouse:
                if xslb_bx_2[self.js].js():
                    # 解决连续点击的问题
                    if not zt and self.lx == 1:
                        if self.name == "缩略图1.png":
                            setting["map"] = "m1"
                        elif self.name == "缩略图2.png":
                            setting["map"] = "m2"
                        elif self.name == "B vs B.png":
                            setting["model"] = "v2"
                        elif self.name == "B vs R.png":
                            setting["model"] = "v1"
                        elif self.name == "开始.png" and setting["zt"] == False:
                            setting["zt"] = True


                    elif zt:
                        if self.lx == 1:
                            if len(yxz) <= 20:
                                yxz.append(self.name)

                            else:
                                pass

                        elif self.lx == 2:
                            global xxsz_all
                            xxsz_all = {"弹药": None, "粮草": None, "进攻": None, "防御": None, "训练": None, "技能": None,
                                        "纪律": None}
                            global xxsz
                            xxsz = self.name
                            global xxsz_bh
                            xxsz_bh = self.bh
                            print(xxsz)
                        elif self.lx == 3:
                            print("出战")
                            global kaizhan
                            kaizhan = True

        elif not pygame.sprite.collide_rect(self, background):
            if self.rect.center != self.oldrect and not zt:
                self.rect[1] += 10
            openm[self.name] = None

    def kill1(self):
        self.kill()


class shubiao(pygame.sprite.Sprite):
    def __init__(self, image_name, *group):
        super(shubiao, self).__init__(*group)
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()

    def update(self, *args):
        self.rect.center = pygame.mouse.get_pos()


class tishi(pygame.sprite.Sprite):
    def __init__(self, image_name, rect, *group):
        super(tishi, self).__init__(*group)
        self.name = image_name
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.center = rect
        self.oldrect = self.rect.center

    def update(self, *args):
        if openm["缩略图1.png"] == "缩略图1.png" or openm["缩略图2.png"] == "缩略图2.png":
            xianshi[0] = True
            xianshi[1] = False
        elif openm["B vs B.png"] == "B vs B.png" or openm["B vs R.png"] == "B vs R.png":
            xianshi[1] = True
            xianshi[0] = False
        else:
            xianshi[1] = False
            xianshi[0] = False


class ztxs:
    def __init__(self, zt, nr, wz, pm, ys=(255, 255, 255)):
        """zt为字体，nr为显示内容，wz为显示位置，pm为显示屏幕，ys为颜色"""
        self.zt = zt
        self.nr = nr
        self.wz = wz
        self.pm = pm
        self.ys = ys

    def update(self):
        self.ss = self.pm.blit(self.zt.render(self.nr, True, self.ys), self.wz)


class djsr(pygame.sprite.Sprite):
    def __init__(self, image_name, jian, rect, *group):
        super(djsr, self).__init__(*group)
        self.name = image_name
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.center = rect
        self.sr = False
        self.nr = None
        self.jian = jian
        self.sr1 = None

        if self.name not in xslb_bx_1:
            xslb_bx_1.append(self.name)
            xslb_bx_2.append(jishi())
        else:
            pass

    def update(self, shubiao1, mouse, sr, screen, *args):
        self.js = xslb_bx_1.index(self.name)
        if pygame.sprite.collide_rect(self, shubiao1):
            if mouse and xslb_bx_2[self.js].js():
                self.sr = True

                # self.sr2 = ztxs(pygame.font.Font('HanDingJianDaSong-2.ttf', 30), "0000000000",(100, 185), screen,(255, 255, 255))
        elif self.sr:
            self.nr = input(self.name+"请输入")
            xxsz_all[self.jian] = self.nr
            self.sr = False

            # self.sr2.update()


class qd(pygame.sprite.Sprite):

    def __init__(self, image_name, rect, *group):
        super(qd, self).__init__(*group)
        self.name = image_name
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.center = rect
        global qdd
        qdd = False
        if self.name not in xslb_bx_1:
            xslb_bx_1.append(self.name)
            xslb_bx_2.append(jishi())
        else:
            pass

    def update(self, shubiao1, mouse, *args):
        self.js = xslb_bx_1.index(self.name)
        if pygame.sprite.collide_rect(self, shubiao1):
            if mouse and xslb_bx_2[self.js].js():
                global qdd
                qdd = True
                print(qdd)
