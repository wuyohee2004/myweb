#!/usr/bin/env python
# Author: Alex Li
import multiprocessing
import sys, os, time
import db_connector, logger, MultiRunCounter
#----------------Use Django Mysql model----------------

cur_dir = os.path.dirname(os.path.abspath(__file__))
print cur_dir
script = 'python %s/run_command4.py' % cur_dir
print script






# batch run process




def run(host,cmd,run_user,track_num):
    print ("Thread-JOB",host)
    task = '''%s %s '%s' %s %s''' % (script, host, cmd, run_user, track_num)
    os.system(task)


if __name__ == "__main__":
    try:
        if sys.argv[1] == '-h':
            print "Usage: "
            sys.exit()
    except IndexError:
        print "argument error,try -h for help"
        sys.exit()
    try:
        if sys.argv[1] == "--auto":
            track_num = MultiRunCounter.AddNumber()
        else:
            track_num = sys.argv[1]
    except IndexError:
        print "argument error,try -h for help"
        sys.exit()
    run_user = sys.argv[4]
    print sys.argv
    raw_ip_list = sys.argv[2].split('_')
    print('raw IP list:',raw_ip_list)
    remove_duplicate_ip = set(raw_ip_list)
    ip_list = list(remove_duplicate_ip)
    if len(ip_list) < 50:
        thread_num = len(ip_list)
    else:
        thread_num = 30
    print ("ip_list",ip_list)
    cmd = sys.argv[3]
    logger.RecordLogSummary('CREATE', 'BatchRunCommand', track_num, run_user, cmd, len(ip_list),'/tmp/opt_%s.log' % track_num)
    pool = multiprocessing.Pool(processes=thread_num)
    result = []
    multiprocessing.freeze_support()
    for ip in ip_list:
        result.append(pool.apply_async(run, (ip,cmd,run_user,track_num)))
    #time.sleep(5)
    #pool.terminate()

    pool.close()
    pool.join()

    for res in result:
        res.get(timeout=5)
