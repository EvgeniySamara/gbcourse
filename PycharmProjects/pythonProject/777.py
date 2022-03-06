from jinja2 import *

def mkpage(text):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template('shablon.html')

    rendered_page = template.render(title1=text)
    return rendered_page


def application(environ, start_response):
    """
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    # сначала в функцию start_response передаем код ответа и заголовки
    start_response('200 OK', [('Content-Type', 'text/html')])

    print (environ)



    inputparams = environ['QUERY_STRING'].split('&')
    if len(inputparams)>0: print ('нам передали параметры',inputparams)
    if environ['REQUEST_METHOD']=='GET':
        pn = environ['PATH_INFO'].strip('/')
        print (pn)
        if pn == 'contacts':
            mp = mkpage('Контакты')
            return [bytes(mp, 'utf-8')]

        elif pn =='page1':
            mp = mkpage('Страница 1')
            return [bytes(mp, 'utf-8')]
        else:
            return [b'mainpage']

# http://127.0.0.1:8000/contacts/?name=max&age=18
# http://127.0.0.1:8000/page1/?name=max&age=18
'''
{'wsgi.errors': <gunicorn.http.wsgi.WSGIErrorsWrapper object at 0x7f94130af670>, 'wsgi.version': (1, 0), 'wsgi.multithread': False, 'wsgi.multiprocess': False, 'wsgi.run_once': False, 'wsgi.file_wrapper': <class 'gunicorn.http.wsgi.FileWrapper'>, 'wsgi.input_terminated': True, 'SERVER_SOFTWARE': 'gunicorn/20.1.0', 'wsgi.input': <gunicorn.http.body.Body object at 0x7f94130aff70>, 'gunicorn.socket': <socket.socket fd=9, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 39100)>, 'REQUEST_METHOD': 'GET', 'QUERY_STRING': 'name=max&age=18', 'RAW_URI': '/some_url/?name=max&age=18', 'SERVER_PROTOCOL': 'HTTP/1.1', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'HTTP_ACCEPT_LANGUAGE': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_SEC_FETCH_DEST': 'document', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_SEC_FETCH_USER': '?1', 'wsgi.url_scheme': 'http', 'REMOTE_ADDR': '127.0.0.1', 'REMOTE_PORT': '39100', 'SERVER_NAME': '127.0.0.1', 'SERVER_PORT': '8000', 'PATH_INFO': '/some_url/', 'SCRIPT_NAME': ''}


'''