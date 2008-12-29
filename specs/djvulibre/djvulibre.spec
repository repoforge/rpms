# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

#{?el5:#undefine _with_mozilla}
%{?el5:%define mozilla xulrunner-devel nspr-devel}

%{?el4:%define mozilla seamonkey-devel}
%{?el4:%define _without_modxorg 1}

%{?el3:%define mozilla seamonkey-devel}
%{?el3:%define _without_modxorg 1}

%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}

%{?el2:%define mozilla seamonkey-devel}
%{?el2:%define _without_modxorg 1}

Summary: DjVu viewers, encoders and utilities
Name: djvulibre
Version: 3.5.20
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://djvu.sourceforge.net/

Source: http://dl.sf.net/djvu/djvulibre-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: libjpeg-devel
BuildRequires: libstdc++-devel
BuildRequires: libtiff-devel
BuildRequires: qt-devel
%{!?_without_modxorg:BuildRequires: libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{?_with_mozilla:BuildRequires: %{mozilla}}
### Provide these here, they're so small, it's not worth splitting them out
Provides: djvulibre-libs = %{version}-%{release}
Obsoletes: djvulibre-libs <= %{version}-%{release}
Provides: djvulibre-mozplugin = %{version}-%{release}
Obsoletes: djvulibre-mozplugin <= %{version}-%{release}
Provides: mozilla-djvulibre = %{version}-%{release}
Obsoletes: mozilla-djvulibre <= %{version}-%{release}

%description
DjVu is a web-centric format and software platform for distributing documents
and images. DjVu content downloads faster, displays and renders faster, looks
nicer on a screen, and consume less client resources than competing formats.
DjVu was originally developed at AT&T Labs-Research by Leon Bottou, Yann
LeCun, Patrick Haffner, and many others. In March 2000, AT&T sold DjVu to
LizardTech Inc. who now distributes Windows/Mac plug-ins, and commercial
encoders (mostly on Windows)

In an effort to promote DjVu as a Web standard, the LizardTech management was
enlightened enough to release the reference implementation of DjVu under the
GNU GPL in October 2000. DjVuLibre (which means free DjVu), is an enhanced
version of that code maintained by the original inventors of DjVu. It is
compatible with version 3.5 of the LizardTech DjVu software suite.

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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__mkdir_p} %{buildroot}%{_libdir}/mozilla/plugins
%{__ln_s} ../../netscape/plugins/nsdejavu.so %{buildroot}%{_libdir}/mozilla/plugins/

# Fix for the libs to get stripped correctly (debuginfo)
find %{buildroot}%{_libdir} -name '*.so*' | xargs %{__chmod} +x

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig
%{_datadir}/djvu/djview3/desktop/register-djview-menu install || :
%{_datadir}/djvu/osi/desktop/register-djvu-mime install || :

%preun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    %{_datadir}/djvu/djview3/desktop/register-djview-menu uninstall || :
    %{_datadir}/djvu/osi/desktop/register-djvu-mime uninstall || :
fi

%files
%defattr(-, root, root, 0755)
%doc COPYING COPYRIGHT NEWS README TODO doc/
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/ja/man1/*.1*
%{_bindir}/*
%{_datadir}/djvu/
%{_includedir}/libdjvu/
%{_libdir}/libdjvulibre.so.*
%{_libdir}/*/plugins/*.so

%files devel
%defattr(-, root, root, 0755)
%doc doc/
%{_libdir}/libdjvulibre.so
%{_libdir}/pkgconfig/ddjvuapi.pc
%exclude %{_libdir}/libdjvulibre.la

%changelog
* Tue Dec 09 2008 Dag Wieers <dag@wieers.com> - 3.5.20-1
- Updated to release 3.5.20.

* Fri Nov 24 2006 Dries Verachtert <dries@ulyssis.org> - 3.5.17-1
- Updated to release 3.5.17.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 3.5.14-2
- Re-enable the lib/mozilla/ symlink to the plugin.
- Add source of /etc/profile.d/qt.sh to fix weird detection problem on FC3...
  ...doesn't fix it, some lib required by qt is probably installed after and
  ldconfig not run.
- Added lib +x chmod'ing to get proper stripping and debuginfo package.

* Sat Oct 16 2004 Matthias Saou <http://freshrpms.net/> 3.5.14-2
- Added update-desktop-database scriplet calls.

* Mon Aug 16 2004 Matthias Saou <http://freshrpms.net/> 3.5.14-1
- Update to 3.5.14.
- Added newly introduced files to the package.

* Mon May 17 2004 Matthias Saou <http://freshrpms.net/> 3.5.13-1
- Update to 3.5.13.
- Added new Japanese man pages.

* Wed May  5 2004 Matthias Saou <http://freshrpms.net/> 3.5.12-4
- Changed the plugin directory for mozilla to %{_libdir}/mozilla,
  as suggested by Matteo Corti.
- Shortened the description.

* Wed Jan 14 2004 Matthias Saou <http://freshrpms.net/> 3.5.12-3
- Added XFree86-devel and libjpeg-devel build requirements.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 3.5.12-2
- Rebuild for Fedora Core 1.

* Mon Sep  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.5.12.

* Thu May  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.5.11.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.5.10.

* Wed Jul 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 3.5.7.

* Fri Jul 19 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and fixes.

* Wed May 29 2002 Leon Bottou <leon@bottou.org>
- bumped to version 3.5.6-1

* Mon Apr 1 2002 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.5-2
- changed group to Applications/Publishing

* Tue Mar 25 2002 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.5-2

* Tue Jan 22 2002 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.4-1.
- fixed for properly locating the man directory.
- bumped to version 3.5.4-2.

* Wed Jan 16 2002 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.3-1

* Fri Dec  7 2001 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.2-1.

* Wed Dec  5 2001 Leon Bottou <leonb@users.sourceforge.net>
- created spec file for rh7.x.

