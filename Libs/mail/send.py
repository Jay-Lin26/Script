# coding = GBK
from Libs.mail.template import *
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import smtplib

# acceptUser = """
# 'linse.zhou@55haitao.com',
# 'taosheng@55haitao.com',
# 'miji.sarwono@55haitao.com',
# 'christine.li@55haitao.com'
# """


def send_email(message):
    mail_host = 'smtp.163.com'
    mail_user = 'z6466660@163.com'
    password = 'YZYPMEHFIAXZPQLJ'
    accept_user = 'linse.zhou@55haitao.com'
    content = MIMEText('%s' % edm_html.format(message=message), 'html', 'utf-8')
    content['Subject'] = Header('测试脚本报警邮件', 'utf-8').encode()
    content['From'] = Header('Maxrebates<noreply@maxrebates.com>', 'utf-8').encode()
    content['To'] = accept_user
    try:
        smtp = SMTP_SSL(mail_host)
        smtp.login(mail_user, password)
        smtp.sendmail(mail_user, accept_user, content.as_string())
        smtp.quit()
    except ConnectionRefusedError:
        return {'message': '邮件发送失败', 'code': 10061}
    except smtplib.SMTPAuthenticationError:
        return {'message': 'user has no permission', 'code': 550}
    except TimeoutError:
        return {'message': 'Connection timeout', 'code': 10062}
    except smtplib.SMTPDataError:
        return {'message': '邮件发送失败', 'code': 554}