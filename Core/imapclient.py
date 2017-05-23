#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from imaplib import IMAP4, IMAP4_SSL
from Core.query import build_search_query
from Core.mailparse import *
import re

class IMAPClient(object):

    def __init__(self, hostname, port = None, ssl = False):
        try:
            self.hostname = hostname
            self.port = port
            self.ssl = ssl
            if ssl:
                self.transport = IMAP4_SSL
                if not self.port:
                    self.port = 993
            else:
                self.transport = IMAP4
                if not self.port:
                    self.port = 143
            self.server = self.transport(self.hostname, self.port)
        except Exception:
            self.server = None
            print("IMAP4 connection error")

    def login(self, username, password):
        self.username = username
        self.password = password
        try:
            self.server.login(self.username, self.password)
            self.server.select()
            return True
        except IMAP4.error:
            print("IMAP4 login error")
            return False
        except AttributeError:
            print("IMAP4 login error")
            return False

    def logout(self):
        self.server.close()
        self.server.logout()

    def count(self, **kwargs):
        return len(self.query_uids(**kwargs))

    def query_uids(self, **kwargs):
        query = build_search_query(**kwargs)
        message, data = self.server.uid('SEARCH', None, query)
        if data[0] is None:
            return []
        return data[0].split()

    def fetch_header_by_uid(self, uid):
        # Выбираем сообщение, используя байт-идентификатор
        message, data = self.server.uid('FETCH', uid, '(BODY.PEEK[HEADER.FIELDS (FROM TO SUBJECT DATE)])') # (BODY.PEEK[])
        raw_email = data[0][1]
        email_object = parse_header(raw_email)
        return email_object

    def fetch_body_by_uid(self, uid):
        # Выбираем сообщение, используя байт-идентификатор
        message, data = self.server.uid('FETCH', uid, '(BODY.PEEK[])')
        raw_email = data[0][1]
        email_object = parse_body(raw_email)
        return email_object

    def fetch_list_headers(self, **kwargs):
        # Генератор - выбираем заголовки всех сообщения
        uid_list = self.query_uids(**kwargs)
        for uid in uid_list:
            yield (uid, self.fetch_header_by_uid(uid))

    def mark_seen(self, uid):
        try:
            # Помечаем письма как просмотренные входной параметр байт-идентификатор (\\Seen FLAG)
            self.server.uid('STORE', uid, '+FLAGS', '(\\Seen)')
            return True
        except IMAP4.error:
            return False

    def delete(self, uid):
        # Помечаем письма как удаленные входной параметр байт-идентификатор (\\Deleted FLAG)
        mov, data = self.server.uid('STORE', uid, '+FLAGS', '(\\Deleted)')
        self.server.expunge()

    def copy(self, uid, destination_folder):
        # Копируем письмо используя  байт-идентификатор в указанную папку
        return self.server.uid('COPY', uid, destination_folder)

    def move(self, uid, destination_folder):
        # Перемещаем письмо используя  байт-идентификатор в указанную папку
        if self.copy(uid, destination_folder):
            self.delete(uid)

    def headers(self, *args, **kwargs):
        folder = kwargs.get('folder', False)
        if folder:
            self.server.select(folder)
        return self.fetch_list_headers(**kwargs)

    def list_folders(self):
        # Возвращает имена всех папок
        return self.server.list()



