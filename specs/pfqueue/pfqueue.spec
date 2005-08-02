# $Id$
# Authority: dag

Summary: Queue manager for the Postfix mail transport agent
Name: pfqueue
Version: 0.4.2
Release: 1
License: GPL
Group: Applications/System
URL: http://pfqueue.sourceforge.net/

Source: http://dl.sf.net/pfqueue/pfqueue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, gcc-c++
Requires: postfix

%description
pfqueue is a console application for managing mail queues used by the
Postfix mail transport agent.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/pfqueue.1*
%{_bindir}/pfqueue
%exclude %{_libdir}/libpfq_*.a
%exclude %{_libdir}/libpfq_*.la
%{_libdir}/libpfq_*.so*

%changelog
* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Fri Jun 10 2005 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Fri May 20 2005 Dag Wieers <dag@wieers.com> - 0.3.8-1
- Updated to release 0.3.8.

* Fri Mar 25 2005 Dag Wieers <dag@wieers.com> - 0.3.5-1
- Initial package. (using DAR)
