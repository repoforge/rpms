# $Id$
# Authority: fabian
# Upstream: 

Summary: Remote control through bluetooth or IR connection
Name: anyremote
Version: 4.18.1
Release: 1
License: GPLv2+
Group: Applications/System
Source0: http://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
URL: http://anyremote.sourceforge.net/
Requires: bc
Requires: anyremote-data >= 4.18.1
BuildRequires: bluez-libs-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: xorg-x11-proto-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The overall goal of this project is to provide remote control service on Linux 
through Bluetooth, InfraRed, Wi-Fi or TCP/IP connection.
anyRemote supports wide range of modern cell phones like Nokia, SonyEricsson, 
Motorola and others. 

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="%{buildroot}"


%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%package data
Summary: Configuration files for anyRemote
Group: Applications/System

%description data
Configuration files for anyRemote

%files data
%defattr(-,root,root,-)
%{_datadir}/%{name}

%package doc
Summary: Documentation for anyRemote
Group: Applications/System

%description doc
Documentation for anyRemote

%files doc
%defattr(-,root,root,-)
%doc %{_defaultdocdir}/%{name}


%changelog
* Sun Jun 21 2009 Fabian Arrotin <fabian.arrotin@arrfab.net> - 4.18.1-1
- Updated to 4.18.1 + package inclusion in RPMforge

* Mon Oct 20 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.11-1
- Fixed issues with non-correct handling of files and directories names with 
  braces and brackets in some configuration files. 
  Several small changes in code.

* Mon Oct 6 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.10-1
- Fixed issue with non-correct handling of files and directories names with 
  braces and brackets in some configuration files. A lot of changes in 
  documentation. Several small changes in code.

* Mon Sep 29 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.9-1
- Get(version) command was introduced. Added possibility to create 
  user-specific phone initialization.

* Tue Sep 9 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.8.1-1
- Small corrections.

* Thu Sep 4 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.8-1
- Added configuration file for gThumb.
  Added GuiDescription field to configuration files.

* Thu Aug 7 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.7.1-1
- Fix crash issue if no bluetooth service runned

* Tue Aug 5 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.7-1
- Small enhancements

* Fri May 30 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.6-1
- Small enhancements

* Sun May 18 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.5-1
- Better integration with anyremote2http: -http command line 
  parameter was added.

* Tue Mar 07 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.4-1.fc8
- Spec file correction. Some minor enhancemens.

* Tue Mar 02 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.3-4.fc8
- Spec file correction. Move J2ME stuff out of the package.

* Tue Feb 26 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.3-3.fc8
- Spec file correction

* Sun Feb 17 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.3-2.fc8
- Spec file correction

* Mon Feb 15 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.3-1.fc8
- Bugfixes and small enhancements.Support for touchscreen devices was improved

* Fri Jan 10 2008 Mikhail Fedotov <anyremote at mail.ru> - 4.2-1.fc8
- Spec file modified.
