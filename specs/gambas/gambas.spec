# $Id$

# Authority: dries

Summary: Free development environment based on a basic interpreter with object extensions.
Name: gambas
Version: 0.90
Release: 1
License: GPL
Group: Development/Tools
URL: http://gambas.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://gambas.sourceforge.net/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Patch0: makefiles-destdir.patch.bz2
Patch0: dont-make-links.patch.bz2
BuildRequires: automake, autoconf, gcc, make, qt-devel, mysql-devel, postgresql-devel
Requires: qt

#(d) primscreenshot: http://gambas.sourceforge.net/2003-06-25.png
#(d) screenshotsurl: http://gambas.sourceforge.net/screenshots.html

%description
Gambas is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic„¢ (but it is NOT a clone !).With
Gambas, you can quickly design your program GUI, access MySQL or PostgreSQL
databases, pilot KDE applications with DCOP, translate your program into
many languages, create network applications easily, and so on...


%description -l nl
Gambas is een vrije ontwikkelomgeving gebaseerd op een basic interpreter met
object extensies, zoals Visual Basic (maar het is geen kloon!). Met Gambas
kan u eenvoudig een GUI ontwerpen, MySQL of PostgreSQL databases gebruiken,
KDE programma's aansturen met DCOP, uw programma vertalen naar vele talen,
eenvoudig netwerktoepassingen maken, enzoverder...

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup
%patch -p1

%build
rm -f  $(find . -type f | egrep "Makefile$") $(find . -type f | egrep "Makefile.in$")
./reconf || echo reconf gives a warning but lets continue anyway
(cd libltdl/;../reconf || echo reconf gives a warning but lets continue anyway)
%configure --datadir=/usr/share/gambas
%{__make} %{?_smp_mflags}

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export PATH=$RPM_BUILD_ROOT/usr/bin:$PATH
%{__make} bindir=$RPM_BUILD_ROOT/usr/bin includedir=$RPM_BUILD_ROOT/usr/include libdir=$RPM_BUILD_ROOT/usr/lib datadir=$RPM_BUILD_ROOT/usr/share/gambas install-strip

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%package help
Summary: The help files for gambas.
Group: Development/Libraries
Requires: %{name} = %{version}

%description help
The gambas-help package contains all the help files for gambas.

%package examples
Summary: The examples for gambas.
Group: Development/Libraries
Requires: %{name} = %{version}

%description examples
The gambas-examples package contains some examples for gambas.

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING INSTALL NEWS README README.REDHAT TODO
%{_libdir}/lib.gb*.so.0.0.0
%{_libdir}/lib.gb*.so.0
%{_libdir}/lib.gb*.component
%{_libdir}/info
%{_bindir}/gambas
%{_bindir}/gbc
%{_bindir}/gba
%{_bindir}/gbi
%{_bindir}/gbx
%{_bindir}/gambas-database-manager
%{_bindir}/Util
%{_includedir}/gambas.h
%{_libdir}/lib.gb*.la
%{_libdir}/lib.gb*.so

%files help
%defattr(-,root,root,0755)
/usr/share/gambas/help

%files examples
%defattr(-,root,root,0755)
/usr/share/gambas/examples

%changelog
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
