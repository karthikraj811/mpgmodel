from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')
# Create your views here.
model2=pickle.load(open('./model3.pkl','rb'))
def home(request):

   return render(request,'home.html')

def result(request):
    print(request)
    if request.method== 'POST':
        cyl=float(request.POST['cylinder'])
        disp=float(request.POST['disp'])
        hp=float(request.POST['hp'])
        wt=float(request.POST['wt'])
        acc=float(request.POST['acc'])
        yr=float(request.POST['yr'])
        orgin=float(request.POST['orgin'])
        df=pd.DataFrame([[cyl,disp,hp,wt,acc,yr,orgin]])

        result=model2.predict(df)[0]
        return render(request,'home.html',{'result':result})
    