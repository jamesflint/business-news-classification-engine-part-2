# Business News Classification Engine (Part 2)
#### Springboard Capstone Project 2 | James Flint | mail@jamesflint.net | 2018-03-28

## Problem

Building on the work done in my first Capstone Project, use CurationCorp’s labelled news database to create a topic classifier using multilayer, CNN, LSTM and VDCNN neural nets and make the best solution available via an online API. 

## Client

My client is CurationCorp.com. This project is the first step in a machine-learning-based classification, tagging and auto-summary project that should be able the company to automate much of its editorial process, and reserve human intervention for final edit and sign-off instead of low-level textual processing tasks.

## Data

CurationCorp has a clean, human-curated database of 43,502 summarised and labelled news articles, to which I have access. For raw source data, I’ll be using a sample of data from a standard news database (LexisNexus Moreover, format: CSV) or the news aggregator dataset at http://archive.ics.uci.edu/ml/datasets/News+Aggregator.

## Approach

1.	Data wrangling2.	Compare Classifiersa.	A multi-layer neural net (NN)b.	A convolutional neural net (CNN)c.	A long/short term memory neural net (LSTM)d.	A very deep convolutional neural net (VDCNN) 3.	Build a prediction API


## Deliverables contained in this repo

* Code for all the above
* An executable online API & manual interface (folder: "topic_api")
* A paper describing the project process, methodologies, trade-offs and decision points (file: "Capstone Project 2 FINAL - Report - James Flint 20180330.pdf")
* A slide deck presenting the project to CurationCorp and suggesting strategic implementation of the technology (file: "Capstone Project 2 FINAL - Presentation - James Flint 20180330.pdf")
* A results matrix (excel file) containing the results of all trials (file: "Results matrix.xlsx")
* All the Jupyter notebooks used in the project (folder: "notebooks")
* Test articles for using with the manual interface (file: "Test articles for online form.rtf)


## Attributions

I owe a huge thank you to all at the excellent [Springboard](https://www.springboard.com/), whose Data Science Career Track course culminated (for me) in this project, and in particular to my tutor [Jan Zikeš](https://www.linkedin.com/in/ziky90/), without whose expertise and encouragement I doubt it would ever have been finished!

On the way I begged, borrowed and stole code from many, many places in order to complete this project. The main sources are listed below, but there were others, including (of course) Stack Overflow. To anyone whose contribution I may have omited here, my apologies; please let me know and I'll add you in!

* [Tokenizing text data in Keras](http://www.orbifold.net/default/2017/01/10/embedding-and-tokenizer-in-keras/) * [Very Deep Convolutional Networks for Text Classification (paper)](https://arxiv.org/abs/1606.01781)* [Keras implementation of a VDCNN model (code)](https://github.com/yuhsinliu1993/VDCNN)* [Keras API 1](https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)* [Keras API 2](https://github.com/jrosebr1/simple-keras-rest-api/blob/master/run_keras_server.py)* [Calculating the F1 metric in Keras](https://stackoverflow.com/questions/43547402/how-to-calculate-f1-macro-in-keras)* [Using GloVe in Python](http://textminingonline.com/getting-started-with-word2vec-and-glove-in-python)* [Text Classification using CNNs](https://richliao.github.io/supervised/classification/2016/11/26/textclassifier-convolutional/)* [Global Vectors for Word Representation](https://nlp.stanford.edu/projects/glove/)* [Build a CNN in 11 lines](http://adventuresinmachinelearning.com/keras-tutorial-cnn-11-lines/)* [How to Develop a Bidirectional LSTM For Sequence Classification](https://machinelearningmastery.com/develop-bidirectional-lstm-sequence-classification-python-keras/)* [Text Generation With LSTM Recurrent Neural Networks](https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/) * [Miguel Grinberg: The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)* [How to deploy a Python Flask app on Heroku](https://medium.com/@johnkagga/deploying-a-python-flask-app-to-heroku-41250bda27d0 )  * [Implementing a RESTful Web API with Python & Flask](http://blog.luisrei.com/articles/flaskrest.html) * [Adit Deshpande: A Beginner's Guide To Understanding Convolutional Neural Networks](https://adeshpande3.github.io/adeshpande3.github.io/A-Beginner's-Guide-To-Understanding-Convolutional-Neural-Networks/) * [Reuters-21578 text classification with Gensim and Keras](https://www.bonaccorso.eu/2016/08/02/reuters-21578-text-classification-with-gensim-and-keras/)* [Classifying Yelp Reviews](http://www.developintelligence.com/blog/2017/06/practical-neural-networks-keras-classifying-yelp-reviews/) 

## Running Locally

To run the API in the "topic_API" folder locally, set up a virtual environment running [Python 3.6](http://install.python-guide.org). Also, install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli); this should handle the installation of the other dependencies listed in "requirements.txt". To run the application, execute:

$ python main.py

## License

This work is licensed under a [Creative Commons Attribution 3.0 Unported License.](http://creativecommons.org/licenses/by/3.0/)


