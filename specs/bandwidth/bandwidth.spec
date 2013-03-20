# $Id$
# Authority: dag
# Upstream: Zack Smith <fbui$comcast,net>

Summary: Artificial benchmark for measuring memory bandwidth
Name: bandwidth
Version: 0.30a
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://zsmith.co/bandwidth.html

Source: http://zsmith.co/archives/bandwidth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
bandwidth is an artificial benchmark for measuring memory bandwidth,
useful for identifying a computer's weak areas.

%prep
%setup

%build
%ifarch %{ix86}
%{__make} bandwidth32
%endif
%ifarch x86_64
%{__make} bandwidth64
%endif

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%ifarch %{ix86}
%{__install} -Dp -m0755 bandwidth32 %{buildroot}%{_bindir}/bandwidth
%endif
%ifarch x86_64
%{__install} -Dp -m0755 bandwidth64 %{buildroot}%{_bindir}/bandwidth
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING.txt README.txt
%{_bindir}/bandwidth

%changelog
* Thu Oct 25 2012 Dag Wieers <dag@wieers.com> - 0.30a-1
- Updated to release 0.30a.

* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 0.26c-1
- Updated to release 0.26c.

* Sat Nov 08 2008 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Sat Jul 28 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
