
import sys
import cgi
from http.server import HTTPServer, SimpleHTTPRequestHandler
from Database import create_table, insert_record, fetch_records

HOST_NAME = "0.0.0.0"
PORT = 8880

def read_html_template(path):
    """function to read HTML file"""
    try:
        with open(path) as f:
            file = f.read()
    except Exception as e:
        file = e
    return file

def show_records(self):
    """function to show records in template"""
    file = read_html_template("Allnotes.html")
    # fetch records from database
    table_data = fetch_records()
    

    table_row = ""
    for data in table_data:
        print(data)
        table_row += "<li>"
        for item in data:
            if item==data[0]:
                table_row += """<a href="#">"""
                table_row += item
                table_row += "</a>"
            else:
                table_row += """<a href="#">"""
                table_row += "<h2>"+item+""
                table_row += "</a>"
        table_row += "</li>"
    # replace {{user_records}} in template by table_row
    file = file.replace("{{user_records}}", table_row)
    self.send_response(200, "OK")
    self.end_headers()
    self.wfile.write(bytes(file, "utf-8"))

class PythonServer(SimpleHTTPRequestHandler):
    
    """Python HTTP Server that handles GET and POST requests"""
   
    def do_GET(self):
        print("GEt")
        if self.path == '/':
            self.path = 'Newnote.html'
            file = read_html_template(self.path)
            self.send_response(200, "OK")
            self.end_headers()
            self.wfile.write(bytes(file, "utf-8"))
       
        if self.path == '/show_records':
            self.path = 'Allnotes.html'
            # call show_records function to show users entered
            show_records(self)
    
    def do_POST(self):
        
        if self.path == '/success':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                full_name = fields.get("full_name")[0]
                country = fields.get("country")[0]
                # create table User if it runs first time else not
                create_table()
                # insert record into User table
                insert_record(full_name, country)
                html = f"<html><head></head><body><h1>Form data successfully recorded!!!</h1></body></html>"
                self.send_response(200, "OK")
                self.end_headers()
                self.wfile.write(bytes(html, "utf-8"))


if __name__ == "__main__":
    
    server = HTTPServer((HOST_NAME, PORT), PythonServer)
    print(f"Server started http://{HOST_NAME}:{PORT}")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped successfully")
        sys.exit(0)