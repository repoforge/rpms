# $Id$

# Authority: dries

Summary: viewer for DXF drawings
Name: dxfscope
Version: 0.2
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://wildspark.com/dxfscope/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://wildspark.com/dxfscope/%{name}-current.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, XFree86-devel
%{?fc1:Requires: XFree86}
%{?fc2:Requires: xorg-x11}

# Screenshot: http://wildspark.com/dxfscope/screenshot-city-thumb.png
# ScreenshotURL: http://wildspark.com/dxfscope/

%description
DXFscope is a viewer for DXF drawings. It supports the most commonly used
entities of the DXF specification.

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
%{_datadir}/dxfscope/help.dxf
%{_datadir}/dxfscope/romans2.cxf

%changelog
* Mon May 24 2004 Dries Verachtert <dries@ulyssis.org> 0.2-3
- install require fix for fedora core 2
  Thanks to Jochen Schlick for reporting the bug!

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 0.2-2
- cleanup of spec file

* Sat Dec 20 2003 Dries Verachtert <dries@ulyssis.org> 0.2-1
- first packaging for Fedora Core 1
 