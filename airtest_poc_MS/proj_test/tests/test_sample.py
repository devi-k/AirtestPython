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
# def test_login(test_install_app):
#     print("setting up" + test_login.func_name)
#     sleep(30.0)
#     wait(Template(r"tpl1644288160934.png", record_pos=(-0.385, 0.395), resolution=(1440, 2560)))
#     touch(Template(r"tpl1644288160934.png", record_pos=(-0.385, 0.395), resolution=(1440, 2560)))
#     assert_exists(Template(r"tpl1644485252051.png", record_pos=(0.077, 0.215), resolution=(1440, 2560)),
#                   "Verify Invalid username /Password combo")


import pytest

from cv2 import imread

from proj_test.common import assertions

#
# def test_1(proj_setup_fix):
#     print("Inside test 1")
#     assertions.assert_equal(5, 5)
#
#
# def test_2(proj_setup_fix):
#     print("Inside test 2")
#     assertions.assert_not_equal(5, 6)


# def Ptest_3():
#     print("Inside test 2")
#
# Ptest_3()
#
#
