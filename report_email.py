from reports import generate_report
import os
from datetime import date
from emails import generate_email
from emails import send_email


def main():
    path = '/test_folder/'
    paragraph = ''
    for file in os.listdir(path):
        with open(path + file) as description:
            lines = description.readlines()
            paragraph += 'name: ' + lines[0] + '<br/>'
            paragraph += 'weight: ' + lines[1] + '<br/><br/>'
    report_title = 'Processed Update on {}'.format(
        date.today().strftime('%b %d,%Y'))
    generate_report('processed.pdf', report_title, paragraph)
    message = generate_email('automation@example.com', 'recipiernt@example.com', 'Upload Completed - Online Fruit Store',
                          'All fruits are uploaded to our website successfully. A detailed list is attached to this email.', r'C:\Users\SaraRyan\processed1.pdf')
    send_email(message)
    print('ran')

if __name__ == '__main__':
    main()
