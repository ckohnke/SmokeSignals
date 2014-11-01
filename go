export CLASSPATH=.:./lib/*
export PYTHONPATH=.:/usr/lib/python2.7/site-packages
jython -Dpython.path=$PYTHONPATH -J-cp $CLASSPATH $*
