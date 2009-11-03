# $Id$
# Authority: dries
# Screenshot: http://gambas.sourceforge.net/2003-06-25.png
# ScreenshotURL: http://gambas.sourceforge.net/screenshots.html

# It compiles, but it does not work on my machine
# Tag: test


%define real_version 1.0

Summary: IDE based on a basic interpreter with object extensions
Name: gambas
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://gambas.sourceforge.net/

Source: http://gambas.sourceforge.net/gambas-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Patch0: dont-make-links.patch
Patch1: automake.patch
BuildRequires: kdelibs-devel, libjpeg-devel, automake, autoconf
BuildRequires: SDL-devel, mysql-devel
BuildRequires: postgresql-devel, zlib-devel
BuildRequires: glibc-headers, sqlite-devel, gcc-c++, automake15
BuildRequires: libtool

%description
Gambas is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic„¢ (but it is NOT a clone !).With
Gambas, you can quickly design your program GUI, access MySQL or PostgreSQL
databases, pilot KDE applications with DCOP, translate your program into
many languages, create network applications easily, and so on...

%prep
%setup -n gambas-%{real_version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize} --force --copy
%{__aclocal} --force
%{__automake} --add-missing
%{__autoconf}
%{__autoheader}
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
export PATH=%{buildroot}/usr/bin:$PATH
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export PATH=%{buildroot}%{_bindir}:$PATH
%makeinstall

%clean
%{__rm} -rf %{buildroot}

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
%doc AUTHORS COPYING INSTALL NEWS README README README.REDHAT TODO
%{_libdir}/gambas
# %{_libdir}/info
%{_bindir}/*
# strange..
# %{_includedir}/gambas.h
%exclude %{_libdir}/gambas/lib.*.la

%files help
%defattr(-, root, root, 0755)
%dir %{_datadir}/gambas/
%{_datadir}/gambas/help

%files examples
%defattr(-, root, root, 0755)
%dir %{_datadir}/gambas/
%{_datadir}/gambas/examples

%changelog
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> 1.0-0
- Updated to release 1.0.

* Tue Sep 14 2004 Dries Verachtert <dries@ulyssis.org> 0.99-0
- Update to version 0.99.

* Fri Jun 25 2004 Dries Verachtert <dries@ulyssis.org> 0.94-0
- Update to version 0.94.

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
