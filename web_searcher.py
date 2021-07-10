import requests
from bs4 import BeautifulSoup
from googlesearch import search
from flask import Flask, render_template, request
# from dbse import insertBLOB

def back_check(query):
    urls = []
    headlines = []
    sub = []
    for j in search(query, num=5, stop=5, pause=0):

        x = requests.get(j)
        soup = BeautifulSoup(x.content, 'lxml')

        url = j
        head = soup.get_text()
        head = head.strip()
        head = " ".join(head.split())
        s = str(url)
        url_check = s[8:20]
        t = "twitter"

        x = "https://"
        y = "/"
        start = s.find(x) + len(x)
        end = s.find(y,9)
        substring = s[start:end]
        if t not in url_check :
            urls.append(url)
            headlines.append(head[:150])
            sub.append(substring)

    l = len(urls)
    return urls,headlines,sub,l

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        quer = request.form['box']
        urls,head,site,l = back_check(quer)
        return render_template('index2.html', urlout=urls,head=head,sites=site,l=l)

    return render_template('index1.html')


@app.route('/load', methods=['POST','GET'])
def abou():
    quer = request.form['box']
    urls,head,site,l=back_check(quer)
    return render_template('index2.html', urlout=urls,head=head,sites=site,l=l)
if __name__ == '__main__':
    app.run(debug=True)

