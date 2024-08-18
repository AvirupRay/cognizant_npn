from flask import Flask, jsonify
import pickle
from hotel_utils import methods
from hotel_utils import findMyHotel

app=Flask(__name__)

hotelModel=pickle.load(open("hotelModelPickle.pkl","rb"))

@app.get("/findHotel")
def findHotel():
    result_df=findMyHotel(hotelModel,"AT",["couple","leisure trip"],1,0)
    return jsonify(result_df.to_dict(orient='records'))

@app.get("/status")
def status():
    return "Flask API Working"

@app.get("/methods")
def methodRoute():
    methods()
    return "hehe"

if __name__ == "__main__":
    app.run(debug=True,port=5000)