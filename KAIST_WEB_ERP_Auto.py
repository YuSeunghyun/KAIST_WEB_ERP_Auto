from time import time, sleep as wait
from datetime import date, datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def select_option(name, option):
    elem = d.find_element_by_xpath("//select[@name='%s']"%name)
    options = elem.find_elements_by_tag_name("option")
    option = options[[str(i.text) for i in options].index(option)]
    option.click()
    
# 파일 읽기
d = {}
with open("../여기에 필요한 내용을 용도에 맞게 입력하세요.txt", 'r', encoding="utf-8") as f:
    for line in f:
        (key, val) = line.replace('\n','').replace(" =","=").replace("= ","=").split(' #')[0].split('=')
        d[key] = val.replace('"','').replace("'",'')
for (n, v) in d.items():
    exec('%s=%s' % (n, repr(v)))
수량 = int(수량)
    
if 검수예정일 == '오늘':
    검수예정일 = date.today().strftime("%Y-%m-%d")
    
    
URL = "https://webs.kaist.ac.kr/erp2/main.do?mode=mainHome&language=ko"
d = webdriver.Chrome('chromedriver.exe')
d.get(URL)
d.implicitly_wait(0.5)
d.switch_to.window(d.window_handles[-1])
d.find_element_by_xpath("//input[@placeholder='아이디']").send_keys(ID)
d.find_element_by_xpath("//input[@placeholder='비밀번호']").send_keys(PW)
d.find_element_by_xpath("//input[@value='로그인']").click()
wait(0.5)
d.switch_to.window(d.window_handles[-1])
d.find_element_by_xpath("//a[@href='/erp2/board.do?mode=bearerPoNotice']").click()
wait(0.5)
d.find_element_by_xpath("//div[@class='caption']").click()
wait(0.5)
d.find_element_by_xpath("//input[@id='po_purpose']").send_keys(문서제목)
d.switch_to.window(d.window_handles[-1])
select_option('poHeader.billType', '신용카드영수증')
wait(0.5)
d.find_element_by_xpath("//a[@name='cardPop']").click()
wait(0.5)
d.switch_to.frame('popFrame')
# 가장 처음꺼 선택
d.find_element_by_xpath("//tr[@class='line_00']/../tr[2]/td/a/img").click()
d.switch_to.default_content()
elem = d.find_element_by_xpath("//input[@name='poHeader.cardUserName']")
elem.send_keys(카드실사용자)
elem.find_element_by_xpath("../a[1]").click()
wait(1)
d.switch_to.frame('popFrame')
elem = d.find_element_by_xpath("//*[text() = '%s']"%내개인번호)
elem.find_element_by_xpath("../td[last()]").click()
wait(0.5)
d.switch_to.default_content()
select_option('poHeader.org_id', 캠퍼스구분)
select_option('poHeader.poType', 물품용도)
d.find_element_by_xpath("//input[@id='chkInfo']").click()
elem = d.find_element_by_xpath("//input[@name='poHeader.inspectPersonNm']")
elem.send_keys(검수예정자)
elem.find_element_by_xpath("../img[1]").click()
wait(0.5)
d.switch_to.frame('popFrame')
elem = d.find_element_by_xpath("//*[text() = '%s']"%검수예정자개인번호)
elem.find_element_by_xpath("../td[last()]").click()
wait(0.5)
d.switch_to.default_content()
d.find_element_by_xpath("//input[@name='poHeader.inspectDate']").send_keys(검수예정일)
select_option('lineType', 라인유형)
elem = d.find_element_by_xpath("//input[@name='using_person_name']")
elem.send_keys(실사용책임자)
elem.find_element_by_xpath("../img[1]").click()
wait(0.5)
d.switch_to.frame('popFrame')
elem = d.find_element_by_xpath("//*[text() = '%s']"%실사용책임자개인번호)
elem.find_element_by_xpath("../td[last()]").click()
wait(0.5)
d.switch_to.default_content()
select_option('assetType', 자산인식여부)
select_option('project_equipment_yn', 연구장비여부)
select_option('project_facility_yn', 연구시설여부)
d.find_element_by_xpath("//input[@name='quantity']").send_keys(수량)
elem = d.find_element_by_xpath("//input[@name='oldSupplyAmount']")
증빙합계 = int(elem.get_attribute("value").replace(',',''))
단가 = int(증빙합계 / 수량)
d.find_element_by_xpath("//input[@name='unit_price']").send_keys(단가)
