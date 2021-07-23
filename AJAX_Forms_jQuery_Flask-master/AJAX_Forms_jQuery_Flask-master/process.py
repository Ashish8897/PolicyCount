from flask import Flask, render_template, request, jsonify
import pandas as pd
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import TimeField
from wtforms import StringField, SubmitField
import datetime



app = Flask(__name__)
app.secret_key='SHH!'
@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	email = request.POST['username']
	name = request.form['From']
    

	if name and email:
		newName =name
        

		return jsonify({'name' : newName})

	return jsonify({'name' : 'Missing data!'})
  
@app.route('/Non-transactional',methods=['POST', 'GET'])
def t():
   test1="C:/Users/AKENGARI/Downloads/Paperless.xlsx"
   df = pd.read_excel(test1, 'Non-transactional',index_col = None, skiprows = 1, usecols = 'A:P')
   header= df.head(1).fillna("").values
   df1 = pd.read_excel(test1, 'Non-transactional',index_col = None, skiprows = 2, usecols = 'A:P')
   return render_template('paperless.html',values=df1.fillna(0).values,headers=header)


@app.route('/TransactionalData',methods=['POST', 'GET'])
def t1():
   test1="C:/Users/AKENGARI/Downloads/Paperless.xlsx"
   #df = pd.read_excel(test1, 'TransactionalData',index_col = None, skiprows = 1, usecols = 'A:P')
   #header= df.head(1).fillna("").values
   #df1 = pd.read_excel(test1, 'TransactionalData',index_col = None, skiprows = 2, usecols = 'A:P')
   df = pd.read_excel(test1, 'TransactionalData')   
   val=df.fillna("").values
   return render_template('Transactional.html',values=val)

class ExampleForm(FlaskForm):
   
    from_date = DateField('DatePicker')
    from_time = TimeField('TimePicker')
    to_date = DateField('DatePicker', format='%d-%m-%Y')
    to_time = TimeField('TimePicker')
    #dropdownlist=['AM','PM']
    #seqSimilarity = SelectField('Delivery Types', choices=dropdownlist, default=1)

@app.route('/getForm', methods=['POST','GET'])
def form_function():
    form = ExampleForm()
    if request.method == "POST":
        
    #Getting the current from date and from time     
        #getting th from date and time
       from_date = request.form.get("from_date")
       #converting from date to month
       #Excample 2021-09-20 to 20-SEP-2021
       Updated_from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").strftime('%d-%b-%Y')
       #getting the time from input
       from_time = request.form.get("from_time").replace(":",".")
       
       #changing the time format with AM/PM as well
       Updated_from_time = datetime.datetime.strptime(from_time, "%H.%M").strftime("%I.%M %p")
       #count=Updated_from_time.len()
     
    #getting the current end date and end time
       to_date = request.form.get("to_date")
       
       Updated_to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d").strftime('%d-%b-%Y')
     
       to_time = request.form.get("to_time").replace(":",".") 
       
       Updated_to_time = datetime.datetime.strptime(to_time, "%H.%M").strftime("%I.%M %p")
     
       #time_stamp=request.form.get("seqSimilarity")
       final_from_curr_date=Updated_from_date+" "+Updated_from_time
       final_to_curr_date=Updated_to_date+" "+Updated_to_time
       count=len(final_from_curr_date)
       
    #getting the preivous week day i.e subtracting 7 days from from_date   
       previous_from= datetime.datetime.strptime(from_date, "%Y-%m-%d")-datetime.timedelta(days=7)
       
       #updating to correctt format
       updated_prev_from=previous_from.strftime('%d-%b-%Y')
       
       previous_to=datetime.datetime.strptime(to_date, "%Y-%m-%d")-datetime.timedelta(days=7)
       #Updating to date with correct format
       updated_prev_to=previous_to.strftime('%d-%b-%Y')
       
       final_from_prev_date=updated_prev_from+" "+Updated_from_time
       final_to_prev_date=updated_prev_to+" "+Updated_to_time
       
       # getting input with name = lname in HTML fo
       #a=read(first_name,dt_to)
       data=[count,final_from_curr_date,final_to_curr_date,final_from_prev_date,final_to_prev_date]
       return render_template('submit.html',final_list=data)
    return render_template('date_picker.html', form=form)


@app.route('/postproduction',methods=['POST', 'GET'])
def production():
    resultant=[]
   
    test1="C:/Users/AKENGARI/Downloads/Copy of PolicyCounts_Bound.xlsx"
    result=read_sheet((test1),resultant)
   
    #resultant.append(count(select_home,product_code,states,df))
   # Dict = dict([('SELECT HOME', select_home[0]),('SELECT AUTO', select_home[1]),('LEGACY AUTO', select_home[2])])
    #resultant=[{'Cancellation': {'SELECT HOME': [0, 32, 144, 23, 199], 'SELECT AUTO': [94, 69, 514, 35, 712], 'LEGACY AUTO': [0, 0, 251, 0, 251]}}, {'Renewal': {'SELECT HOME': [0, 49, 377, 29, 455], 'SELECT AUTO': [408, 140, 2661, 111, 3320], 'LEGACY AUTO': [0, 0, 197, 0, 197]}}, {'Policy Change': {'SELECT HOME': [0, 61, 309, 53, 423], 'SELECT AUTO': [409, 209, 3110, 139, 3867], 'LEGACY AUTO': [0, 0, 507, 0, 507]}}, {'Submission': {'SELECT HOME': [0, 16, 245, 11, 272], 'SELECT AUTO': [55, 11, 272, 9, 347], 'LEGACY AUTO': [0, 0, 0, 0, 0]}}, {'Reinstatement': {'SELECT HOME': [0, 2, 12, 2, 16], 'SELECT AUTO': [13, 8, 64, 4, 89], 'LEGACY AUTO': [0, 0, 24, 0, 24]}}, {'Rewrite': {'SELECT HOME': [0, 5, 4, 2, 11], 'SELECT AUTO': [0, 3, 64, 1, 68], 'LEGACY AUTO': [0, 0, 2, 0, 2]}}, {'Rewrite New Term': {'SELECT HOME': [0, 0, 0, 0, 0], 'SELECT AUTO': [0, 0, 0, 0, 0], 'LEGACY AUTO': [0, 0, 0, 0, 0]}}]
    return render_template('policycount.html', counts=result)

def read_sheet(test1,resultant):
    transactions=['Cancellation','Renewal','Policy Change','Submission','Reinstatement','Rewrite','Rewrite New Term']

    for transaction in transactions:
        print('started for transaction',transaction)
        
        df = pd.read_excel(test1,transaction)
       
        
        result1=count(df)
        result=dict([(transaction, result1)])
        print('result after the dict values',result)
    
        resultant.append(result)
        print('resultant after temporary update',resultant)
    #rint('resultatnt after the final update ',resultant)
    return resultant

def count(df):
    product_code=['Homeowners','PersonalAuto','LegacyAuto']
    states=['Florida','Georgia','Michigan','Tennessee']
    select_home=[]
    for product in product_code:
        print('inside product',product)
        temp=[]
           
        df_product=df.loc[df['PRODUCTCODE']==product]
       
        for state in states:
            print('inside state',state)
            df_state= df_product.loc[df_product['STATE']==state]
            print('state count for ',state,'is',df_state.shape[0])
            temp.append(df_state.shape[0])
        count=sum(temp)
        print('total count is ',count)
        temp.append(count)
        print('temp value are',temp)
        select_home.append(temp)
        print('select home after updation is ',select_home)
    total=[]
    sum1=0
    for i in range(len(select_home[0])):
       
        sum1=select_home[0][i]+select_home[1][i]+select_home[2][i]  
        print('column sum is ',sum1)
        total.append(sum1)
    select_home.append(total)
    print('select home was after updattion',select_home)
    abc=dict([('SELECT HOME', select_home[0]),('SELECT AUTO', select_home[1]),('LEGACY AUTO', select_home[2]),('TOTAL', select_home[3])])
    print('dicitonary with ',abc)
    return  abc



if __name__ == '__main__':
	app.run(debug=True)