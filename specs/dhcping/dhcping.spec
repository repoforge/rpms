# $Id$
# Authority: dries
# Upstream: Edwin Groothuis <edwin$mavetju,org>

Summary: DHCP daemon ping program
Name: dhcping
Version: 1.2
Release: 2.2%{?dist}
License: BSD
Group: Applications/Internet
URL: http://sourceforge.net/projects/mavetju/

#Source: http://dl.sf.net/mavetju/dhcping-%{version}.tar.gz
Source: http://www.mavetju.org/download/dhcping-%{version}.tar.gz
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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-2.2
- Rebuild for Fedora Core 5.

* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 1.2-2
- Cosmetic changes.
- Fix program-prefix for RH73 and older.

* Sun Mar 21 2004 Dries Verachtert <dries@ulyssis.org> 1.2-1
- Initial package
