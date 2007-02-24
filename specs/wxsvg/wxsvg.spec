# $Id$
# Authority: matthias

%define prever b7

Summary: C++ library to create, manipulate and render SVG files
Name: wxsvg
Version: 1.0
Release: 0.1.%{prever}
License: wxWidgets Library Licence
Group: System Environment/Libraries
URL: http://wxsvg.sourceforge.net/
Source: http://dl.sf.net/wxsvg/wxsvg-%{version}%{prever}_1.tar.gz
Patch0: wxsvg-1.0b7-freetype.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libart_lgpl-devel
BuildRequires: pkgconfig
BuildRequires: pango-devel
BuildRequires: freetype-devel
BuildRequires: wxGTK-devel

%description
wxSVG is C++ library to create, manipulate and render SVG files.


%package devel
Summary: Development files for the wxSVG library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
wxSVG is C++ library to create, manipulate and render SVG files.


%prep
%setup -n %{name}-%{version}%{prever}
%patch0 -p1 -b .freetype


%build
%configure --disable-static
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING TODO
%{_bindir}/svgview
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/wxSVG/
%{_includedir}/wxXML/
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Fri Jan 19 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.1.b7
- Initial RPM release.

