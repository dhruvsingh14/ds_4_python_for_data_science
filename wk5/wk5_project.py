##############
# numpy prep #
##############

# importing libraries
import pandas as pd
from bokeh.plotting import figure, output_file, show, output_notebook
output_notebook

##############################
# writing dashboard function #
##############################

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)

# setting links using dictionary

links = {'GDP': 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
    'unemployment': 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

##############################
# q1: creating GDP dataframe #
##############################
# pulling data from online platform
x = pd.read_csv(links["GDP"])
print(x.head())


############################
# q2: creating a dataframe #
############################
x2 = pd.read_csv(links["unemployment"])
print(x2.head())


###############################
# q3: subsetting by threshold #
###############################
print(x2[unemployment > 8.5])































# in order to display plot within window
# plt.show()
