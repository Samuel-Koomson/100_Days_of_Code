##################### Extra Hard Starting Project ######################
import random
import smtplib
import pandas
import datetime as dt


# 1. Update the birthdays.csv
birthday = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
week_day = today.weekday()
print(week_day)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if week_day == 6:
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt", "r") as sample_letters:
        ready_letter = sample_letters.readlines()

    for index, row in birthday.iterrows():
        if row.day == today.day and row.month == today.month:
            name = row.name
            letter_template = random.choice(ready_letter)
            final_letter = letter_template.replace('[NAME]', 'name')

    source_email = "kskoomson1989@outlook.com"
    password = "Koomson@1989"

    source_connection = smtplib.SMTP("smtp.outlook.office365.com", port=587)
    source_connection.starttls()
    source_connection.login(user=source_email, password=password)
    source_connection.sendmail(from_addr=source_email, to_addrs="kofipythondev@gmail.com, ",
                               msg=f"Subject:Hello\n\n{final_letter}".encode('utf-8'))
    source_connection.close()
# 4. Send the letter generated in step 3 to that person's email address.




