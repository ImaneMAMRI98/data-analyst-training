import re
import os
dept = []
for root, dirs, files in os.walk("/home/data-09/Bureau/Formation_data/5-Syst/iteration_3/archive/WDGAS"):
    for file in files:
        res = re.sub(r'\d','',file)
        res = res.replace("-","_")
        nom = res.split('_')
        for i in nom:
            if (len(i) == 2 and i.isupper()):
                dept.append(i)
print(set(dept))