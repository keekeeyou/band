import band_chatbots
from selenium import webdriver
import time
import pprint
import pathlib
import traceback
import importlib
from os import rename
# from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':

    driver = webdriver.Chrome('C:\\zextor\\chromedriver.exe')
    print("ChromeW Driver : ", driver)
    band_chatbots.ChatBot.set_driver(driver)
    c = band_chatbots.ChatBot()

    while True:

        try:

            if pathlib.Path("update.now").is_file():
                # 인스턴스 제거
                band_chatbots.ChatBot.clear_instance()
                # 모듈 교체
                importlib.reload(band_chatbots)
                # 인스턴스 새로 생성
                c = band_chatbots.ChatBot()
                # 파일이름 재설정
                rename("update.now", "update.complete(change .now for reload)")
                print("Module Reloaded!")

            c.work()

            # sleep interval 1 sec
            time.sleep(1)

        except KeyboardInterrupt:
            print("Terminate by user requests.")
            exit(1)
        except Exception:
            traceback.print_exc()
            time.sleep(60)
            pass
