from sklearn.ensemble import GradientBoostingClassifier
import pandas as strpd
strdf = strpd.read_csv('stresset.csv')
strdf["PDMax?"] = strdf["PDMax?"].map({'PDMaxAbnormal':-1,'PDMaxProlonged':0,'PDMaxNormal':1})
strdf["MeanPD?"] = strdf["MeanPD?"].map({'UsualMeanPD':1,'PoorMeanPD':0})
strdf["XPDMax?"] = strdf["XPDMax?"].map({'XPDMaxnormal':1,'XPDMaxabnormal':0})
strdf["XPDMin?"] = strdf["XPDMin?"].map({'XPDMinUp':1,'XPDMinDown':0})
strdf["YPDMax?"] = strdf["YPDMax?"].map({'UsualYPDMax':1,'DepressedYPDMax':0})
strdf["YPDMin?"] = strdf["YPDMin?"].map({'YPDMinnormal':1,'YPDMinabnormal':0})
strdf["PDMin?"] = strdf["PDMin?"].map({'PDMinaboveRange':-1,'PDMinbelowRange':0,'PDMininRange':1})
strdf["PDSkew?"] = strdf["PDSkew?"].map({'RegularPDSkew':1,'IrregularPDSkew':0})
strdf["PDVariance?"] = strdf["PDVariance?"].map({'EffectivePDVariance':1,'IneffectivePDVariance':0})
strdf["PDMedian?"] = strdf["PDMedian?"].map({'NormalPDMedian':1,'AbnormalPDMedian':0})
strdf["StressLevel?"] = strdf["StressLevel?"].map({'Low':2,'Medium':1,'High':0})
strdata = strdf[["PDMax?","MeanPD?","XPDMax?","XPDMin?","YPDMax?","YPDMin?","PDMin?","PDSkew?","PDVariance?","PDMedian?","StressLevel?"]].to_numpy()
strinputs = strdata[:,:-1]
stroutputs = strdata[:, -1]
strtraining_inputs = strinputs[:400]
strtraining_outputs = stroutputs[:400]
testing_strinputs = strinputs[400:]
testing_stroutputs = stroutputs[400:]
classifier = GradientBoostingClassifier()
classifier.fit(strtraining_inputs, strtraining_outputs)
StressLevels = classifier.predict(testing_strinputs)
from sklearn.metrics import accuracy_score
accuracy = 100.0 * accuracy_score(testing_stroutputs, StressLevels)
print ("The accuracy of GB Classifier on testing strdata is: " + str(accuracy))
testSet = [[0,0,1,0,0,0,0,0,0,0]]
test = strpd.DataFrame(testSet)
StressLevels = classifier.predict(test)
print('GB prediction on the first test set is:',StressLevels)
testSet = [[0,0,1,0,1,1,1,0,0,1]]
test = strpd.DataFrame(testSet)
StressLevels = classifier.predict(test)
print('GB prediction on the second test set is:',StressLevels)
testSet = [[1,1,1,0,1,1,0,1,1,1]]
test = strpd.DataFrame(testSet)
StressLevels = classifier.predict(test)
print('GB prediction on the third test set is:',StressLevels)
