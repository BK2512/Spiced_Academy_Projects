from flask import Flask,render_template, request
from recom_function import nmf
from recom_function import Final

app = Flask(import_name=__name__)

random_movie_list=[]

@app.route("/")
def home():
    return render_template('home.html')
            
@app.route("/movie_recommandation")
def result():
    global random_movie_list
    random_movie_list=[]
    query=request.args.to_dict()
    Top10=nmf(query)
    random_movie_list.append(Top10)
    
    
    return render_template(
        'result.html',
        my_title_list=Top10,
             
    )
    
@app.route("/Final_Movie")
def random_result():
    print (random_movie_list)
    return render_template(
        'Finalsheet.html',
    )

if __name__=='__main__':
    app.run(debug=True)     
  