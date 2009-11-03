# $Id$
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%define desktop_vendor rpmforge

Summary: CHM file viewer
Name: kchmviewer
Version: 4.0
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://kchmviewer.sourceforge.net/

Source: http://dl.sf.net/kchmviewer/kchmviewer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, cmake
BuildRequires: qt-devel >= 3.2, chmlib-devel
BuildRequires: kdelibs-devel, desktop-file-utils
%{?el4:BuildRequires: libselinux-devel}
%{?fc4:BuildRequires: libselinux-devel}
%{?fc3:BuildRequires: libselinux-devel}
%{?fc2:BuildRequires: libselinux-devel}

%description
Kchmviewer is a CHM file viewer for KDE.

%prep
%setup

%build
%{__mkdir} build
cd build
cmake -DLIBINSTALL_DIR=%{_libdir} -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
cd build
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING
%{_bindir}/kchmviewer
%{_datadir}/applications/kde4/kchmviewer.desktop
%{_libdir}/kde4/kio_msits*
%{_datadir}/kde4/services/msits.protocol
%{_datadir}/icons/crystalsvg/*/apps/kchmviewer.png

%changelog
* Tue Dec  2 2008 Dries Verachtert <dries@ulyssis.org> - 4.0-1
- Updated to release 4.0.

* Sun Jun 17 2007 Dries Verachtert <dries@ulyssis.org> - 3.1-1
- Updated to release 3.1.

* Mon Mar 19 2007 Dries Verachtert <dries@ulyssis.org> - 3.0-1
- Updated to release 3.0.

* Fri Dec 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.7-1
- Updated to release 2.7.

* Mon Aug 09 2006 Dries Verachtert <dries@ulyssis.org> - 2.6-1
- Updated to release 2.6.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 2.5-1
- Updated to release 2.5.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 2.0-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org>  2.0-1
- Updated to release 2.0.

* Mon Nov 28 2005 Dries Verachtert <dries@ulyssis.org>  1.3-1
- Upgrade to release 1.3.

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org>  1.2-1
- Upgrade to release 1.2.

* Wed Nov 02 2005 Dries Verachtert <dries@ulyssis.org>  1.1-1
- Upgrade to release 1.1.

* Thu Jul 28 2005 Dries Verachtert <dries@ulyssis.org>  1.0-1
- Upgrade to release 1.0.

* Tue Jul 26 2005 Dries Verachtert <dries@ulyssis.org> 0.9.1-1
- First packaging.
