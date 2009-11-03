# $Id$
# Authority: matthias

Summary: Xorp is an Open Router Platform
Name: xorp
Version: 1.4
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.xorp.org/
Source: http://www.xorp.org/releases/%{version}/xorp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, openssl-devel, ncurses-devel, net-snmp-devel
BuildRequires: python

%description
XORP is an open router platform being developed at the ICSI Center for
Open Networking (ICON) at the International Computer Science Institute
in Berkeley, California, USA. XORP primary goal is to be both a research
tool and a stable deployment platform that can be used to close the gap
between network research and real world.


%prep
%setup


%build
%configure \
	--datadir="%{_datadir}/xorp"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	datadir="%{buildroot}%{_datadir}/xorp"


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc BUGS BUILD_NOTES ERRATA LICENSE README RELEASE_NOTES TODO VERSION
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/xorp/


%changelog
* Thu Mar 22 2007 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Updated to release 1.3.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net/> 1.1-1
- Update to 1.1.

* Fri Dec  3 2004 Matthias Saou <http://freshrpms.net/> 1.0-1
- Initial RPM release.

