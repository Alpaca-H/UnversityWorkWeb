# -*- coding:utf-8 -*-
__author__ = 'hzj'


import  random,string
from apps.user.models import EamilVerifyRecord
from django.core.mail import send_mail
from SearchSystem.settings import EMAIL_FROM


def email_link_send(email,sent_type="register"):
    email_record = EamilVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = sent_type
    email_record.save()

    url = "http://127.0.0.1:8000/active/{0}"

    if sent_type == "register":
        email_title = "账号注册激活链接"
        email_body = "非常感谢您能够注册我们的网站,请点击以下链接完成注册{0}".format(url.format(code))
    elif sent_type == "forget":
        email_title = "重新修改密码链接"
        email_body = "哇,怎么能把这么重要的密码忘记呢，请点击以下链接完成密码的重置{0}".format(url.format(code))

    send_status  = send_mail(email_title,email_body,EMAIL_FROM,[email])
    if send_status:
        pass




def random_str(slen=16):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))  #生成随机字符串



# if __name__ == '__main__':
#     ss = random_str(10)
#     print(ss)