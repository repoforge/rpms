# $Id$
# Authority: dag

%{?dtag:%{expand: %%define %dtag 1}}

%{?el3:%define _without_freeglut 1}
%{?rh9:%define _without_freeglut 1}
%{?rh7:%define _without_freeglut 1}
%{?el2:%define _without_freeglut 1}

Summary: The 3D Studio File Format Library
Name: lib3ds
Version: 1.2.0
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://lib3ds.sourceforge.net/

Source: http://dl.sf.net/lib3ds/lib3ds-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### No default is needed (works without BuildRequires too)
%{!?_without_freeglut:BuildRequires: freeglut-devel}
%{?_without_freeglut:BuildRequires: glut-devel}

%description
Lib3ds is a free alternative to Autodesk's 3DS File Toolkit for handling
3DS files It's main goal is to simplify the creation of 3DS import and
export filters.

This project is not related in any form to Autodesk. The library is
based on unofficial information about the 3DS format found on the web.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL README TODO
%doc %{_mandir}/man1/3ds2m.1*
%doc %{_mandir}/man1/3dsdump.1*
%doc %{_mandir}/man1/lib3ds-config.1*
%{_bindir}/3ds2m
%{_bindir}/3dsdump
%{_bindir}/lib3ds-config
%{_datadir}/aclocal/lib3ds.m4
%{_includedir}/lib3ds/
%{_libdir}/lib3ds.a

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Cosmetic changes.

* Sat Jun 14 2003 Che
- initial rpm release
