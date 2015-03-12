
import sys 
from tkinter import *
from math import *



def CND(X):

    (a1,a2,a3,a4,a5) = (0.31938153, -0.356563782, 1.781477937,
                        -1.821255978, 1.330274429)
    L = abs(X)
    K = 1.0 / (1.0 + 0.2316419 * L)
    w = 1.0 - 1.0 / sqrt(2*pi)*exp(-L*L/2.) * (a1*K + a2*K*K + a3*pow(K,3) +
    a4*pow(K,4) + a5*pow(K,5))
    if X<0:

        w = 1.0-w

    return w


def BSMc():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
  

    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    d2 = d1-(v*sqrt((T/365)))

    call = S*CND(d1)-X*exp(-r*(T/365))*CND(d2)
    return (call)
    
    
def BSMp():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
  

    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    d2 = d1-(v*sqrt((T/365)))
    
    put = X*exp(-r*(T/365))*CND(-d2)-S*CND(-d1)
    return (put)

def deltac():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())

    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    deltac = CND(d1)
    return (deltac)

def deltap():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())

    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    deltap = CND(d1)-1
    return (deltap)

def vegac():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))

    dNd=(1/sqrt(2*pi))*exp(-(d1*d1)/2)
    vegac = S*sqrt(T/365)*dNd
    return vegac/100

def vegap():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))

    vegap = (S*sqrt(T/365)*(exp(-0.5*d1**2))/(sqrt(2*pi)))
    return vegap/100

def thetac():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    d2 = d1-(v*sqrt((T/365)))

    dnd2 = (1/sqrt(2*pi))*exp(-(d2*d2)/2)
    thetac = -X*exp(-r*T/365)*(r*CND(d2)+((v*dnd2)/(2*sqrt(T/365))))
    return thetac/365

def thetap():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    d2 = d1-(v*sqrt((T/365)))

    dnd2 = (1/sqrt(2*pi))*exp(-(d2*d2)/2)
    thetap = -X*exp(-r*T/365)*(r*CND(-d2)-((v*dnd2)/(2*sqrt(T/365))))
    return thetap/365

def rhoc():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    d2 = d1-(v*sqrt((T/365)))

    rhoc = T/365*X*exp(-r*T/365)*CND(d2)
    return rhoc

def rhop():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    d2 = d1-(v*sqrt((T/365)))

    rhop = T/365*X*exp(-r*T/365)*CND(-d2)
    return rhop

def gamma():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    d2 = d1-(v*sqrt((T/365)))
    dnd2 = (1/sqrt(2*pi))*exp(-(d2*d2)/2)

    gamma = (X*exp(-r*T/365)*dnd2)/(S*S*v*sqrt(T/365))
    return gamma

def ivc():
    S = float(stock.get())
    X = float(strike.get())

    ivc = S - X
    return ivc

def ivp():
    S = float(stock.get())
    X = float(strike.get())

    ivp = X - S
    return ivp

def tvc():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
  

    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    d2 = d1-(v*sqrt((T/365)))

    call = S*CND(d1)-X*exp(-r*(T/365))*CND(d2)
    ivc = S - X
    tvc = call - ivc 
    return tvc


def tvp():
    S = float(stock.get())
    X = float(strike.get())
    v = float(vol.get())
    r = float(risk.get())
    T = float(time.get())
  

    d1 = (log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))
    d2 = d1-(v*sqrt((T/365)))
    
    put = X*exp(-r*(T/365))*CND(-d2)-S*CND(-d1)
    ivp = X - S
    tvp = put - ivp
    return tvp

############Trying to implement Newton Raphson method



def newtonRaphsonc():
    tol=1.0e-9
    S = float(stock.get())
    X = float(strike.get())
    r = float(risk.get())
    T = float(time.get())
    MVc = float(mvc.get())
    v = 0.5
    
    for i in range(100):
        dx = -(S*CND((log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365))))-X*exp(-r*T/365)*CND(((log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))-(v*sqrt((T/365)))))-MVc)/(sqrt(T/365)*X*exp(-r*T/365)*(1/sqrt(2*pi))*exp(-(pow(((log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))-(v*sqrt((T/365)))),2))/2))
        v = v+dx
        if abs(dx)<tol:
            return v
            
    
def newtonRaphsonp():
    tol=1.0e-9
    S = float(stock.get())
    X = float(strike.get())
    r = float(risk.get())
    T = float(time.get())
    MVp = float(mvp.get())
    v = 0.5
    
    for i in range(100):
        dx = -(X*exp(-r*T/365)*CND(-((log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))-(v*sqrt((T/365)))))-S*CND(-(log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365))))-MVp)/(sqrt(T/365)*X*exp(-r*T/365)*(1/sqrt(2*pi))*exp(-(pow(((log(S/X)+(r+v*v/2)*(T/365))/(v*sqrt((T/365)))-(v*sqrt((T/365)))),2))/2))
        v = v+dx
        if abs(dx)<tol:
            return v
            print (v)
      

    
def calculateall():
    callv.set(round(BSMc(), 4))
    putv.set(round(BSMp(), 4))
    deltacall.set(round(deltac(), 4))
    deltaput.set(round(deltap(), 4))
    vegacall.set(round(vegac(), 4))
    vegaput.set(round(vegap(), 4))
    thetacall.set(round(thetac(), 4))
    thetaput.set(round(thetap(), 4))
    rhocall.set(round(rhoc(), 4))
    rhoput.set(round(rhop(), 4))
    gammaall.set(round(gamma(), 4))
    intrensicc.set(round(ivc(), 4))
    intrensicp.set(round(ivp(), 4))
    timevc.set(round(tvc(), 4))
    timevp.set(round(tvp(), 4))
    impvc.set(round(newtonRaphsonc(),4))
    impvp.set(round(newtonRaphsonp(),4))

    
root = Tk()


root.geometry('600x350+300+300')
root.title('BSM Option Pricing Calculator')

#Labels for the input parameters
Label1 = Label(root, text='Stock Price').place(x=50, y=80)
Label2 = Label(root, text='Strike Price').place(x=50, y=100)
Label3 = Label(root, text='Standard Deviation').place(x=50, y=120)
Label4 = Label(root, text='Risk Free Rate').place(x=50, y=140)
Label5 = Label(root, text='Days to Expiration').place(x=50, y=160)

#Labels for option value and Greeks
Label6 = Label(root, text='Theoretical Value').place(x=300, y=80)
Label7 = Label(root, text='Intrensic Value').place(x=300, y=120)
Lable8 = Label(root, text='Time Value').place(x=300, y=145)
Label10 = Label(root, text='Delta').place(x=300, y=180)
Label11 = Label(root, text='Vega').place(x=300, y=205)
Label12 = Label(root, text='Theta').place(x=300, y=230)
Label13 = Label(root, text='Rho').place(x=300, y=255)
Label14 = Label(root, text='Gamma').place(x=300, y=280)
Label12 = Label(root, text='Call').place(x=400, y=60)
Label13 = Label(root, text='Put').place(x=460, y=60)
Label14 = Label(root, text='Call').place(x=160, y=200)
Label15 = Label(root, text='Put').place(x=220, y=200)
Label16 = Label(root, text='Market Value').place(x=50, y=220)
Label17 = Label(root, text='Implied Volatility').place(x=50, y=240)

#String placeholders for the input data
stock = StringVar()
strike = StringVar()
vol = StringVar()
risk = StringVar()
time = StringVar()
mvc = StringVar()
mvp = StringVar()

#Entryboxes for the user input parameters
Entry1 = Entry(root, width=10, textvariable=stock).place(x=160, y=80)
Entry2 = Entry(root, width=10, textvariable=strike).place(x=160, y=100) 
Entry3 = Entry(root, width=10, textvariable=vol).place(x=160, y=120)
Entry4 = Entry(root, width=10, textvariable=risk).place(x=160, y=140) 
Entry5 = Entry(root, width=10, textvariable=time).place(x=160, y=160)
Entry6 = Entry(root, width=7, textvariable=mvc).place(x=160, y=220)
Entry7 = Entry(root, width=7, textvariable=mvp).place(x=220, y=220)

#Displayboxes for Option Values and Greeks
callv = StringVar()
putv = StringVar()
intrensicc = StringVar()
intrensicp = StringVar()
timevc = StringVar()
timevp = StringVar()
deltacall = StringVar()
deltaput = StringVar()
vegacall = StringVar()
vegaput = StringVar()
thetacall = StringVar()
thetaput = StringVar()
rhocall = StringVar()
rhoput = StringVar()
gammaall = StringVar()
impvc = StringVar()
impvp = StringVar()


callvalue = Label(root, width=6, textvariable=callv, bg="snow3").place(x=400, y=80)
putvalue =Label(root, width=6, textvariable=putv, bg="snow3").place(x=460, y=80)

intrensiccall = Label(root, width=6, textvariable=intrensicc, bg="snow3").place(x=400, y=120)
intrensicput = Label(root, width=6, textvariable=intrensicp, bg="snow3").place(x=460, y=120)
timevalcall = Label(root, width=6, textvariable=timevc, bg="snow3").place(x=400, y=145)
timevalput = Label(root, width=6, textvariable=timevp, bg="snow3").place(x=460, y=145)

delta1 = Label(root, width=6, textvariable=deltacall, bg="snow3").place(x=400, y=180)
delta2 = Label(root, width=6, textvariable=deltaput, bg="snow3").place(x=460, y=180)
vega1 = Label(root, width=6, textvariable=vegacall, bg="snow3").place(x=400, y=205) 
vega2 = Label(root, width=6, textvariable=vegaput, bg="snow3").place(x=460, y=205)
theta1 = Label(root, width=6, textvariable=thetacall, bg="snow3").place(x=400, y=230)
theta2 = Label(root, width=6, textvariable=thetaput, bg="snow3").place(x=460, y=230)
rho1 = Label(root, width=6, textvariable=rhocall, bg="snow3").place(x=400, y=255)
rhoa2 = Label(root, width=6, textvariable=rhoput, bg="snow3").place(x=460, y=255)
gamma1 = Label(root, width=6, textvariable=gammaall, bg="snow3").place(x=400, y=280)
gamma2 = Label(root, width=6, textvariable=gammaall, bg="snow3").place(x=460, y=280)
impliedvolc =Label(root, width=6, textvariable=impvc, bg='snow3').place(x=160, y=245)
impliedvolp =Label(root, width=6, textvariable=impvp, bg='snow3').place(x=220, y=245)

Calculate = Button(root, bg='grey', text='Calculate', width=8, command = calculateall).place(x=50, y=290)
#Reset = Button(text='Reset', command = reset()).place(x=100, y=280)
Exit = Button(root, text='Quit', width=8, bg='grey', command = root.destroy).place(x=150, y=290)





root.mainloop()



