# -*- coding: utf-8 -*-
"""
Created on Fri May 15 08:40:22 2026

@author: Anh Thu
"""

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# Đọc file excel
df = pd.read_excel("contacts.xlsx")

# Gmail account
EMAIL = "kute24thu@gmail.com"
PASSWORD = "yfxv rvhq oizs iadv" 


# Kết nối gmail
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(EMAIL, PASSWORD)

for index, row in df.iterrows():

    company = row["company"]
    person = row["person"]
    receiver = row["email"]

    subject = "Thư mời hợp tác"
    body = f"""
Kính gửi {person},

Em là Anh Thư đến từ CLB XYZ.

Hiện tại CLB chúng em đang tổ chức chương trình ABC và rất mong có cơ hội được đồng hành cùng {company} với vai trò nhà tài trợ.

Chúng em tin rằng chương trình sẽ mang lại nhiều giá trị truyền thông tích cực và phù hợp với hình ảnh doanh nghiệp.

Em xin phép gửi proposal đính kèm để anh/chị tham khảo thêm.

Trân trọng,
Anh Thư
Ban Đối ngoại - Đội CTV khoa Tài 
"""

    msg = MIMEText(body)

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = EMAIL
    msg["To"] = receiver

    server.sendmail(EMAIL, receiver, msg.as_string())

    print(f"Đã gửi tới {company}")

server.quit()
