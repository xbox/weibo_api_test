'''
Created on 2012-10-26

@author: Administrator
'''
from weibo import APIClient
if __name__=='__main__':
    APP_KEY = '1493558139'
    APP_SECRET = '528bd5aae83b0ed539320dff7d533811'
    CALLBACK_URL = 'http://an7.me'
    client = APIClient(app_key=APP_KEY,app_secret=APP_SECRET,redirect_url=CALLBACK_URL)
    starturl = client.get_authorize_url()
    import webbrowser
    webbrowser.open(starturl)
    code = raw_input('input code:')





