echo "put -r /users/nikitatarasov/git/above-the-hills/webserver/ /root/server_test" | sftp -i ~/.ssh/mts root@membrain.ru
echo "rename /root/server_test/webserver/webserver.py /root/server_test/webserver.py" | sftp -i ~/.ssh/mts root@membrain.ru
echo "rename /root/server_test/webserver/sqlserver.py /root/server_test/sqlserver.py" | sftp -i ~/.ssh/mts root@membrain.ru