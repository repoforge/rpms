# $Id: $

# Authority: dries

Summary: DHCP daemon ping program
Name: dhcping
Version: 1.2
Release: 1
License: BSD
Group: Applications/Internet
URL: http://www.mavetju.org/unix/general.php

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.mavetju.org/download/dhcping-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}

%description
Dhcping allows the system administrator to check if a remote DHCP 
server is still functioning.

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
%defattr(-, root, root, 0755)
%doc CHANGES CONTACT LICENSE
%{_bindir}/dhcping
%{_datadir}/man/man8/dhcping.8.gz

%changelog
* Sun Mar 21 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- Initial package
