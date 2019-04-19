# encoding = tf -8
'''
from util.ObjiectMap import *
from util.KeyBoradUtil import KeyboardKeys
from util.ClipboardUtil import Clipbard
from util.WaitUtil import WaitUtil
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time




def TestSendMaiWithAttachemtn():
    #创建Chrome 浏览器实例
    driver = webdriver.Chrome()
    #最大化浏览器窗口
    driver.maximize_window()

    print("启动成功")
    print("访问126登录网页")

    driver.get("https://www.126.com/")
    time.sleep(3)
    assert u"你的专业电子邮局"  in driver.title
    print(u"访问126邮箱登录成功成功")

    wait = WaitUtil(driver)
    wait.frame_available_and_switch_to_it("xpath","//iframe[contains(@id,'x-URS-iframe')]")
    print("输入登录用户名")
    username = getElement(driver,"xpath","//input[@name='email']")
    username.send_keys('sunsmileak007')
    print('输入登录密码')
    passwd = getElement(driver, "xpath","//input[@name='password']")
    passwd.send_keys('wgwgwg0051')
    print('登录')
    time.sleep(3)
    passwd.send_keys(Keys.ENTER)
    #等待五秒，一遍更成功的页面加载完成
    time.sleep(3)
    assert "网易邮箱" in driver.title
    print('登录成功')

    element = wait.visibility_element_located("xpath","//span[text()= '写 信']")
    element.click()

    print('写信')
    receiver =getElement(driver,"xpath","//div[contains(@id ,'_mail_emailinput')]/input" )
    #输入收信人地址
    receiver.send_keys("125081306@qq.com")

    # subject = getElements(driver,"xpath","//div[@aria-label="邮件主题输入框，请输入邮件主题"]/input")
    # 输入邮件主题
    subject = getElements(driver,"xpath","//div[@id='_mail_input_2_192']/input")
    subject.sund_kesy("新邮件")
    #设置粘贴板内容
    Clipbard.setTest(u"G:\\a.txt")
    #获取剪贴板内容
    Clipbard.getText()
    attachment =getElements(driver,"xpath","//a[@title ='点击添加附件']")
    attachment.click()
    time.sleep(3)
    #上传附件Windows弹窗中粘贴板中的内容
    KeyboardKeys.twoKeys("ctrl","v")
    #模拟回车键
    KeyboardKeys.oneKey("enter")

    #切换邮件正文frame
    # wait.frame_available_and_switch_to_it("xpath","//body[@class='nui-scroll']")
    wait.frame_available_and_switch_to_it("xpath","//iframe[@tabindex= '1']")
    # body = getElements("xpath","//body[@class='nui-scroll']")
    body = getElement(driver,"xpath","/thml/body")
    # body.click()
    body.send_keys("发给光荣之路的一封信")
    #切出邮件正文输入框
    driver.switch_to.default_content()
    print("写信完成")
    getElements(driver,"xpath","//span[text()= '发送']").click()
    print("邮件开始发送")
    assert "发送成功" in driver.page_source
    print("邮件发送成功")
    driver.quit()

if __name__ == "__main__":
    TestSendMaiWithAttachemtn()



#enconding = utf -8
from action.PageAction import *
from util.WaitUtil import WaitUtil

import  time
def TestSendMailWithAttachment():
    print("启动浏览器")
    open_browser('chrome')
    maximize_brower()
    print("访问登录126邮箱页面")
    visit_url("https://mail.126.com/")
    time.sleep(2)
    assert_string_in_pagesource(u"你的专业电子邮局")
    print(u"访问126登录页面成功")
    time.sleep(3)
    waitFrameToBeAvailableAndSwitchToIt("xpath","//iframe[contains(@id,'x-URS-iframe')]")
    print("输入登录名")
    input_string("xpath","//input[@name='email']","sunsmileak007")
    print("输入登录密码")
    input_string("xpath","//input[@name='password']","wgwgwg0051")
    click("id","dologin")
    time.sleep(3)
    assert_title(u"网易邮箱")
    print("登录成功")
    waitVisibilityOfElementLocated("xpath","//span[text()= '写 信']")
    click("xpath","//span[text()= '写 信']")
    print("开始写信")
    print("输入收件人地址")
    input_string("xpath","//div[contains(@id ,'_mail_emailinput')]/input","125081306@qq.com")
    print("输入邮件主题")
    input_string("xpath","//div[@aria-label='邮件主题输入框，请输入邮件主题']/input",'带附件的邮件')
    print("单击上传单击附件按钮")
    click("xpath","//a[@title ='点击添加附件']")
    time.sleep(3)
    print("上传附件")
    paste_string(u"G:\\KeyWordFromeWork\\a.txt")
    press_enter_key()
    waitFrameToBeAvailableAndSwitchToIt("xpath","//iframe[@tabindex= '1']")
    print("写入邮件正文")
    input_string("xpath","/thml/body","正文写给ssssssssss")
    switch_to_default_content()
    print("写信完成")
    print("开始发送邮件")
    click("xpath","//span[text()= '发送']")
    time.sleep(3)
    assert_string_in_pagesource("发送成功")
    print("邮件发送成功")
    close_browser()

if __name__ == "__main__":
    TestSendMailWithAttachment()

'''

from action.PageAction import *
from util.ParseExcel import ParseExcel
from config.VarConfig import *
import traceback
from util.Log import *
import time

# 设置此次测试环境的环境编码utf-8
# python3中 没有setedfaultencoding 语法
# import sys
# reload(sys)
# sys.setedfaultencoding("utf-8")

# 设置此次测试环境的环境编码utf-8
# import sys
# sys.getdefaultencoding()

# import sys
# import imp
# imp.reload(sys)


# 创建解析Excel对象
excelObj = ParseExcel()

# 将Excel数据文件加载到内存
excelObj.loadWorkBook(dataFilePath)


# 用例或用例步骤执结束后，向Excel 中写执行结果信息
def writeTestResult(sheetObj, rowNo, colsNo, testResult,
                    errorInfo=None, picPath=None):
    # 测试通过结果信息为绿色，失败为红色
    colorDict = {"pass": "green",
                 "faile": "red"}
    # 因为测试用例工作表和用例步骤sheet 表 中都有测试执行时间和
    # 测试结果列，定分义此字典对象是为了区具体应该写那个工作表
    colsDict = {
        "testCase": [testCase_runTime, testCase_testResult],
        "caseStep": [testStep_runTime, testStep_testResult]
    }
    try:
        # 在测试步骤sheet中，写入测试时间
        excelObj.writeCellCurrentTime(sheetObj,
                                      rowNo=rowNo, colsNo=colsDict[colsNo][0])
        # 在测试步骤中写入测试结果
        excelObj.writCell(sheetObj, content=testResult,
                          rowNo=rowNo, colsNo=colsDict[colsNo][1],
                          style=colorDict[testResult])

        if errorInfo and picPath:
            # 在测试步骤sheet中，写人测试结果
            excelObj.writCell(sheetObj, content=errorInfo,
                              rowNo=rowNo, colsNo=testStep_errorInfo)
            # 在测试步骤sheet中，写入异常异常截图路径
            excelObj.writCell(sheetObj, content=picPath,
                              rowNo=rowNo, colsNo=testStep_errorPic)
        else:
            # 在测试步骤sheet中，清空异常信息单元格
            excelObj.writCell(sheetObj, content="",
                              rowNo=rowNo, colsNo=testStep_errorInfo)

            # 在测试步骤 sheet 中，清空异常信息单元格
            excelObj.writCell(sheetObj, content="",
                              rowNo=rowNo, colsNo=testStep_errorPic)

    # except  Exception as e:
    #     print("写excel出错", traceback.print_exc())

    except Exception as e:
        # 在日志中写入详细异常堆栈信息
        logging.debug("写excel出错，%s" % traceback.format_exc())


def TestSendMailWithAttachment():
    try:
        # 跟进Excel 文件中的sheet名获取sheet对象
        caseSheet = excelObj.getSheetByName("测试用例")
        # print(type(caseSheet))
        # 获取测试用例sheet中是否执行列对象
        isExecuteColumn = excelObj.getColumn(caseSheet, testCase_isExecute)
        # 纪录执行成功的测试用例个数
        successfulCase = 0
        # 纪录需要执行的用例个数
        requiredCase = 0

        for idx, i in enumerate(isExecuteColumn[1:]):
            # 因为用例sheet中第一行为标题行，无需执行
            # print(i.value)
            # 循环遍历“测试用例 表中的测试用例，执行被设置为执行的用例
            if i.value.lower() == "y":
                requiredCase += 1
                # 获取“测试用例 表中第 idx + 2 行数据
                caseRow = excelObj.getRow(caseSheet, idx + 2)
                # print(caseRow)
                # 获取低idx +2 行 步骤sheet 单元格内容
                caseStepSheetName = caseRow[testCase_testStepSheetName - 1].value
                # print(caseStepSheetName)

                # 根据用例步骤名获取步骤sheet对象
                stepSheet = excelObj.getSheetByName(caseStepSheetName)
                # print(stepSheet)
                # 获取步骤sheet中步骤数
                stepNum = excelObj.getRowsNumber(stepSheet)
                # print(stepNum)
                # 纪录测试用例I的步骤成功数
                successfulSteps = 0
                # print("开始执行用例 %s" % (caseRow[testCase_testCaseName - 1].value))

                logging.info("------开始执行用例------ %s------" % caseRow[testCase_testCaseName - 1].value)

                for step in range(2, stepNum + 1):
                    # 因为步骤sheet 中的第一行为标题行，无需执行
                    # 获取步骤，sheet中的第step行对象
                    stepRow = excelObj.getRow(stepSheet, step)

                    # 获取关键字座位调用的函数名
                    keyWord = stepRow[testStep_keyWords - 1].value
                    # 获取操作元素定位方式作为调用函数的参数
                    locationType = stepRow[testStep_locationType - 1].value
                    # 获取操作元素的定位表达式作为调用函数的参数
                    locatorExpression = stepRow[testStep_locatorExpression - 1].value
                    # 获取操作值作为调用函数的参数
                    operateValue = stepRow[testStep_operateValue - 1].value

                    # 讲操作值作为数字类型的数据转成字符串类型，方便字符串拼接
                    if isinstance(operateValue, int):
                        operateValue = str(operateValue)
                    # print(keyWord, locationType, locatorExpression, operateValue)

                    expressionStr = ""
                    # 构造需要执行的Python语句
                    # 对应的事pageAction.py 文件中的页面动作函数调用的字符串表示
                    if keyWord and operateValue and locationType is None and locatorExpression is None:
                        expressionStr = keyWord.strip() + "(' " + operateValue + " ')"
                    elif keyWord and operateValue is None and locationType is None and locatorExpression is None:
                        expressionStr = keyWord.strip() + "()"
                    elif keyWord and locationType and operateValue and locatorExpression is None:
                        expressionStr = keyWord.strip() + \
                                        "(' " + locationType.strip() + "," + operateValue + "')"
                    elif keyWord and locationType and locatorExpression and operateValue:
                        expressionStr = keyWord.strip() + "('" + locationType.strip() + "','" + \
                                        locatorExpression.replace("'", '"').strip() + "','" + operateValue + "')"
                    elif keyWord and locationType and locatorExpression and operateValue is None:
                        expressionStr = keyWord.strip() + "('" + locationType.strip() + "','" + \
                                        locatorExpression.replace("'", '" ').strip() + "')"

                    # print (expressionStr)
                    try:
                        # 通过eval函数，将拼接的页面动作函数调用的字符串表示
                        # 当成有效的Python表达式执行，从而执行测试步骤的sheet中
                        # 关键字在ageAction.py 文件中对应的映射方法，
                        # 来完成页面元素的操作
                        eval(expressionStr)
                        # 在测试执行时间列写入执行时间
                        excelObj.writeCellCurrentTime(stepSheet, rowNo=step, colsNo=testStep_runTime)
                    except Exception as e:
                        # 截取异常屏幕截图
                        capturePic = capture_screen()
                        # 获取异常的堆栈信息
                        errorInfo = traceback.format_exc()
                        # 在测试步骤中写入失败信息
                        writeTestResult(stepSheet, step, "caseStep",
                                        "faile", errorInfo, capturePic)

                        # print("'步骤'%s '执行失败'" % (stepRow[testStep_testStepDescribe - 1].value))
                        logging.info("步骤'%s 执行通过！" % stepRow[testStep_testStepDescribe - 1].value)

                    else:
                        # 在测试步骤sheeet中写入成功信息
                        writeTestResult(stepSheet, step, "caseStep", "pass")
                        # 每成功一步 successfulSteps变量自增1
                        successfulSteps += 1
                        # print("步骤'%s 执行通过！" % (stepRow[testStep_testStepDescribe - 1].value))
                        logging.info("步骤'%s 执行通过！" % stepRow[testStep_testStepDescribe - 1].value)

                if successfulSteps == stepNum - 1:
                    # 当测试步骤sheet中的步骤都执行成功
                    # 方认为此测试用例通过，然后将成功信息写入
                    # 测试用例工作表中，否则吸入失败信息
                    writeTestResult(caseSheet, idx + 2, "testCase", "pass")
                    successfulCase += 1
                else:
                    writeTestResult(caseSheet, idx + 2, "testCase", "faild")
            # print("共 %d 条用例，%d 条需要被执行，本次执行通过%d条" % (len(isExecuteColumn) - 1, requiredCase, successfulCase))
        logging.info("共 %d 条用例，%d 条需要被执行，本次执行通过%d条" % (len(isExecuteColumn) - 1, requiredCase, successfulCase))

    except Exception as e:
        # 打印详细的异常堆栈信息
        print(traceback.print_exc())


if __name__ == "__main__":
    TestSendMailWithAttachment()
