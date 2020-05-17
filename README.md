# Simple Flask App
Prints headers and request fields

## Usage
`pip install -r requirements.txt `

`export FLASK_RUN_PORT=8000`

`flask run`

## Sample Output
```
Flask App
Req Headers
Host :    192.168.1.179

Cache-Control :    max-age=0

Upgrade-Insecure-Requests :    1

User-Agent :    Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36

Accept :    text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

Accept-Encoding :    gzip, deflate

Accept-Language :    en-US,en;q=0.9

X-Forwarded-Port :    80

X-Forwarded-For :    192.168.1.179

Req Fields
method :    GET

url :    http://192.168.1.179/

base_url :    http://192.168.1.179/

charset :    utf-8

url_root :    http://192.168.1.179/

url_rule :    /

host_url :    http://192.168.1.179/

host :    192.168.1.179

script_root :   

path :    /

full_path :    /?

args :    ImmutableMultiDict([])
```