from fabric.api import *
from fabric.colors import green, red
from fabfile_local import SERVER_PASSWORD, DB_PASSWORD


def server():
    env.host_string = 'inodoro.homelinux.org'
    env.user = 'pocsuperproto'
    env.password = SERVER_PASSWORD


def local():
    env.host_string = 'localhost'
    env.user = 'flecox'
    env.password = 'Flecmaf77'


def create_database():
    """Creates role and database"""
    db_user = 'pocsuperproto' # define these
    db_pass = DB_PASSWORD
    db_table = 'crashplusplus'
    sudo('psql -c "DROP DATABASE %s"' % db_table, user='postgres')
    sudo('psql -c "DROP USER %s"' % db_user, user='postgres')
    sudo('psql -c "CREATE USER %s ENCRYPTED PASSWORD E\'%s\'"' % (db_user, db_pass), user='postgres')
    sudo('psql -c "CREATE DATABASE %s WITH OWNER %s"' % (
        db_table, db_user), user='postgres')


def scratch_project():
    print(red("Beginning Deploy from scratch:"))
    sudo("apt-get install postgresql")
    sudo("pip install virtualenv")
    run("rm -rf crashplusplus")
    run("git clone https://github.com/flecox/crashplusplus.git")
    create_database()
    with cd("crashplusplus"):
        run("virtualenv -p python2.7 .")
        print(green("installing dependencies..."))
        run("source bin/activate && pip install -r requeriments.txt")
        print(green("creating keys..."))
        run("rm -rf keys")
        run("mkdir keys")
        run("source bin/activate && keyczart create --location='keys' --purpose='crypt' --name='crashplusplus'")
        run("source bin/activate && keyczart addkey --location='keys' --status='primary'")

    with cd("crashplusplus/crashplusplus"):
        run("rm -f settings_local.py")
        run("touch settings_local.py")
        run('echo "DATABASES = {" >> settings_local.py')
        run('echo "\'default\': {" >> settings_local.py')
        run('echo "\'ENGINE\': \'django.db.backends.postgresql_psycopg2\'," >> settings_local.py')
        run('echo "\'NAME\': \'crashplusplus\', " >> settings_local.py')
        run('echo "\'USER\': \'pocsuperproto\'," >> settings_local.py')
        run('echo "\'PASSWORD\': \'%s\'," >> settings_local.py' % DB_PASSWORD)
        run('echo "\'HOST\': \'localhost\'," >> settings_local.py')
        run('echo "\'PORT\': \'\', " >> settings_local.py')
        run('echo "}" >> settings_local.py')
        run('echo "} " >> settings_local.py')
        run('echo "DEBUG = False" >> settings_local.py')
        run('echo "TEMPLATE_DEBUG = DEBUG" >> settings_local.py')
        run('echo "ALLOWED_HOSTS = [\'127.0.0.1\', \'localhost\', \'inodoro.homelinux.org\']" >> settings_local.py')


    with cd("crashplusplus"):
        print(green("sync database..."))
        run("source bin/activate && python manage.py syncdb --migrate")
        run("source bin/activate && python manage.py init_table")
        run("mkdir static")
        print(green("collect staticfiles..."))
        run("source bin/activate && echo 'yes\n'| python manage.py collectstatic")
        print(green("start wsgi server"))
        run("chmod +x production")
        run("chmod +x start_env.sh")


def update():
    with cd("crashplusplus"):
        run("git pull")
