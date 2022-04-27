import codecademylib
import numpy as np
from matplotlib import pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# 2
total_ceballos = round((sum([1 for n in survey_responses if n == "Ceballos"])), 2)
# print(total_ceballos)

# 3
percentage_ceballos = (total_ceballos/len(survey_responses))*100
print(percentage_ceballos)

# 4
len_responses = len(survey_responses)
possible_surveys = np.random.binomial(kont, 0.54, size=10000)/len_responses
print(possible_surveys)
# 5
plt.hist(possible_surveys, bins=20)
plt.show()

# 6
ceballos_loss_surveys = (np.mean(possible_surveys < 50))
print(ceballos_loss_surveys)

# 7
large_survey = np.random.binomial(7000, 0.54, size=10000)
print(large_survey)
large_survey_mean = np.mean(large_survey < 3500)
print(large_survey_mean)



