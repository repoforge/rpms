# $Id$
# Authority: dag

%{?el5:%define _without_poptdevel 1}
%{?el4:%define _without_poptdevel 1}
%{?el3:%define _without_poptdevel 1}

Summary: Filesystem load benchmarking tool
Name: dbench
Version: 4.0
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://samba.org/ftp/tridge/dbench/README

Source: http://samba.org/ftp/tridge/dbench/dbench-%{version}.tar.gz 
Patch0: dbench-4.0-destdir.patch
Patch1: dbench-4.0-datadir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
%{?_without_poptdevel:BuildRequires: popt}
%{!?_without_poptdevel:BuildRequires: popt-devel}

%description
Dbench is a file system benchmark that generates load patterns similar
to those of the commercial Netbench benchmark, but without requiring a
lab of Windows load generators to run. It is now considered a de facto
standard for generating load on the Linux VFS.

%prep
%setup
%patch0 -p1 -b .destdir
%patch1 -p1 -b .datadir

%build
./autogen.sh 
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    mandir="%{_mandir}/man1" \
    INSTALLCMD="install -p"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man1/dbench.1*
%doc %{_mandir}/man1/tbench.1*
%doc %{_mandir}/man1/tbench_srv.1*
%{_bindir}/dbench
%{_bindir}/tbench
%{_bindir}/tbench_srv
%dir %{_datadir}/dbench/
%{_datadir}/dbench/client.txt

%changelog
* Wed Jun 09 2010 Dag Wieers <dag@wieers.com> - 4.0-1
- Initial package. (using DAR)
