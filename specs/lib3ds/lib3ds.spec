# $Id$
# Authority: rudolf

%{?dist:%{expand: %%define %{dist} 1}}

Summary: The 3D Studio File Format Library
Name: lib3ds
Version: 1.2.0
Release: 0
License: GPL
Group: Development/Libraries
URL: http://lib3ds.sourceforge.net/

Packager: Rudolf Kastl <che666 at uni.de>
Vendor: http://newrpms.sunsite.dk/

Source: http://dl.sf.net/lib3ds/lib3ds-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

### No default is needed (works without BuildRequires too)
#%{!?dist:BuildRequires: freeglut-devel}
%{?fc2:BuildRequires: freeglut-devel}
%{?fc1:BuildRequires: freeglut-devel}
%{?rh9:BuildRequires: glut-devel}

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
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/aclocal/*.m4
%{_includedir}/lib3ds/
%{_libdir}/*.a

%changelog
* Sat Jun 14 2003 Che
- initial rpm release
