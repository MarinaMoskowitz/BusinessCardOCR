#!/usr/bin/python

import string
import re
import argparse

class ContactInfo():
    email = ""
    phoneNumber = ""
    name = ""

    def __init__(self, **kwargs):
        """passing keyword arguments to the contructor"""
        self.email = kwargs["email"]
        self.phoneNumber = kwargs["phoneNumber"]
        self.name = kwargs["name"]

    def get_email(self):
        """returns the full name of the individual"""
        return format(self.email)

    def get_phone_number(self):
        """returns the email address"""
        return format(self.phoneNumber)

    def get_name(self):
        """returns the phone number formatted as a sequence of digits"""
        return format(self.name)


class BusinessCardParser():
    def email_helper(self, line):
        emailAsList = re.findall('\S+@\S+', line)
        email = ''.join(emailAsList)

        if email:
            return email
        else:
            return 'No email found'

    def phone_number_helper(self, line):
        phoneNumberAsList = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
        phoneNumber = ''.join(phoneNumberAsList)

        # checking to see if the contact card has a phone number
        if phoneNumber:
            # remove punctuation from phone number and format it
            phoneNumber = phoneNumber.translate(None, string.punctuation)
            return phoneNumber
        else:
            return 'No phone number found'


    def name_helper(self, line, nameInEmail):
        # getting the last word of each line, which is a potenntal last name
        lastName = line.split()[-1]

        # converting the characters in all of the potential last names to lowercase
        lastName = lastName.lower()

        # checking one of the potental last names of a person is in the email address
        if lastName in nameInEmail:
            name = line
            return name.strip()

    def get_contact_info(self, document):
        """function to get the name, phone number, and email address from the given business card"""
        email = None
        phoneNumber = None
        name = None

        if document is None:
            logging.warning("No Document Given. Empty ContactInfo Object Returned.")
            return ContactInfo()

        for line in document:
            # removing "\n" because it is annoying
            line.strip()

            # checking if there is an @ symbol in the line to get the email address
            if '@' in line:
                email = self.email_helper(line)

                # last name is always contained in email before @ symbol
                # must get everything before @ and not use entire email address because company name is after email address
                # and company name could also be a potental last name, so only want everything before @ symbol
                nameInEmail = email.split('@')[0]

            # checking to be sure it is a phone number and not a fax number
            if "Fax" not in line and sum(num.isdigit() for num in line) > 9:
                phoneNumber = self.phone_number_helper(line)

            # getting the name of the person
            if name == None:
                name = self.name_helper(line, nameInEmail)

        return ContactInfo(name=name, phoneNumber=phoneNumber, email=email)


def main():
    parser = argparse.ArgumentParser(description='A program to parse the name, phone number, and email from the given business card')
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    # reading the file in reverse order to get the email, which will be used to get the name
    document =  args.file.readlines()
    document.reverse()

    # creating a BusinessCardParser object
    BCP = BusinessCardParser()

    # getting the contact information from the given business card
    card = BCP.get_contact_info(document)

    # outputting the name, phone number, and email address for the given business card
    print "Name:", card.get_name()
    print "Phone:", card.get_phone_number()
    print "Email:", card.get_email()


if (__name__ == "__main__" ):
    main()



