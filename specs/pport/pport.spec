# $Id$

# Authority: dries

Summary: Utility for accessing the output pins of a parallel port.
Name: pport
Version: 0.5h
Release: 1
License: GPL
Group: Applications/System
URL: http://freshmeat.net/projects/pport

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/pport/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
PPort is a simple yet handy program for accessing the output pins of a 
parallel port. Using this bundle, one can successfully control any 
household appliance or electronic device with minimal hassle and 
practically no changes.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man8
strip pport
cp pport $RPM_BUILD_ROOT/usr/sbin
cp man/pport.8.gz $RPM_BUILD_ROOT/usr/share/man/man8

%files
%defattr(-,root,root, 0755)
%doc AUTHORS ChangeLog COPYING FAQ INSTALL NEWS doc/README THANKS doc/FRANKY-HOWTO
/usr/sbin/pport
/usr/share/man/man8/pport.8.gz

%changelog
* Sun Feb 3 2004 Dries Verachtert <dries@ulyssis.org> 0.5h-1
- new version: 0.5h

* Sun Feb 1 2004 Dries Verachtert <dries@ulyssis.org> 0.5g-1
- first packaging for Fedora Core 1
