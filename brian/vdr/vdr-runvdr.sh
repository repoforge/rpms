#!/bin/bash

# runvdr - VDR launcher
#
# runvdr [VDROPTION]...

VDR=/usr/sbin/vdr
PLUGINDIR=/usr/lib/vdr
PLUGINVER=VDR_PLUGIN_VERSION

prog=$(basename $0)
log()
{
    [ -x /usr/bin/logger ] && \
        /usr/bin/logger -s -pdaemon.info -t"$prog" "$1" || echo "INFO: $1"
}

plugconf()
{
    local plugin="$1" PLUGIN_OPTIONS= PLUGIN_ENABLED=
    if [ -e "/etc/sysconfig/vdr-plugins.d/$plugin.conf" ] ; then
        . "/etc/sysconfig/vdr-plugins.d/$plugin.conf"
    fi
    case "$PLUGIN_ENABLED" in no|false|0) return ;; esac
    VDR_OPTIONS[${#VDR_OPTIONS[@]}]=-P
    if [ -z "$PLUGIN_OPTIONS" ] ; then
        VDR_OPTIONS[${#VDR_OPTIONS[@]}]="$plugin"
    else
        VDR_OPTIONS[${#VDR_OPTIONS[@]}]="$plugin $PLUGIN_OPTIONS"
    fi
}

build_cmdline()
{
    local file= plugin= p= libsuf=$1
    # Add "priority" plugins.
    if [ -n "$VDR_PLUGIN_ORDER" ] ; then
        for plugin in $VDR_PLUGIN_ORDER ; do
            if [ -e $PLUGINDIR/libvdr-${plugin}.so$libsuf ] ; then
                plugconf $plugin
            fi
        done
    fi
    # Add the rest available.
    for file in $PLUGINDIR/libvdr-*.so$libsuf ; do
        plugin=`basename $file | sed -e 's/^libvdr-\(.*\)\.so.*$/\1/'`
        if [ -n "$VDR_PLUGIN_ORDER" ] ; then
            for p in $VDR_PLUGIN_ORDER ; do
                if [ "$plugin" = "$p" ] ; then
                    # Already added.
                    continue 2
                fi
            done
        fi
        if [ -e "$file" ] ; then
            plugconf "$plugin"
        fi
    done
}

reload_dvb()
{
    modules=$(/sbin/lsmod | grep ^dvb_core | awk '{ print $4 }' | tr , ' ')
    /sbin/modprobe -r $modules dvb_core
    for module in $modules ; do
        /sbin/modprobe $module
    done
}

rc=
while true ; do

    VDR_OPTIONS=()
    if [ -n "$VDR_INIT" ] ; then
        [ -f /etc/sysconfig/vdr ] && . /etc/sysconfig/vdr
        if [ -n "$DAEMON_COREFILE_LIMIT" ] ; then
            ulimit -S -c $DAEMON_COREFILE_LIMIT >/dev/null 2>&1 && \
                cd ${TMPDIR:-/tmp}
        fi
        build_cmdline ${PLUGINVER:+.$PLUGINVER}
    fi

    $VDR "$@" "${VDR_OPTIONS[@]}"
    rc=$?

    # 137: "kill -KILL" eg in killproc(), others: "man vdr"
    case $rc in
        0|2|137)
            log "VDR exited with status $rc, exiting"
            break
            ;;
        *)
            log "VDR exited with status $rc, attempting restart"
            reload_dvb
            ;;
    esac

done

exit $rc
