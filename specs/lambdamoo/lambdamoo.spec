# $Id$
# Authority: shuff
# Upstream: 

%define moologdir %{_localstatedir}/log/lambdamoo
%define moodatadir %{_datadir}/lambdamoo
%define moostatedir %{_sharedstatedir}/lambdamoo

Summary: MUD, Object Oriented server
Name: lambdamoo
Version: 1.8.1
Release: 1%{?dist}
License: BSD
Group: Applications/Daemons
URL: http://www.moo.mud.org/

Source: http://downloads.sourceforge.net/project/lambdamoo/lambdamoo/%{version}/LambdaMOO-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge
Requires: /bin/sh
Requires: /usr/bin/compress
Requires: /usr/bin/nohup

%description
LambdaMOO is a network-accessible, multi-user, programmable, interactive system
well-suited to the construction of text-based adventure games, conferencing
systems, and other collaborative software. Its most common use, however, is as
a multi-participant, low-bandwidth virtual reality.

%prep
%setup -n MOO-%{version}

%{__cat} <<'EOF' >restart.sh
#!/bin/sh

# Copyright (c) 1992, 1995, 1996 Xerox Corporation.  All rights reserved.
# Portions of this code were written by Stephen White, aka ghond.
# Conversion to Bourne shell and other modifications by Steve Huff.
# Use and copying of this software and preparation of derivative works based
# upon this software are permitted.  Any distribution of this software or
# derivative works must comply with all applicable United States export
# control laws.  This software is made available AS IS, and Xerox Corporation
# makes no warranty about the software, its performance or its conformity to
# any specification.  Any person obtaining a copy of this software is requested
# to send their name and post office or electronic mail address to:
#   Pavel Curtis
#   Xerox PARC
#   3333 Coyote Hill Rd.
#   Palo Alto, CA 94304
#   Pavel@Xerox.Com

SBINDIR="%{_sbindir}"
STATEDIR="%{moostatedir}"
LOGDIR="%{moologdir}"

if [[ "${#@}" < 1 || "${#@}" > 2 ]]; then
    echo 'Usage: restart dbase-prefix [port]'
    exit 1
fi

DB="${STATEDIR}/${1}.db"
LOG="${LOGDIR}/${1}.log"
MOO="${SBINDIR}/lambdamoo"
PORT="${2}"

if [ ! -r "${DB}" ]; then
    echo "Unknown database: ${DB}"
    exit 1
fi

if [ -r "${DB}.new" ]; then
    mv "${DB}" "${DB}.old" && \
    mv "${DB}.new" "${DB}" && \
    rm -f "${DB}.old.Z" && \
    compress "${DB}.old"
fi

if [ -f "${LOG}" ]; then
    cat "${LOG}" >> "${LOG}.old" && \
    rm -f "${LOG}"
fi

echo `date`: RESTARTED >> "${LOG}"
#unlimit descriptors
nohup "${MOO}" "${DB}" "${DB}.new" ${PORT} >> "${LOG}" 2>&1 &

###############################################################################
# $Log: restart,v $
# Revision 1.1.1.1  1997/03/03 03:45:05  nop
# LambdaMOO 1.8.0p5
#
# Revision 2.1  1996/02/08  07:25:52  pavel
# Updated copyright notice for 1996.  Release 1.8.0beta1.
#
# Revision 2.0  1995/11/30  05:14:17  pavel
# New baseline version, corresponding to release 1.8.0alpha1.
#
# Revision 1.4  1992/10/23  23:15:21  pavel
# Added copyright notice.
#
# Revision 1.3  1992/08/18  00:34:52  pavel
# Added automatic compression of the .old database and the provision of a new
# log file for each activation, saving the old log file on the end of a
# .log.old file.
#
# Revision 1.2  1992/07/20  23:29:34  pavel
# Trying out an RCS change log in this file to see if it'll work properly.
#
###############################################################################
EOF

%build
./configure --prefix=%{_prefix} --exec-prefix=%{_exec_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -m755 -d %{buildroot}%{_bindir}
%{__install} -m755 restart.sh %{buildroot}%{_bindir}/lambdamoo-restart
%{__install} -m755 -d %{buildroot}%{_sbindir}
%{__install} -m755 moo %{buildroot}%{_sbindir}/lambdamoo
%{__install} -m755 -d %{buildroot}%{moodatadir}
%{__install} -m644 Minimal.db %{buildroot}%{moodatadir}
%{__install} -m755 -d %{buildroot}%{moostatedir}
%{__install} -m755 -d %{buildroot}%{moologdir}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post
if [ ! -r "%{moostatedir}/Minimal.db" ]; then
    cp "%{moodatadir}/Minimal.db" "%{moostatedir}"
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AddingNewMOOTypes.txt ChangeLog.txt MOOCodeSequences.txt README README.Minimal README.rX
%{_bindir}/*
%{_sbindir}/*
%{moodatadir}
%dir %{moostatedir}
%dir %{moologdir}

%changelog
* Wed Jun 6 2012 Steve Huff <shuff@vecna.org> - 1.8.1-1
- Initial package.
