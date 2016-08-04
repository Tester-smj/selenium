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
    num = api_sheet.cell(i,0)
    password = api_sheet.cell(i,1)
    api_host = api_sheet.cell(i,2)
    request_url = api_sheet.cell(i,3)
    data=api_sheet.cell(i,6)
    cv = num.value
    pv = api_host.value
    sv = request_url.value
    url= pv+sv
    tata=data.value
    tata1=eval(tata)
    # print(pv)
    # print(sv)
    # print(url)
    # print(tata1)
    z=requests.get(url,tata1)
    status =z.status_code
    if status == 200 :
      logging.info('用例编号'+str(cv) + '执行结果是:'+'成功，返回code是' + str(status) + ', ')
    else:
      logging.info('用例编号'+str(cv) + '执行结果是:' + '失败！返回code是' + str(status) + ', ')
if __name__=="__main__":
  excel_data(xlsfile1)