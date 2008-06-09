#!/bin/sh

# http://www.pathname.com/fhs/pub/fhs-2.3.html#MEDIAMOUNTPOINT

for file in /media/* ; do
    if [ -d "$file" ] ; then
        type="`basename $file`"
        if [ "$type" = cdrom ] ; then
            echo "$file;CD-ROM;1"
        elif [ "$type" = cdrecorder ] ; then
            echo "$file;CD Writer;1"
        elif [ "$type" = zip ] ; then
            echo "$file;Zip Drive;1"
        fi
    fi
done
