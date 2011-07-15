# $Id$
# Authority: dag

### EL6 ships with lua-5.1.4-4.1.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Lua scripting language
Name: lua
Version: 5.1.4
Release: 3%{?dist}
License: MIT
Group: Development/Libraries
URL: http://www.lua.org/

Source: http://www.lua.org/ftp/lua-%{version}.tar.gz
Patch0: lua-5.1.4-autotoolize.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: readline-devel

Provides: lua = 5.1

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
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1
# fix perms on auto files
chmod u+x autogen.sh config.guess config.sub configure depcomp install-sh missing



%build
%configure --with-readline
%{__perl} -pi -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g;' libtool
%{__perl} -pi -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g;' libtool
# hack so that only /usr/bin/lua gets linked with readline as it is the
# only one which needs this and otherwise we get License troubles
%{__make} %{?_smp_mflags} LIBS="-lm -ldl" luac_LDADD="liblua.la -lm -ldl"
# also remove readline from lua.pc
%{__perl} -pi -e 's/-lreadline -lncurses //g;' etc/lua.pc


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__rm} %{buildroot}%{_libdir}/*.la
%{__mkdir_p} %{buildroot}%{_libdir}/lua/5.1
%{__mkdir_p} %{buildroot}%{_datadir}/lua/5.1

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
%{_libdir}/liblua*.so
%dir %{_datadir}/lua/5.1
%dir %{_libdir}/lua/5.1

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/lauxlib.h
%{_includedir}/lua.h
%{_includedir}/lua.hpp
%{_includedir}/luaconf.h
%{_includedir}/lualib.h
%{_libdir}/liblua.a
%{_libdir}/liblua.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jul 15 2011 Steve Huff <shuff@vecna.org> - 5.1.4-3
- Enable dynamic library loading.
- Port over autotools patch from EPEL.

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
