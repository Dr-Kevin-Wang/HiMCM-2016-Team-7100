import urllib

for i in range(1,9):
    urllib.urlretrieve("https://www.ups.com/using/services/servicemaps/maps25/Recmap_000"+str(i)+".gif","./Hello/000"+str(i)+".gif")
    
for i in range(10,99):
    urllib.urlretrieve("https://www.ups.com/using/services/servicemaps/maps25/Recmap_00"+str(i)+".gif","./Hello/00"+str(i)+".gif")
    
for i in range(100,692):
    urllib.urlretrieve("https://www.ups.com/using/services/servicemaps/maps25/Recmap_0"+str(i)+".gif","./Hello/0"+str(i)+".gif")
