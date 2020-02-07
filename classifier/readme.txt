Presenting the submission in two ways :- 

1) Webapp
2) Code for classifying the given test data and exporting the data

Webapp :- 

Link to github repositary - https://github.com/BeingHomosapien/patentclassifier
Link to webapp - https://patent-classifier.herokuapp.com/

Code :- 

1) Open the classifier folder in the repositary :- 
https://github.com/BeingHomosapien/patentclassifier/tree/master/classifier

2) Install the dependencies from requirements.txt using
pip install -r requirements.txt

3) To train the model and make predictions, run "code.py"

4) To predict using the trained model (dump inside model folder), follow the steps :-

	a) Navigate to the model folder
	b) Run - "pip install joblib"
	c) Create a python file with the code :- 

		from sklearn.feature_extraction.text import CountVectorizer
		import joblib
		clf = joblib.load("finalmodel.sav")  
		cv = joblib.load("count_vect")

		#Add additional lines of code, to work with the model
		#clf is model object
		#cv is count vectorizer object






