# $Id$
# Authority: dag

Summary: Queue manager for the Postfix and Exim mail transport agents
Name: pfqueue
Version: 0.5.6
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://pfqueue.sourceforge.net/

Source: http://dl.sf.net/pfqueue/pfqueue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, gcc-c++
### Work with both postfix and Exim
#Requires: postfix

%description
pfqueue is a console application for managing mail queues used by the
Postfix and Exim mail transport agents.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/pfqueue.1*
%doc %{_mandir}/man5/pfqueue.conf.5*
%{_bindir}/pfqueue
%{_bindir}/spfqueue
%exclude %{_libdir}/libpfq*.a
%exclude %{_libdir}/libpfq*.la
%{_libdir}/libpfq*.so*

%changelog
* Tue Feb 13 2007 Dag Wieers <dag@wieers.com> - 0.5.6-1
- Updated to release 0.5.6.

* Fri Feb 02 2007 Dag Wieers <dag@wieers.com> - 0.5.5.1-1
- Updated to release 0.5.5.1.

* Fri Feb 02 2007 Dag Wieers <dag@wieers.com> - 0.5.5-1
- Updated to release 0.5.5.

* Sat Jan 20 2007 Dag Wieers <dag@wieers.com> - 0.5.4-1
- Updated to release 0.5.4.

* Sat Sep 30 2006 Dag Wieers <dag@wieers.com> - 0.5.3-1
- Updated to release 0.5.3.

* Fri Jun 09 2006 Dag Wieers <dag@wieers.com> - 0.5.2-2
- Removed postfix dependency as it can be used with exim. (Bryan Muthig)

* Mon Feb 06 2006 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Updated to release 0.5.2.

* Thu Jan 12 2006 Dag Wieers <dag@wieers.com> - 0.5.1-1
- Updated to release 0.5.1.

* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Updated to release 0.5.0.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Fri Jun 10 2005 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Fri May 20 2005 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Updated to release 0.3.8.

* Fri Mar 25 2005 Dag Wieers <dag@wieers.com> - 0.3.5-1
- Initial package. (using DAR)
