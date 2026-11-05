# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]

# set comprehension to extract a clean, unique set of lowercase email addresses
clean_emails = {email.lower() for email in raw_emails}

# print the clean set of email addresses
print(clean_emails)

# Optional - consider the case where some of the emails are not valid (i.e., without the @ in the email address).
raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com", "admin@site.com", "UserB@yahoo.com"]
valid_emails = {email.lower() for email in raw_emails2 if '@' in email}
print(valid_emails)
