# -*- coding: UTF-8 -*-
from aip import AipSpeech

APP_ID = '5969165'
API_KEY = 'jGrO7KspSytuSntkIk5Lrp8a'
SECRET_KEY = 'et37Is5TN7LpBdWOd8skCcoZ48dp5PGf'


def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


def main():
    file_name = '2018-05-22_18_55_13.wav'
    content = get_file_content(file_name)
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.asr(content)
    print(result)


if __name__ == '__main__':
    print("hello")
    main()
