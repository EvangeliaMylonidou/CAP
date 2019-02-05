import pandas as pd

score = pd.read_csv('whole dataset', sep=',', usecols=['Scoring'])

feat = pd.read_csv('A.csv', sep=',', header=None)
print(feat)
f = pd.DataFrame(data=feat.loc[0])
print(f)

k = []
c = 209
h = []
lab = []  # Label

for i in range(0, len(score), 105):
    if 209 < (len(score) - i):
        if (score['Scoring'][i][0] == 'S' or score['Scoring'][i][0] == 'E') and (
                score['Scoring'][i + c][0] == 'S' or score['Scoring'][i + c][0] == 'E'):
            lab.append('c0')

        elif (score['Scoring'][i][0] == 'S' or score['Scoring'][i + c][0] == 'E') and score['Scoring'][i + c][0] == 'A':
            lab.append('c1')

        elif score['Scoring'][i][0] == 'A' and score['Scoring'][i + c][0] == 'A':
            lab.append('c2')

        elif score['Scoring'][i][0] == 'A' and (score['Scoring'][i + c][0] == 'S' or score['Scoring'][i + c][0] == 'E'):
            lab.append('c3')
        else:
            h.append(i)
    else:
        c = len(score) - i - 1
        k.append(i)
        if (score['Scoring'][i][0] == 'S' or score['Scoring'][i][0] == 'E') and (
                score['Scoring'][i + c][0] == 'S' or score['Scoring'][i + c][0] == 'E'):
            lab.append('c0')

        elif (score['Scoring'][i][0] == 'S' or score['Scoring'][i + c][0] == 'E') and score['Scoring'][i + c][0] == 'A':
            lab.append('c1')

        elif score['Scoring'][i][0] == 'A' and score['Scoring'][i + c][0] == 'A':
            lab.append('c2')

        elif score['Scoring'][i][0] == 'A' and (score['Scoring'][i + c][0] == 'S' or score['Scoring'][i + c][0] == 'E'):
            lab.append('c3')
        else:
            h.append(i)

f['targets'] = lab

# len(lab) must be equal to 33530
# 3520615/105
#
# 3520545/105


f.targets.unique()
