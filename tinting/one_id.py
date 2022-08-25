import requests
import json


class OneID:
    @staticmethod
    def getData():
        getData_url = "https://id.egov.uz/api/v1/statistic/getData"

        payload = {}
        headers = {}

        response = requests.request("GET", getData_url, headers=headers, data=payload)

        return response.json()

    @staticmethod
    def signin(login, password):
        url = "https://id.egov.uz/api/v1/secure/signIn"

        payload = json.dumps({
            "login": f"{login}",
            "password": f"{password}",
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()

    @staticmethod
    def register():
        pass


class StepOne:
    @staticmethod
    def get_info_by_number(car_number):
        getNumUrl = "https://my.gov.uz/uz/dictionary/get-info-by-number"

        payload = f"gosNumber={car_number}"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'smart_top=1; epigu-common=7ud1rerodr2aqoddiuqj7o59ef; _language=2f9598ab25269d75ecfa71342ada1360b2bba5fd82ba71899db338868541defba%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_language%22%3Bi%3A1%3Bs%3A2%3A%22uz%22%3B%7D; _csrf-myap=3b9aa9974430be53ef630150b4351ad88f1d84807516ae493e271f374cbe853ca%3A2%3A%7Bi%3A0%3Bs%3A10%3A%22_csrf-myap%22%3Bi%3A1%3Bs%3A32%3A%22sgGduNN0L3Sgu4k6cjAo10rh7qLHqw30%22%3B%7D; _language=2f9598ab25269d75ecfa71342ada1360b2bba5fd82ba71899db338868541defba%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_language%22%3Bi%3A1%3Bs%3A2%3A%22uz%22%3B%7D',
            'X-CSRF-Token': 'aR8jjO_9bs-FHtQ2KBOUz2BCiX1J6AGLFQsDWuG8kvQaeGTomrMg_8kth1FdJ__5AyjIEnjYc-Miek8SkMuhxA==',
            'X-Requested-With': 'XMLHttpRequest',
        }

        response = requests.request("POST", getNumUrl, headers=headers, data=payload)

        return response.json()


class StepTwo:
    @staticmethod
    def check_region(region_name):
        pass


class StepThree:
    @staticmethod
    def get_ariza(plate_number, id, string):
        pass


class StepFour:
    @staticmethod
    def final_pay(id, string):
        pass


x = OneID.getData()
y = OneID.signin("as_software_engineer", "sH23c6Jfcu")
gosNumber = StepOne.get_info_by_number('40O089MA')
print(gosNumber, gosNumber['error'], gosNumber['message'])
print(x['data'])
print(y['data'])
