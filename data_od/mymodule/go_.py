import pytesseract
import pyautogui
import sys
sys.path.append('C:/my_games/coobcco2/data_od/mymodule')

import variable as v_

def go_test(cla):
    from action import go_mynumber_, go_bag, go_potion_off
    from chango import go_chango, chango_, auction
    from function import imgs_set, click_pos_2, text_check_get, text_check_get_2, text_check_get_3, text_check_get_4, imgs_set_, click_pos_reg, menuOpen, myPotion_check, go_to_home, potion_count, drag_pos, get_region, image_processing
    from event_get import game_event_get_ready, game_event_get, go_item_open, go_ticket_open, go_get_open
    import numpy as np
    from schedule import myQuest_number_check, start_id_search, myQuest_play_check
    import cv2
    import os
    import time
    from login_start import get_cla_count, characterChange
    from dungeon import dunjeon_cla_ready
    import git

    print("test", cla)

    v_.global_howcla = "onecla"

    cla = "one"

    if cla == 'one':
        plus = 0
    if cla == 'two':
        plus = 960

    # get_cla_count(cla)

    #dunjeon_cla_ready(cla, "gonghu")
    #menuOpen(cla)

    # myPotion_check("jadong", cla)
    # go_to_home("start", cla)

    print("aaaaaaaaaaaaaaaaaaaaa")

    full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\check\\full_bag_1.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(820, 0, 960, 100, cla, img, 0.9)
    if imgs_ is not None and imgs_ != False:
        print("가방 가득 참", imgs_)
    else:
        print("파악 안됨")

    go_get_open(cla)


    # potion_count_ = text_check_get_3(865, 825, 945, 850, 3, cla)
    # print("potion_count_", potion_count_)
    #
    # img = pyautogui.screenshot(region=(get_region(865, 825, 945, 850, cla)))
    # white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
    # potion_count_ = pytesseract.image_to_string(white_img, lang=None)
    # print("good", potion_count_)

    # bom_wind = text_check_get(670, 397, 715, 415, cla)
    # print("bom_wind", bom_wind)
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\sold_out.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(380, 560, 460, 640, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("sold_out", imgs_)
    # else:
    #     print("sold_out 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\sold_out.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(530, 560, 610, 640, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("sold_out", imgs_)
    # else:
    #     print("sold_out 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\imgs\\event_complete.png"  # '완료' 그림 갯수 파악
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 0, 900, 900, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("event_complete", imgs_)
    #
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\complete_1.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(300, 530, 380, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("complete_1", imgs_)
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\55\\zero.png"  # zero 파악
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(230, 380, 275, 435, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("zero1", imgs_)
    # else:
    #     full_path = "c:\\my_games\\coobcco2\\data_od\\item\\55\\zero.png"  # zero 파악
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(230, 380, 380, 435, cla, img, 0.9)
    #     if imgs_ is not None and imgs_ != False:
    #         print("zero2", imgs_)
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\black_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(220, 570, 320, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event1", imgs_)
    # else:
    #     print("1 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\black_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(490, 570, 590, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event2", imgs_)
    # else:
    #     print("2 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\black_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(220, 630, 320, 660, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event3", imgs_)
    # else:
    #     print("3 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\yellow_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(220, 570, 320, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event1", imgs_)
    # else:
    #     print("11 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\yellow_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(490, 570, 590, 600, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event2", imgs_)
    # else:
    #     print("22 없")
    #
    # full_path = "c:\\my_games\\coobcco2\\data_od\\item\\six\\yellow_six_check.png"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(220, 630, 320, 660, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("black_six_check_event3", imgs_)
    # else:
    #     print("33 없")

