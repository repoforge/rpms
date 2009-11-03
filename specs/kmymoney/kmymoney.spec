# $Id$
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh8:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}
%{?rh6:%define _without_selinux 1}
%{?yd3:%define _without_selinux 1}

%define real_name kmymoney2

Summary: Double-entry accounting software package
Name: kmymoney
Version: 0.8.8
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://kmymoney2.sourceforge.net/

Source: http://dl.sf.net/kmymoney2/kmymoney2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, kdelibs-devel
%{!?_without_selinux:BuildRequires: libselinux-devel}

%description
KMyMoney is striving to be a full-featured replacement for your
Windows-based finance software. We are a full double-entry accounting
software package, for personal or small-business use.

%prep
%setup -n %{real_name}-%{version}

%build
source %{_sysconfdir}/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source %{_sysconfdir}/profile.d/qt.sh
%makeinstall
%find_lang %{real_name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog ChangeLog.original COPYING INSTALL README TODO
%doc %{_datadir}/doc/HTML/en/kmymoney2
%doc %{_mandir}/man?/*
%{_datadir}/apps/kmymoney2
%{_datadir}/applications/kde/kmymoney2.desktop
%{_datadir}/icons/*/*/apps/kmymoney2.png
%{_datadir}/icons/*/*/mimetypes/kmy.png
%{_datadir}/mimelnk/application/x-kmymoney2.desktop
%{_bindir}/*
%{_includedir}/kmymoney/
%{_libdir}/libkmm*
%{_datadir}/servicetypes/kmymoney*.desktop

%changelog
* Wed Dec 19 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.8-1
- Updated to release 0.8.8.

* Mon Mar 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.6-1
- Updated to release 0.8.6.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.5-1
- Updated to release 0.8.5.

* Tue May 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.4-1
- Updated to release 0.8.4.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.3-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Wed Jan 01 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.3-1
- Updated to release 0.8.3.

* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.2-1
- Updated to release 0.8.2.

* Sun Nov 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Updated to release 0.8.1.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Sun Jun 20 2004 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Initial package.
