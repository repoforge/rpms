# $Id$
# Authority: dries

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _with_python15 1}
%{?el2:%define _with_python15 1}

Summary: Software CONStruction tool, next-generation build tool
Name: scons
Version: 1.2.0
Release: 1
License: MIT
Group: Development/Tools
URL: http://www.scons.org/

Source: http://dl.sf.net/scons/scons-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel >= 1.5
%{?_with_python15:BuildRequires: python-distutils}
Requires: python

%description
SCons is an Open Source software construction tool--that is, a
next-generation build tool. Think of SCons as an improved, cross-platform
substitute for the classic Make utility with integrated functionality
similar to autoconf/automake and compiler caches such as ccache. In short,
SCons is an easier, more reliable and faster way to build software.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root="%{buildroot}" --install-data="%{_datadir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES.txt LICENSE.txt README.txt RELEASE.txt
%doc %{_mandir}/man1/scons.1*
%doc %{_mandir}/man1/scons-time.1*
%doc %{_mandir}/man1/sconsign.1*
%{_bindir}/scons
%{_bindir}/scons-%{version}
%{_bindir}/scons-time
%{_bindir}/scons-time-%{version}
%{_bindir}/sconsign
%{_bindir}/sconsign-%{version}
%{_prefix}/lib/scons-%{version}/

%changelog
* Sun Jul 12 2009 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 0.98.1-1
- Updated to release 0.98.1.

* Tue May 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.97-1
- Updated to release 0.97.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 0.96.1-2
- Make the package noarch as it always should have been.

* Tue Aug 24 2004 Matthias Saou <http://freshrpms.net/> 0.96.1-1
- Update to 0.96.1.

* Sat Aug 21 2004 Dries Verachtert <dries@ulyssis.org> 0.96-1
- Update to version 0.96.

* Mon Jul  5 2004 Matthias Saou <http://freshrpms.net/> 0.95-2
- Files fix for x86_64.

* Fri Jun  4 2004 Matthias Saou <http://freshrpms.net/> 0.95-2
- Spec file cleanup.
- Don't manually compress man pages, let rpm do that.
- Added python dependency.
- Removed unnecessary ldconfig calls (it's python ;-)).
- Removed unnecessary install paths.

* Sat May 22 2004 Dries Verachtert <dries@ulyssis.org> 0.95-1
- Initial package (spec file based on the spec file distributed by Steven
  Knight <knight AT scons DOT org>).
