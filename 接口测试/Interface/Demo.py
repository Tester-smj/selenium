#coding=utf-8
import xlrd,os,requests,logging
import sys
xlsfile1 = os.path.join(os.getcwd(),'testCaseFile.xlsx')
#保存log
log_file = os.path.join(os.getcwd(),'log/sas.log')
log_format = '[%(asctime)s] [%(levelname)s] %(message)s'     #配置log格式
logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(log_format)
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
def excel_data(xlsfile):
  #读取测试用例
  xlsfile1 = os.path.join(os.getcwd(),'testCaseFile.xlsx')
  if not os.path.exists(xlsfile1):
    logging.error('测试用例文件不存在！')
    sys.exit()
  book = xlrd.open_workbook(xlsfile)
  api_sheet = book.sheet_by_index(0)
  nrows = api_sheet.nrows
  #遍历用例
  for i in range(1,nrows):
    num = api_sheet.cell(i,0).value
    password = api_sheet.cell(i,1).value
    api_host = api_sheet.cell(i,2).value
    request_url = api_sheet.cell(i,3).value
    method=api_sheet.cell(i,4).value
    data=api_sheet.cell(i,6).value
    url= api_host+request_url
    headers = {'content-type': 'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko','Accept':'application/x-ms-application, image/jpeg, application/xaml+xml, image/gif, image/pjpeg, application/x-ms-xbap, */*','Accept-Language':'zh-CN'}
    cookies={'Transfer-Encoding': 'chunked', 'Set-Cookie': 'JSESSIONID=; Path=/sbborders/; HttpOnly, sidd=7421BEEDAE6F253D15DB775C6FD2871E; Expires=Mon, 25-Jul-2016 10:23:07 GMT', 'Content-Type': 'application/json;charset=utf-8', 'Date': 'Fri, 15 Jul 2016 10:23:07 GMT', 'Server': 'Apache-Coyote/1.1'}
    #字符串强转字典类型
    tata1=eval(data)
    # print(type(data))
    # print(type(tata1))
    if method == 'Get':
      z=requests.get(url,tata1,headers=headers,cookies=cookies)
    else :
      z=requests.post(url,tata1,headers=headers,cookies=cookies)
    status =z.status_code
    # print(z.text)
    if status == 200 :
      logging.info('用例编号'+str(num) + '执行结果是:'+'成功，返回code是' + str(status) + ', ')
      logging.warn(z.text)
    else:
      logging.info('用例编号'+str(num) + '执行结果是:' + '失败！返回code是' + str(status) + ', ')
      logging.warn(z.text)
    if request_url=='/login':
        print(z.cookies)
        print(z.headers)

from email.mime.text import MIMEText
import smtplib,ConfigParser

def get_conf():
    conf_file = ConfigParser.ConfigParser()

    conf_file.read(os.path.join(os.getcwd(),'conf.ini'))

    conf = {}

    conf['sender'] = conf_file.get("email","sender")

    conf['receiver'] = conf_file.get("email","receiver")

    conf['smtpserver'] = conf_file.get("email","smtpserver")

    conf['username'] = conf_file.get("email","username")

    conf['password'] = conf_file.get("email","password")

    return conf
def sendMail(text):
      mail_info = get_conf()
      sender = mail_info['sender']
      receiver = mail_info['receiver']
      subject = '[AutomationTest]接口自动化测试报告通知'
      smtpserver = mail_info['smtpserver']
      username = mail_info['username']
      password = mail_info['password']
      msg = MIMEText(text,'html','utf-8')
      msg['Subject'] = subject
      msg['From'] = sender
      msg['To'] = ''.join(receiver)
      smtp = smtplib.SMTP()
      smtp.connect(smtpserver)
      smtp.login(username, password)
      smtp.sendmail(sender, receiver, msg.as_string())
      smtp.quit()
if __name__=="__main__":
  excel_data(xlsfile1)