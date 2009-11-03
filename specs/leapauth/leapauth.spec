# $Id$
# Authority: dag
# Upstream:

%define real_name ipaqleap

Summary: Utility for doing LEAP authentication on WLAN
Name: leapauth
Version: 0.0
Release: 0.20050322.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.noomore.org/leap/

Source: http://www.noomore.org/leap/ipaqleap.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
leapauth is a utility for doing LEAP authentication on WLAN.

%prep
%setup -n leap

%{__rm} -f leapauth *.o

%build
%{__make} %{?_smp_mflags} -C libmd-0.2 clean libmd.a \
	CC="%{__cc}" \
	AR="%{__ar}" \
	RANLIB="%{__ranlib}" \
	PATH="$PATH"

%{__make} %{?_smp_mflags} \
	CC="%{__cc}" \
	PATH="$PATH"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 leapauth %{buildroot}%{_sbindir}/leapauth
#%{__install} -Dp -m0755 libmd-0.2/libmd.so %{buildroot}%{_libdir}/libmd.so
#%{__install} -Dp -m0755 libmd-0.2/libmd.so.0 %{buildroot}%{_libdir}/libmd.so.0
#exit 1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_sbindir}/leapauth

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0-0.20050322.2
- Rebuild for Fedora Core 5.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 0.0-0.20050322
- Initial package. (using DAR)
