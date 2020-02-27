import os

package_list = ['sklearn', 'numpy', 'nltk']

for item in package_list:
    try:
        __import__(item)
    except:
        os.system('pip install '+item)

