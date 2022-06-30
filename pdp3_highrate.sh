#pdp3 -m k -cfg ./config/config_highrate -s 2022/03/22 -e 2022/03/22 23:59:59 -i 1 ./data/2022/081/ASJH0810.22o

declare -a file_name 
file_name=(./data/2022/081-082/IES/RINEX/????081?.22o)
for tmp in ${file_name[@]};
do    
    pdp3 -m k -cfg ./config/config_highrate -s 2022/081 -e 2022/082  -i 0.02 $tmp
done

#pdp3 -m k -cfg ./config/config_highrate -s 2022/081 -e 2022/082 23:59:59 -i 1 ./data/2022/081-082/WULU0810.22o

