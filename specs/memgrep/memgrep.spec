# $Id$

# Authority: dag

Summary: Search/replace/dump memory from running processes and core files.
Name: memgrep
Version: 0.8.0
Release: 0
License: GPL
Group: System Environment/Base
URL: http://www.hick.org/code/skape/memgrep/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.hick.org/code/skape/memgrep/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


#BuildRequires: 

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

%build
%configure
%{__make} %{?_smp_mflags}

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
* Tue Dec 30 2003 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Initial package. (using DAR)
