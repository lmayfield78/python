import requests
from urls.all import All_urls
from utilities.smtp import SendMessage
from shops.all_shop_links import all_shop_urls


def status_200_check():
    '''
    This function will go through all of the urls in urls.all and verify if they return a 200 or 400.
    If any urls return either a 400 or 500 status, an email will be sent out to all watching teammates.

    '''
    email = SendMessage()
    go = All_urls()
    urls = go.urls
    go2 = all_shop_urls()
    urls2 = go2.shop_urls

    # This covers funnels

    for i in urls.values():
        print('Checking : ' + i)
        result = requests.get(i)
        print(str(result) + '\n')
        error = i + " returns " + str(result)

        code = result.status_code # print this to view the int code.

        if code == 404:
            email.sendEmail(error)

        elif code == 500:
            email.sendEmail(error)

    #This covers all e-commerce urls

    for i in urls2.values():
        print('Checking : ' + i)
        result = requests.get(i)
        print(str(result) + '\n')
        error = i + " returns " + str(result)

        code = result.status_code # print this to view the int code.

        if code == 404:
            email.sendEmail(error)

        elif code == 500:
            email.sendEmail(error)


status_200_check()
