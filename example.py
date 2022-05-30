import __init__ as griffin

griffin.HTTPResponse('Hello, World from Griffin! Soar now!', CSSclass='text', centerresponse=True)
griffin.HTTPResponse(griffin.CSS(""".text {
    text-align: center;
    }
.myimg {
    margin: auto;
    display: block;
    }"""))
griffin.HTTPResponse(griffin.Image('https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Orion_Nebula_-_Hubble_2006_mosaic_18000.jpg/640px-Orion_Nebula_-_Hubble_2006_mosaic_18000.jpg', 'The Orion Nebula', 'class="myimg"'))
griffin.HTTPResponse('^^ The Orion Nebula from Wikipedia', CSSclass='text')
griffin.runserver('test.html', 4000)
