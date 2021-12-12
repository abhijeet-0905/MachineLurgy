import joblib
import numpy as np
import warnings
warnings.filterwarnings('ignore')

model_tensile=joblib.load('web_app\\lab\\tensile_model.obj')
model_yield=joblib.load('web_app\\lab\\yield_model_v21.obj')
model_elong=joblib.load('web_app\\lab\\elongation_model_v21.obj')
model_ria=joblib.load('web_app\\lab\\ria_model_v21.obj')

class MechanicalProperties():
    
    def __init__(self,vals):
        self.vals=vals
        self.pred=np.array(self.vals).reshape(1,len(self.vals))

    def predict_tensile_strength(self):
        return model_tensile.predict(self.pred)[0]

    def predict_yield_strength(self):
        return model_yield.predict(self.pred)[0]

    def predict_elongation(self):
        return np.round(model_elong.predict(self.pred)[0],2)

    def predict_reduction_in_area(self):
        return np.round(model_ria.predict(self.pred)[0],2)
