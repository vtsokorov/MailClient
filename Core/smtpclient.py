#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time, email, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate


def str_to_internaldate(datestring="", formatstring='%d.%m.%Y'):
    # Преобразуем строку к формату ('%d.%m.%Y')
    return formatdate(timeval=time.mktime(time.strptime(datestring, formatstring)), localtime=True)

class SMTPClient(object):

    def __init__(self, host, port, ssl = False):
        try:
            self._sender = None
            self._recipient = None
            self._date = None
            self._body = None
            self._attachments = []
            self.current_mail = None
            self.host = str(host).strip()
            self.port = str(port)
            self.use_ssl = ssl
            if self.use_ssl:
                self.connection = smtplib.SMTP_SSL(self.host, self.port)
            else:
                self.connection = smtplib.SMTP(self.host, self.port)
        except Exception:
            self.connection = None
            print("SMTP connection error")

    def login(self, username, password):
        try:
            self.username = username
            self.password = password
            if self.connection != None:
                self.connection.login(self.username, self.password)
                self.current_mail = MIMEMultipart()
                return True
            return False
        except Exception:
            self.current_mail = None
            print("SMTP login error")
            return False

    def send(self):
        if self.current_mail == None and self.connection == None:
            return -1
        if not len(self._recipient):
            return -2
        if not self._sender:
            self._sender = self.username
        if not self._date:
            self._date = formatdate(localtime=True)
        self.current_mail['From'] = self._sender
        self.current_mail['To'] = self._recipient
        self.current_mail['Date'] = self._date
        self.current_mail['Subject'] = self._subject
        body_type = 'plain'
        self.current_mail.attach(MIMEText(self._body, body_type, "utf-8"))
        for f in self._attachments:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(f,"rb").read())
            email.encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            self.current_mail.attach(part)
        self.connection.sendmail(self._sender, self._recipient, self.current_mail.as_string())
        self.connection.close()


    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = str_to_internaldate(value.strip()) # date in format dd.mm.yyyy (%d.%m.%Y)

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        self._sender = value.strip()

    @property
    def recipient(self):
        return self._recipient

    @recipient.setter
    def recipient(self, value):
        self._recipient = value.strip()

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value.strip()

    @property
    def body(self):
        pass

    @body.getter
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        self._body = value

