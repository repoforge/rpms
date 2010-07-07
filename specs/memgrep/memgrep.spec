# $Id$
# Authority: dag

Summary: Search/replace/dump memory from running processes and core files
Name: memgrep
Version: 0.8.0
Release: 2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.hick.org/code/skape/memgrep/

Source: http://www.hick.org/code/skape/memgrep/memgrep-%{version}.tar.gz
Patch0: memgrep-0.8.0-include.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%filter_from_requires /^libc.so.6(GLIBC_PRIVATE)/d
%filter_from_provides /^libpthread.so/d
%filter_setup

%description
Search/replace/dump memory from running processes and core files.

%prep
%setup
%patch0 -p0

### FIXME: Make Makefile use autotool directory standard. (Please fix upstream)
%{__perl} -pi.orig -e '
        s|/usr/bin$|\$(DESTDIR)\$(bindir)|g;
        s|/usr/lib$|\$(DESTDIR)\$(libdir)|g;
        s|/usr/include$|\$(DESTDIR)\$(includedir)|g;
    ' Makefile.in

%{__perl} -pi.orig -e 's|regs.esp|regs.rsp|g;' src/memgrep.c

%build
%configure
### Has problems with -jX and X > 1
%{__make} FLAGS="%{optflags} -I../include" #%{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_includedir}
%{__install} -d -m0755 %{buildroot}%{_libdir}
%{__make} install DESTDIR="%{buildroot}" \
    bindir="%{_bindir}" \
    includedir="%{_includedir}" \
    libdir="%{_libdir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog docs/html/
%{_bindir}/memgrep
%{_includedir}/memgrep.h
%{_libdir}/heaplist.so
%{_libdir}/libmemgrep.so
%exclude %{_libdir}/libmemgrep.a

%changelog
* Sun Jul 04 2010 Dag Wieers <dag@wieers.com> - 0.8.0-2
- Fix include for RHEL4+.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 0.8.0-1
- Fixes find_provides and find_requires.

* Tue Dec 30 2003 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Initial package. (using DAR)
