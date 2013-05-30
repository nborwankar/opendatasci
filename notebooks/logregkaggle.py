# logreg kaggle
# from http://datascience101.wordpress.com/2012/05/23/your-first-kaggle-submission/


from sklearn.linear_model import LogisticRegression
import csv_io
import math
import scipy


def main():
    #read in the training file
    train = csv_io.read_data("train.csv")
    #set the training responses
    target = [x[0] for x in train]
    #set the training features
    train = [x[1:] for x in train]
    #read in the test file
    realtest = csv_io.read_data("test.csv")

    # code for logistic regression
    lr = LogisticRegression()
    lr.fit(train, target)
    predicted_probs = lr.predict_proba(realtest)
    
    # write solutions to file
    predicted_probs = ["%f" % x[1] for x in predicted_probs]
    csv_io.write_delimited_file("log_solution.csv", predicted_probs)
    
    print ('Logistic Regression Complete! Submit log_solution.csv to Kaggle')

if __name__=="__main__":
    main()