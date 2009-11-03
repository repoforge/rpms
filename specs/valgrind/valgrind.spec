# $Id$
# Authority: matthias
# Upstream: Julian Seward <jseward$acm,org>


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

### Valgrind ships with FC3
# ExcludeDist: fc3 el4


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%define _use_internal_dependency_generator 0

%define _pkglibdir %{_libdir}/%{name}

Summary: Debugging and profiling system for x86-GNU/Linux platforms
Name: valgrind
Version: 2.1.1
Release: 1%{?dist}
License: GPL
Group: Development/Debuggers
URL: http://valgrind.kde.org/

Source: http://developer.kde.org/~sewardj/valgrind-%{version}.tar.bz2
Source1: valgrind-nptltest.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: %{ix86}
#BuildRequires: gdb
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Valgrind is a GPL'd tool to help you find memory-management problems in
your programs. When a program is run under Valgrind's supervision, all
reads and writes of memory are checked, and calls to malloc/new/free/delete
are intercepted. As a result, Valgrind can detect problems such as:

    * Use of uninitialised memory
    * Reading/writing memory after it has been free'd
    * Reading/writing off the end of malloc'd blocks
    * Reading/writing inappropriate areas on the stack
    * Memory leaks -- where pointers to malloc'd blocks are lost forever
    * Passing of uninitialised and/or unaddressible memory to system calls
    * Mismatched use of malloc/new/new [] vs free/delete/delete []
    * Some misuses of the POSIX pthreads API


%prep
%setup

%{__perl} -pi.orig -e 's|^(nptl_threading)=.*$|nptl_threading="$($VALGRIND/nptltest)"|' coregrind/valgrind.in

%build
%{__cc} %{optflags} %{SOURCE1} -lpthread -o nptltest || echo -e '#!/bin/sh\necho no' >nptltest

%configure
### Workaround for broken make (RHbz #88846)
unset CFLAGS
env - PATH="$PATH" %{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	docdir="%{_builddir}/%{buildsubdir}/rpm-doc"

%{__install} -Dp -m0755 nptltest %{buildroot}%{_libdir}/valgrind/nptltest

echo -e "#!/bin/sh\nexec %{__find_provides} | grep -v '^libpthread.so'" >%{_builddir}/%{buildsubdir}/find-provides
chmod +x %{_builddir}/%{buildsubdir}/find-provides
%define __find_provides %{_builddir}/%{buildsubdir}/find-provides

echo -e "#!/bin/sh\nexec %{__find_requires} | grep -v GLIBC_PRIVATE" >%{_builddir}/%{buildsubdir}/find-requires
chmod +x %{_builddir}/%{buildsubdir}/find-requires
%define __find_requires %{_builddir}/%{buildsubdir}/find-requires


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS AUTHORS COPYING NEWS README* TODO
%doc rpm-doc/
%{_bindir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/valgrind/
%{_includedir}/valgrind/


%changelog
* Wed Apr 07 2004 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Updated to release 2.1.1.

* Tue Mar  2 2004 Matthias Saou <http://freshrpms.net/> 2.0.0-1.fr
- Minor spec file fixes.
- Clean up remains of ntpl stuff.
- Use the $PATH fix for the build to actually work.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 2.0.0-0
- Updated to release 2.0.0.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 1.9.6-1
- Fixes the find_provides and find_requires for RH73 and RH80.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 1.9.6-0
- Updated to release 1.9.6.

* Wed Apr 23 2003 Dag Wieers <dag@wieers.com> - 1.9.5-0
- Updated to release 1.9.5.
- Added a program to test for NPTL at runtime.

* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 1.0.4-0
- Initial package. (using DAR)

