# $Id$
# Authority: dag

%define memgrep_find_provides %{_builddir}/memgrep-find-provides
%define memgrep_find_requires %{_builddir}/memgrep-find-requires

%define _use_internal_dependency_generator 0

Summary: Search/replace/dump memory from running processes and core files
Name: memgrep
Version: 0.8.0
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.hick.org/code/skape/memgrep/

Source: http://www.hick.org/code/skape/memgrep/memgrep-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Search/replace/dump memory from running processes and core files.

%prep
%setup

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
		s|/usr/bin$|\$(bindir)|g;
		s|/usr/lib$|\$(libdir)|g;
		s|/usr/include$|\$(includedir)|g;
	' Makefile.in

%{__cat} <<EOF >%{memgrep_find_provides}
#!/bin/sh
%{__find_provides} | grep -v '^libpthread.so'
exit 0
EOF
chmod +x %{memgrep_find_provides}
%define __find_provides %{memgrep_find_provides}

%{__cat} <<EOF >%{memgrep_find_requires}
#! /bin/sh
%{__find_requires} | grep -v 'libc.so.6(GLIBC_PRIVATE)'
exit 0
EOF
chmod +x %{memgrep_find_requires}
%define __find_requires %{memgrep_find_requires}


%build
%configure
### Has problems with -jX and X > 1
%{__make} #%{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_includedir}

%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog docs/html/
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*.h

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.0-1.2
- Rebuild for Fedora Core 5.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Fixes find_provides and find_requires.

* Tue Dec 30 2003 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Initial package. (using DAR)
