# Authority: dag

# Upstream: Julian Seward <jseward@acm.org>

Summary: Debugging and profiling system for x86-GNU/Linux platforms
Name: valgrind
Version: 2.0.0
Release: 1.fr
Group: Development/Tools
License: GPL
URL: http://valgrind.kde.org/
Source: http://developer.kde.org/~sewardj/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
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


%prep
%setup


%build
%configure
env - PATH="$PATH" %{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot.
%{__rm} -rf %{buildroot}%{_docdir}/valgrind/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS AUTHORS ChangeLog COPYING NEWS PATCHES* README* TODO
%doc docs/*.html
%{_bindir}/*
%{_libdir}/valgrind/
%{_includedir}/valgrind/


%changelog
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

