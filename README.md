
# Implement KNN Classification and Regression using Python

<b>Language Used :</b> Python<br>
<b>Operating System :</b> MAC OSX<br>
<b>Libraries :</b> csv, random, math, operator<br>
<b>Dataset :</b> iris.data.csv and pima-indians-diabetes-data.csv<br>

<p>There are a few important things that need to be noted while running this
program. The classification problem can only be solved for discrete data and for
continuous data, the regression part is going to be used. A very unique feature
that I chose to follow here is randomization of data due to which the program
was able to train itself on using different tuples each time thus giving a robust
verification of the accuracy. For the implementation of the algorithm, the
following steps need to be followed :<br>

1. Data import from a CSV file. The most important thing about the CSV file I
that the class prediction should be on the last column as the program
contains logic to hand the data in that structure.<br>

2. Step 2 is to find the nearest k neighbors based on the Euclidean distance<br>

3. This is the defining step for the classification as well as regression
problem. If the problem is classification problem, maximum votes are
calculated for each class and the class with highest votes gets its place in
the result set. Whereas, if is a regression problem, it is not possible for us
to divide the data into separate classes as the data is continuous, so we
will have to calculate the average for each attribute of the k nearest
neighbors.<br>

4. Now, for the testing phase, we will pass the test data to the training
sample and repeat steps 2 and 3 for each testing instance. Thus, for each
testing instance, we will find a result set which will be our prediction.<br>

5. Accuracy can be found out for the classification problem only as the data
is discrete and countable.<br>
</p>
<p>We can use different values of k in order to find different and new observations.
The steps to run the program are as follows :<br>

1. Download the contents of the project from the mail server. Now, we need
to check the path for the data file as we need to import the data from a
different location. You will need to modify the file path.<br>

2. The next important thing in the program is the k value. The K-value can
be inserted in the program itself in the source code as desired.<br>

3. Once step 1 and step 2 are completed, you are ready to run the program.<br>

4. Once you run the program and the data is inserted, you will be asked
whether you want to perform classification or regression. Select the
correct option and it will run the algorithm for you and give you the final
results.<br>
</p>

## Observations :

<p>
K= 2<br><br>
When I have selected the value of k as 2, an accuracy can be achieved in the
range of 94 to 97<br>

K=3, 4,5, 6<br><br>
For higher values of k, the result keeps fluctuating based on the training set and
the we can get an accuracy in the range of 88 to 97.<br>
