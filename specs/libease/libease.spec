# $Id$
# Authority: dries
# Upstream: stroppytux$hotmail,com

Summary: Easing algorithms for graphical effects and mathematical calculations
Name: libease
Version: 0.0.1
Release: 1.2
License: GPL
Group: Development/Libraries
URL: http://libease.sourceforge.net/

Source: http://dl.sf.net/libease/libease-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:

%description
libease is a shared library containing easing algorithms that can be used
for graphical effects or mathematical calculations. The main goal of this
project is to try and create a centralised library for easing effects within
the window manager environment.

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
%{__perl} -pi -e "s|.*ldconfig.*||g;" Makefile
%{__perl} -pi -e "s|ln -s (.*)/libease(.*) (.*)/libease.so|ln -s %{_libdir}/libease\$2 \${3}/libease.so|g;" Makefile

%build
# FIXME 'make' without arguments also installs everything

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_includedir} %{buildroot}%{_bindir} %{buildroot}%{_libdir}
%{__make} all install PREFIX=%{buildroot}%{_prefix}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL
%{_libdir}/libease.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ease.h
%{_libdir}/libease.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.1-1.2
- Rebuild for Fedora Core 5.

* Thu Sep 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.1-1
- Initial package.
