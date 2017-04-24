
import threading

import requests
import time

import wx
import wx.html2

from bottle import Bottle, run
from bottle import ServerAdapter

from routes import rapp

app = Bottle()
app.merge(rapp)

class Browser(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = wx.html2.WebView.New(self)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        self.reload = wx.Button(self, wx.ID_ANY, "Startover")
        sizer.Add(self.reload, 0, wx.EXPAND, 0)
        self.reload.Bind(wx.EVT_BUTTON, self.Go)
        self.SetSizer(sizer)
        self.SetSize((1280, 720))
        
    def Go(self, event):
        self.browser.LoadURL('http://localhost:8080')

class WSGIRefServer(ServerAdapter):
    server = None
    
    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kwargs): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()
        
    def stop(self):
        self.server.shutdown()
        print("shutting down the web server")

server = WSGIRefServer(host="localhost", port=8080)        

def start_server():
    app.run(server=server)
    
if __name__ == '__main__':
    webserver = threading.Thread(name='websever', target=start_server)
    webserver.setDaemon(True)
    print("Starting server")
    webserver.start()
    
    status = 0
    while status != 200:
        resp = requests.head("http://localhost:8080")
        status = resp.status_code
        print('checking...')
        time.sleep(0.05)
        
    print("Starting client")
    webclient = wx.App()
    dialog = Browser(None, wx.ID_ANY)
    dialog.browser.LoadURL("http://localhost:8080")
    dialog.Show()
    webclient.MainLoop()
    print("Closed client")
   
    server.stop()
    print("Closed server")
    
    