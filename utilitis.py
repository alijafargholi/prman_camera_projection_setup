import smtplib

fromaddr = 'ali.jafargholi@gmail.com'
toaddrs  = 'ali.jafargholi@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = 'ali.jafargholli@gmail.com'
password = 'pass'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
# server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()