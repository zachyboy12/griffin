"""
An easy front-end development maker for building websites. It was built for Javascript programmers. It, however, requires at least a little bit of
knowledge of CSS (mainly CSS), Javascript (if you want advanced functionality), and HTML (if you're serious). 
It can integrate with any front-end or back-end resource."""


__HTMLCode = """<!DOCTYPE html>
<html>
"""
apps = {}


def get_html_source_code():
    return __HTMLCode


def currentwebpage():
    """
    Alias of get_html_source_code. Used like this: griffin.apps['appname'] = currentwebpage()

    Returns:
        str: Source code of webpage
    """
    return get_html_source_code()


def Image(url: str, alternatetext: str, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<img src="{url}" alt="{alternatetext}" id="{Javascriptid}" class="{CSSid}" {headers}>
"""


def Video(localurl: str, width=500, height=500, autoplay='true', Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<video src="{localurl}" width="{width}" height="{height}" autoplay="{autoplay}" id="{Javascriptid}" class="{CSSid}" {headers}></video>
"""


def CSS(CSSstyle: str, headers=''):
    global __HTMLCode
    __HTMLCode += f"""<style {headers}>
{CSSstyle}
</style>"""


def JavaScript(JavaScript: str, headers=''):
    global __HTMLCode
    """Note: Cannot work with griffin.runserver"""
    __HTMLCode += f"""<script {headers}>
{JavaScript}
</script>"""


def Articlebox(articlecontent: str, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<article id="{Javascriptid}" class="{CSSid}" {headers}>{articlecontent}</article>"""


def Sidebar(sidebarcontent: str, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<aside id="{Javascriptid}" class="{CSSid}" {headers}>{sidebarcontent}</aside>"""


def Audio(url: str, ifnotsupportedtext: str, loopaudio: bool, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    if loopaudio:
        __HTMLCode += f"""<audio src="{url}" loop id="{Javascriptid}" class="{CSSid}" {headers}>{ifnotsupportedtext}</audio>"""
    

def DirectedText(text: str, direction: str, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    d = direction.lower()
    if d == 'right':
        __HTMLCode += f"""<bdo dir="ltr" id="{Javascriptid}" class="{CSSid}" {headers}>{text}</bdo>"""
    elif d == 'left':
        __HTMLCode += f"""<bdo dir="rtl" id="{Javascriptid}" class="{CSSid}" {headers}>{text}</bdo>"""


def Hyperlink(url: str, text: str, seperatetab: bool, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    if seperatetab:
        parameter = 'target="_blank"'
    elif not seperatetab:
        parameter = ''
    __HTMLCode += f"""<a href="{url}" {parameter} id="{Javascriptid}" class="{CSSid}" {headers}>{text}</a>
"""


def Quote(quotetext: str, quoteurl: str, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<blockquote cite="{quoteurl}" id="{Javascriptid}" CSSid="{CSSid}" {headers}>{quotetext}</blockquote>
"""


def DocumentContent(content: str, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<body id="{Javascriptid}" class="{CSSid}" {headers}>{content}</body>
"""


def NewLine(Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<br id="{Javascriptid}" class="{CSSid}" {headers}>
"""


def Button(buttontext: str, buttonname: str, buttontype: str, javascriptonclick: str, buttonvalue='', Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<button name="{buttonname}" type="{buttontype}" onclick="{javascriptonclick}" value="{buttonvalue}" id="{Javascriptid}" class="{CSSid}" {headers}>{buttontext}</button>
"""


def CanvasScreen(Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<canvas id="{Javascriptid}" class="{CSSid}" {headers}></canvas>
"""


def TableTitle(titletext: str, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<caption id="{Javascriptid}" class="{CSSid}" {headers}>{titletext}</caption>
"""



def Text(text: str, Javascriptid='', CSSid='', headers=''):
    global __HTMLCode
    __HTMLCode += f"""<pre id="{Javascriptid}" class="{CSSid}" {headers}>{text}</pre>
"""


def help():
    """
    Some help for griffin. All you need to do is call this function.
    """
    print('@%  Griffin (https://github.com/zachyboy12/griffin)  @%')
    print('''To create an app, type in (with 'appname' replaced with your app name):
griffin.apps['appname'] = griffin.currentwebpage()
To make an http server, type in (With 'port' replaced with your port number (or none at all, since this is optional)):
griffin.runserver(4567)''')
    print('An Element in griffin means anything in the webpage, like text, a button, even an invisible canvas!')
    print('Copyright @ zachyboy12 (https://github.com/zachyboy12), all rights reserved.')




def runserver(port=8000):
    global __HTMLCode
    from os import system, mkdir
    from webbrowser import open_new_tab as newtab
    for appname in apps:
        __HTMLCode += '</html>'
        if appname != '/':
            try:
                mkdir(appname)
            except:
                pass
            open(appname + '/index.html', 'w').write(__HTMLCode)
            newtab(f'http://127.0.0.1:{port}/' + appname)
        else:
            open('index.html', 'w').write(__HTMLCode)
            newtab(f'http://127.0.0.1:{port}/')
        system(f'python3 -m http.server {port} --bind 127.0.0.1')
