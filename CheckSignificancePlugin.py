import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
import PyPluMA

def check_significance(metadata_pd, column, myoutfile, variable, val1, val2):
    users = metadata_pd[metadata_pd[variable]==val1][column]
    nonUsers = metadata_pd[metadata_pd[variable]==val2][column]
    try:
        myoutfile.write(column+": "+str(ttest_ind(users, nonUsers))+"\n")
    except TypeError:
        myoutfile.write("column '{}' has unappropriated type".format(column)+"\n")

class CheckSignificancePlugin:
    def input(self, infile):
        self.parameters = dict()
        inputfile = open(infile, 'r')
        for line in inputfile:
           contents = line.strip().split('\t')
           self.parameters[contents[0]] = contents[1]

    def run(self):
       self.metadata_pd = pd.read_csv(PyPluMA.prefix()+"/"+self.parameters["csvfile"])
       ignore = open(PyPluMA.prefix()+"/"+self.parameters["ignore"])
       self.myignore = []
       for line in ignore:
          self.myignore.append(line.strip())

    def output(self, outfile):
       columns=list(self.metadata_pd.columns)
       outputfile = open(outfile, 'w')
       for col in columns:
        if not col in self.myignore:
           check_significance(self.metadata_pd, col, outputfile, self.parameters["variable"], self.parameters["val1"], self.parameters["val2"])


#check_significance(metadata_pd, "interleukin6")
#metadata_pd.boxplot("interleukin6")
#sns.boxplot(x="Cocain_Use", y="interleukin6", data=metadata_pd)
# sns.barplot(x="Cocain_Use", y="eme_hisp_lati", data=metadata_pd, estimator=sum)
#plt.show()
