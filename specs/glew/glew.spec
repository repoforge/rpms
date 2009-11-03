# $Id$
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: OpenGL Extension Wrangler Library
Name: glew
Version: 1.3.5
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://glew.sourceforge.net/

Source: http://dl.sf.net/glew/glew-%{version}-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_modxorg:BuildRequires: libXext-devel, libXi-devel, libXmu-devel, mesa-libGL-devel, mesa-libGLU-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
The OpenGL Extension Wrangler Library (GLEW) is a cross-platform C/C++ 
extension loading library. GLEW provides efficient run-time mechanisms 
for determining which OpenGL extensions are supported on the target 
platform. OpenGL core and extension functionality is exposed in a single 
header file.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n glew

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install GLEW_DEST=%{buildroot}%{_prefix}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README.txt doc/*
%{_bindir}/glewinfo
%{_bindir}/visualinfo
%{_libdir}/libGLEW.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/GL/*.h
%{_libdir}/libGLEW.a
%{_libdir}/libGLEW.so

%changelog
* Sun Jan 27 2007 Dries Verachtert <dries@ulyssis.org> - 1.3.5-1
- Initial package.
