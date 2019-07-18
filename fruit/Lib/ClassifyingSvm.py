#from sklearn.model_selection import train_test_split
#X_train,X_test,y_train,y_test=train_test_split()
#import os
#SVM자료분석을 위한 지도학습모델이다
import random
import copy
from sklearn.svm import SVC
#from sklearn.matrix import classification_report

colors = ['red', 'yellow', 'orange', 'brown', 'green']
rgb = [[205, 22, 15], [225, 212, 95], [157, 79, 14], [59, 43, 33], [74, 91, 66]]


from sklearn.metrics import classification_report, confusion_matrix
class ClassifyingSvm:
    def readSVM(self):

        svclassifier=SVC()
        #X_train = [[245,0,0],[255,0,0],[255,254,243],[230,243,220], [244,0,0],[254,0,0],[254,254,244],[252,243,220], [245,0,0],[253,0,0],[255,254,243],[230,243,220], [245,0,0],[255,0,0],[255,254,243],[230,243,220]]
        #y_train = ['Red','Red','White','White', 'Red','Red','White','White', 'Red','Red','White','White', 'Red','Red','White','White']

        x_train,y_train = self.create_data_set(10000, 10)
        x_test, y_test = self.create_data_set(10, 10)
        svclassifier.fit(x_train, y_train)


        y_pred=svclassifier.predict(x_test)
        print(y_pred)
        print(y_test)
  #      print(svclassifer.prediction_report(y_test, y_pred))

        return svclassifier

    #using sigmoid value as kernel parameter of SVC class
    #Mapping data points from low dimensional space to a higher dimensional space can make it possible to apply SVM even for non-linear data sample.
    #os.chdir("C:\Users\신재현\EpitechSummerTeamProject\fruit\Lib\Training")
    #os.listdir()

    def create_data_set(self, how_many, max_range):
        entry = []
        label = []

        while len(entry) != how_many:
            rand = random.randint(0, len(rgb) - 1)
            color = copy.deepcopy(rgb[rand])
            label.append(colors[rand])
            for x, lettre in enumerate(color):
                range = random.sample([-1, 1], 1)[0]
                color[x] = lettre + (range * random.randint(0, max_range))
            entry.append(color)
        return entry, label
#
# accuracy = correct predictions / total predictions * 100
# accuracy = 3 / 5 * 100
# accuracy = 60%


