# $Id$
# Authority: dag

### EL6 ships with lua-5.1.4-4.1.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Lua scripting language
Name: lua
Version: 5.1.4
Release: 2%{?dist}
License: MIT
Group: Development/Libraries
URL: http://www.lua.org/

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
        s|^(INSTALL_TOP=).*$|$1%{buildroot}%{_prefix}|;
        s|^(INSTALL_LIB=).*$|$1%{buildroot}%{_libdir}|;
        s|^(INSTALL_MAN=).*$|$1%{buildroot}%{_mandir}/man1|;
        s|^(INSTALL_EXEC=).*$|$1%{__install} -p -m0755|;
        s|^(INSTALL_DATA=).*$|$1%{__install} -p -m0644|;
    ' Makefile
%{__perl} -pi.orig -e '
        s|^(CFLAGS=).*$|$1%{optflags} -fPIC|;
    ' src/Makefile

%build
%{__make} linux all

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT doc/*gif doc/*html HISTORY INSTALL README
%doc %{_mandir}/man1/lua.1*
%doc %{_mandir}/man1/luac.1*
%{_bindir}/lua
%{_bindir}/luac

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/lauxlib.h
%{_includedir}/lua.h
%{_includedir}/lua.hpp
%{_includedir}/luaconf.h
%{_includedir}/lualib.h
%{_libdir}/liblua.a

%changelog
* Fri May 14 2010 Dag Wieers <dag@wieers.com> - 5.1.4-2
- Adapt compiler flags.

* Sun Jul 12 2009 Dag Wieers <dag@wieers.com> - 5.1.4-1
- Updated to release 5.1.4.

* Sun Feb 10 2008 Dag Wieers <dag@wieers.com> - 5.1.3-1
- Updated to release 5.1.3.

* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 5.0.2-1
- Updated to release 5.0.2.

* Sun Oct 12 2003 Dag Wieers <dag@wieers.com> - 5.0-0
- Initial package. (using DAR)
