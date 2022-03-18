import urllib.request as req
import re


def get_clocl_isip():
    result_web = req.urlopen('https://aditiawan.com/isip/clock2.php')

    # convert encoding
    result_web = str(result_web.read(), encoding='UTF-8')
    clock = re.findall(r"[\d:]{8}", result_web)[0]
    return clock


def main():
    print(get_clocl_isip())


if __name__ == "__main__":
    main()
