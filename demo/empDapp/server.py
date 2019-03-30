from flask import Flask, render_template, request
from web3 import Web3, HTTPProvider
import json
import datetime

web3=Web3(HTTPProvider('http://172.22.6.121:8081'))
EMP_ABI = json.loads('[{"constant": false,"inputs": [{"name": "_empName","type": "string"},{"name": "_empDeparment","type": "string"}],"name": "signUp","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function","signature": "0xa469a332"},{"constant": false,"inputs": [{"name": "_date","type": "string"}],"name": "markAttendance","outputs": [],"payable": false,"stateMutability": "nonpayable","type": "function","signature": "0x59267a00"},{"constant": false,"inputs": [],"name": "viewAttendance","outputs": [{"name": "","type": "string[]"}],"payable": false,"stateMutability": "nonpayable","type": "function","signature": "0xcd8e231a"},{"constant": false,"inputs": [{"name": "_empaddress","type": "address"}],"name": "viewEmpAttendance","outputs": [{"name": "","type": "string[]"}],"payable": false,"stateMutability": "nonpayable","type": "function","signature": "0x27e7b3b6"},{"constant": false,"inputs": [{"name": "_empaddress","type": "address"}],"name": "viewEmpName","outputs": [{"name": "","type": "string"}],"payable": false,"stateMutability": "nonpayable","type": "function","signature": "0x734a238a"},{"constant": false,"inputs": [],"name": "viewEmpAccounts","outputs": [{"name": "","type": "address[]"}],"payable": false,"stateMutability": "nonpayable","type": "function","signature": "0xf0706c98"}]')
emp = web3.eth.contract(address="0x872a7B0be0d019b285e3BfcE1B6e9798E01CBBe8", abi=EMP_ABI)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/defaultAccount', methods=["POST"])
def defaultAccount():
    empid = int(request.form['empid'])
    web3.eth.defaultAccount = web3.eth.accounts[empid]
    web3.personal.unlockAccount(web3.eth.accounts[empid],"redhat",0)
   
    if empid == 0:
        isAdmin = True
    else:
        isAdmin = False

    return render_template('index.html',isAdmin=isAdmin)
@app.route('/signup', methods=["GET"])
def signupp():
    emp.functions.empSignUp().transact()
    return render_template('index.html')

@app.route('/giveattendance', methods=["GET"])
def giveAttendance():
    now = datetime.datetime.now()
    emp.functions.markAttendance(now.strftime("%d-%m-%Y")).transact()
    return render_template('index.html')

@app.route('/viewattendance', methods=["GET"])
def getAttendance():
    data = emp.functions.viewAttendance().call()
    return render_template('index.html',data=data)

@app.route('/viewempattendance', methods=["GET"])
def getAttendance():
    data = emp.functions.viewEmpAttendance().call()
    return render_template('index.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)
