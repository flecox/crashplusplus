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
        run('"DATABASES = {" >> settings_local.py')
        run('"\'default\': {" >> settings_local.py')
        run('"\'ENGINE\': \'django.db.backends.postgresql_psycopg2\'," >> settings_local.py')
        run('"\'NAME\': \'crashplusplus\', " >> settings_local.py')
        run('"\'USER\': \'pocsuperproto\'," >> settings_local.py')
        run('"\'PASSWORD\': \'%s\'," >> settings_local.py' % DB_PASSWORD)
        run('"\'HOST\': \'localhost\'," >> settings_local.py')
        run('"\'PORT\': \'\', " >> settings_local.py')
        run('"}" >> settings_local.py')
        run('"} " >> settings_local.py')
        run('"DEBUG = False" >> settings_local.py')
        run('"TEMPLATE_DEBUG = DEBUG" >> settings_local.py')

    with cd("crashplusplus"):
        print(green("sync database..."))
        run("source bin/activate && python manage.py syncdb --migrate")

