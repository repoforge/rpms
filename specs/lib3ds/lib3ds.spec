# $Id: $
# Authority: newrpms

Summary: The 3D Studio File Format Library
Name: lib3ds
Version: 1.2.0
Release: 1
License: GPL
Group: Development/Libraries
URL: http://lib3ds.sourceforge.net

Packager: Rudolf Kastl <che666 at uni.de>
Vendor: http://newrpms.sunsite.dk/

Source: http://dl.sf.net/lib3ds/lib3ds-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glut-devel

%description
Lib3ds is a free alternative to Autodesk's 3DS File Toolkit for handling
3DS files It's main goal is to simplify the creation of 3DS import and
export filters.

This project is not related in any form to Autodesk. The library is
based on unofficial information about the 3DS format found on the web.

This  program  is  distributed in  the  hope that it will  be useful,  but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
License for more details.

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
