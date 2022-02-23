# -*- encoding=utf8 -*-
__author__ = "RH0539"

import pytest
from airtest.core.api import *


# def setup_module(module):
#     print("before each module")
#
#
# def teardown_module(module):
#     print("after each module")
#
#
# def setup_function(function):
#     print("before each test")
#
#
# def teardown_function(function):
#     print("after each test")

# @pytest.mark.usefixtures("test_install_app")
def test_login_valid_credentials(test_install_app):
    sleep(30.0)
    try:
        assert_equal("Real opponents", "xyz", "Checking the text exist")
    except AssertionError:
        log("Assertion error", timestamp=time.time(), desc="Assertion error", snapshot=True)
    assert_equal("Real opponents", "xyz", "verify value")
    wait(Template(r"ageCheckbox.png", rgb=True, record_pos=(-0.385, 0.395), resolution=(1440, 2560)))
    touch(Template(r"ageCheckbox.png", rgb=True, record_pos=(-0.385, 0.395), resolution=(1440, 2560)))
    wait(Template(r"btnLetsPlay.png", record_pos=(-0.022, 0.652), resolution=(1440, 2560)))
    touch(Template(r"btnLetsPlay.png", record_pos=(-0.022, 0.652), resolution=(1440, 2560)))
    wait(Template(r"popupPracticegame.png", record_pos=(-0.002, -0.017), resolution=(1440, 2560)))
    touch(Template(r"btnOkayPracticegame.png", record_pos=(0.005, 0.084), resolution=(1440, 2560)))
    wait(Template(r"tpl1644288305866.png", record_pos=(0.356, -0.817), resolution=(1440, 2560)))
    touch(Template(r"btnLogin.png", record_pos=(0.356, -0.817), resolution=(1440, 2560)))
    wait(Template(r"popupLogin.png", record_pos=(-0.002, 0.026), resolution=(1440, 2560)))
    assert_exists(Template(r"popupLogin.png", record_pos=(-0.002, 0.026), resolution=(1440, 2560)),
                  "verify login popup exists")



    # wait(Template(r"txtbxUsernameLogin.png", record_pos=(-0.022, -0.139), resolution=(1440, 2560)))
    # touch(Template(r"tpl1644288890150.png", record_pos=(-0.022, -0.139), resolution=(1440, 2560)))
    # wait(Template(r"tpl1644469091319.png", record_pos=(-0.002, -0.106), resolution=(1440, 2560)))
    # text("accionlabs", enter=True)
    # touch(Template(r"tpl1644288550917.png", record_pos=(0.003, 0.096), resolution=(1440, 2560)))
    # wait(Template(r"tpl1644469195863.png", record_pos=(0.001, 0.007), resolution=(1440, 2560)))
    # text("Password123", enter=False)
    # touch(Template(r"tpl1644288614104.png", record_pos=(0.244, 0.448), resolution=(1440, 2560)))
    # assert_exists(Template(r"tpl1644485252051.png", record_pos=(0.077, 0.215), resolution=(1440, 2560)),
    #               "Verify Invalid username /Password combo")

# def test_second(test_install_app):
#     sleep(30.0)
#     wait(Template(r"tpl1644288160934.png", record_pos=(-0.385, 0.395), resolution=(1440, 2560)))
#     touch(Template(r"tpl1644288160934.png", record_pos=(-0.385, 0.395), resolution=(1440, 2560)))
#     exists(Template(r"tpl1644288260454.png", record_pos=(-0.002, -0.017), resolution=(1440, 2560)))
