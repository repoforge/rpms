#!/bin/sh
# $Id: build-x86.sh,v 1.1 2004/02/26 10:51:55 thias Exp $

# For my laptop ;-)
# rpmbuild -bb --define 'cards maestro3' --target i686 \
# --without isapnp --define 'kernel ...
                                                                                
if [ -z "$1" ]; then
        echo "Script to rebuild source and all possible x86 binary packages."
        echo "Usage : $0 <kernel> <rpmbuild options>"
        exit 1
fi
                                                                                
kernel="$1"
shift
for arch in i386 i586 i686 athlon; do
        rpmbuild -ba --target ${arch} --define "kernel ${kernel}" $* *.spec
done
                                                                                
for arch in i686 athlon; do
        rpmbuild -bb --target ${arch} --define "kernel ${kernel}smp" $* *.spec
done
                                                                                
echo "*** DON'T FORGET TO SIGN ALL PACKAGES IF NEEDED ***"

