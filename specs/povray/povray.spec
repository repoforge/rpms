# $Id$

# Authority: dries
# Upstream:

# The source isn't available yet :(
# will be available in a few weeks


Summary: Persistence of Vision Raytracer
Name: povray
Version: 3.6.0
Release: 1.2%{?dist}
License: Other
Group: Amusements/Graphics
URL: http://www.povray.org/

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires:

%description
The Persistence of Vision Raytracer is a high-quality, totally free tool for
creating stunning three-dimensional graphics.

The license of povray is quite complicated, more information can be found
at:
http://www.povray.org/povlegal.html
http://www.povray.org/distribution-license.html

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.6.0-1.2
- Rebuild for Fedora Core 5.

* Mon Jun 14 2004 Dries Verachtert <dries@ulyssis.org> - 3.6.0-1
- Initial package.

