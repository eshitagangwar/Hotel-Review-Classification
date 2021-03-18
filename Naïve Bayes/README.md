
# Programs
You will write two programs in Python 3: nblearn.py will learn a naive Bayes model from the training data, and nbclassify.py will use the model to classify new data.

The learning program will be invoked in the following way:

> python nblearn.py /path/to/input

The argument is the directory of the training data; the program will learn a naive Bayes model, and write the model parameters to a file called nbmodel.txt. 

The format of the model  should follow the following guidelines:

The model file should contain sufficient information for nbclassify.py to successfully label new data.
The model file should be human-readable, so that model parameters can be easily understood by visual inspection of the file.
The classification program will be invoked in the following way:

> python nbclassify.py /path/to/input

The argument is the directory of the test data; the program will read the parameters of a naive Bayes model from the file nbmodel.txt, classify each file in the test data, and write the results to a text file called nboutput.txt in the following format:

label_a label_b path1
label_a label_b path2
⋮

In the above format, label_a is either “truthful” or “deceptive”, label_b is either “positive” or “negative”, and pathn is the path of the text file being classified.
