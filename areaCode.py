#!/usr/bin/python
from __future__ import print_function
import re
phone = "602-343-8747"
expr = r"(\d{3})-\d{3}-\d{4}"

match = re.match(expr,phone)
print("The phone number is: ", match.group())
print("The area code is: ", match.group(1))
