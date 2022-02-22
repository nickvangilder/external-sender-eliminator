import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

port = 465
smtp_server = "mail-server.com"
login = "username" 
password = "password"
sender_email = str(Header('No Reply <noreply@some-domain.com>'))
receiver_email = "john.smith@company.com"
message = MIMEMultipart("alternative")

#these are tabs to designed to push the [external] designation out of the preview pane. Some email gateway policies won't append "external" to the front of the message if it's elsewhere in the subject line
message['Subject'] = 'Hello \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t [external]'
#message['X-Priority'] = '1'

message["From"] = sender_email
message["To"] = receiver_email

text = """\
"""


# some email gateways will insert their "external sender" warnings into a table. To prevent rendering, you can mess with the table properties to make the text unreadable within the email client
html = """\
<!DOCTYPE html>
<html>

<head>
<style type="text/css">


table  	{
		display: none !important;
		}
		
.test	{
	  	display: block !important;
	  	color: black;
     	}
		

</style>
</head>
<body>
	<class="test">This is a test</p>
</body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

#print(message)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(login, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print('Sent') 