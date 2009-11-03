# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag@wieers.com>

%{?dist: %{expand: %%define %dist 1}}

Summary: Giving presentations (or control applications) with your Wiimote
Name: wiipresent
Version: 0.7.5.2
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://dag.wieers.com/home-made/wiipresent/

Source: http://dag.wieers.com/home-made/wiipresent/wiipresent-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bluez-libs-devel
BuildRequires: libwiimote-devel
BuildRequires: libX11-devel
BuildRequires: xorg-x11-proto-devel

%description
wiipresent is a program to control applications using your wiimote. It was
originally developed for giving presentations with your wiimote, but can also
be used to control your mouse-pointer and control various applications.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" lib="%{_lib}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post
/usr/bin/update-desktop-database -q || :

%postun
/usr/bin/update-desktop-database -q || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO docs/*.html docs/*.txt
%doc %{_mandir}/man1/wiipresent.1*
#config %{_sysconfdir}/X11/xinit/xinitrc.d/wiipresent.sh
%{_bindir}/wiipresent
%{_datadir}/applications/wiipresent.desktop
%{_datadir}/pixmaps/wiipresent.svg

%changelog
* Sat Aug 22 2009 Dag Wieers <dag@wieers.com> - 0.7.5.2-1
- Updated to release 0.7.5.2.

* Thu Aug 20 2009 Dag Wieers <dag@wieers.com> - 0.7.5.1-1
- Updated to release 0.7.5.1.

* Thu Aug 20 2009 Dag Wieers <dag@wieers.com> - 0.7.5-1
- Updated to release 0.7.5.

* Fri Apr 17 2009 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Mon Mar 16 2009 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Thu Mar 05 2009 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Mon Mar 02 2009 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Tue Feb 10 2009 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Mon Feb 09 2009 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
