# $Id: $

# Authority: dries
# Upstream: 

Summary: Software construction tool
Name: scons
Version: 0.95
Release: 1
License: MIT
Group: Development/Tools
URL: http://www.scons.org/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/scons/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python, python-devel

%description
SCons is an Open Source software construction tool--that is, a
next-generation build tool. Think of SCons as an improved, cross-platform
substitute for the classic Make utility with integrated functionality
similar to autoconf/automake and compiler caches such as ccache. In short,
SCons is an easier, more reliable and faster way to build software. 

%prep
%setup

%build
python setup.py build

%install
%{__rm} -rf %{buildroot}
python setup.py install --root=%{buildroot} --install-lib=%{_libdir}/scons --install-scripts=%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
gzip -c scons.1 > %{buildroot}/%{_mandir}/man1/scons.1.gz
gzip -c sconsign.1 > %{buildroot}/%{_mandir}/man1/sconsign.1.gz

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt 
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/scons
%{_mandir}/man1/scons*

%changelog
* Sat May 22 2004 Dries Verachtert <dries@ulyssis.org> 0.95-1
- Initial package
  spec file based on the spec file distributed by Steven Knight <knight AT scons DOT org>


