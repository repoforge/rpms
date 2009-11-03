# $Id$
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}


Summary: 3D plotting widget for scientific data and mathematical expressions
Name: qwtplot3d
Version: 0.2.6
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://qwtplot3d.sourceforge.net/

Source: http://dl.sf.net/qwtplot3d/qwtplot3d-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel, gcc-c++
%{!?_without_modxorg:BuildRequires: libXmu-devel}

%description
qwtplot3d is a graphics extension to the Qt GUI application framework that 
provides a 3D plotting widget for scientific data and mathematical 
expressions.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}

%build
qmake -d qwtplot3d.pro
#configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_includedir} %{buildroot}%{_libdir}
%{__install} include/* %{buildroot}%{_includedir}/
%{__install} lib/* %{buildroot}%{_libdir}/
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc examples
%{_libdir}/libqwtplot3d.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/qwt3d_*.h
%{_libdir}/libqwtplot3d.so

%changelog
* Thu Aug 03 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.6-1
- Initial package.
