if [ $# -eq 0 ];
then
    echo -e " Usag:\n	./operate.sh start\n	./operate.sh stop";
    exit
fi

case "$1" in
        "start")
                echo "start service success"
		        nohup python3 run.py> out.file 2>&1 &
                #输出两个分号
                ;;
        "stop")
                echo "stop service success"
		        kill `netstat -nlp | grep :443 | awk '{print $7}' | awk -F"/" '{ print $1 }'`
                ;;
        *)
                #其它输入
                echo "output error,please input 1/2/2"
                ;;
esac
