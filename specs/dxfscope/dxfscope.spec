# $Id$

# Authority: dries

Summary: viewer for DXF drawings
Name: dxfscope
Version: 0.2
Release: 2
License: GPL
Group: Applications/Multimedia
URL: http://wildspark.com/dxfscope/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://wildspark.com/dxfscope/%{name}-current.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, XFree86-devel
Requires: XFree86

#(d) primscreenshot: http://wildspark.com/dxfscope/screenshot-city-thumb.png
#(d) screenshotsurl: http://wildspark.com/dxfscope/

%description
DXFscope is a viewer for DXF drawings. It supports the most commonly used
entities of the DXF specification.

%description -l nl
DXFscope is een viewer voor DXF tekeningen. Het ondersteunt de meest
gebruikte onderdelen van de DXF specificatie.

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
sed -i "s/\/local//" Makefile
sed -i "s/\/dxfscope\/share/\/share\/dxfscope/" Makefile
%{__make} %{?_smp_mflags}

%install
echo RPM_BUILD_ROOT is $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
install -s -D -oroot -m0755 dxfscope $RPM_BUILD_ROOT/usr/bin/dxfscope
install -D -oroot -m0644 help.dxf $RPM_BUILD_ROOT/usr/share/dxfscope/help.dxf
install -D -oroot -m0644 romans2.cxf $RPM_BUILD_ROOT/usr/share/dxfscope/romans2.cxf

%files
%defattr(-,root,root,0755)
%doc README COPYING HACKING TODO
%{_bindir}/dxfscope
/usr/share/dxfscope/help.dxf
/usr/share/dxfscope/romans2.cxf

%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.2-2
- cleanup of spec file

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.2-1
- first packaging for Fedora Core 1
 