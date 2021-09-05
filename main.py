import pygame
import random
import piece1
import sys
import re
import time

zt = [True, False, False]
mouse = False
start = None
sr = None

blue_army = {a: None for a in range(20)}
print(blue_army)


def up(ztxs):
    for ii in ztxs:
        ii.update()


def dj():
    global mouse
    global sr
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            zt[0] = False
            sys.exit()
            f.close()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if not mouse:
                mouse = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = False


pygame.init()

screen = pygame.display.set_mode((1280, 720))  # pygame.FULLSCREEN
font1 = pygame.font.Font('HanDingJianDaSong-2.ttf', 30)
# pygame.mouse.set_visible(False)

all_group = pygame.sprite.Group()
red_shiji_group = pygame.sprite.Group()
blue_shiji_group = pygame.sprite.Group()
_UI_group = pygame.sprite.Group()
shubiao_group = pygame.sprite.Group()
tishi_group = pygame.sprite.Group()
djsr_group = pygame.sprite.Group()

background = piece1.ui("背景.png", (640, 360), 1, all_group)

back = [piece1.ui("B vs R.png", (300, 334), 1, all_group, _UI_group)
    , piece1.ui("B vs B.png", (300, 486), 1, all_group, _UI_group)
    , piece1.ui("缩略图1.png", (700, 410), 1, all_group, _UI_group)
    , piece1.ui("缩略图2.png", (1000, 410), 1, all_group, _UI_group)]
shubiao1 = piece1.shubiao("检测.png", all_group, shubiao_group)
tishi1 = piece1.tishi("选择地图.png", (850, -100), all_group, tishi_group)
tishi2 = piece1.tishi("选择模式.png", (300, -100), all_group, tishi_group)

all_group.draw(screen)
pygame.display.update()
f = open("budui.txt", "w+")
ff = open("budui1.txt", "w+")
f.write("#请勿修改#")
ff.write("#请勿修改#")

while zt[0]:
    _UI_group.update(shubiao1, mouse, zt[1])
    tishi_group.update()
    shubiao_group.update()
    all_group.draw(screen)
    pygame.display.update()
    if not zt[1] and not zt[2]:
        if piece1.setting["model"] is not None and piece1.setting["map"] is not None and start is None:
            start = piece1.ui("开始.png", (1200, 410), 1, all_group, _UI_group)
        if piece1.setting["zt"] and zt[1] != True:
            zt[1] = True

        if piece1.xianshi[0]:
            tishi1.rect.center = (850, 260)
        elif not piece1.xianshi[0]:
            tishi1.rect.center = (850, -100)
        if piece1.xianshi[1]:
            tishi2.rect.center = (300, 260)
        elif not piece1.xianshi[1]:
            tishi2.rect.center = (300, -100)
    elif zt[1]:
        _UI_group.empty()
        djsr_group.empty()
        all_group.empty()
        background = piece1.ui("背景.png", (640, 360), 1, all_group)
        background2 = piece1.ui("BR设置1.png", (640, 360), 1, all_group)
        chuzhan = piece1.ui("出战.png", (1200, 600), 3, all_group, _UI_group)
        daixuan_B = [piece1.ui("步兵B.png", (60, 200), 1, all_group, _UI_group)
            , piece1.ui("机械化步兵B.png", (60, 300), 1, all_group, _UI_group)
            , piece1.ui("炮兵部队B.png", (60, 400), 1, all_group, _UI_group)
            , piece1.ui("装甲部队B.png", (60, 500), 1, all_group, _UI_group)
            , piece1.ui("防空部队B.png", (60, 600), 1, all_group, _UI_group)]
        sr1 = [piece1.djsr("点击输入.png", "弹药", (900, 150), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "粮草", (900, 240), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "进攻", (1000, 320), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "防御", (1000, 400), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "训练", (900, 460), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "技能", (900, 550), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "纪律", (900, 640), all_group, djsr_group)]
        ztxs1 = [piece1.ztxs(font1, "步兵", (100, 185), screen, (255, 255, 255))
            , piece1.ztxs(font1, "机械化步兵", (100, 285), screen, (255, 255, 255))
            , piece1.ztxs(font1, "炮兵部队", (100, 385), screen, (255, 255, 255))
            , piece1.ztxs(font1, "装甲部队", (100, 485), screen, (255, 255, 255))
            , piece1.ztxs(font1, "防空部队", (100, 585), screen, (255, 255, 255))]
        qd = piece1.qd("确定.png", (1200, 100), all_group)

        ztxs = [screen.blit(font1.render("步兵", True, (255, 255, 255)), (100, 200))]
        print("初始")
        while zt[1]:
            # print(pygame.key.get_pressed())

            _UI_group.update(shubiao1, mouse, zt[1])
            djsr_group.update(shubiao1, mouse, sr, screen)
            shubiao_group.update()
            all_group.draw(screen)
            up(ztxs1)
            dj()

            if piece1.yxz:
                cs = 0
                yxzq = []
                for iii in piece1.yxz:
                    if cs < 10:
                        yxzq.append(piece1.ui(iii, (360, 200 + cs * 50), 2, all_group, _UI_group, bh=cs))
                    elif 9 < cs < 20:
                        yxzq.append(piece1.ui(iii, (410, 200 + (cs - 10) * 50), 2, all_group, _UI_group, bh=cs))
                    cs += 1
                    dj()
            if piece1.xxsz:

                for iiii in piece1.xxsz_all.items():
                    up([piece1.ztxs(font1, iiii[1], piece1.xxsz_pos[iiii[0]], screen, (255, 255, 255))])

                qd.update(shubiao1, mouse)

                if piece1.qdd:
                    print(piece1.xxsz_bh)
                    pat1 = r"!" + str(piece1.xxsz_bh) + "-"
                    f.seek(0)
                    find = re.findall(pat1, f.read())
                    print("qd")
                    if find:
                        f.seek(0)
                        cc = re.sub(r"{{.*?}}}", "{{" + "!" + str(piece1.xxsz_bh) + "-" + piece1.xxsz + "/" + str(
                            piece1.xxsz_all) + "}}", f.read())
                        print(cc)
                        f.close()
                        f = open("budui.txt", "w+")
                        f.write(cc)
                    else:
                        f.write("\n" + "{{" + "!" + str(piece1.xxsz_bh) + "-" + piece1.xxsz + "/" + str(
                            piece1.xxsz_all) + "}}")
                    piece1.qdd = False
                # pygame.display.update()
            if piece1.kaizhan:
                print("kz")
                if background2.name == "BR设置1.png":
                    piece1._r_b_shezhi[0] = True
                    piece1.kaizhan = False
                    f.seek(0)
                    b1 = re.findall(r"!\d-(.*?).png", f.read())
                    f.seek(0)
                    b2 = re.findall(r"{{.*?/({.*?})}", f.read())
                    for w1 in range(len(b1)):
                        piece1.shiji(b1[w1] + ".png", 100, "alpha" + str(w1), b2[w1], blue_shiji_group)

                    _UI_group.empty()
                    djsr_group.empty()
                    all_group.empty()
                    background = piece1.ui("背景.png", (640, 360), 1, all_group)
                    background2 = piece1.ui("BR设置2.png", (640, 360), 1, all_group)
                    chuzhan = piece1.ui("出战.png", (1200, 600), 3, all_group, _UI_group)
                    daixuan_B = [piece1.ui("步兵R.png", (60, 200), 1, all_group, _UI_group)
                        , piece1.ui("机械化步兵R.png", (60, 300), 1, all_group, _UI_group)
                        , piece1.ui("炮兵部队R.png", (60, 400), 1, all_group, _UI_group)
                        , piece1.ui("装甲部队R.png", (60, 500), 1, all_group, _UI_group)
                        , piece1.ui("防空部队R.png", (60, 600), 1, all_group, _UI_group)]
                    sr1 = [piece1.djsr("点击输入1.png", "弹药", (900, 150), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "粮草", (900, 240), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "进攻", (1000, 320), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "防御", (1000, 400), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "训练", (900, 460), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "技能", (900, 550), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "纪律", (900, 640), all_group, djsr_group)]
                    ztxs1 = [piece1.ztxs(font1, "步兵", (100, 185), screen, (255, 255, 255))
                        , piece1.ztxs(font1, "机械化步兵", (100, 285), screen, (255, 255, 255))
                        , piece1.ztxs(font1, "炮兵部队", (100, 385), screen, (255, 255, 255))
                        , piece1.ztxs(font1, "装甲部队", (100, 485), screen, (255, 255, 255))
                        , piece1.ztxs(font1, "防空部队", (100, 585), screen, (255, 255, 255))]
                    qd = piece1.qd("确定.png", (1200, 100), all_group)
                    piece1.yxz = []

                    ztxs = [screen.blit(font1.render("步兵", True, (255, 255, 255)), (100, 200))]
                    print("初始")
                    while not zt[2]:
                        # print(pygame.key.get_pressed())

                        _UI_group.update(shubiao1, mouse, zt[1])
                        djsr_group.update(shubiao1, mouse, sr, screen)
                        shubiao_group.update()
                        all_group.draw(screen)

                        up(ztxs1)
                        dj()

                        if piece1.yxz:
                            cs = 0
                            yxzq = []
                            for iii in piece1.yxz:
                                if cs < 10:
                                    yxzq.append(piece1.ui(iii, (360, 200 + cs * 50), 2, all_group, _UI_group, bh=cs))
                                elif 9 < cs < 20:
                                    yxzq.append(
                                        piece1.ui(iii, (410, 200 + (cs - 10) * 50), 2, all_group, _UI_group, bh=cs))
                                cs += 1
                                dj()
                        if piece1.xxsz:

                            for iiii in piece1.xxsz_all.items():
                                up([piece1.ztxs(font1, iiii[1], piece1.xxsz_pos[iiii[0]], screen, (255, 255, 255))])

                            qd.update(shubiao1, mouse)

                            if piece1.qdd:
                                print("dfd")
                                print(piece1.xxsz_bh)
                                pat1 = r"!" + str(piece1.xxsz_bh) + "-"
                                ff.seek(0)
                                find = re.findall(pat1, ff.read())
                                print("qd")
                                if find:
                                    ff.seek(0)
                                    cc = re.sub(r"{{.*?}}}",
                                                "{{" + "!" + str(piece1.xxsz_bh) + "-" + piece1.xxsz + "/" + str(
                                                    piece1.xxsz_all) + "}}", ff.read())
                                    print(cc)
                                    ff.close()
                                    ff = open("budui1.txt", "w+")
                                    ff.write(cc)
                                else:
                                    ff.write("\n" + "{{" + "!" + str(piece1.xxsz_bh) + "-" + piece1.xxsz + "/" + str(
                                        piece1.xxsz_all) + "}}")
                                piece1.qdd = False
                        if piece1.kaizhan:

                            piece1._r_b_shezhi[1] = True
                            piece1.kaizhan = False
                            ff.seek(0)
                            b1 = re.findall(r"!\d-(.*?).png", ff.read())
                            ff.seek(0)
                            b2 = re.findall(r"{{.*?/({.*?})}", ff.read())
                            for w1 in range(len(b1)):
                                piece1.shiji(b1[w1] + ".png", 100, "beta" + str(w1), b2[w1], red_shiji_group)
                            zt[2] = True
                            zt[1] = False
                            break
                        pygame.display.update()


            pygame.display.update()
    elif zt[2]:

        _UI_group.empty()
        djsr_group.empty()
        all_group.empty()
        background = piece1.ui("背景.png", (640, 360), 1, all_group)
        background2 = piece1.ui("地图1.png", (640, 360), 1, all_group)

        while zt[2]:
            _UI_group.update(shubiao1, mouse, zt[1])
            djsr_group.update(shubiao1, mouse, sr, screen)
            shubiao_group.update()
            all_group.draw(screen)
            red_shiji_group.draw(screen)
            blue_shiji_group.draw(screen)
            pygame.display.update()
            dj()
    dj()
import pygame
import random
import piece1
import sys
import re
import time

zt = [True, False, False]
mouse = False
start = None
sr = None

blue_army = {a: None for a in range(20)}
print(blue_army)


def up(ztxs):
    for ii in ztxs:
        ii.update()


def dj():
    global mouse
    global sr
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            zt[0] = False
            sys.exit()
            f.close()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if not mouse:
                mouse = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = False


pygame.init()

screen = pygame.display.set_mode((1280, 720))  # pygame.FULLSCREEN
font1 = pygame.font.Font('HanDingJianDaSong-2.ttf', 30)
# pygame.mouse.set_visible(False)

all_group = pygame.sprite.Group()
red_shiji_group = pygame.sprite.Group()
blue_shiji_group = pygame.sprite.Group()
_UI_group = pygame.sprite.Group()
shubiao_group = pygame.sprite.Group()
tishi_group = pygame.sprite.Group()
djsr_group = pygame.sprite.Group()

background = piece1.ui("背景.png", (640, 360), 1, all_group)

back = [piece1.ui("B vs R.png", (300, 334), 1, all_group, _UI_group)
    , piece1.ui("B vs B.png", (300, 486), 1, all_group, _UI_group)
    , piece1.ui("缩略图1.png", (700, 410), 1, all_group, _UI_group)
    , piece1.ui("缩略图2.png", (1000, 410), 1, all_group, _UI_group)]
shubiao1 = piece1.shubiao("检测.png", all_group, shubiao_group)
tishi1 = piece1.tishi("选择地图.png", (850, -100), all_group, tishi_group)
tishi2 = piece1.tishi("选择模式.png", (300, -100), all_group, tishi_group)

all_group.draw(screen)
pygame.display.update()
f = open("budui.txt", "w+")
ff = open("budui1.txt", "w+")
f.write("#请勿修改#")
ff.write("#请勿修改#")

while zt[0]:
    _UI_group.update(shubiao1, mouse, zt[1])
    tishi_group.update()
    shubiao_group.update()
    all_group.draw(screen)
    pygame.display.update()
    if not zt[1] and not zt[2]:
        if piece1.setting["model"] is not None and piece1.setting["map"] is not None and start is None:
            start = piece1.ui("开始.png", (1200, 410), 1, all_group, _UI_group)
        if piece1.setting["zt"] and zt[1] != True:
            zt[1] = True

        if piece1.xianshi[0]:
            tishi1.rect.center = (850, 260)
        elif not piece1.xianshi[0]:
            tishi1.rect.center = (850, -100)
        if piece1.xianshi[1]:
            tishi2.rect.center = (300, 260)
        elif not piece1.xianshi[1]:
            tishi2.rect.center = (300, -100)
    elif zt[1]:
        _UI_group.empty()
        djsr_group.empty()
        all_group.empty()
        background = piece1.ui("背景.png", (640, 360), 1, all_group)
        background2 = piece1.ui("BR设置1.png", (640, 360), 1, all_group)
        chuzhan = piece1.ui("出战.png", (1200, 600), 3, all_group, _UI_group)
        daixuan_B = [piece1.ui("步兵B.png", (60, 200), 1, all_group, _UI_group)
            , piece1.ui("机械化步兵B.png", (60, 300), 1, all_group, _UI_group)
            , piece1.ui("炮兵部队B.png", (60, 400), 1, all_group, _UI_group)
            , piece1.ui("装甲部队B.png", (60, 500), 1, all_group, _UI_group)
            , piece1.ui("防空部队B.png", (60, 600), 1, all_group, _UI_group)]
        sr1 = [piece1.djsr("点击输入.png", "弹药", (900, 150), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "粮草", (900, 240), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "进攻", (1000, 320), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "防御", (1000, 400), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "训练", (900, 460), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "技能", (900, 550), all_group, djsr_group)
            , piece1.djsr("点击输入.png", "纪律", (900, 640), all_group, djsr_group)]
        ztxs1 = [piece1.ztxs(font1, "步兵", (100, 185), screen, (255, 255, 255))
            , piece1.ztxs(font1, "机械化步兵", (100, 285), screen, (255, 255, 255))
            , piece1.ztxs(font1, "炮兵部队", (100, 385), screen, (255, 255, 255))
            , piece1.ztxs(font1, "装甲部队", (100, 485), screen, (255, 255, 255))
            , piece1.ztxs(font1, "防空部队", (100, 585), screen, (255, 255, 255))]
        qd = piece1.qd("确定.png", (1200, 100), all_group)

        ztxs = [screen.blit(font1.render("步兵", True, (255, 255, 255)), (100, 200))]
        print("初始")
        while zt[1]:
            # print(pygame.key.get_pressed())

            _UI_group.update(shubiao1, mouse, zt[1])
            djsr_group.update(shubiao1, mouse, sr, screen)
            shubiao_group.update()
            all_group.draw(screen)
            up(ztxs1)
            dj()

            if piece1.yxz:
                cs = 0
                yxzq = []
                for iii in piece1.yxz:
                    if cs < 10:
                        yxzq.append(piece1.ui(iii, (360, 200 + cs * 50), 2, all_group, _UI_group, bh=cs))
                    elif 9 < cs < 20:
                        yxzq.append(piece1.ui(iii, (410, 200 + (cs - 10) * 50), 2, all_group, _UI_group, bh=cs))
                    cs += 1
                    dj()
            if piece1.xxsz:

                for iiii in piece1.xxsz_all.items():
                    up([piece1.ztxs(font1, iiii[1], piece1.xxsz_pos[iiii[0]], screen, (255, 255, 255))])

                qd.update(shubiao1, mouse)

                if piece1.qdd:
                    print(piece1.xxsz_bh)
                    pat1 = r"!" + str(piece1.xxsz_bh) + "-"
                    f.seek(0)
                    find = re.findall(pat1, f.read())
                    print("qd")
                    if find:
                        f.seek(0)
                        cc = re.sub(r"{{.*?}}}", "{{" + "!" + str(piece1.xxsz_bh) + "-" + piece1.xxsz + "/" + str(
                            piece1.xxsz_all) + "}}", f.read())
                        print(cc)
                        f.close()
                        f = open("budui.txt", "w+")
                        f.write(cc)
                    else:
                        f.write("\n" + "{{" + "!" + str(piece1.xxsz_bh) + "-" + piece1.xxsz + "/" + str(
                            piece1.xxsz_all) + "}}")
                    piece1.qdd = False
                # pygame.display.update()
            if piece1.kaizhan:
                print("kz")
                if background2.name == "BR设置1.png":
                    piece1._r_b_shezhi[0] = True
                    piece1.kaizhan = False
                    f.seek(0)
                    b1 = re.findall(r"!\d-(.*?).png", f.read())
                    f.seek(0)
                    b2 = re.findall(r"{{.*?/({.*?})}", f.read())
                    for w1 in range(len(b1)):
                        piece1.shiji(b1[w1] + ".png", 100, "alpha" + str(w1), b2[w1], blue_shiji_group)

                    _UI_group.empty()
                    djsr_group.empty()
                    all_group.empty()
                    background = piece1.ui("背景.png", (640, 360), 1, all_group)
                    background2 = piece1.ui("BR设置2.png", (640, 360), 1, all_group)
                    chuzhan = piece1.ui("出战.png", (1200, 600), 3, all_group, _UI_group)
                    daixuan_B = [piece1.ui("步兵R.png", (60, 200), 1, all_group, _UI_group)
                        , piece1.ui("机械化步兵R.png", (60, 300), 1, all_group, _UI_group)
                        , piece1.ui("炮兵部队R.png", (60, 400), 1, all_group, _UI_group)
                        , piece1.ui("装甲部队R.png", (60, 500), 1, all_group, _UI_group)
                        , piece1.ui("防空部队R.png", (60, 600), 1, all_group, _UI_group)]
                    sr1 = [piece1.djsr("点击输入1.png", "弹药", (900, 150), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "粮草", (900, 240), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "进攻", (1000, 320), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "防御", (1000, 400), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "训练", (900, 460), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "技能", (900, 550), all_group, djsr_group)
                        , piece1.djsr("点击输入1.png", "纪律", (900, 640), all_group, djsr_group)]
                    ztxs1 = [piece1.ztxs(font1, "步兵", (100, 185), screen, (255, 255, 255))
                        , piece1.ztxs(font1, "机械化步兵", (100, 285), screen, (255, 255, 255))
                        , piece1.ztxs(font1, "炮兵部队", (100, 385), screen, (255, 255, 255))
                        , piece1.ztxs(font1, "装甲部队", (100, 485), screen, (255, 255, 255))
                        , piece1.ztxs(font1, "防空部队", (100, 585), screen, (255, 255, 255))]
                    qd = piece1.qd("确定.png", (1200, 100), all_group)
                    piece1.yxz = []

                    ztxs = [screen.blit(font1.render("步兵", True, (255, 255, 255)), (100, 200))]
                    print("初始")
                    while not zt[2]:
                        # print(pygame.key.get_pressed())

                        _UI_group.update(shubiao1, mouse, zt[1])
                        djsr_group.update(shubiao1, mouse, sr, screen)
                        shubiao_group.update()
                        all_group.draw(screen)

                        up(ztxs1)
                        dj()

                        if piece1.yxz:
                            cs = 0
                            yxzq = []
                            for iii in piece1.yxz:
                                if cs < 10:
                                    yxzq.append(piece1.ui(iii, (360, 200 + cs * 50), 2, all_group, _UI_group, bh=cs))
                                elif 9 < cs < 20:
                                    yxzq.append(
                                        piece1.ui(iii, (410, 200 + (cs - 10) * 50), 2, all_group, _UI_group, bh=cs))
                                cs += 1
                                dj()
                        if piece1.xxsz:

                            for iiii in piece1.xxsz_all.items():
                                up([piece1.ztxs(font1, iiii[1], piece1.xxsz_pos[iiii[0]], screen, (255, 255, 255))])

                            qd.update(shubiao1, mouse)

                            if piece1.qdd:
                                print("dfd")
                                print(piece1.xxsz_bh)
                                pat1 = r"!" + str(piece1.xxsz_bh) + "-"
                                ff.seek(0)
                                find = re.findall(pat1, ff.read())
                                print("qd")
                                if find:
                                    ff.seek(0)
                                    cc = re.sub(r"{{.*?}}}",
                                                "{{" + "!" + str(piece1.xxsz_bh) + "-" + piece1.xxsz + "/" + str(
                                                    piece1.xxsz_all) + "}}", ff.read())
                                    print(cc)
                                    ff.close()
                                    ff = open("budui1.txt", "w+")
                                    ff.write(cc)
                                else:
                                    ff.write("\n" + "{{" + "!" + str(piece1.xxsz_bh) + "-" + piece1.xxsz + "/" + str(
                                        piece1.xxsz_all) + "}}")
                                piece1.qdd = False
                        if piece1.kaizhan:

                            piece1._r_b_shezhi[1] = True
                            piece1.kaizhan = False
                            ff.seek(0)
                            b1 = re.findall(r"!\d-(.*?).png", ff.read())
                            ff.seek(0)
                            b2 = re.findall(r"{{.*?/({.*?})}", ff.read())
                            for w1 in range(len(b1)):
                                piece1.shiji(b1[w1] + ".png", 100, "beta" + str(w1), b2[w1], red_shiji_group)
                            zt[2] = True
                            zt[1] = False
                            break
                        pygame.display.update()


            pygame.display.update()
    elif zt[2]:

        _UI_group.empty()
        djsr_group.empty()
        all_group.empty()
        background = piece1.ui("背景.png", (640, 360), 1, all_group)
        background2 = piece1.ui("地图1.png", (640, 360), 1, all_group)

        while zt[2]:
            _UI_group.update(shubiao1, mouse, zt[1])
            djsr_group.update(shubiao1, mouse, sr, screen)
            shubiao_group.update()
            all_group.draw(screen)
            red_shiji_group.draw(screen)
            blue_shiji_group.draw(screen)
            pygame.display.update()
            dj()
    dj()
