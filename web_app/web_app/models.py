from web_app import db

class Alloys(db.Model):

    __tabelname__='alloys'

    id=db.Column(db.Integer,primary_key=True)
    #sr_id=db.Column(db.Integer)
    c=db.Column(db.Numeric(2,4),nullable=False,index=True)
    si=db.Column(db.Numeric(2,4),nullable=False,index=True)
    mn=db.Column(db.Numeric(2,4),nullable=False,index=True)
    p=db.Column(db.Numeric(2,4),nullable=False,index=True)
    s=db.Column(db.Numeric(2,4),nullable=False,index=True)
    ni=db.Column(db.Numeric(2,4),nullable=False,index=True)
    cr=db.Column(db.Numeric(2,4),nullable=False,index=True)
    mo=db.Column(db.Numeric(2,4),nullable=False,index=True)
    cu=db.Column(db.Numeric(2,4),nullable=False,index=True)
    v=db.Column(db.Numeric(2,4),nullable=False,index=True)
    al=db.Column(db.Numeric(2,4),nullable=False,index=True)
    n=db.Column(db.Numeric(2,4),nullable=False,index=True)
    nt=db.Column(db.Numeric(2,4),nullable=False,index=True)
    temp=db.Column(db.Integer,nullable=False,index=True)
    tensile=db.Column(db.Numeric(5,4),nullable=False,index=True)
    yield_=db.Column(db.Numeric(5,4),nullable=False,index=True)
    elongation=db.Column(db.Numeric(5,4),nullable=False,index=True)
    reduction=db.Column(db.Numeric(5,4),nullable=False,index=True)

    def __init__(self,c,si,mn,p,s,ni,cr,mo,cu,v,al,n,nt,temp,tensile,yield_,elongation,reduction):
        self.c,self.si,self.mn,self.p,self.s,self.ni,self.cr,self.mo,self.cu,self.v,self.al,self.n,self.nt,self.temp,self.tensile,self.yield_,self.elongation,self.reduction=c,si,mn,p,s,ni,cr,mo,cu,v,al,n,nt,temp,tensile,yield_,elongation,reduction

    # def __repr__(self):
    #     return f"Carbon:{self.c},Silicon:{self.si},Manganese:{self.mn},Phosphorus:{self.p},Sulphur:{self.s},Nickel:{self.ni},Chromium:{self.cr},Molybdenum:{self.mo},Copper:{self.cu},Vanadium:{self.v},Aluminium:{self.al},Nitrogen:{self.n},Nb+Ta:{self.nt},Temperature:{self.temp},Tensile Strength:{self.tensile}"
