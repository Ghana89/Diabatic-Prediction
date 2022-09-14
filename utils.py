import pickle
import numpy as np
import mysql.connector
class pred():

    def __init__ (self ,data):
        self.data = data
    def model_open(self):
        with open ('model.pkl' , 'rb') as file:
            self.model= pickle.load(file)
    def output(self):
        self.model_open()
        
        Glucose  = float(self.data['Glucose'] )                 
        BloodPressure  =  float(self.data['BloodPressure'] )           
        SkinThickness  =  float(self.data['SkinThickness'])
        Insulin  = float(self.data['Insulin'])
        BMI      =  float(self.data['BMI'])               
        DiabetesPedigreeFunction  = float(self.data['DiabetesPedigreeFunction'])
        Age   = float(self.data['Age'])


        conn = mysql.connector.connect(host = 'localhost' ,
                                database ='ghana',
                                user ='root',
                                password = '*Qy5LUJ3')
        query ="insert into kn_diabatics1 (Glucose , BloodPressure , SkinThickness , Insulin , BMI , DiabetesPedigreeFunction , Age ) values (%s , %s , %s , %s ,%s ,%s , %s)"
    
        cursor = conn.cursor()
        data1 = (Glucose ,BloodPressure ,SkinThickness ,Insulin ,BMI ,
        DiabetesPedigreeFunction ,Age)
        cursor.execute(query ,data1)
        conn.commit()
        conn.close()

        array = np.array([Glucose ,BloodPressure ,SkinThickness ,Insulin ,BMI ,
        DiabetesPedigreeFunction ,Age] , ndmin=2)

        result = self.model.predict(array)[0]
        return result


data = {'Glucose':148.0 , 'BloodPressure':50 , 'SkinThickness':35 ,'Insulin':0 , 'BMI':33.6 ,
'DiabetesPedigreeFunction':0.627  ,'Age': 50}
if __name__ == '__main__':
    obj = pred(data)

    result = obj.output()
