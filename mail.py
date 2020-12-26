import imaplib

M=imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
email=getpass.getpass("Email: ")
password=getpass.getpass("Password: ")
M.login(email,password)
