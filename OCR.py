import string
import re
import sys
import argparse
import inspect, os
import os.path
from nameparser import HumanName


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

    document = args.file.readlines()

    name = ""
    phoneNumber = ""
    email = ""
    emailName = ""

    for line in document:
        # removing "\n" because it is annoying
        line.strip()
        line_parts = line.split()
        #print line_parts

        allInformation = ''.join(map(lambda x:x.lower(), line))
        #print allInformation


        # checking to be sure it is a phone number and not a fax number
        if "Fax" not in line:
            phoneNumberAsList = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
            phoneNumber = ''.join(phoneNumberAsList)

            # checking to see if the contact card has a phone number
            if phoneNumber:
                # remove punctuation from phone number and format it
                phoneNumber = 'Phone: ' + phoneNumber.translate(None, string.punctuation)
                #print phoneNumber

        # checking to see if the contact card has an email on it
        if '@' in line:
            emailAsList = re.findall('\S+@\S+', line)
            email = ''.join(emailAsList)

            if email:
                email = email
                #print email


                emailName = email.split('@')[0]
                #print emailName

        #if '@' not in line:
        name = HumanName(allInformation)

            #print name.last

        if name.last not in emailName:
            print 'no - ' + name.last
        else:
            print 'yes - ' + name.first

    # for line in document:
    #     allInformation = ''.join(map(lambda x:x.lower(), line))
    #     name = HumanName(allInformation)
    #     print allInformation
    #     print name.last

    #     # checking to be sure it is a phone number and not a fax number
    #     if "Fax" not in line:
    #         phoneNumberAsList = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
    #         phoneNumber = ''.join(phoneNumberAsList)

    #         # checking to see if the contact card has a phone number
    #         if phoneNumber:
    #             # remove punctuation from phone number and format it
    #             phoneNumber = 'Phone: ' + phoneNumber.translate(None, string.punctuation)
    #             #print phoneNumber

    #     # checking to see if the contact card has an email on it
    #     if '@' in line:
    #         emailAsList = re.findall('\S+@\S+', line)
    #         email = ''.join(emailAsList)

    #         if email:
    #             email = 'Email: ' + email
    #             #print email

    #             #name = ''.join(map(lambda x:x.lower(), line))
    #             #name = name.split('@')[0]

    #             #print name
    #     if name.last in email:
    #         print name.last



    #     lines = ''.join(map(lambda x:x.lower(), line))
    #     #print lines




if (__name__ == "__main__" ):
    main();

