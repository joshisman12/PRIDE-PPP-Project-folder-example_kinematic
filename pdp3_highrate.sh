declare -a file_name #declare an array
file_name=(./data/2022/????0020.22o) #just need the first day file name of the station
for tmp in ${file_name[@]}; # if using @ or * as an index, the word expands to all members of the array.
do    
    pdp3 -m k -cfg ./config/config_highrate -s 2022/002 -e 2022/003 12:00:00 -i 30 $tmp
done
#pdp3 -m k -cfg ./config/config_highrate -s 2016/02/05 -e 2016/02/06 23:59:59 -i 1 ./data/2016/multiday/gs890360.16o