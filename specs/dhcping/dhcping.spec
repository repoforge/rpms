# $Id: $
# Authority: dries
# Upstream: Edwin Groothuis <edwin$mavetju,org>

Summary: DHCP daemon ping program
Name: dhcping
Version: 1.2
Release: 2
License: BSD
Group: Applications/Internet
URL: http://sf.net/projects/mavetju/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/mavetju/dhcping-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Dhcping allows the system administrator to check if a remote DHCP 
server is still functioning.

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CONTACT LICENSE
%doc %{_mandir}/man?/*
%{_bindir}/dhcping

%changelog
* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 1.2-2
- Cosmetic changes.
- Fix program-prefix for RH73 and older.

* Sun Mar 21 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- Initial package
