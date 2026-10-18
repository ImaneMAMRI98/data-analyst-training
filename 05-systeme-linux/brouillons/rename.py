import os

for root,dirs,files in os.walk("/arborescence"):
    for name in files:
        old_path = os.path.join(root,name)
        new_path = os.path.join(root,name.lower().replace(' ','_').replace('-','_'))
        os.rename(old_path, new_path)




