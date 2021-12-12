from flask import render_template,request,redirect,url_for,Blueprint
from web_app.lab.test_model import MechanicalProperties
from web_app import db
from web_app.models import Alloys

lab=Blueprint('lab',__name__)


@lab.route('/lab',methods=["GET","POST"])
def lab_():

    if request.method=="POST":
        _c,_si,_mn,_p,_s,_ni,_cr,_mo,_cu,_v,_al,_n,_nt,_temp=request.form.get("_carbon"),request.form.get("_silicon"),request.form.get("_manganese"),request.form.get("_phosphorus"),request.form.get("_sulphur"),request.form.get("_nickel"),request.form.get("_chromium"),request.form.get("_molybdenum"),request.form.get("_copper"),request.form.get("_vanadium"),request.form.get("_aluminium"),request.form.get("_nitrogen"),request.form.get("_nbta"),request.form.get("_temp")

        elems=[_c,_si,_mn,_p,_s,_ni,_cr,_mo,_cu,_v,_al,_n,_nt,_temp]
        if _si==_p==_s==_ni==_cr==_mo==_cu==_v==_al==_n==_nt==_temp or (_si==_p==_s==_ni==_cr==_mo==_cu==_v==_al==_n==_nt):
            error="All values can not be same!"
            return render_template('lab.html',elm1=_c,elm2=_si,elm3=_mn,elm4=_p,elm5=_s,elm6=_ni,elm7=_cr,elm8=_mo,elm9=_cu,elm10=_v,elm11=_al,elm12=_n,elm13=_nt,elm14=_temp,error=error)
        
        elif elems.count('0')>6:
            error="Too many values are null!"
            return render_template('lab.html',elm1=_c,elm2=_si,elm3=_mn,elm4=_p,elm5=_s,elm6=_ni,elm7=_cr,elm8=_mo,elm9=_cu,elm10=_v,elm11=_al,elm12=_n,elm13=_nt,elm14=_temp,error=error)

        mp=MechanicalProperties(elems)
        pred_tensile=mp.predict_tensile_strength()
        pred_yield=mp.predict_yield_strength()
        pred_elong=mp.predict_elongation()
        pred_ria=mp.predict_reduction_in_area()
        
        comps=Alloys(c=_c,si=_si,mn=_mn,p=_p,s=_s,ni=_ni,cr=_cr,mo=_mo,cu=_cu,v=_v,al=_al,n=_n,nt=_nt,temp=_temp,tensile=pred_tensile,yield_=pred_yield,elongation=pred_elong,reduction=pred_ria)
        db.session.add(comps)
        db.session.commit()
        
        return render_template('lab.html',ria_val=pred_ria,elong_val=pred_elong,yield_val=pred_yield,tensile_val=pred_tensile,elm1=_c,elm2=_si,elm3=_mn,elm4=_p,elm5=_s,elm6=_ni,elm7=_cr,elm8=_mo,elm9=_cu,elm10=_v,elm11=_al,elm12=_n,elm13=_nt,elm14=_temp)

    return render_template('lab.html')
