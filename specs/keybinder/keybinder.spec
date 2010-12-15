# $Id$
# Authority: shuff
# Upstream: Ulrik Sverdrup <ulrik$kaiser,se>
# ExcludeDist: el3 el4 el5

%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Register global keyboard shortcuts for GTK apps
Name: keybinder
Version: 0.2.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://kaizer.se/wiki/keybinder/

Source: http://kaizer.se/publicfiles/keybinder/keybinder-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk2-devel >= 2.20
BuildRequires: lua-devel
BuildRequires: python-devel
BuildRequires: rpm-macros-rpmforge

%description
Keybinder is a library for registering global keyboard shortcuts.  Keybinder
works with GTK-based applications using the X Window System.

%package devel
Summary: Development headers for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Install this package if you want to develop C code that uses %{name}.

%package -n lua-%{name}
Summary: Lua bindings for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: lua

%description -n lua-%{name}
This package contains Lua bindings for %{name}.

%package -n python-%{name}
Summary: Python bindings for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: python

%description -n python-%{name}
This package contains Python bindings for %{name}.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* COPYING NEWS README examples/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%files -n lua-%{name}
%defattr(-, root, root, 0755)

%files -n python-%{name}
%defattr(-, root, root, 0755)
%{python_sitelib}/*

%changelog
* Wed Dec 15 2010 Steve Huff <shuff@vecna.org> - 0.2.2-1
- Initial package.
