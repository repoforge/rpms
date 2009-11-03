# $Id$
# Authority: dag

Summary: Send a wake-on-lan (WOL) packet
Name: wakelan
Version: 1.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet

Source: ftp://sunsite.unc.edu/pub/Linux/system/network/misc/wakelan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: autoconf

%description
WakeLan sends a properly formatted UDP packet across the network which
will cause a wake-on-lan enabled computer to power on.

%prep
%setup

%build
#{__autoconf}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__make} install \
	bindir="%{buildroot}%{_bindir}" \
	mandir="%{buildroot}%{_mandir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man1/wakelan.1*
%{_bindir}/wakelan

%changelog
* Fri Feb 23 2007 Dag Wieers <dag@wieers.com> - 1.1-1
- Initial package. (using DAR)
