#Author: Alex Li
import os,sys

Working_dir = '/usr/local/TriAquae'
Web_dir = '/var/www/TriAquae'
Max_batch_threads =  35
Tri_sftp_dir = '%s/TriSFTP' % Working_dir
Tri_sftp_send_dir = '%s/TriSFTP/send' % Working_dir
Tri_sftp_recv_dir = '%s/TriSFTP/recv' % Working_dir
Dangerous_cmd_list = '%s/share/dangerous_cmd.txt' % Working_dir
RRDTOOL_install_dir = '%s/rrdtool' % Working_dir
RRDTOOL_png_dir = '%s/rrdtool_png' % Web_dir 
RRDTOOL_rrd_file_dir= '%s/rrdtool/rrd_files' % Working_dir
Shellinaboxed_install_dir = '%s/shellinaboxed' % Working_dir
#TriAquae database info
MySQL_Name = 'TriAquae'	# Change the database name is not currently supported, use the default
MySQL_User = 'root'
MySQL_Pass = 'alex3714'

#TriAquae Log settings
Log_dir = '%s/TriAquae/logs' % Working_dir
Snmp_temp_log = '%s/snmp_temp.log' % Log_dir

Tri_IP = '118.244.168.45'
Tri_connector_username = 'tri_connector'
#Tri_connector_password = 'OwP9xQ3vVs2PbYiR4lSM'
Tri_connector_password = '1'
Tri_connector_baoleiuser = '%s/TriAquae/backend/baoleiuser.py' % Working_dir
Tri_connector_baoleihost = '%s/TriAquae/backend/baoleihost.py' % Working_dir

Asset_collection_dir = '%s/asset_collection' % Log_dir
Asset_collection_backup_dir = '%s/asset_collection_backup' % Log_dir
Ops_log_temp_purge_days = 1

SMTP_server = 'smtp.126.com'
Mail_username = 'lijie3721'
Mail_password = 'Motherfucker!23'

Asset_collect_user = 'triaquae'
Asset_user_password = 'h7VN1Af4qYx3wcJfBtNI'

dir_list = [Working_dir, Web_dir,Tri_sftp_dir, Log_dir,Tri_sftp_send_dir, Tri_sftp_recv_dir, Dangerous_cmd_list, RRDTOOL_install_dir,RRDTOOL_png_dir,RRDTOOL_rrd_file_dir,Shellinaboxed_install_dir,Asset_collection_dir,Asset_collection_backup_dir]


try:
    if sys.argv[1] == '--initial':
        for d in dir_list:
            try:
            	os.mkdir(d)
            except OSError:continue
except IndexError:pass
