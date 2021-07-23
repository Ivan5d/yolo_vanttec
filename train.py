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

#test.txt or train.txt
file = open("/home/ivan5d/darknet/Robosub2021_sim/train.txt", "a")

#train: (1,71))
for i in range (1,71):
    #gate, police y gangster esta en gate
    file.write('Robosub2021_sim/dataset/train/gate_'+str(i)+'.png')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/gate_'+str(i)+'(2).png')
    file.write('\n')
    #gun
    file.write('Robosub2021_sim/dataset/train/gun_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/gun_'+str(i)+'(2).jpg')
    file.write('\n')
    #badge
    file.write('Robosub2021_sim/dataset/train/badge_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/badge_'+str(i)+'(2).jpg')
    file.write('\n')
    #marker
    file.write('Robosub2021_sim/dataset/train/marker_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/marker_'+str(i)+'(2).jpg')
    file.write('\n')
    #pathmarker2
    file.write('Robosub2021_sim/dataset/train/pathmarker2_'+str(i)+'.png')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/pathmarker2_'+str(i)+'(2).png')
    file.write('\n')
    #bin1
    file.write('Robosub2021_sim/dataset/train/bin1_'+str(i)+'.png')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/bin1_'+str(i)+'(2).png')
    file.write('\n')
    #bin2
    file.write('Robosub2021_sim/dataset/train/bin2_'+str(i)+'.png')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/bin2_'+str(i)+'(2).png')
    file.write('\n')
    #table includes axe, dolar and bottle 
    file.write('Robosub2021_sim/dataset/train/table_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/table_'+str(i)+'(2).jpg')
    file.write('\n')
    #octagon 
    file.write('Robosub2021_sim/dataset/train/octagon_'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/octagon_'+str(i)+'(2).jpg')
    file.write('\n')
    #torpedos includes bootlegger and gman 
    file.write('Robosub2021_sim/dataset/train/torpedos'+str(i)+'.jpg')
    file.write('\n')
    file.write('Robosub2021_sim/dataset/train/torpedos_'+str(i)+'(2).jpg')
    file.write('\n')