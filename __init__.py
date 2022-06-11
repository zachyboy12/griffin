"""
An easy front-end development maker for building websites. It was built for Javascript programmers. It, however, requires at least a little bit of
knowledge of CSS (mainly CSS), Javascript (if you want advanced functionality), and HTML (if you're serious). 
It can integrate with any front-end or back-end resource."""


class App:
    """
    Main class of griffin.
    """

    def __init__(self, filename: str) -> None:
        from os.path import abspath, dirname
        from os import system
        system(f'cd {abspath(dirname(filename))}')
        self.__HTMLCode = """<!DOCTYPE html>
<html>
"""
        self.__approute = ''


    def get_html_source_code(self):
        return self.__HTMLCode


    def Comment(self, comment: str):
        self.__HTMLCode += f"""<!--{comment}-->
"""
    
    
    def register(self, urlroute: str):
        """Registers an app by creating a directory.

        Args:
            urlroute (str): The route for the url.
        """
        from os import mkdir
        self.__HTMLCode += '</html>'
        if urlroute != '/':
            try:
                mkdir(urlroute[1:len(urlroute)])
            except:
                pass
            self.__approute = urlroute[1:] + 'index.html'
            open(self.__approute, 'w').write(self.__HTMLCode)
        else:
            self.__approute = 'index.html'
            open(self.__approute, 'w').write(self.__HTMLCode)


    def Image(self, url: str, alternatetext: str, Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<img src="{url}" alt="{alternatetext}" id="{Javascriptid}" class="{CSSid}" {headers}>
"""


    def Video(self, localurl: str, width=500, height=500, autoplay='true', Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<video src="{localurl}" width="{width}" height="{height}" autoplay="{autoplay}" id="{Javascriptid}" class="{CSSid}" {headers}></video>
"""


    def CSS(self, CSSstyle: str, headers=''):
        self.__HTMLCode += f"""<style {headers}>
    {CSSstyle}
</style>"""


    def JavaScript(self, JavaScript: str, headers=''):
        self.__HTMLCode += f"""<script type="text/javascript" {headers}>
    {JavaScript}
</script>"""


    def Articlebox(self, articlecontent: str, Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<article id="{Javascriptid}" class="{CSSid}" {headers}>{articlecontent}</article>
"""


    def Sidebar(self, sidebarcontent: str, Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<aside id="{Javascriptid}" class="{CSSid}" {headers}>{sidebarcontent}</aside>
"""


    def Audio(self, url: str, ifnotsupportedtext: str, loopaudio: bool, Javascriptid='', CSSid='', headers=''):
        if loopaudio:
            self.__HTMLCode += f"""<audio src="{url}" loop id="{Javascriptid}" class="{CSSid}" {headers}>{ifnotsupportedtext}</audio>
"""
        elif not loopaudio:
            self.__HTMLCode += f"""<audio src="{url}" id="{Javascriptid}" class="{CSSid}" {headers}>{ifnotsupportedtext}</audio>
"""
        

    def DirectedText(self, text: str, direction: str, Javascriptid='', CSSid='', headers=''):
        d = direction.lower()
        if d == 'right':
            self.__HTMLCode += f"""<bdo dir="ltr" id="{Javascriptid}" class="{CSSid}" {headers}>{text}</bdo>
"""
        elif d == 'left':
            self.__HTMLCode += f"""<bdo dir="rtl" id="{Javascriptid}" class="{CSSid}" {headers}>{text}</bdo>
"""


    def Hyperlink(self, url: str, text: str, seperatetab: bool, textifhovered: str, Javascriptid='', CSSid='', headers=''):
        if seperatetab:
            parameter = 'target="_blank"'
        elif not seperatetab:
            parameter = ''
        self.__HTMLCode += f"""<a href="{url}" {parameter} id="{Javascriptid}" class="{CSSid}" title="{textifhovered}" {headers}>{text}</a>
"""


    def Quote(self, quotetext: str, quoteurl: str, Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<blockquote cite="{quoteurl}" id="{Javascriptid}" CSSid="{CSSid}" {headers}>{quotetext}</blockquote>
"""


    def DocumentContent(self, content: str, Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<body id="{Javascriptid}" class="{CSSid}" {headers}>{content}</body>
"""


    def NewLine(self, Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<br id="{Javascriptid}" class="{CSSid}" {headers}>
"""


    def Button(self, buttontext: str, buttonname: str, buttontype: str, javascriptonclick: str, buttonvalue='', Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<button name="{buttonname}" type="{buttontype}" onclick="{javascriptonclick}" value="{buttonvalue}" id="{Javascriptid}" class="{CSSid}" {headers}>{buttontext}</button>
"""


    def CanvasScreen(self, Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<canvas id="{Javascriptid}" class="{CSSid}" {headers}></canvas>
"""


    def TableTitle(self, titletext: str, Javascriptid='', CSSid='', headers=''):
        self.__HTMLCode += f"""<caption id="{Javascriptid}" class="{CSSid}" {headers}>{titletext}</caption>
"""



    def Text(self, text: str, size='defult', Javascriptid='', CSSid='', headers=''):
        if size == 'defult':
            self.__HTMLCode += f"""<pre id="{Javascriptid}" class="{CSSid}" {headers}>{text}</pre>
"""
        else:
            self.__HTMLCode += f"""<h{size} id="{Javascriptid}" class="{CSSid}" {headers}>{text}</h{size}>
"""


class Griffin(App):
    """
    The clone of griffin.App()
    """
    pass


def tips_and_help():
    """
    Some tips and help for griffin. All you need to do is call this function.
    """
    print('@%  Griffin (https://github.com/zachyboy12/griffin)  @%')
    print('''To create an app, type in (with 'appname' replaced with your app name):
griffin.register_app('appname')
To make the app the homepage, type in:
griffin.register_app('')
Or:
griffin.register_app('/')
To make an http server, type in (With 'port' replaced with your port number (or none at all, since this is optional)):
griffin.runserver(4567)''')
    print('An Emmiter in griffin means anything in the webpage, like text, a button, even an invisible canvas: Because it emmits an HTTP response!')
    print('A Shape in griffin is an HTML element for reuse for python.')
    print('Views in griffin are called a percent. A parent directory for a percent is called the percent root. Griffin is used to make percents.')
        
        
def getshapetext(appname: str, Javascriptidname: str):
    linein = False
    thisline = ''
    for line in open(appname + '/index.html').read().split('\n'):
        if Javascriptidname in line:
            thisline = line
            linein = True
            break
    if linein is True:
        return str(thisline).split('<')[1][thisline.find('>'):]

    
    
def runserver(port=8000):
    """Runs a server at the givin port. After doing this, will make a new tab in your browser with the server url. *NOT FOR PRODUCTION*

    Args:
        port (int, optional): The port number. Defaults to 8000.
    """
    from os import system
    from webbrowser import open_new_tab as newtab
    
    print("""!!!! GRIFFIN SERVER !!!!
* WARNING: THIS SERVER IS NOT FOR PRODUCTION. USE A WSGI SERVER *
Running server...""")
    newtab(f'http://127.0.0.1:{port}/')
    system(f'python3 -m http.server {port} --bind 127.0.0.1')
