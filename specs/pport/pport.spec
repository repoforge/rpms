# $Id$
# Authority: dries
# Upstream: <pport-developement@lists.sf.net>

%define real_version 0.5h

Summary: Utility for accessing the output pins of a parallel port
Name: pport
Version: 0.6
Release: 1
License: GPL
Group: Applications/System
URL: http://sf.net/projects/pport/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/pport/pport-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel

%description
PPort is a simple yet handy program for accessing the output pins of a 
parallel port. Using this bundle, one can successfully control any 
household appliance or electronic device with minimal hassle and 
practically no changes.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 pport %{buildroot}%{_sbindir}/pport
%{__install} -D -m0644 man/pport.8.gz %{buildroot}%{_mandir}/man8/pport.8.gz

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS doc/README THANKS doc/FRANKY-HOWTO
%doc %{_mandir}/man8/pport.8.gz
%{_sbindir}/pport

%changelog
* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.
- Cosmetic changes.

* Sun Feb 1 2004 Dries Verachtert <dries@ulyssis.org> 0.5g-1
- first packaging for Fedora Core 1
