# $Id$
# Authority: dag
# Upstream: Marius Aamodt Eriksen <marius$monkey,org>

### FIXME: Create a proper sysv script for trickled based on the template.

Summary: portable lightweight userspace bandwidth shaper
Name: trickle
Version: 1.06
Release: 3%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.monkey.org/~marius/trickle/

Source: http://www.monkey.org/~marius/trickle/trickle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libevent-devel

%description
trickle is a portable lightweight userspace bandwidth shaper. It can run
in collaborative mode (together with trickled) or in stand alone mode.

trickle works by taking advantage of the unix loader preloading.
Essentially it provides, to the application, a new version of the
functionality that is required to send and receive data through sockets.
It then limits traffic based on delaying the sending and receiving of
data over a socket. trickle runs entirely in userspace and does not
require root privileges.

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
%doc LICENSE README TODO
%doc %{_mandir}/man1/trickle.1*
%doc %{_mandir}/man5/trickled.conf.5*
%doc %{_mandir}/man8/trickled.8*
%{_bindir}/trickle
%{_bindir}/tricklectl
%{_bindir}/trickled
%{_libdir}/trickle/

%changelog
* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 1.06-3
- Rebuild against libevent-1.1a on EL5.

* Wed Mar 07 2007 Dag Wieers <dag@wieers.com> - 1.06-2
- Rebuild against libevent-1.3b.

* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Rebuild against libevent-1.3a.

* Tue Aug 05 2003 Dag Wieers <dag@wieers.com> - 1.06-0
- Initial package. (using DAR)
