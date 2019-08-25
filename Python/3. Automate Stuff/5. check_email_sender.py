import imaplib, email

def getBody(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)

user = '#####'
password = '######'
imap_url = '######'

con = imaplib.IMAP4_SSL(imap_url)
con.login(user, password)
con.select('INBOX')

result, data = con.fetch(b'10','(RFC822)')

print(data)


# print(con.select('INBOX'))
# print(con.select('Sent'))
