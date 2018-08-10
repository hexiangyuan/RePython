import re


def verify_user_name(name):
    if len(name) > 20 or len(name) < 2:
        return False
    return True


# 至少八个字符，至少一个字母和一个数字：
def verify_password(password):
    if len(password) > 24 or len(password) < 6:
        return False
    return True
