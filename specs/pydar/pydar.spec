# $Id: $

# Authority: dries

# Far from finished, not to be released :)

Summary: far from finished attempt of a buildserver in python
Name: pydar
Version: 0.003
Release: 1
License: GPL
Group: Development/Tools
URL: NoUrlYet

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: pydar-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: mach
Requires: mach, coreutils

%description
Not finished, not to be released!

%package server
Summary: server part
Group: Development/Tools
Requires: mach = 0.4.3
Requires: %{name} = %{version}-%{release}

%package client
Summary: client part
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description server
Not finished, not to be released!

%description client
Not finished, not to be released!


%prep
%setup -n pydar

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
# cat /usr/bin/mach | grep -v builtin > %{buildroot}/%{_datadir}/pydar/pydar/mach.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_datadir}/pydar/pydar/*.py
%{_datadir}/pydar/defaults.conf
%config(noreplace) %{_sysconfdir}/pydar/pydar.conf


%files server
%defattr(-, root, root, 0755)
%{_sysconfdir}/rc.d/init.d/pydar-buildserver-master
%{_sysconfdir}/rc.d/init.d/pydar-buildserver-slave
%{_datadir}/pydar/pydar-buildserver-master.py
%{_datadir}/pydar/pydar-buildserver-slave.py

%files client
%defattr(-, root, root, 0755)
%{_bindir}/dar-remote
%{_bindir}/dar-speccheck
%{_datadir}/pydar/pydar-remote.py
%{_datadir}/pydar/pydar-speccheck.py
%{_datadir}/pydar/dbinit.sql

%changelog
* Tue Apr 28 2004 Dries Verachtert <dries@ulyssis.org> 0.002-1
- update

* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 0.001-1
- Initial package
