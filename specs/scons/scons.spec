# $Id$
# Authority: dries

Summary: Software CONStruction tool, next-generation build tool
Name: scons
Version: 0.95
Release: 2
License: MIT
Group: Development/Tools
URL: http://www.scons.org/
Source: http://dl.sf.net/scons/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python
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
python setup.py install --root=%{buildroot}
%{__install} -D -m 644 scons.1 %{buildroot}/%{_mandir}/man1/scons.1
%{__install} -D -m 644 sconsign.1 %{buildroot}/%{_mandir}/man1/sconsign.1


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt 
%{_bindir}/*
%{_libdir}/scons
%{_mandir}/man1/*


%changelog
* Fri Jun  4 2004 Matthias Saou <http://freshrpms.net/> 0.95-2
- Spec file cleanup.
- Don't manually compress man pages, let rpm do that.
- Added python dependency.
- Removed unnecessary ldconfig calls (it's python ;-)).
- Removed unnecessary install paths.

* Sat May 22 2004 Dries Verachtert <dries@ulyssis.org> 0.95-1
- Initial package (spec file based on the spec file distributed by Steven
  Knight <knight AT scons DOT org>).

