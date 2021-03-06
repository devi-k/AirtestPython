")""""Base conftest.py."""
from pathlib import Path
import self as self
from airtest.core.android import Android
import pytest
from airtest.core.api import *
from airtest.report.report import *
from airtest.report.report import simple_report

auto_setup(__file__, logdir=True)

ST.LOG_FILE = "log.txt"
set_logdir(str(Path().absolute().parent) + '\\log')
PKG = "com.gsn.worldwinner"


# APK = str(Path().absolute().parent) + '\\app\\WorldWinner.apk'

@pytest.fixture(scope="function")
def test_install_app():
    # if PKG not in device().list_app():
    self.android = Android()
    if PKG not in self.android.list_app():
        connect_device("Android:///")
        self.android.install_app(r"C:\Users\RH0539\Downloads\WorldWinner.apk")
        self.android.start_app(PKG)
    else:
        self.android.stop_app(PKG)
        self.android.clear_app(PKG)
        self.android.start_app(PKG)
    yield
    simple_report(__file__, logpath=True, logfile=str(Path().absolute().parent) + '\\log\\log.txt',
                  output=str(Path().absolute().parent) + '\\log\\report.html')
    self.android.stop_app(PKG)
    self.android.clear_app(PKG)





    # self.android.start_app(PKG)
    # self.android.uninstall_app(PKG)

# @pytest.fixture(scope="function")
# @pytest.fixture(scope="module")
# @pytest.fixture(scope="session")


# auto_setup(__file__, devices=["Android:///"], logdir=True)
# set_logdir(r'D:\log')
# APK = os.path.join(PWD, "C:/Users/RH0539/Downloads/WorldWinner.apk")
# simple_report(__file__, logpath=True, logfile=r"D:\log\log.txt", output=r"D:\log\report.html")
