# $Id$
# Authority: dag

# Rationale: We replace the RHEL version as it fixes a transparancy bug with compiz
### EL6 ships with rdesktop-1.6.0-8.el6
### EL5 ships with rdesktop-1.6.0-3
### EL4 ships with rdesktop-1.3.1-10
### EL3 ships with rdesktop-1.2.0-3
# Tag: rfx

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: X client for remote desktop into Windows Terminal Server
Name: rdesktop
Version: 1.7.0
Release: 0.1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://www.rdesktop.org/

Source: http://dl.sf.net/rdesktop/rdesktop-%{version}.tar.gz
Patch1: rdesktop-1.6.0-gcc296.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libsamplerate-devel
BuildRequires: openssl-devel
%{!?_without_modxorg:BuildRequires: libXt-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
rdesktop is an open source client for Windows NT Terminal Server and
Windows 2000 & 2003 Terminal Services, capable of natively speaking
Remote Desktop Protocol (RDP) in order to present the user's NT
desktop. Unlike Citrix ICA, no server extensions are required.

%prep
%setup
%patch1 -p1 -b .gcc296

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING doc/*.txt doc/AUTHORS doc/ChangeLog doc/HACKING doc/TODO README
%doc %{_mandir}/man1/rdesktop.1*
%{_bindir}/rdesktop
%{_datadir}/rdesktop/

%changelog
* Wed Apr 20 2011 Dag Wieers <dag@wieers.com> - 1.7.0-0.1
- Updated to release 1.7.0.

* Thu Sep  4 2008 Tom G. Christensen <swpkg@statsbiblioteket.dk> - 1.6.0-0.1
- Fix build on el2.
- Updated to release 1.6.0.

* Sat Sep 30 2006 Dag Wieers <dag@wieers.com> - 1.5.0-0
- Updated to release 1.5.0.

* Fri May 27 2005 Dag Wieers <dag@wieers.com> - 1.4.1-0
- Initial package. (using DAR)
