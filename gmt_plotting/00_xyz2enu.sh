
for i in ./kin*

do 
    sta_name=$(echo ${i} | cut -d'_' -f3) #$() let the output of the command import to parameter
    echo ${sta_name}
    time=$(echo ${i} | cut -d'_' -f2)
    ../../bin/xyz2enu ${i} "./enu_${time}_${sta_name}"

done