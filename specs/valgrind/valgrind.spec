# Authority: dag

# Upstream: Julian Seward <jseward@acm.org>

Summary: An open-source memory debugger for x86-GNU/Linux.
Name: valgrind
Version: 2.0.0
Release: 0
Group: Development/Tools
License: GPL
URL: http://valgrind.kde.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://developer.kde.org/~sewardj/%{name}-%{version}.tar.bz2
#Source1: valgrind-nptltest.c
#Patch0: valgrind-1.9.5-nptl.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: XFree86-devel

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

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1 -b .nptl

### For reference only.
#cat <<EOF >nptl.c
#//#define _XOPEN_SOURCE
##define _POSIX_C_SOURCE 2
##include <unistd.h>
##include <stdio.h>
#
#int main(void) {
#        char *buf; size_t n;
#
#        n=confstr(_CS_GNU_LIBPTHREAD_VERSION, NULL, (size_t) 0);
#        if ((buf = (char *) malloc(n)) == NULL) abort();
#        confstr(_CS_GNU_LIBPTHREAD_VERSION, buf, n);
#        fprintf(stdout, "%s\n", buf); exit(0);
#}
#EOF

#echo -e "#!/bin/bash\n%{__find_provides} | grep -v '^libpthread.so'" >find_provides.sh
#echo -e "#!/bin/bash\n%{__find_requires} | grep -v 'libc.so.6(GLIBC_PRIVATE)'" >find_requires.sh
#chmod +x find_provides.sh find_requires.sh

#define __find_provides find_provides.sh 
#define __find_requires find_requires.sh

%build
### FIXME: Fix for realtime NPTL handling.
#{__perl} -pi.orig -e 's|^nptl_threading=.*$|nptl_threading="\$(if getconf GNU_LIBPTHREAD_VERSION &>/dev/null; then echo "yes"; else echo "no"; fi)"|' coregrind/valgrind.in
%configure
### FIXME: See RH BugZilla #88846
#unset CFLAGS
%{__make} %{?_smp_mflags}

### For reference only.
#if ! %{__cc} %{optflags} -o nptl nptl.c; then
#	echo -e "#!/bin/false" > nptl;
#fi

%install
%{__rm} -rf %{buildroot}
%makeinstall

#%{__install} -m0755 nptl %{buildroot}%{_libdir}/valgrind/

### Clean up buildroot.
%{__rm} -rf %{buildroot}%{_docdir}/valgrind/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS AUTHORS ChangeLog COPYING NEWS PATCHES* README* TODO docs/*.html
%{_bindir}/*
%{_libdir}/valgrind/
%{_includedir}/valgrind/

%changelog
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
