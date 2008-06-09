#!/bin/sh

mplayer=/usr/bin/mplayer
mencoder=/usr/bin/mencoder

if [ -z "$4" -o "$1" = "-?" -o "$1" = "-h" -o "$1" = "--help" ]; then
    echo "Usage: $0 <dir> <name> <size> <count>"
    echo "       Split video file"
    echo "       dir   - Directory with original video file and for part files"
    echo "       name  - Name of video file without extention"
    echo "       size  - Size of part files in MegaBytes"
    echo "       count - Part count"
    echo "Example: vdrripsplit.sh /video/mplayer/temp Example_Video 700 2"
    echo "  splits /video/mplayer/temp/Example_Video.avi"
    echo "    into /video/mplayer/temp/Example_Video-1.avi (700MB)"
    echo "     and /video/mplayer/temp/Example_Video-2.avi (remaining part)"
    exit 1
fi

tempdir=$1
name=$2
filesize=$3
filenumbers=$4

function split () {
#
# splits the encoded movie into $filenumbers pieces
#

#  local overlap=3
  local overlap=5

  local count=1
  local splitpos=0

  # workaround to get the right filesize from mencoder with -endpos
  let local splitsize=filesize*99/100

  while [ $count -le $filenumbers ]
  do
    local ofile="$name-$count.avi"

    if [ $count -eq $filenumbers ]
    then
      local endpos=""
    else
      local endpos="-endpos ${splitsize}mb"
    fi

    # split file
    local splitcmd="$mencoder -ovc copy -oac copy $tempdir/$name.avi \
                    -ss $splitpos $endpos -o $tempdir/$ofile"
    $splitcmd 2>/dev/null

    # detect length of splitted file and add it to $splitpos
    local length=`length "$tempdir/$ofile"`
    let splitpos=splitpos+length-overlap
    let count=count+1
  done
}

function length1 () {
    # print length of video to stdout
    "$mplayer" -vo null -ao null -identify -frames 0 "$1" 2>/dev/null | \
        grep ID_LENGTH | cut -d"=" -f2
}

function length () {
    # detect length of video and print it to stdout
    local length=`length1 "$1"`

    # workaround: repeat command if failed first time
    if [ -z "$length" ]; then
        length=`length1 "$1"`
    fi
    echo "$length"
}

split
