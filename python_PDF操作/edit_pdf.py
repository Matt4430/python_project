import re
import pdfplumber

path = './TCL科技：TCL科技集团股份有限公司2016年面向合格投资者公开发行公司债券（第二期）跟踪评级报告（2021）.pdf'
with pdfplumber.open(path) as pdf:
    first_page = pdf.pages[14]
    content = first_page.extract_tables()
    for i in content:
        for j in i:
            print(j)