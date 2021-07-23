#!/usr/bin/env python

#Robosub2021_sim has the following classes: 
# police
# gangster
# gate
# gun
# badge
# marker
# marker_2
# bin1
# bin2
# dolar
# axe
# octagon
# bottle
# bootlegger
# gman

#val.txt or train.txt
file = open("/home/ivan5d/darknet/Robosub2021_sim/val.txt", "a")

#train: (1,71), val:(71,101)
for i in range (71,101):
    #gate, police y gangster esta en gate
    file.write('Robosub2021_sim/dataset/val/gate_'+str(i)+'.png')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/val/gate_'+str(i)+'(2).png')
    file.write('\n')
    #gun
    file.write('Robosub2021_sim/dataset/val/gun_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/val/gun_'+str(i)+'(2).jpg')
    file.write('\n')
    #badge
    file.write('Robosub2021_sim/dataset/val/badge_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/val/badge_'+str(i)+'(2).jpg')
    file.write('\n')
    #marker
    file.write('Robosub2021_sim/dataset/val/marker_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/val/marker_'+str(i)+'(2).jpg')
    file.write('\n')
    #pathmarker2
    file.write('Robosub2021_sim/dataset/val/pathmarker2_'+str(i)+'.png')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/val/pathmarker2_'+str(i)+'(2).png')
    file.write('\n')
    #bin1
    file.write('Robosub2021_sim/dataset/val/bin1_'+str(i)+'.png')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/val/bin1_'+str(i)+'(2).png')
    file.write('\n')
    #bin2
    file.write('Robosub2021_sim/dataset/val/bin2_'+str(i)+'.png')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/val/bin2_'+str(i)+'(2).png')
    file.write('\n')
    #table includes axe, dolar and bottle 
    file.write('Robosub2021_sim/dataset/val/table_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/val/table_'+str(i)+'(2).jpg')
    file.write('\n')
    #octagon 
    file.write('Robosub2021_sim/dataset/val/octagon_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/val/octagon_'+str(i)+'(2).jpg')
    file.write('\n')
    #torpedos includes bootlegger and gman 
    #file.write('Robosub2021_sim/dataset/val/torpedos_'+str(i)+'.jpg')
    #file.write('\n')
    #file.write('Robosub2021_sim/dataset/val/torpedos_'+str(i)+'(2).jpg')
    #file.write('\n')