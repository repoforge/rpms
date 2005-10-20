# $Id$
# Authority: dag

### Ships with Fedora Core / Red Hat Enterprise
# Tag: test

Summary: X client for remote desktop into Windows Terminal Server
Name: rdesktop
Version: 1.4.1
Release: 0
License: GPL
Group: User Interface/Desktops
URL: http://www.rdesktop.org/

Source: http://dl.sf.net/rdesktop/rdesktop-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, XFree86-devel

%description
rdesktop is an open source client for Windows NT Terminal Server and
Windows 2000 & 2003 Terminal Services, capable of natively speaking 
Remote Desktop Protocol (RDP) in order to present the user's NT
desktop. Unlike Citrix ICA, no server extensions are required.

%prep
%setup

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
* Fri May 27 2005 Dag Wieers <dag@wieers.com> - 1.4.1-0
- Initial package. (using DAR)
