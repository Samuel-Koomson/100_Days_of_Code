import _datetime as dt
import random
import smtplib


current = dt.datetime.now()
week_day = current.weekday()

if week_day == 6:
    with open("quotes.txt", "r", encoding="utf-8") as quote_file:
        content = quote_file.readlines()
        quote_list = random.choice(content)
        print(quote_list)

    source_email = "kskoomson1989@outlook.com"
    password = "******"

    source_connection = smtplib.SMTP("smtp.outlook.office365.com", port=587)
    source_connection.starttls()
    source_connection.login(user=source_email, password=password)
    source_connection.sendmail(from_addr=source_email, to_addrs="kofipythondev@gmail.com", msg=f"Subject:Hello\n\n{quote_list}".encode('utf-8'))
    source_connection.close()



