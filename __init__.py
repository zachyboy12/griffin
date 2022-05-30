HTMLCode = ''


def Image(url: str, alternatetext: str, headers=''):
    return 'WEBSIG', f"""<img src="{url}" alt="{alternatetext}" {headers}>
"""


def Video(localurl: str, width=500, height=500, autoplay='true', headers=''):
    return 'WEBSIG', f"""<video src="{localurl}" width="{width}" height="{height}" autoplay="{autoplay}" {headers}></video>
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


def HTTPResponse(response, Javascriptid='', CSSclass='', centerresponse=False):
    global HTMLCode
    if response[0] == 'WEBSIG':
        if centerresponse:
            HTMLCode += f"""{response[1]}
"""
        elif not centerresponse:
            HTMLCode += f"""{response[1]}
"""
    else:
        HTMLCode += f"""<div id="{Javascriptid}" class="{CSSclass}"><pre>{response}</pre></div>
"""


def runserver(HTTPRequestedfile: str, port=8000):
    global HTMLCode
    from os import system
    from webbrowser import open as newtab
    open(HTTPRequestedfile, 'w').write(HTMLCode)
    newtab(f'http://127.0.0.1:{port}/' + HTTPRequestedfile)
    system(f'python3 -m http.server {port} --bind 127.0.0.1')
