# $Id$
# Authority: dag
# Upstream: Jochen Baier <email$jochen-baier,de>

Summary: Dock any application into the system tray
Name: alltray
Version: 0.40
Release: 1
License: GPL
Group: System Environment/Desktops
URL: http://alltray.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/alltray/alltray-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.4

%description
alltray allows you to dock any application into the system tray/notification
area. A high-light feature is that a click on the "close" button will
minimize to system tray.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' configure Makefile.in */Makefile.in

%build
%configure
%{__make}  %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/alltray

%changelog
* Fri Feb 25 2005 Dag Wieers <dag@wieers.com> - 0.40-1
- Updated to release 0.40.

* Tue Feb 15 2005 Dag Wieers <dag@wieers.com> - 0.35-1
- Updated to release 0.35.

* Fri Dec 17 2004 Che
- initial rpm release
