import re
import dns
import dns.resolver
import smtplib

class MailVerify:
    def __init__(self, raw_email_address):
        self.raw_email_address = raw_email_address
        self.list_email_address = []
        self.user_address = ''
        self.domain_address = ''

    def validate_email(self):
        re_mail_validate = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.search(re_mail_validate,self.raw_email_address):
            print('valid')
            self.list_email_address = self.raw_email_address.split('@')
            self.user_address = self.list_email_address[0]
            self.domain_address = self.list_email_address[1]
            print(self.user_address)
            print(self.domain_address)
        else:
            return "Invalid"

    def validate_domain(self):
        try:
            result = dns.resolver.query(self.domain_address, 'MX')
            for exdata in result:
                print(exdata.exchange)
            return "Valid domain"
        except Exception as e:
            print(e)
            return "Invalid Domain"

    def email_box_ping(self):
        print("============ping=======")
        server = smtplib.SMTP(host='alt4.gmail-smtp-in.l.google.com', port=25)
        server.connect()
        print(server)