# $Id$
# Authority: dag
# Upstream: Peter Eriksson

Summary: Peter's disk-to-disk copying tool
Name: pcopy
Version: 1.5
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.lysator.liu.se/~pen/pcopy/

Source: ftp://ftp.lysator.liu.se/pub/unix/pcopy/pcopy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Pcopy is a small program for doing disk-to-disk copies as fast as possible,
that can handle bad sectors in a graceful way, and that also displays
a progress counter while doing the copying.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 pcopy %{buildroot}%{_bindir}/pcopy

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README
%{_bindir}/pcopy

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Initial package. (using DAR)
