"""An easy front-end development maker for building websites. It, however, requires at least a little bit of
knowledge of CSS (mainly CSS), Javascript (if you want advanced functionality), and HTML (if you're hardcore). 
It can integrate with any front-end or back-end resource."""


__HTMLCode = ''


def Image(url: str, alternatetext: str, Javascriptid='', CSSid='', headers=''):
    return 'WEBSIG', f"""<img src="{url}" alt="{alternatetext}" id="{Javascriptid}" class="{CSSid}" {headers}>
"""


def Video(localurl: str, width=500, height=500, autoplay='true', Javascriptid='', CSSid='', headers=''):
    return 'WEBSIG', f"""<video src="{localurl}" width="{width}" height="{height}" autoplay="{autoplay}" id="{Javascriptid}" class="{CSSid}" {headers}></video>
"""


def CSS(CSSstyle: str, headers=''):
    return 'WEBSIG', f"""<style {headers}>
{CSSstyle}
</style>"""


def JavaScript(JavaScript: str, headers=''):
    """Note: Cannot work with griffin.runserver"""
    return 'WEBSIG', f"""<script {headers}>
{JavaScript}
</script>"""


def Articlebox(articlecontent: str, Javascriptid='', CSSid='', headers=''):
    return 'WEBSIG', f"""<article id="{Javascriptid}" class="{CSSid}" {headers}></article>"""


def Hyperlink(url: str, text: str, seperatetab: bool, Javascriptid='', CSSid='', headers=''):
    if seperatetab:
        parameter = 'target="_blank"'
    elif not seperatetab:
        parameter = ''
    return 'WEBSIG', f"""<a href="{url}" {parameter} id="{Javascriptid}" class="{CSSid}" {headers}>{text}</a>
"""


def HTTPResponse(*response, Javascriptid='', CSSid='', centerresponse=False):
    global __HTMLCode
    for r in response:
        if r[0] == 'WEBSIG':
            __HTMLCode += f"""{r[1]}
"""
        else:
            __HTMLCode += f"""<pre id="{Javascriptid}" class="{CSSid}">{r}</pre>
"""


def runserver(HTTPRequestedfile: str, port=8000):
    global __HTMLCode
    from os import system
    from webbrowser import open as newtab
    open(HTTPRequestedfile, 'w').write(__HTMLCode)
    newtab(f'http://127.0.0.1:{port}/' + HTTPRequestedfile)
    system(f'python3 -m http.server {port} --bind 127.0.0.1')
