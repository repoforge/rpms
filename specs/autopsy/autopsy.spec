# $Id$

# Authority: dag
# Upstream: Brian Carrier <carrier@sleuthkit.org>

Summary: A forensic browser for use with Sleuth Kit.
Name: autopsy
Version: 1.74
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.sleuthkit.org/autopsy/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/autopsy/autopsy-%{version}.tar.gz
Patch0: autopsy.patch-1.74
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: sleuthkit >= 1.61
Provides: perl(conf.pl), perl(define.pl), perl(fs.pl), perl(search.pl), perl(autopsyfunc)

%description
The Autopsy forensic browser is a graphical interface to utilities
found in the Sleuth Kit.  Autopsy is the only open source graphical
interface for the forensic analysis of Microsoft and UNIX file systems.

It allows the allocated and deleted files, directories, blocks, and
inodes of file system images to be analyzed in a read-only environment.
Images can be searched for strings and regular expressions to recover
deleted material.  It also allows one to create a detailed time line of
the Modified, Access, and Changed times of files.

%prep
%setup 

%{__cat} <<'EOF' >autopsy
#!%{__perl} -wT
use lib '%{_datadir}/autopsy';
EOF
%{__cat} base/autopsy.base >>autopsy

%{__cat} <<'EOF' >autopsyfunc.pm
#!%{__perl} -wT
EOF
%{__cat} base/autopsyfunc.pm.base >>autopsyfunc.pm

%{__perl} -pi.orig -e 's|\$INSTALLDIR/|%{_datadir}/autopsy/|' autopsy 
%{__perl} -pi.orig -e 's|\$INSTALLDIR|%{_datadir}/autopsy|' define.pl

%patch0 -p1

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_datadir}/autopsy/ \
			%{buildroot}%{_localstatedir}/log/autopsy/ \
			%{buildroot}%{_localstatedir}/morgue/ \
			%{buildroot}%{_mandir}/man1/
%{__install} -m0755 autopsy %{buildroot}%{_sbindir}
%{__install} -m0755 autopsyfunc.pm fs.pl search.pl %{buildroot}%{_datadir}/autopsy/
%{__install} -m0600 conf.pl define.pl %{buildroot}%{_datadir}/autopsy/
%{__install} -m0644 man/man1/* %{buildroot}%{_mandir}/man1/
%{__cp} -r help/ pict/ %{buildroot}%{_datadir}/autopsy/
#%{__cp} base/fsmorgue %{buildroot}%{_localstatedir}/morgue/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README TODO 
%doc %{_mandir}/man?/*
%config(noreplace) %{_datadir}/autopsy/conf.pl
%config(noreplace) %{_datadir}/autopsy/define.pl
%{_sbindir}/*
%{_localstatedir}/log/autopsy/
%{_localstatedir}/morgue/
%{_datadir}/autopsy/

%changelog
* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.74-1
- Fix installation.

* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 1.74-0
- Updated to release 1.74.

* Sun Jul 13 2003 Dag Wieers <dag@wieers.com> - 1.73-0
- Initial package. (using DAR)
