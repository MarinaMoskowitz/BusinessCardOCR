import string
import re
import sys
import argparse
import inspect, os
import os.path


class ContactInfo():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    document = args.file.readlines()

    name = ""
    phoneNumber = ""
    email = ""

    def getName():
        '''
        returns the full name of the individual
        '''

    def getPhoneNumber():
        '''
        returns the phone number formatted as a sequence of digits
        '''
        for line in document:
        # removing "\n" because it is annoying
            line.strip()
            line_parts = line.split()
            print line_parts

            # checking to be sure it is a phone number and not a fax number
            if "Fax" not in line:
                phoneNumberAsList = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
                phoneNumber = ''.join(phoneNumberAsList)

                # checking to see if the contact card has a phone number
                if phoneNumber:
                    # remove punctuation from phone number and format it
                    phoneNumber = 'Phone: ' + phoneNumber.translate(None, string.punctuation)
                    return phoneNumber

    def getEmailAddress():
        '''
        returns the email address
        '''
        for line in document:
            # removing "\n" because it is annoying
            line.strip()
            line_parts = line.split()
            print line_parts

            # checking to see if the contact card has an email on it
            if '@' in line:
                emailAsList = re.findall('\S+@\S+', line)
                email = ''.join(emailAsList)

                if email:
                    email = 'Email: ' + email
                    return email

# class BusinessCardParser:
#     def contact_info(document):


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    # reading the file in reverse order to get the email, which will be used to get the name
    document = reversed(args.file.readlines())

    nameInEmail = ""

    for line in document:
        # removing "\n" because it is annoying
        line.strip()
        line_parts = line.split()

        # checking to be sure it is a phone number and not a fax number
        if "Fax" not in line:
            getPhoneNumber(line)

        # checking if there is an @ symbol in the line to get the email address
        if '@' in line:
            email = getEmail(line)

            # last name is always contained in email before @ symbol
            # must get everything before @ and not use entire email address because company name is after email address
            # and company name could also be a potental last name, so only want everything before @ symbol
            nameInEmail = email.split('@')[0]

        # getting the name of the person
        getName(line, nameInEmail)

def getPhoneNumber(line):
        phoneNumberAsList = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
        phoneNumber = ''.join(phoneNumberAsList)

        # checking to see if the contact card has a phone number
        if phoneNumber:
            # remove punctuation from phone number and format it
            phoneNumber = 'Phone: ' + phoneNumber.translate(None, string.punctuation)
            return phoneNumber


def getEmail(line):
    emailAsList = re.findall('\S+@\S+', line)
    email = ''.join(emailAsList)

    if email:
        return email

def getName(line, nameInEmail):
    # getting the last word of each line, which is a potenntal last name
    lastName = line.split()[-1]

    # converting the characters in all of the potential last names to lowercase
    lastName = ''.join(map(lambda x:x.lower(), lastName))

    # checking one of the potental last names of a person is in the email address
    if lastName not in nameInEmail:
        print 'not in emailName - ' + lastName
    else:
        print 'yes in emailName - ' + lastName


if (__name__ == "__main__" ):
    main();

