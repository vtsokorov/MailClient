# -*- coding: utf-8 -*-

import configparser

class Settings:
    def __init__(self):
        self.settings = dict()
        self.config = configparser.ConfigParser()

    def __setitem__(self, key, value):
        self.settings[key] = value

    def __getitem__(self, key):
        return self.settings[key]

    def load(self):
        try:
            self.settings.clear()
            self.config.read("settings.ini")
            self.settings["imap_server"] = self.config.get("MAILSERVER", "imap_server")
            self.settings["smtp_server"] = self.config.get("MAILSERVER", "smtp_server")
            self.settings["imap_port"] = self.config.getint("MAILSERVER", "imap_port")
            self.settings["smtp_port"] = self.config.getint("MAILSERVER", "smtp_port")
            self.settings["ssl"] = True if self.config.get("MAILSERVER", "ssl").lower() == "yes" else False
            self.settings["mail"] = self.config.get("MAILSERVER", "mail")
        except KeyError as error:
            print("Error load settings ...")
            self.settings["imap_server"] = "imap.yandex.ru"
            self.settings["smtp_server"] = "smtp.yandex.ru"
            self.settings["imap_port"] = 993
            self.settings["smtp_port"] = 465
            self.settings["ssl"] = True
            self.settings["mail"] = ""

    def save(self):
        with open("settings.ini", "w") as configfile:
            self.config.write(configfile)

    def set(self, key, value):
        self.config.set('MAILSERVER', key, value)
