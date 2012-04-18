# $Id$
# Authority: dag

### EL5 ships with scribus-1.3.3.2-3.el5
%{?el5:# Tag: rfx}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Graphical desktop publishing (DTP) application
Name: scribus
Version: 1.4.0
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://web2.altmuehlnet.de/fschmid/

Source: http://dl.sf.net/scribus/scribus-%{version}.tar.bz2
# http://bugs.scribus.net/view.php?id=10485
Patch0: scribus-1.4.0-swatches.patch
# http://bugs.scribus.net/view.php?id=10486
Patch1: scribus-1.4.0-profiles.patch
# use versioned documentation directory
Patch2: scribus-1.4.0-docdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: aspell-devel
BuildRequires: boost-devel
BuildRequires: cairo-devel
BuildRequires: cmake
BuildRequires: cups-devel
BuildRequires: freetype-devel
BuildRequires: gnutls-devel
BuildRequires: hyphen-devel
BuildRequires: lcms-devel >= 1.12
BuildRequires: libart_lgpl-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: openssl-devel
BuildRequires: podofo-devel
BuildRequires: python >= 2.3
BuildRequires: python-devel >= 2.3
BuildRequires: qt4-devel
BuildRequires: zlib-devel
%{?!_without_freedesktop:BuildRequires: desktop-file-utils}
Requires: ghostscript
Requires: python
Requires: python-imaging
Requires: shared-mime-info
Requires: tkinter

%filter_provides_in %{_libdir}/scribus/plugins
%filter_setup

%description
Scribus is an desktop open source page layout program with
the aim of producing commercial grade output in PDF and
Postscript, primarily, though not exclusively for Linux.

While the goals of the program are for ease of use and simple easy to
understand tools, Scribus offers support for professional publishing
features, such as CMYK color, easy PDF creation, Encapsulated Postscript
import/export and creation of color separations.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p2 -b .swatches
%patch1 -p2 -b .profiles
%patch2 -p1 -b .docdir

%build
%cmake -DWANT_DISTROBUILD=YES .
%{__make} %{?_smp_mflags} VERBOSE=1

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 %{buildroot}%{_datadir}/scribus/icons/scribus.png %{buildroot}%{_datadir}/pixmaps/scribus.png
%{__install} -Dp -m0644 %{buildroot}%{_datadir}/scribus/icons/scribusdoc.png %{buildroot}%{_datadir}/pixmaps/x-scribus.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
    --add-category X-Red-Hat-Base              \
    --dir %{buildroot}%{_datadir}/applications \
    scribus.desktop

### Clean up buildroot
%{__rm} -f %{buildroot}%{_datadir}/mimelnk/application/*scribus.desktop

%post
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database &> /dev/null || :


%postun
update-mime-database %{_datadir}/mime > /dev/null 2>&1 || :
update-desktop-database &> /dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README TODO
%doc %{_mandir}/man1/scribus.1*
%doc %{_mandir}/*/man1/scribus.1*
%{_bindir}/scribus
%{_datadir}/applications/%{desktop_vendor}-scribus.desktop
%{_datadir}/mime/packages/scribus.xml
%{_datadir}/pixmaps/scribus.png
%{_datadir}/pixmaps/x-scribus.png
%{_datadir}/scribus/
%{_includedir}/scribus/
%{_libdir}/scribus/
%exclude %{_datadir}/scribus/samples/*.py[co]
%exclude %{_datadir}/scribus/scripts/*.py[co]

%changelog
* Sun Feb 12 2012 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Updated to release 1.4.0.

* Wed Jan 09 2008 Dag Wieers <dag@wieers.com> - 1.3.3.10-1
- Updated to release 1.3.3.10.

* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 1.3.3.9-1
- Updated to release 1.3.3.9.

* Fri Mar 02 2007 Dries Verachtert <dries@ulyssis.org> - 1.3.3.8-1
- Updated to release 1.3.3.8.

* Sat Jan 13 2007 Dries Verachtert <dries@ulyssis.org> - 1.3.3.7-1
- Updated to release 1.3.3.7.

* Sun Jan 07 2007 Dries Verachtert <dries@ulyssis.org> - 1.3.3.6-2
- Also build th python scripts on amd64, thanks to Rohan Walsh.

* Tue Dec 05 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.3.6-1
- Updated to release 1.3.3.6.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.3.5-1
- Updated to release 1.3.3.5.

* Mon Aug 09 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.3.3-1
- Updated to release 1.3.3.3.

* Sun Jan 29 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Updated to release 1.3.2.

* Wed Dec 28 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.1-2
- Fixes in the buildrequirements, thanks to Peter Linell.

* Wed Oct 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Updated to release 1.3.1.

* Wed Sep 14 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.3-1
- Updated to release 1.2.3.

* Wed Jul 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2.1-1
- Updated to release 1.2.2.1.

* Mon Jul 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2-1
- Updated to release 1.2.2.

* Sun Jan 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.1-1
- Updated to release 1.2.1.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Tue Aug 12 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
