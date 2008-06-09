#!/bin/sh
#
# Minimal script for launching MPlayer from VDR.
#
# Expectations:
# - mplayer is found in $PATH
# - everything is configured properly in mplayer's config files

file="$1"
opts=

case "$file" in
    *.pls|*.m3u) opts="$opts -playlist" ;;
esac

while shift ; do
    case "$1" in
        SLAVE) opts="$opts -slave -quiet -nolirc" ;;
        AID)   opts="$opts -aid $2" ; shift ;;
    esac
done

exec mplayer $opts "$file"
