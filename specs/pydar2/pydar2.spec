# $Id$

# Authority: dries

# Again far from finished, not to be released :)

Summary: buildserver in python
Name: pydar2
Version: 0.007
Release: 1
License: GPL
Group: Development/Tools
URL: http://dries.ulyssis.org/pydar2/

Source: http://dries.ulyssis.org/pydar2/files/pydar2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-log4py

%description
Not finished, not to be released!
But if you want to try anyway, try to follow the howto.txt

%package master
Summary: pydar2 master server
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%package client
Summary: pydar2 client
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%package slave
Summary: pydar2 slave
Group: Development/Tools
Requires: %{name} = %{version}-%{release}

%description master
Not finished

%description client
Not finished

%description slave
Not finished

%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/howto.txt
%{_datadir}/pydar2/pydar
%dir %{_sysconfdir}/pydar2


%files master
%defattr(-, root, pydar2master, 0740)
%attr(0740, root, pydar2master) %config(noreplace) %{_sysconfdir}/pydar2/master.conf
%attr(0740, root, pydar2master) %config(noreplace) %{_sysconfdir}/pydar2/specrepositories.conf
%attr(0740, root, pydar2master) %config(noreplace) %{_sysconfdir}/pydar2/targets.conf
%attr(0740, root, pydar2master) %config(noreplace) %{_sysconfdir}/pydar2/accounts.conf
%defattr(-, pydar2master, pydar2master, 0700)
%dir %{_var}/lib/pydar2/specrepos
%defattr(-, pydar2master, pydar2master, 0755)
%dir %{_var}/lib/pydar2/masterwebroot
%defattr(-, root, root, 0755)
%dir %{_var}/lib/pydar2
%{_datadir}/pydar2/sql
%{_datadir}/pydar2/pydar-buildserver-master.py

%files slave
%defattr(-, root, pydar2slave, 0740)
%config(noreplace) %{_sysconfdir}/pydar2/slave.conf
%defattr(-, pydar2slave, pydar2slave, 0700)
%dir %{_var}/lib/pydar2/slavedataroot
%dir %{_var}/lib/pydar2/roots
%dir %{_var}/lib/pydar2/yum
%defattr(-, root, root, 0755)
%{_datadir}/pydar2/pydar-buildserver-slave.py

%files client
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/pydar2/client.conf
%{_datadir}/pydar2/pydar-remote.py

%pre
/usr/sbin/groupadd pydar2master || :
/usr/sbin/groupadd pydar2slave || :
/usr/sbin/useradd -g pydar2master pydar2master || :
/usr/sbin/useradd -g pydar2slave pydar2slave || :

%changelog
* Sat May 14 2005 Dries Verachtert <dries@ulyssis.org> 0.007-1
- Update

* Tue May 9 2004 Dries Verachtert <dries@ulyssis.org> 0.004-1
- this version actually works with different buildmachines

* Tue Apr 28 2004 Dries Verachtert <dries@ulyssis.org> 0.002-1
- update

* Sat Mar 20 2004 Dries Verachtert <dries@ulyssis.org> 0.001-1
- Initial package
