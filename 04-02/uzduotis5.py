"""
Parašykite programą, apibrėžiančią funkciją extract_email_addresses(),
kuri priima tekstą kaip įvestį ir iš teksto ištraukia visus el. pašto adresus
"""

# import re
# def extract_emails(text):
#         # Define the regular expression pattern for an email address
#         pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#
#         # Use the findall() function to extract all email addresses from the text
#         emails = re.findall(pattern, text)
#
#         return emails
# text = "Contact us at email@example.com or support@example.org for assistance."
# emails = extract_emails(text)
# print(emails)


def extract_email_addresses():
    enter = input("Enter text containing Email addresses: ")
    emails = []
    for email in enter.split():
        if "@" in email and "." in email:
            emails.append(email)
        return emails


emails = extract_email_addresses()
print(emails)


#
# tekstas=('Contact us at email@example.com or support@example.org for assistance')
# kapotas_tekstas = tekstas.split()
# def extract_email_addresses(tekstas:str) -> str:
#         if kapotas_tekstas == '@' and kapotas_tekstas == '.':
#                 return
#
# a = kapotas_tekstas
# print(a)
