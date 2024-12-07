from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

from .models import *
import xlrd
from .tf import tf

from .Prediction import Prediction
from .RandomGen import getnum

timings={1:'10:00 AM',2:'11:00 AM',3:'12:00 PM',4:'1:00 PM',5:'2:00 PM',6:'3:00 PM',7:'4:00 PM', 8:'5:00 PM'}

# Create your views here.
def home(request):
	request.session["bookdoc"]=''
	request.session["di"]=''
    	
	return render(request, 'index.html')
def signupdef(request):
	return render(request, 'signup.html')

def usignupactiondef(request):
	email=request.POST['mail']
	pwd=request.POST['pwd']
	name=request.POST['name']
	age=request.POST['age']
	gen=request.POST['gen']

		
	d=onlineuser.objects.filter(email__exact=email).count()
	if d>0:
		return render(request, 'signup.html',{'msg':"Email Already Registered"})
	else:
		d=onlineuser(name=name,email=email,pwd=pwd,gender=gen,age=age)
		d.save()
		return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})

	return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})

def userlogindef(request):
	return render(request, 'user.html')

def userloginactiondef(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pwd=request.POST['pwd']
		d=onlineuser.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
		if d>0:
			d=onlineuser.objects.filter(email__exact=uid)
			name=""
			for d1 in d:
				name=d1.name

			request.session['email']=uid
			request.session['name']=name
			return render(request, 'user_home.html',{'data': d[0]})

		else:
			return render(request, 'user.html',{'msg':"Login Fail"})

	else:
		return render(request, 'user.html')

def userhomedef(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=onlineuser.objects.filter(email__exact=uid)
		return render(request, 'user_home.html',{'data': d[0]})

	else:
		return render(request, 'user.html')

def userlogoutdef(request):
	try:
		del request.session['email']
	except:
		pass
	return render(request, 'user.html')


def adminlogin(request):
    return render(request, 'admin.html')


def adminloginaction(request):
    userid=request.GET['aid']
    pwd=request.GET['pwd']
    print(userid, pwd,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if userid=='admin' and pwd=="admin":
        request.session['adminid']='admin'
        return render(request, 'adminhome.html')
    else:
        err='Your Login Data is wrong !!' 
        return render(request, 'admin.html',{'msg':err})

def adminhome(request):
    return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'admin.html')

def upload(request):
    return render(request, 'upload.html')



def training(request):
    return render(request, 'training.html')


def nbtrain(request):
    from .Training import Training
    Training.train('nb')

    return render(request, 'training.html', {'msg':"Naive Bayes Algorithm's training completed"})

def rftrain(request):
    from .Training import Training
    Training.train('rf')
    return render(request, 'training.html', {'msg':"Random Forest Algorithm's training completed"})

def svmtrain(request):
    from .Training import Training
    Training.train('svm')
    return render(request, 'training.html', {'msg':"SVM Algorithm's training completed"})

def nntrain(request):
    from .Training import Training
    Training.train('nn')
    return render(request, 'training.html', {'msg':"Neural Networks Algorithm's training completed"})
def testing(request):
	d=performance.objects.all()
	d.delete()
	from .Testing import Testing
	sc=Testing('nb.sav','Testset.csv')
	d=performance(alg_name='Naive Bayes', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
	d.save()
	sc=Testing('nn.sav','Testset.csv')
	
	d=performance(alg_name='Neural Networks', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
	d.save()
	sc=Testing('svm.sav','Testset.csv')
	d=performance(alg_name='SVM', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
	d.save()
	
	sc=Testing('rf.sav','Testset.csv')
	d=performance(alg_name='Random Forest', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
	d.save()
	return render(request, 'training.html', {'msg':"Testing process completed"})



def viewacc(request):

    d=performance.objects.all()
    val=dict({})
    for d1 in d:
        val[d1.alg_name]=d1.sc1

    from .Graphs import viewg
    viewg(val)
    return render(request, 'viewacc.html', {'data': d})




def upload1(request):
	if "adminid" in request.session:
		file=request.POST['file']
		file="symptom_Description.xlsx"
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		Description.objects.all().delete()
		for r in range(1, sheet.nrows):
			f0 = sheet.cell(r, 0).value
			f1 = sheet.cell(r, 1).value
			d=Description(Disease=f0,Description=f1)
			d.save()
		return render(request, 'upload.html',{'msg':"Description Dataset Uploaded Successfully"})
	else:
		return render(request, 'admin.html')

def upload2(request):
	if "adminid" in request.session:
		file=request.POST['file']
		file="symptom_precaution.xlsx"
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		precautions.objects.all().delete()
		for r in range(1, sheet.nrows):
			f0 = sheet.cell(r, 0).value
			f1 = sheet.cell(r, 1).value
			f2 = sheet.cell(r, 2).value
			f3 = sheet.cell(r, 3).value
			f4 = sheet.cell(r, 4).value
			d=precautions(Disease=f0,Precaution_1=f1,Precaution_2=f2,Precaution_3=f3,Precaution_4=f4)
			d.save()
		return render(request, 'upload.html',{'msg':"Precautions Dataset Uploaded Successfully"})
	else:
		return render(request, 'admin.html')


def adddata(request):
    if "adminid" in request.session:
        d = queries.objects.all()
        
        return render(request, 'adddata.html', {'data': d})

    else:
        return render(request, 'admin.html')




def addquery(request):
    q=request.POST['q']
    a=request.POST['a']
    
        
    d=queries(q_n=q,an_s=a)
    d.save()
    
    d = queries.objects.all()
    return render(request, 'adddata.html', {'data': d,'msg':'Query Added.'})





def chatpage(request):
    
    chat.objects.all().delete()
    
    d=chat.objects.filter().all()
    return render(request, 'chat.html',{'data': d})

def chatpage2(request):
    
    f1=open('msg.txt')
    msg=f1.read()
    d=chat.objects.filter().all()
    return render(request, 'chat.html',{'data': d,'msg': msg})



def chataction(request):
    message=request.POST['message']
    message=message.replace('.','')
    m=message.split(',')

    if str(request.session["bookdoc"])=='true':
    	d=doctors.objects.filter(docid=message).count()

    	if d>0:
    		d=chat(name=request.session["name"],email=request.session["email"],message=message)
    		d.save()
    		d=chat(name='chatbot',email='chatbot',message="Enter booking date: (YYYY-MM-DD)")
    		d.save()
    		request.session["di"]=message
    		request.session["bookdoc"]="date"
    		d=chat.objects.filter().all()
    		return render(request, 'chat.html',{'data': d})
    	else:
    		d=chat(name=request.session["name"],email=request.session["email"],message=message)
    		d.save()
    		d=chat(name='chatbot',email='chatbot',message="Invalid Doctor ID")
    		d.save()
    		d=chat.objects.filter().all()
    		return render(request, 'chat.html',{'data': d})


    if str(request.session["bookdoc"])=='date':
    	d=chat(name=request.session["name"],email=request.session["email"],message=message)
    	d.save()



    	d=bookings.objects.filter(docid=request.session["di"]).filter(dat_e=message).count()
    	
    	t=''
    	if d>7:
    		d=chat(name='chatbot',email='chatbot',message="No appointments for today, chage the date: (Ex: YYYY-MM-DD)")
    		d.save()
    		d=chat.objects.filter().all()
    		return render(request, 'chat.html',{'data': d})
    	else:
            d = d + 1
            t = timings[d]
            s = doctors.objects.filter(docid=request.session["di"])
            docid = request.session["di"]
            dname = s[0].name
    
            d = bookings(docid=request.session["di"], docname=dname, pname=request.session["name"],
                         pemail=request.session["email"], dat_e=message, stz='Confirmed', tim_e=t)
            d.save()
    
            d = chat(name='chatbot', email='chatbot',
                     message="Your Request Accepted,\nCheck your booking page..\nThank you for contacting us..\nGood Day..")
            d.save()
    
            request.session["bookdoc"] = ''
            request.session["di"] = ''
            d = chat.objects.filter().all()
            return render(request, 'chat.html', {'data': d})
        
    if len(m)>1:
    	message=""
    	for m1 in m:
    		m1=m1.strip()
    		message=message+" "+m1.replace(' ','_')

    print(message,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

    
    uemail=request.session["email"]
    uname=request.session["name"]
    d=chat(name=request.session["name"],email=uemail,message=message)
    d.save()


    ans='Sorry, Not Understood'

    cid=tf.calc(message)
    if cid!=-1:
        d=queries.objects.filter(id__exact=cid)
        for d1 in d:
            ans=d1.an_s

        d=chat(name='chatbot',email='chatbot',message=ans)
        d.save()

        d=chat.objects.filter().all()
        return render(request, 'chat.html',{'data': d})

    
    else:
        
        r=Prediction.do(message)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',r)
        request.session['disease']=r
        ans="Based on your symptoms, expected disease is "+r
        d=chat(name='chatbot',email='chatbot',message=ans)
        d.save()


        d=chat.objects.filter().all()

        return render(request, 'chat.html',{'data': d,'bt':True})


def moredetails(request):

    disease=request.session['disease']
    des=Description.objects.filter(Disease=disease)



    d=chat(name='chatbot',email='chatbot',message=des[0].Description)
    d.save()
    d=chat.objects.filter().all()

    return render(request, 'chat.html',{'data': d, 'bt':True})
        



def moredetails2(request):

    disease=request.session['disease']
    des=precautions.objects.filter(Disease=disease)

    ans=""

    for d1 in des:
    	ans=d1.Precaution_1+"; "+d1.Precaution_2+"; "+d1.Precaution_3+"; "+d1.Precaution_4+"; "


    d=chat(name='chatbot',email='chatbot',message=ans)
    d.save()
    d=chat.objects.filter().all()

    return render(request, 'chat.html',{'data': d, 'bt':True})
        

def moredetails3(request):

    disease=request.session['disease']
    disease=disease.strip()
    print(disease,'@@@@@@@@@@@@@@@@@@@@@@@@')
    des=doctors.objects.filter(Disease=disease).count()
    if des>0:
    	d=chat(name='chatbot',email='chatbot',message="Please find the list of doctors")
    	d.save()
    	d=doctors.objects.filter(Disease=disease)
    	s=""
    	for d1 in d:
    		s+="Doctor ID:"+d1.docid+"\nDr. "+d1.name+"\n"+d1.designation+"\nAddress"+d1.address
    		s+="\n----------------------------------------------\n"
    	
    	d=chat(name='chatbot',email='chatbot',message=s)
    	d.save()
    	d=chat(name='chatbot',email='chatbot',message="Enter Doctor ID to book your appointment:")
    	d.save()

    	request.session["bookdoc"]='true'


    else:
    	d=chat(name='chatbot',email='chatbot',message="Sorry no doctors available !! ")
    	d.save()
    d=chat.objects.filter().all()

    return render(request, 'chat.html',{'data': d})
        


def getmesg(request):
    from .speech import main
    main('D:\\Django\\MedicalChatService\\msg.txt')
    return redirect('chatpage2')


def adddoctor(request):
	if request.method=='POST':
		disease=request.POST['dis']
		disease=disease.strip()
		no=request.POST['no']
		name=request.POST['name']
		des=request.POST['des']
		addr=request.POST['addr']
		d=doctors(Disease=disease,docid=no, name=name, designation=des, address=addr)
		d.save()

		diseases=[]

		d=Description.objects.all()
		for d1 in d:
			diseases.append(d1.Disease)

		
		
			

		no=getnum()
		return render(request, 'adddoctor.html',{'msg': "Doctor Added Successfully!! ", 'no':no, 'diseases':diseases})

		
	else:

		no=getnum()
		diseases=[]
		d=Description.objects.all()
		for d1 in d:
			diseases.append(d1.Disease)
		

		return render(request, 'adddoctor.html', {'no':no, 'diseases':diseases})




def viewdoc(request):
    if "adminid" in request.session:
        d = doctors.objects.all()
        
        return render(request, 'viewdoc.html', {'data': d})

    else:
        return render(request, 'admin.html')



def viewapp(request):
    if request.method=='POST':
        dt=request.POST['dt']
        print(dt,'<<<<<<<<<<<')
        d = bookings.objects.filter(dat_e=dt)

        
        return render(request, 'viewapp2.html', {'data': d})

    else:
        return render(request, 'viewapp.html')



def uviewapp(request):
    if "email" in request.session:
        dt=request.session['email']
        print(dt,'<<<<<<<<<<<')
        d = bookings.objects.filter(pemail=dt)

        
        return render(request, 'uviewapp.html', {'data': d})

    else:
        return render(request, 'viewapp.html')

