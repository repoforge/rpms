# $Id$
# Authority: dag

Summary: tool for figuring out network masks
Name: netmask
Version: 2.3.6
Release: 0
License: GPL
Group: Applications/Internet
URL: http://packages.qa.debian.org/n/netmask.html

Source: http://http.us.debian.org/debian/pool/main/n/netmask/netmask_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This is a tiny program handy if you work with firewalls or routers
or are a network admin of sorts.  It can determine the smallest set of
network masks to specify a range of hosts.  It can also convert between
common IP netmask and address formats.

%prep
%setup

%build
### FIXME: Doesn't build for RH80 or RH90 ;(
%{__aclocal}
%{__automake} --add-missing
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 netmask %{buildroot}%{_bindir}/netmask
%{__install} -Dp -m0644 netmask.1 %{buildroot}%{_mandir}/man1/netmask.1

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man?/*
%doc %{_infodir}/*.info*
%{_bindir}/*

%changelog
* Sun Jul 13 2003 Dag Wieers <dag@wieers.com> - 2.3.5-0
- Initial package. (using DAR)
