import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #웹에 글씨 써주는 모듈
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from account import *
from email.message import EmailMessage
import schedule


def job(): 
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\skwon\OneDrive\Desktop\PythonWorkspace'})
    browser = webdriver.Chrome(options=chrome_options)   #만약 웹드라이버가 다른 폴더에 있다면 경로 적어주기 예: "c:/downloads/chromedriver.exe"
    #browser.maximize_window()

    url = "http:\\imedidata.com"
    browser.get(url)
    browser.maximize_window()
    #time.sleep(1)

    elem = browser.find_element_by_id("session_username") #find_element_by_id도 가능
    elem.click()
    elem.send_keys("skwon1")
    #browser.back() #이전페이지
    #browser.forward() 
    #browser.refresh() #새로고침

    elem1= browser.find_element_by_id("session_password")
    elem1.click()
    elem1.send_keys("Janssen11")
    elem1.send_keys(Keys.ENTER)  #엔터키 누르는 효과

    #같은 값의 xpath가 여러 개면, find_elements_by_xpath(“A”)[2].click() 등으로 가능
    browser.find_elements_by_link_text("Rave EDC")[2].click() 
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") #제일 아래로 스크롤
    #browser.execute_script("window.scrollTo(0, Y);") 특정 위치까지만 스크롤다운

    browser.find_element_by_xpath("//*[@id='Table1']/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[7]/td[2]/a").click() 
    browser.find_element_by_id("PromptsBox_sg_Label").click()
    elem = browser.find_element_by_id("PromptsBox_sg_List")
    elem.click()
    elem.send_keys("KOR")
    elem.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element_by_id("PromptsBox_ms_LabelDiv").click()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.ID, 'PromptsBox_ms_FrontEndCBList_2'))) #expected condition-튜플값으로 설정이 나타날때까지 시도해보기/ Xpath/class등으로도 설정 가능
        browser.find_element_by_id("PromptsBox_ms_FrontEndCBList_2").click()
    except:
        print("실패")

    browser.execute_script("window.scrollTo(0, 0);")
    browser.find_element_by_id("RunTheReport").click()

    window_after = browser.window_handles[-1]  #새로 열린 윈도우 위치
    browser.switch_to.window(window_after) #새 윈도우로 이동

    try:
        WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.ID, 'btnExport'))) #expected condition-튜플값으로 설정이 나타날때까지 시도해보기/ Xpath/class등으로도 설정 가능
        browser.find_element_by_id("btnExport").click()
        time.sleep(2)
    except:
        print("실패")

    browser.quit()

######################################################################################
    # chrome_options = Options()
    # chrome_options.add_experimental_option('prefs', {'download.default_directory':r'C:\Users\skwon\OneDrive\Desktop\PythonWorkspace'})
    # browser = webdriver.Chrome(options=chrome_options)   #만약 웹드라이버가 다른 폴더에 있다면 경로 적어주기 예: "c:/downloads/chromedriver.exe"
    # #browser.maximize_window()

    url = "http:\\imedidata.com"
    browser.get(url)
    browser.maximize_window()
    #time.sleep(1)

    elem = browser.find_element_by_id("session_username") #find_element_by_id도 가능
    elem.click()
    elem.send_keys("skwon1")
    #browser.back() #이전페이지
    #browser.forward() 
    #browser.refresh() #새로고침

    elem1= browser.find_element_by_id("session_password")
    elem1.click()
    elem1.send_keys("Janssen11")
    elem1.send_keys(Keys.ENTER)  #엔터키 누르는 효과

    #같은 값의 xpath가 여러 개면, find_elements_by_xpath(“A”)[2].click() 등으로 가능
    browser.find_elements_by_link_text("Rave EDC")[2].click() 
    time.sleep(1)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") #제일 아래로 스크롤
    #browser.execute_script("window.scrollTo(0, Y);") 특정 위치까지만 스크롤다운

    browser.find_element_by_xpath("//*[@id='Table1']/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[11]").click() 
    browser.find_element_by_id("PromptsBox_sg_Label").click()
    elem = browser.find_element_by_id("PromptsBox_sg_List")
    elem.click()
    elem.send_keys("KOR")
    elem.send_keys(Keys.ENTER)
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element_by_id("PromptsBox_ms_LabelDiv").click()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    try:
        WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.ID, 'PromptsBox_ms_FrontEndCBList_2'))) #expected condition-튜플값으로 설정이 나타날때까지 시도해보기/ Xpath/class등으로도 설정 가능
        browser.find_element_by_id("PromptsBox_ms_FrontEndCBList_2").click()
    except:
        print("실패")

    browser.execute_script("window.scrollTo(0, 0);")
    browser.find_element_by_id("RunTheReport").click()

    window_after = browser.window_handles[-1]  #새로 열린 윈도우 위치
    browser.switch_to.window(window_after) #새 윈도우로 이동

    try:
        WebDriverWait(browser, 5).until(EC.presence_of_all_elements_located((By.ID, 'btnExport'))) #expected condition-튜플값으로 설정이 나타날때까지 시도해보기/ Xpath/class등으로도 설정 가능
        browser.find_element_by_id("btnExport").click()
        time.sleep(2)
    except:
        print("실패")

    browser.quit()

###########################################################################################
    msg = EmailMessage() #메시지 객체 생성
    msg["Subject"] = "PCR3011 Daily Query and Missing Page Report"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = "skwon@its.jnj.com"  #여러명에게 보내고 싶을때는 "A@gmail.com, B@gmail.com" / 
    msg.set_content("Dear All, Attached is today's Query and missing page Reports pulled from iMedidata.") #메일 본문 / 이 방법으로는 한글로도 전송 가능

    # #구글에서 MINE 타입 검색 후 maintype/subtype 참고하기
    # #이미지 첨부하기
    # # with open("icon.png", "rb") as f: #파일을 rb로 읽어와서 f로 저장
    # #     msg.add_attachment(f.read(), maintype = "image", subtype = "png", filename = f.name)

    # #워드를 PDF로 변환 후 첨부하기
    # # with open("test.pdf", "rb") as f:
    # #     msg.add_attachment(f.read(), maintype = "application", subtype="pdf", filename=f.name)

    # # #엑셀 첨부하기
    with open("C:/Users/skwon/Downloads/_EDCStdRpt-MissingPages.csv", "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="csv", filename=f.name)

    with open("C:/Users/skwon/Downloads/__EDCStdRpt-QueryDetails.csv", "rb") as f:
        msg.add_attachment(f.read(), maintype="text", subtype="csv", filename=f.name)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

#########################################################################################3
#schedule.every(10).minutes.do(job)
schedule.every().days.at("9:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)