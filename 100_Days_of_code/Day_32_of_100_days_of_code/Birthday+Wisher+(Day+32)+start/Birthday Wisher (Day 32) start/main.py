import smtplib

source_email = "kskoomson1989@outlook.com"
password = "**********"

source_connection = smtplib.SMTP("smtp.outlook.office365.com", port=587)
source_connection.starttls()
source_connection.login(user=source_email, password=password)
source_connection.sendmail(from_addr=source_email, to_addrs="kofipythondev@gmail.com", msg="Subject:Hello\n\nHello this is Sammy Koomson"
                                                                                            " and I am writing python automation codes")
source_connection.close()

"""the above code should work and be able to send the code but it fails execution as a 
result of google authentication issues
we can also make use of the with open option to prevent having to close the connection after use
"""
