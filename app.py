from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

from forms import WithdrawalForm, DepositForm, EnterPINForm
from ATMModels import BankAccount, Transaction, EnterPIN

import jsonpickle
import os.path
import json

app = Flask ( __name__ )
app.debug = True
app.config['SECRET_KEY'] = 'secret key 11829@#%737aJFa^$sdfiED098SDFAd88@%'


bankAccount = BankAccount.FactoryDataRestore()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='PHTRS Home',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='CSU Global CS505',
        year=datetime.now().year,
        developer='Kenneth Ceglia'
    )


@app.route('/Withdrawal/', methods=['get', 'post'])
def Withdrawal():
    form = WithdrawalForm()
    if form.validate_on_submit():
        f = form
        tx = Transaction()
        tx.amount = float(f.amount.data)
        tx.amount = float(tx.amount) * float(-1.00)
        if bankAccount.balance + tx.amount >= 0:
            bankAccount.AddTransaction(tx)
            BankAccount.FactoryDataSave(bankAccount)
        else:
            return render_template('CloseAccountBalanceZero.html')
        return redirect(url_for('Withdrawal'))

    return render_template('Withdrawal.html', form=form)

@app.route('/Deposit/', methods=['get', 'post'])
def Deposit():
    form = DepositForm()
    if form.validate_on_submit():
        f = form
        tx = Transaction()
        tx.amount = float(f.amount.data)
        bankAccount.AddTransaction(tx)
        BankAccount.FactoryDataSave(bankAccount)
        return redirect(url_for('Deposit'))

    return render_template('Deposit.html', form=form)

@app.route('/EnterPIN/', methods=['get', 'post'])
def EnterPIN():
    form = EnterPINForm()
    if form.validate_on_submit():
        f = form

        if f.pin != bankAccount.pin:
            bankAccount.currentRetry = bankAccount.currentRetry + 1
            if bankAccount.currentRetry < 3 :
                return render_template('ErrorPinInvalid.html')
            else:
                return render_template('ErrorPinInvalidLocked.html')

        return redirect(url_for('EnterPIN'))

    return render_template('EnterPIN.html', form=form)

@app.route('/Transactions/', methods=['get', 'post'])
def Transactions():
    transActions = bankAccount.GetAllTransactions()
    balance = bankAccount.GetBalance()
    return render_template('Transactions.html', txReport = transActions, bx = balance)

if __name__ == '__main__' :
    app.run ()
