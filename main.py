"""
Author: Aldrienne Janne Maniti
Description: Determine if email address is valid
"""
import re
from MailVerify import MailVerify

# Step 1: Check email syntax is valid
# The domain part can contain alphanumeric characters (both upper and lower case).
# It can also contain a hyphen (-) if it is not the first or last character.
# The hyphen cannot be used consecutively.

# Step 2: Check domain using PyNslookup OR dnslookup

# Step 3: Email Ping

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    str_test_mail = 'aldriennej@gmail.com'
    str_invalid_mail = 'test@asdflkajdsf.dog'

    test_mail = MailVerify(str_test_mail)
    test_mail.validate_email()
    test_mail.validate_domain()
    test_mail.email_box_ping()
