# $Id$
# Authority: rudolf

Summary: Lua scripting language
Name: lua
Version: 5.0.2
Release: 1
License: MIT
Group: Development/Libraries
URL: http://www.lua.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.lua.org/ftp/lua-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Lua is a powerful light-weight programming language designed for extending
applications. Lua is also frequently used as a general-purpose, stand-alone
language. Lua is free software.

Lua combines simple procedural syntax with powerful data description
constructs based on associative arrays and extensible semantics. Lua is
dynamically typed, interpreted from bytecodes, and has automatic memory
management with garbage collection, making it ideal for configuration,
scripting, and rapid prototyping.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup 

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|^(INSTALL_ROOT=).*$|$1 \$(prefix)|;
		s|^(INSTALL_BIN=).*$|$1 \$(bindir)|;
		s|^(INSTALL_INC=).*$|$1 \$(includedir)|;
		s|^(INSTALL_LIB=).*$|$1 \$(libdir)|;
		s|^(INSTALL_MAN=).*$|$1 \$(mandir)/man1|;
		s|^(INSTALL_EXEC=).*$|$1 %{__install} -m0755|;
		s|^(INSTALL_DATA=).*$|$1 %{__install} -m0644|;
	' config

%build
%{__make} %{?_smp_mflags} all so \
	MYCFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -m0755 lib/*.so* %{buildroot}%{_libdir}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT HISTORY INSTALL MANIFEST README UPDATE doc/*html doc/*gif
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 5.0.2-1
- Updated to release 5.0.2.

* Sun Oct 12 2003 Dag Wieers <dag@wieers.com> - 5.0-0
- Initial package. (using DAR)
