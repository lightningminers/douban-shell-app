__author__ = 'xiangwenwen'
import douban_client
import http.client
import urllib.parse
import urllib.request
import http.cookiejar
import json
import config
COOKIE = http.cookiejar.CookieJar()

#填写自己申请的api key
# API_KEY = ''
# API_SECRET = ''
DOUBAN_DIC = {}
douban_key = config.configKey()
API_KEY = douban_key['API_KEY']
API_SECRET = douban_key['API_SECRET']
def addOAuth():
    SCOPE = 'douban_basic_common,shuo_basic_r,shuo_basic_w,book_basic_r,book_basic_w'
    CALLBACK_URL = 'http://wenren.ddnode.com/search'
    client = douban_client.DoubanClient(API_KEY,API_SECRET,CALLBACK_URL,SCOPE)
    print('welcome to douban shell center ')
    # print('oauth URL :' + client.authorize_url)
    email = input('enter the your email: ')
    emailpass = input('enter the your password: ')
    doubanData = {
        'user_email':email,
        'user_passwd':emailpass,
        'confirm':'授权'
    }
    print(doubanData)
    #数据提交给豆瓣，让用户赋权限。
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(COOKIE))
    response = opener.open(client.authorize_url,urllib.parse.urlencode(doubanData).encode())
    #注意，两个问题。
    #字符串，以及其他类型的数据，需要转字节
    #回调服务器，不要做其他的操作，包括状态码
    # print(response.headers)
    # print(response.info())
    # help(response)
    responseData = response.read().decode()
    try:
        responseCode = json.loads(responseData)
    except ValueError:
        return 'error'
    code = responseCode['code']
    opener.close()
    client.auth_with_code(code)
    #token
    token_code = client.token_code
    refresh_token_code = client.refresh_token_code
    client.refresh_token(refresh_token_code)
    DOUBAN_DIC['token_code'] = token_code
    DOUBAN_DIC['refresh_token_code'] = refresh_token_code
    DOUBAN_DIC['code'] = code
    print(DOUBAN_DIC)
    return client
    pass