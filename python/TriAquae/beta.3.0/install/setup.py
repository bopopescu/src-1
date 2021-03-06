#!/usr/bin/env python

''' TriAquae software environmental requirement '''
#  python       <== 2.6
#  python-pip   <== 1.1
#  httpd        <== 2.2
#  mysql-server <== 5.0
#  snmpd        <== 5.4
#  django       <== 1.5
#  rrdtool      <== 1.47
#  shellinabox  <==2.10
#  paramiko     <== 1.10.1
#  MySQLdb
#  django_admin_bootstrapped.admin.models

# tab completion
import readline
readline.parse_and_bind('tab: complete')
# history file
import os
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')

import platform
import subprocess
import os,sys,re,time
import random_pass
import onykey_ins
import tri_config
sys.path.append(tri_config.Working_dir)
config_file = 'tri_config.py'
#import TriAquae.backend.db_connector
#from TriAquae.hosts.models import TriConfig

def Usage():
    print
    print '''\033[;32mUsage: %s 
    build --prefix=dir  Check and prepare the pre-installation environment 
    install             install software
    init		initialization TriAquae
    \033[0m''' % sys.argv[0]
    sys.exit()

try:
    if len(sys.argv[0]) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        Usage()
except IndexError:
    Usage()


''' check system release version '''
sys_info = platform.platform().lower()
if "ubuntu" in sys_info:
    sys_version = "ubuntu"
    print '\033[32;1mStart to check pre-installation environment...................................\n\033[0m'
    #must install package
    os.system('apt-get install sysstat -y >/dev/null 2>&1')
elif "redhat" in sys_info or "centos" in sys_info:
    sys_version = "redhat"
    print '\033[32;1mStart to check pre-installation environment...................................\n\033[0m'
    #must install package
    os.system('yum install sysstat -y >/dev/null 2>&1')
else:
    print '\033[;31mOnly tested RedHat,Centos and Ubuntu\033[0m'
    sys.exit()


#  setup_build function
#    a. call checking env script (write --prefix into tri_config.py Working_dir)
#    b. ask client to confirm whether to installed the required programs (yes/no)
#    c. install the relative programs by using pip install or make comipler

def setup_build(Ins_Dir):
    ''' install path write into tri_config Working_dir '''
    Working_dir = tri_config.Working_dir
    f = open(config_file,'r')
    content = f.read()
    f.close()
    new_content = re.sub("Working_dir =.*","Working_dir = '%s'" % Ins_Dir,content)
    f = open(config_file,'w')
    f.write(new_content)
    f.flush()
    f.close()

    ''' checking install environment '''
    #'''software_name : [version,command] '''
    CheckSoft = {
        "python":["2.6","python -V 2>&1|awk '{print $2}'"],
        "python-pip":["1.0","pip --version |awk '{print $2}'"],
        "rrdtool":["1.4","rrdtool -v|awk 'NR==1{print $2}'"],
        "mysql-server":["5.0","mysql -V|awk -F'[ ,]' '{print $6}'"],
        "snmpd":["5.3","snmpd -v |awk 'NR==2{print $3}'"],
        "shellinabox":["2.1","shellinaboxd --version 2>&1 |awk '{print $3}'"],
        "httpd":["2.2","apachectl -version|awk -F'/' 'NR==1{print $2}'"],
    }
    #'''models_name : [version,command] '''
    CheckMod = {
        "django":["django","1.5","django-admin.py --version"],
        "paramiko":["paramiko","1.10.1","paramiko.__version__"],
        "MySQL-python":["MySQLdb","0","0"],
        "django-admin-bootstrapped":["django_admin_bootstrapped.admin.models","0","0"],
    }

    soft_exec_list = []
    mod_exec_list = []

    ''' check software environment '''
    def check_soft():
        for soft,list in CheckSoft.items():
            version = subprocess.Popen(list[1], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout.read()
            #print soft,version
            '''judge whether number'''
            if re.match('^[a-zA-Z]',version):
                print '%s Check:\t\t \033[;31m[  NO  ]\033[0m' % soft
                print '\033[;31m%s not install\033[0m' % soft
                soft_exec_list.append(soft)
            elif len(version) == 0:
                print '%s Check:\t\t \033[;31m[  NO  ]\033[0m' % soft
                print '\033[;31m%s not install\033[0m' % soft
                soft_exec_list.append(soft)
            else:
                if version >= list[0]:
                    print '%s Check:\t\t \033[;32m[  OK  ]\033[0m' % soft
                else:
                    print '%s Check:\t\t \033[;31m[  NO  ]\033[0m' % soft
                    print '\033[;31m%s less than %s version\033[0m' % (soft,list[0])
                    soft_exec_list.append(soft)


    ''' check models environment '''
    def check_mod():
        for mod,list in CheckMod.items():
            try:
                #module = __import__(mod)
                module = __import__(list[0])
                print '%s Check:\t\t \033[;32m[  OK  ]\033[0m' % mod
            except ImportError:

                print '%s Check:\t\t \033[;31m[  NO  ]\033[0m' % mod
                print '\033[;31m%s not install\033[0m' % mod
                mod_exec_list.append(mod)
                continue
            #print '%s Check:\t \033[;32m[  OK  ]\033[0m' % mod

            #version = eval(list[2])
            #print version
            #if version >= list[1]:
            #    print '%s Check:\t\t \033[;32m[  OK  ]\033[0m' % mod
            #else:
            #    print '%s Check:\t\t \033[;31m[  NO  ]\033[0m' % mod
            #    print '\033[;31m%s less than %s version\033[0m' % (mod,list[1])
            #    mod_exec_list.append(mod)

    check_soft()
    check_mod()
    #print soft_exec_list
    #print mod_exec_list
    if len(soft_exec_list) == 0 and len(mod_exec_list) == 0:
        print "\nIf no error printed out , you can run '\033[32;40;1mpython setup.py install\033[0m' to install the program \n"
    else:
        choice = raw_input('Whether to solve above issues automatically?(y|n): ')
        if choice == 'y':
            print "You can view \033[;33m'/tmp/install.log'\033[0m for detailed installation log"
            print "You can view \033[;33m'/tmp/install_err.log'\033[0m for detailed error installation log\n"
            onykey_ins.SoftIns(soft_exec_list,sys_version,Ins_Dir)
            onykey_ins.ModIns(mod_exec_list)
            time.sleep(5)
            setup_build(Ins_Dir)
        else:
            print "\033[;31mCouldn't sovle above problems, TriAquae will not work properly before fix these errors\033[0m"


#  setup_build function
#    a. According "tri_config" to "Working_dir" parameter of file will copy the installation package to install path
#    b. 

def setup_install():
    Working_dir = tri_config.Working_dir
    if not os.path.exists(Working_dir):
        os.makedirs(Working_dir)       
    #FileCopy='cp -rp bin conf INSTALL.txt include logs modules scripts %s' % Working_dir
    FileCopy='cd ../ && cp -rp * %s' % Working_dir

    os.system(FileCopy)

    time.sleep(3)
    print '\n\033[32;1mInstall Complete\033[0m\n'
    print "If no error printed out , you can run '\033[32;40;1mpython setup.py init\033[0m' Initialize the program\n"
    print "\033[33;1m*Please create a database and make sure the database configuration in tri_config.py is correct!\033[0m"


#  setup_init function
#    a. exec manage.py syncdb (Write to the database table structure)
#    b. create "Tri_connector_username" and "Asset_collect_user" user. use random password into tri_config.py and Hardware_Check_Client_Script.py
#    c. Initialize OpsLog and IP table. OpsLog(track_mark) and IP(localhost info)

def setup_init():
    Working_dir = tri_config.Working_dir
    MySQL_Name = tri_config.MySQL_Name
    MySQL_User = tri_config.MySQL_User
    MySQL_Pass = tri_config.MySQL_Pass
    Tri_IP = tri_config.Tri_IP
    if len(tri_config.MySQL_Pass) == 0:
        import_db = "mysql -u'%s' <TriAquae.sql" % tri_config.MySQL_User
    else:
        import_db = "mysql -u'%s' -p'%s' <TriAquae.sql" % (tri_config.MySQL_User,tri_config.MySQL_Pass)
    #print import_db
    if os.system(import_db) == 0:
        ''' generate "Tri_connector_username" and "Asset_collect_user" random user passwd to tri_config and db(TriConfig) '''
        tri_connector_password = random_pass.main()
        asset_collect_user = tri_config.Asset_collect_user
        asset_user_password = random_pass.main()
        #print 'tri_connector_password',tri_connector_password
        #print 'asset_user_password',asset_user_password
        modify_tri_connector_pass = '''sed -i "s#^Tri_connector_password = .*#Tri_connector_password = '%s'#g" %s/install/%s''' % (tri_connector_password,Working_dir,config_file)
        modify_asset_pass = '''sed -i "s#^Asset_user_password = .*#Asset_user_password = '%s'#g" %s/install/%s''' % (asset_user_password,Working_dir,config_file)
        #modify asset management script username and password by DengLei
        modify_username = '''sed -i "s#^triaquae_user=.*#triaquae_user='%s'#g" %s/TriAquae/backend/Tri_Scrwer.py''' % (asset_collect_user,Working_dir)
        modify_password = '''sed -i "s#^old_passwd=.*#old_passwd='%s'#g" %s/TriAquae/backend/Tri_Scrwer.py''' % (asset_user_password,Working_dir)


        #modify install directory db connector info
        modify_MySQL_Name = '''sed -i "s#^MySQL_Name = .*#MySQL_Name = '%s'#g" %s/install/tri_config.py''' % (MySQL_Name,Working_dir)
        modify_MySQL_User = '''sed -i "s#^MySQL_User = .*#MySQL_User = '%s'#g" %s/install/tri_config.py''' % (MySQL_User,Working_dir)
        modify_MySQL_Pass = '''sed -i "s#^MySQL_Pass = .*#MySQL_Pass = '%s'#g" %s/install/tri_config.py''' % (MySQL_Pass,Working_dir)
        modify_Tri_IP = '''sed -i "s#^Tri_IP = .*#Tri_IP = '%s'#g" %s/install/tri_config.py''' % (Tri_IP,Working_dir)
        os.system(modify_tri_connector_pass)
        os.system(modify_asset_pass)
        os.system(modify_username)
        os.system(modify_password)
        os.system(modify_MySQL_Name)
        os.system(modify_MySQL_User)
        os.system(modify_MySQL_Pass)
        os.system(modify_Tri_IP)
        time.sleep(2)

        ''' TriAquae configure tri_connector user '''
        tri_connector_username = tri_config.Tri_connector_username
        tri_connector_password = tri_connector_password
        tri_connector_scripts = tri_config.Tri_connector_baoleiuser
        if os.system('id %s >/dev/null 2>&1' % tri_connector_username) != 0:
            if sys_version == "ubuntu":
                os.system('useradd -r -m -s /bin/bash %s' % (tri_connector_username))
                os.system('echo %s:%s |chpasswd' % (tri_connector_username,tri_connector_password))
                #configure .profile
                f = open('/home/%s/.profile' % tri_connector_username,'a')
                f.write('python %s\nlogout\n' % tri_connector_scripts)
                f.flush()
                f.close()
            elif sys_version == "redhat":
                os.system('useradd %s' % (tri_connector_username))
                os.system('echo %s |passwd %s --stdin >/dev/null 2>&1' % (tri_connector_password,tri_connector_username))
                #configure .profile
                f = open('/home/%s/.bash_profile' % tri_connector_username,'a')
                f.write('python %s\nlogout\n' % tri_connector_scripts)
                f.flush()
                f.close()

        ''' Create all related dirs '''
        os.system('python tri_config.py --initial')

        ''' Timing to perform asset management to collect '''
        if sys_version == "ubuntu":
            cron_path = "/var/spool/cron/crontabs/root"
        elif sys_version == "redhat":
            cron_path = "/var/spool/cron/root"
        cmd = '''
        \n# TriAquae Automatically collect hardware information
        \n00 00 * * * /usr/bin/python %s/TriAquae/backend/Hardware_Multiprocess_Run_Collect_And_write.py\n''' % Working_dir
        f = open(cron_path,'a')
        f.write(cmd)
        f.close()


        '''Customize django_admin'''
        import django_admin_bootstrapped
        os.system('/bin/cp -rp admin %s/templates/' % ''.join(django_admin_bootstrapped.__path__))

    else:
        print '\033[;31mYour database configuration errors\033[0m'
        sys.exit(1)


''' Determine the user steps '''
if sys.argv[1] == "build":
    try:
        sys.argv[2]
    except IndexError:
        print '\n\033[;31mError: You must specify where to install this program\033[0m\n'
        sys.exit()

    if sys.argv[2].startswith('--prefix='):
        Ins_Dir = sys.argv[2].split('=')[1]
        if len(Ins_Dir) == 0:
            Ins_Dir = "/usr/local/TriAquae"
        setup_build(Ins_Dir)
    else:
        Usage()

elif sys.argv[1] == "install":
    setup_install()
elif sys.argv[1] == "init":
    setup_init()
else:
    Usage()

