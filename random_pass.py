import random

from click import echo


low_case = "abcdefghijklmnopqrstuvwxy"
up_case = "ABCDEFGHIJKLMNOPQSTUVWXYZ"

number = "0123456789"
symbols = "@#$%&!"
make_pass = low_case + up_case + number + symbols

length_pass = 8

password = "".join(random.sample(make_pass, length_pass))

echo(f"\nyour password is: {password}\n")