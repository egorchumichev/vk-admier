import json
import requests

class Client:
    def __init__(self, group_id, access_token, api_version = "5.131"):
        self.__defaults = {
            "group_id": group_id,
            "access_token": access_token,
            "v": api_version
        }

        self.__server = self.__get_server()

    def connect(self, handle):
        while True:
            event = self.__listen(self.__server)
            self.__server["ts"] = event["ts"]
            handle(event)
    
    def request(self, method, params):
        url = "https://api.vk.com/method/" + method
        response = requests.get(url, self.__defaults | params)
        return json.loads(response.text)

    def __listen(self, server):
        url = server["address"]
        params = {
            "act": server["act"],
            "key": server["key"],
            "ts": server["ts"],
            "wait": server["delay"]
        }

        response = requests.get(url, params)
        return json.loads(response.text)

    def __get_server(self, params = {}):
        server = self.request("groups.getLongPollServer", params)["response"]
        return {
            "address": server["server"],
            "key": server["key"],
            "ts": server["ts"],
            "act": "a_check",
            "delay": "25"
        }
    
