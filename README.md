# CheckSignificance
# Language: Python
# Input: TXT
# Output: TXT
# Tested with: PluMA 2.0, Python 3.6
# Dependencies: pandas==1.1.5, matplotlib==3.3.3, scipy==1.4.1, sklearn==0.23.1

PluMA plugin to check significance of a variable for differentiating two sample sets.
Scores are sent to an output TXT.

Input is a TXT file of tab-delimited keyword-value pairs:
csvfile: metadata
ignore: attributes to ignore
variable: target variable
val1: Group A separator
val2: Group B separator

