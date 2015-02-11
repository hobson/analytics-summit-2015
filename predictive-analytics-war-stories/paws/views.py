import cgi
from flask import render_template, abort, request, redirect, url_for, jsonify
from flask.ext.login import login_user, logout_user, login_required, current_user
from jinja2 import TemplateNotFound
from twilio import twiml
from twilio.rest import TwilioRestClient

from .config import TWILIO_NUMBER, REDIS_PORT

from . import redis_db, VOTELOG

from .forms import LoginForm, PresentationForm
from .models import User, Presentation, Choice

from . import app, socketio, db, login_manager



client = TwilioRestClient()

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.route('/', methods=['GET'])
def list_public_presentations():
    presentations = Presentation.query.filter_by(is_active=True)
    return render_template('list_presentations.html', 
                           presentations=presentations)

@app.route('/votelog/', methods=['GET'])
def votelog():
    try:
        return jsonify(**VOTELOG)
    except:
        abort(500)



@app.route('/<presentation_name>/', methods=['GET'])
def presentation(presentation_name):
    try:
        votes = dict([('paws'+str(i +1), redis_db.get('paws'+str(i+1))) for i in range(6)])
        return render_template('/presentations/' + presentation_name + '.slides.com.html', **votes)
    except TemplateNotFound:
        abort(404)


@app.route('/paws/twilio/webhook/', methods=['POST'])
def twilio_callback():
    to = request.form.get('To', '')
    from_ = request.form.get('From', '')
    message = request.form.get('Body', '')
    print("FROM:    '{0}'".format(from_))
    print("TO:      '{0}'".format(to))
    print("MESSAGE: '{0}'".format(message))
    print("VOTELOG:  {0}".format(VOTELOG))
   
    if to[-10:] == TWILIO_NUMBER[-10:]:
        message = message.strip().lower()
        if len(message):
            try:
                message = str(int(message[0]))
            except:
                message = str(int(message[-1]))
            message = cgi.escape('paws' + message)
            print("PAWSMSG: '{0}'".format(message))
            if VOTELOG and 'votes' in VOTELOG.keys():
                if message in VOTELOG['votes'].keys():
                    VOTELOG['votes'][message] = VOTELOG['votes'][message] + 1
                total_votes = VOTELOG['votes'].get(message, 0)
            elif REDIS_PORT:
                redis_db.incr(message)
                total_votes = redis_db.get(message)
            socketio.emit('msg', {'div': message,
                                  'val': str(total_votes)},
                          namespace='/paws')
        if isinstance(from_, basestring) and len(from_.strip()):
            if VOTELOG and 'voters' in VOTELOG.keys():
                VOTELOG['voters'][from_] = VOTELOG['voters'].get(from_, '') + cgi.escape(request.form.get('Body', '') + "|.....|")
            else:
                try:
                    redis_db.incr(cgi.escape(from_.strip()))
                except:
                    print('Unable to log vote from "{0}"'.format(cgi.escape(from_)))
    resp = twiml.Response()
    resp.message("Thanks for your vote!")
    return str(resp)


@app.route('/admin/', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('admin_list_presentations'))
    return render_template('admin/sign_in.html', form=form, no_nav=True)


@app.route('/sign-out/', methods=['GET'])
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('list_public_presentations'))


@app.route('/admin/presentations/', methods=['GET'])
@login_required
def admin_list_presentations():
    presentations = Presentation.query.all()
    return render_template('admin/presentations.html', 
                           presentations=presentations)

@app.route('/admin/presentation/', methods=['GET', 'POST'])
@login_required
def admin_new_presentation():
    form = PresentationForm()
    if form.validate_on_submit():
        p = Presentation(name=form.name.data, filename=form.filename.data)
        if form.is_active.data:
            p.is_active = form.is_active.data
        if form.number.data:
            p.choices_number = form.choices_number.data
        if form.email.data:
            p.choices_email = form.choices_email.data
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('admin_list_presentations'))
    return render_template('admin/presentation.html', form=form, is_new=True)


@app.route('/admin/presentation/<int:id>/', methods=['GET', 'POST'])
@login_required
def admin_edit_presentation(id):
    form = PresentationForm()
    p = Presentation.query.get_or_404(id)
    if form.validate_on_submit():
        p.name = form.name.data
        p.filename = form.filename.data
        # todo: save rest of fields
        db.session.merge(p)
        db.session.commit()
    else:
        form.name.data = p.name
        form.filename.data = p.filename
        # todo: fill in rest of fields
    return render_template('admin/presentation.html', form=form,
                           presentation=p)



