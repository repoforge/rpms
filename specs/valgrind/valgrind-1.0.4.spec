# Authority: dag

# Upstream: Julian Seward <jseward@acm.org>

Summary: An open-source memory debugger for x86-GNU/Linux.
Name: valgrind
Version: 1.0.4
Release: 0
Group: Development/Tools
License: GPL
URL: http://developer.kde.org/~sewardj/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://developer.kde.org/~sewardj/%{name}-%{version}.tar.bz2
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

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot.
%{__rm} -rf %{buildroot}%{_datadir}/doc/valgrind/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ACKNOWLEDGEMENTS AUTHORS ChangeLog COPYING NEWS PATCHES* README* TODO docs/*.html
%{_bindir}/*
%{_libdir}/valgrind/
%{_includedir}/*.h

%changelog
* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 1.0.4-0
- Initial package. (using DAR)
