# $Id$
# Authority: dries
# Upstream: Nikolay Pultsin <geometer$mawhrin,net>

%define desktop_vendor rpmforge

Summary: E-book reader
Name: fbreader
Version: 0.8.11
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://only.mawhrin.net/fbreader/

Source: http://only.mawhrin.net/fbreader/fbreader-sources-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: enca-devel, qt-devel >= 3.2, kdelibs-devel, gcc-c++

%description
FBReader is an e-book reader for Linux PDAs and desktop computers.
FBReader supports several e-book formats: plucker, palmdoc, zTXT, 
HTML, fb2, and plain text.

%prep
%setup

%build
%{__make} %{?_smp_mflags}  MOC="moc" EXTERNALINCLUDE="-I${QTDIR}/include" UILIBS="-L${QTDIR}/lib -lqt-mt" TARGET_ARCH="desktop" UI_TYPE="qt" INSTALLDIR="%{_prefix}" LIBDIR="%{_libdir}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALLDIR="%{_prefix}" LIBDIR="%{_libdir}" EXTERNALINCLUDE="-I${QTDIR}/include" UILIBS="-L${QTDIR}/lib -lqt-mt" TARGET_ARCH="desktop" UI_TYPE="qt" MOC=moc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc fbreader/LICENSE
%{_bindir}/FBReader
%{_datadir}/FBReader/
%{_libdir}/libzlcore.so*
%{_libdir}/libzltext.so*
%dir %{_libdir}/zlibrary/
%dir %{_libdir}/zlibrary/ui/
%{_libdir}/zlibrary/ui/zlui-qt.so
%{_datadir}/applications/FBReader.desktop
%{_datadir}/pixmaps/FBReader.png
%{_datadir}/pixmaps/FBReader/
%{_datadir}/zlibrary/

%changelog
* Fri Jan 18 2008 Dries Verachtert <dries@ulyssis.org> - 0.8.11-1
- Updated to release 0.8.11.

* Tue Jan  1 2008 Dries Verachtert <dries@ulyssis.org> - 0.8.9-1
- Updated to release 0.8.9.

* Fri Nov 30 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.8-1
- Updated to release 0.8.8.

* Mon Oct 22 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.7-1
- Updated to release 0.8.7.

* Mon Aug 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.6-1
- Updated to release 0.8.6.

* Sun Jul 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.5-1
- Updated to release 0.8.5.

* Thu Jun 07 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.4-1
- Updated to release 0.8.4.

* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.3-1
- Updated to release 0.8.3.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.8.2-1
- Updated to release 0.8.2.

* Fri May 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.4-1
- Updated to release 0.7.4.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.3-1
- Updated to release 0.7.3.

* Fri Feb 17 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to release 0.7.2.

* Wed Dec 07 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1-0.b
- Initial package.
