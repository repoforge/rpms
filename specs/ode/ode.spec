# Authority: dries
# Upstream: Russell Smith <russ_smith$users,sourceforge,net>

Summary: OpenDE Library
Name: ode
Version: 0.6
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://ode.org

Source: http://dl.sf.net/opende/%{name}-src-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
ODE is a free, industrial quality library for simulating articulated
rigid body dynamics - for example ground vehicles, legged creatures,
and moving objects in VR environments. It is fast, flexible, robust
and platform independent, with advanced joints, contact with friction,
and built-in collision detection.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{version}

%build
%configure --enable-release --enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG.txt INSTALL.txt LICENSE.TXT LICENSE-BSD.TXT README.txt
%{_libdir}/libode.so

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ode/
%{_bindir}/ode-config
%{_libdir}/libode.a

%changelog
* Tue Jul 25 2006 Vincent Knecht <vknecht@users.sourceforge.net> - 0.6-1
- Initial packaging.
