import re
import dnspython as dns
import dns.resolver

class MailVerify:
    def __init__(self, raw_email_address):
        self.raw_email_address = raw_email_address
        self.list_email_address = raw_email_address.split('@')
        self.user_address = self.list_email_address[0]
        self.domain_address = self.list_email_address[1]

    def validate_email(self):
        re_mail_validate = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if re.search(re_mail_validate,self.email_address):
            return "valid"
        else:
            return "false"

        