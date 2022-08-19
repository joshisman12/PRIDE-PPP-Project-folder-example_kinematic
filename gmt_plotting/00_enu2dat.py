import os
os.system("bash 00_xyz2enu.sh")

import glob
sta = glob.glob(r'./enu*')
for i in sta:
    station=i.split('_')[2]
    inp = open(i,'r')
    lines = inp.readlines()
    
    UTC_eq_time = '20220101_19_57_30' #Date_HR_MIN_SEC
    #inputs are GPST!!
    event_sec = float(UTC_eq_time.split('_')[1])*3600+float(UTC_eq_time.split('_')[2])*60+float(UTC_eq_time.split('_')[3])
    event_Mjd = 59581 #Modified julian date
    
    out = open('./PRIDEPPP_'+station+'.dat','w')

    #find earthquake origin position o_epos, o_npos, o_upos
    for i, line in enumerate(lines):
        Mjd = float(line.split()[0])
        sec = float(line.split()[1])
        epos = float(line.split()[2])
        npos = float(line.split()[3])
        upos = float(line.split()[4])
        if sec == event_sec and Mjd == event_Mjd:
            o_epos=float(epos)
            o_npos=float(npos)
            o_upos=float(upos)

    leap_sec = 18
    
    #make all data relative to earthquake origin time 
    for i, line in enumerate(lines):
        Mjd = float(line.split()[0])
        sec = float(line.split()[1])
        epos = float(line.split()[2])
        npos = float(line.split()[3])
        upos = float(line.split()[4])
        if Mjd == event_Mjd:
            out_sec = sec - event_sec - leap_sec
            out_epos = (epos - o_epos)*100
            out_npos = (npos - o_npos)*100
            out_upos = (upos - o_upos)*100
            out.write(f'{out_sec:.2f}  {out_epos:.3f}  {out_npos:.3f}  {out_upos:.3f}\n')
        else:
            days = Mjd - event_Mjd
            out_sec = sec+(days*86400) - event_sec - leap_sec
            out_epos = (epos - o_epos)*100
            out_npos = (npos - o_npos)*100
            out_upos = (upos - o_upos)*100
            out.write(f'{out_sec:.2f}  {out_epos:.3f}  {out_npos:.3f}  {out_upos:.3f}\n')

    #output unit: "cm"
    inp.close()
    out.close()    
         
