from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    hdrs = dict(request.headers)
    fields = {
        
        'method': request.method,              
        'url': request.url,                 
        'base_url': request.base_url,            
        'charset': request.charset,         
        'url_root': request.url_root,            
        'url_rule': str(request.url_rule),       
        'host_url': request.host_url,           
        'host': request.host,               
        'script_root': request.script_root,
        'path': request.path,           
        'full_path': request.full_path,         
        'args': request.args,               
    }
    

    return render_template('index.html', hdrs=hdrs, fields=fields)


if __name__ == "__main__":
    app.run(debug=True)
