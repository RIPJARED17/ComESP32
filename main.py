import tkinter as tk
from tkinter import tk
import socket
import time

IP_ESP32 = "192.168.20.20"
PUERTO = 80


class DatosSensor:
    def __init__(self, valor):
        self