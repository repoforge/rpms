# $Id$
# Authority: dag
# Upstream: <gnupg-devel$gnupg,org>

### RHEL 5.4 ships with 0.7.3-3.el5
# ExclusiveDist el3 el4

%{?dtag: %{expand: %%define %dtag 1}}

%{?el3:%define _without_gtk24 1}
%{?el3:%define _without_qt33 1}
%{?rh9:%define _without_gtk24 1}
%{?rh9:%define _without_qt33 1}
%{?rh7:%define _without_gtk24 1}
%{?rh7:%define _without_qt33 1}
%{?el2:%define _without_gtk24 1}
%{?el2:%define _without_qt33 1}

Summary: PIN or passphrase entry dialog
Name: pinentry
Version: 0.7.2
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.gnupg.org/aegypten/

Source: http://ftp.gnupg.org/gcrypt/pinentry/pinentry-%{version}.tar.gz
Patch: pinentry-0.7.2-info.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel >= 1.2, gtk+-devel >= 1.2
%{!?_without_gtk24:BuildRequires: gtk2-devel >= 2.4}
%{!?_without_qt33:BuildRequires: qt-devel >= 3.3}
BuildRequires: ncurses-devel
Requires: chkconfig, info

Provides: pinentry-curses = %{version}-%{release}
Obsoletes: pinentry-curses <= %{version}-%{release}
Provides: pinentry-gtk = %{version}-%{release}
Obsoletes: pinentry-gtk <= %{version}-%{release}
Provides: pinentry-gui = %{version}-%{release}
Obsoletes: pinentry-gui <= %{version}-%{release}
%{!?_without_qt33:Provides: pinentry-qt = %{version}-%{release}}
%{!?_without_qt33:Obsoletes: pinentry-qt <= %{version}-%{release}}

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the aegypten project; see
http://www.gnupg.org/aegypten/ for details.

%prep
%setup
%patch0 -p1

%build
source "/etc/profile.d/qt.sh"
%configure \
%{?_without_gtk24:--disable-pinentry-gtk2} \
%{?_without_qt33:--disable-pinentry-qt}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source "/etc/profile.d/qt.sh"
%{__make} install DESTDIR="%{buildroot}"

touch %{buildroot}%{_bindir}/pinentry

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir

%post
install-info %{_infodir}/pinentry.info.gz %{_infodir}/dir
update-alternatives --install %{_bindir}/pinentry pinentry %{_bindir}/pinentry-curses 10
update-alternatives --install %{_bindir}/pinentry pinentry %{_bindir}/pinentry-gtk 40
%{!?_without_gtk24:update-alternatives --install %{_bindir}/pinentry pinentry %{_bindir}/pinentry-gtk-2 50}
%{!?_without_qt33:update-alternatives --install %{_bindir}/pinentry pinentry %{_bindir}/pinentry-qt 30}

%postun
if [ $1 -eq 0 ]; then
	install-info --delete %{_infodir}/pinentry.info.gz %{_infodir}/dir
	update-alternatives --remove pinentry %{_bindir}/pinentry-curses
	update-alternatives --remove pinentry %{_bindir}/pinentry-gtk
%{!?_without_gtk24:update-alternatives --remove pinentry %{_bindir}/pinentry-gtk-2}
%{!?_without_qt33:update-alternatives --remove pinentry %{_bindir}/pinentry-qt}
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%doc %{_infodir}/*.info*
%{_bindir}/pinentry-curses
%{_bindir}/pinentry-gtk
%{!?_without_gtk24:%{_bindir}/pinentry-gtk-2}
%{!?_without_qt33:%{_bindir}/pinentry-qt}
%ghost %{_bindir}/pinentry

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.6.8-1
- Initial package. (using DAR)
