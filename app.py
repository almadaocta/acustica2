from flask import Flask, render_template, request, jsonify, session      
import time
import sys
sys.path.insert(0, 'functions')
from runCalc import run_Calc
from flask import send_from_directory
import os
path = os.getcwd()

app = Flask(__name__)

app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'

@app.route("/")
def main():
    return render_template('home.html', reload = time.time())

@app.route("/api")
def add():
    material = request.args.get('material')
    material2 = request.args.get('material2')
    filtrado = request.args.get('filtrado')
    length = float(request.args.get('length'))
    height = float(request.args.get('height'))
    thickness = float(request.args.get('thickness'))
    thickness2=request.args.get('thickness2')
    if thickness2:
        thickness2 = float(thickness2)
    ly = request.args.get('layer')

    
    
    rc,rd,rs,ri,calcData,fileName=run_Calc(filtrado,length,height,thickness,material,ly,thickness2,material2)

    freq=calcData['filterVector']
    C=calcData['C']
    Ctr= calcData['Ctr']
    C503150=calcData['C503150']
    C505000=calcData['C505000']
    C1005000=calcData['C1005000']
    CTR501350=calcData['CTR501350']
    CTR505000=calcData['CTR505000']
    CTR1005000=calcData['CTR1005000']
    rw=calcData['Rw']
    stc=calcData['STC']
    session["exportPath"]=fileName

    

    N = [None] * len(freq)
    for i in range (0,len(freq)):
        N[i]=i

    
    return jsonify({
        "rc"        :  rc,
        "rd"        :  rd,
        "rs"        :  rs,
        "ri"        :  ri,
        "freq"      :  freq,
        "N"         :  N,
        "rw"        :  rw,
        "stc"       :  stc,
        "C"         :  C,
        "Ctr"       :  Ctr,
        "C503150"   :  C503150,
        "C505000"   :  C505000,
        "C1005000"  :  C1005000,
        "CTR501350" :  CTR501350,
        "CTR505000" :  CTR505000,
        "CTR1005000":  CTR1005000
    })

@app.route('/export-file/') 
def plot_csv():     
    return send_from_directory(directory='export', filename=session.get("exportPath",None)+'.xlsx', as_attachment=True)

                     
if __name__ == "__main__":
    app.run(debug=True)
