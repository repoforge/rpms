# $Id$
# Authority: dries

# Screenshot: http://gambas.sourceforge.net/2003-06-25.png
# ScreenshotURL: http://gambas.sourceforge.net/screenshots.html

%define real_version 0.93b

Summary: Free development environment based on a basic interpreter with object extensions
Name: gambas
Version: 0.93
Release: 0.b
License: GPL
Group: Development/Tools
URL: http://gambas.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://gambas.sourceforge.net/gambas-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Patch0: makefiles-destdir.patch.bz2
Patch0: dont-make-links.patch
BuildRequires: kdelibs-devel, libjpeg-devel, automake, autoconf, gcc, make, qt-devel, SDL-devel, mysql-devel, postgresql-devel, XFree86-devel, zlib-devel, glibc-headers, sqlite-devel, gcc-c++
#Requires: qt, zlib, XFree86, sqlite, SDL, libjpeg

%description
Gambas is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic„¢ (but it is NOT a clone !).With
Gambas, you can quickly design your program GUI, access MySQL or PostgreSQL
databases, pilot KDE applications with DCOP, translate your program into
many languages, create network applications easily, and so on...

%prep
%setup -n gambas-%{real_version}
%patch -p1

%build
rm -f  $(find . -type f | egrep "Makefile$") $(find . -type f | egrep "Makefile.in$")
./reconf || echo reconf gives a warning but lets continue anyway
# (cd libltdl/;../reconf || echo reconf gives a warning but lets continue anyway)
%configure \
	--datadir="%{_datadir}/gambas" \
	--enable-intl \
	--enable-conv \
	--enable-qt \
	--enable-kde \
	--enable-net \
	--enable-curl \
	--enable-postgresql \
	--enable-mysql \
	--enable-sqlite \
	--enable-sdl \
	--enable-vb
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf "${RPM_BUILD_ROOT}"
export PATH=%{buildroot}/usr/bin:$PATH
#  {__make} bindir=$RPM_BUILD_ROOT/usr/bin includedir=$RPM_BUILD_ROOT/usr/include libdir=$RPM_BUILD_ROOT/usr/lib datadir=$RPM_BUILD_ROOT/usr/share/gambas install-strip
%makeinstall
#  \
#	datadir="%{buildroot}/usr/share/gambas"

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%package help
Summary: The help files for gambas
Group: Development/Libraries
Requires: %{name} = %{version}

%description help
The gambas-help package contains all the help files for gambas.

%package examples
Summary: The examples for gambas
Group: Development/Libraries
Requires: %{name} = %{version}

%description examples
The gambas-examples package contains some examples for gambas.

%files
%defattr(-, root, root, 0755)
%doc README AUTHORS COPYING INSTALL NEWS README README.REDHAT TODO
%{_libdir}/gambas/*.so.*
%{_libdir}/gambas/lib.gb*.component
# %{_libdir}/info
%{_bindir}/gambas
%{_bindir}/gbc
%{_bindir}/gba
%{_bindir}/gbi
%{_bindir}/gbx
%{_bindir}/gambas-database-manager
%{_bindir}/Util
%{_includedir}/gambas.h
%exclude %{_libdir}/gambas/lib.*.la
%{_libdir}/gambas/lib.*.so

%files help
%defattr(-,root,root,0755)
%dir %{_datadir}/gambas/
%{_datadir}/gambas/help

%files examples
%defattr(-,root,root,0755)
%dir %{_datadir}/gambas/
%{_datadir}/gambas/examples

%changelog
* Fri Jun 4 2004 Dries Verachtert <dries@ulyssis.org> 0.93-0.b
- update to 0.93a

* Sun Apr 18 2004 Dries Verachtert <dries@ulyssis.org> 0.92a-1
- update to version 0.92a

* Mon Mar 22 2004 Dries Verachtert <dries@ulyssis.org> 0.91-1
- update to version 0.91

* Thu Feb 26 2004 Dries Verachtert <dries@ulyssis.org> 0.90-1
- update to version 0.90

* Tue Feb 25 2004 Dries Verachtert <dries@ulyssis.org> 0.84a-1
- update to version 0.84a
- subpackages: help and examples

* Tue Jan 27 2004 Dries Verachtert <dries@ulyssis.org> 0.82-1
- update to version 0.82

* Sun Dec 21 2003 Dries Verachtert <dries@ulyssis.org> 0.74-1
- first fully packaged version with buildroot (patched most of the
  Makefile.am files)
- new version 0.74

* Sun Dec 7 2003 Dries Verachtert <dries@ulyssis.org> 0.73-1
- first packaging for Fedora Core 1
