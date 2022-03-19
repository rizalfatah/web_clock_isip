import re
import requests
from datetime import timedelta
from dateutil import parser


def get_time_isip():
    url = "https://internsip.kemkes.go.id"

    result = get_time_from_server(url)
    if result['status']:
        # get date and time only
        time = re.findall(r"\d{2} \w{3} \d{4} [\d:]{8}", result["result"])

        # change time to WIB (GMT +7)
        time = parser.parse(time[0])
        time += timedelta(hours=7)

        time_isip = {}
        time_isip['date'] = time.strftime("%m-%d-%Y")
        time_isip['clock'] = time.strftime("%H:%M:%S")
        return time_isip

    return None


def get_time_from_server(url):
    try:
        r = requests.get(url)
        return {"status": True, "result": r.headers['Date']}
    except requests.ConnectionError:
        return {"status": False, "result": "Koneksi Bermasalah"}
    except requests.Timeout:
        return {"status": False, "result": "Koneksi Timeout"}
    except Exception:
        return {"status": False, "result": "Bermasalah"}


def main():
    print(get_time_isip())
    print('Selesai')


if __name__ == "__main__":
    main()
