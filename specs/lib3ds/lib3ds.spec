# $Id: $

# Authority: newrpms


Summary:        The 3D Studio File Format Library
Name:		lib3ds
Version:	1.2.0
Release:	1
Source0:	http://dl.sf.net/lib3ds/lib3ds-%{version}.tar.gz
License:	GPL
Group:		Development/Libraries
URL:		http://lib3ds.sourceforge.net
BuildRequires:	glut-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

Packager: Rudolf Kastl <che666 at uni.de>
Vendor: http://newrpms.sunsite.dk/

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
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README TODO
%{_libdir}/%{name}.a
%{_includedir}/%{name}
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/*
%defattr(755,root,root,755)
%{_bindir}/*

%changelog
* Sat Jun 14 2003 Che
- initial rpm release
