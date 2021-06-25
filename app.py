from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

from forms import WithdrawalForm, DepositForm, EnterPINForm
from ATMModels import DataStore, Transaction, WorkOrder, DamageClaim, EnterPIN

import jsonpickle
import os.path
import json

app = Flask ( __name__ )
app.debug = True
app.config['SECRET_KEY'] = 'secret key 11829@#%737aJFa^$sdfiED098SDFAd88@%'

#ds = DataStore()

ds = DataStore.FactoryDataRestore()

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
        ph = Transaction()
        ph.amount = f.amount.data

        return redirect(url_for('Withdrawal'))

    return render_template('Withdrawal.html', form=form)

@app.route('/Deposit/', methods=['get', 'post'])
def Deposit():
    form = DepositForm()
    if form.validate_on_submit():
        f = form
        ph = Transaction()
        ph.amount = f.amount.data

        return redirect(url_for('Deposit'))

    return render_template('Deposit.html', form=form)

@app.route('/EnterPIN/', methods=['get', 'post'])
def EnterPIN():
    form = EnterPINForm()
    if form.validate_on_submit():
        f = form

        flash('Thank you for registering')
        return redirect('/EnterPIN')

        return redirect(url_for('EnterPIN'))

    return render_template('EnterPIN.html', form=form)



if __name__ == '__main__' :
    app.run ()
