import os
dosya = open("metin.txt", 'r')
for satir in dosya:
    print(satir[:-1])

#-1 satır boşlupunu görmemek için var