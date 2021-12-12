from flask import render_template,request,redirect,url_for,Blueprint
from web_app import db
from web_app.models import Alloys

logs=Blueprint('logs',__name__)

@logs.route('/logs',methods=["GET","POST"])
def log():
    alloys_=Alloys.query.all()

    if request.method == 'POST':
        if request.form.get('Continue')=='Continue':
            db.session.query(Alloys).delete()
            db.session.commit()
        return redirect(url_for("logs.log",alloys_=alloys_))

    return render_template('log.html',alloys_=alloys_)

# @history.route('/history',methods=["GET","POST"])
# def delete_row(pid):
#     num=0
#     if request.method == 'POST':
#         if request.form.get('Delete') == 'Delete':
#             print('now in here')
#             pid=pid
#             del_id=request.form.get("id")
#             return redirect(url_for('history.html',alloys_=alloys_,num=pid))

#         else:
#             return redirect(url_for('history.html',alloys_=alloys_,num=pid))

# @history.route('/history',methods=["GET","POST"])
# def clear():
#     print('its in clear')
#     if request.method == 'POST':
#         if request.form.get('clear_num')==1:
#             db.session.query(Alloys).delete()
#             db.session.commit()
#             print('it worked!')
#             return redirect(url_for('history.hist'))