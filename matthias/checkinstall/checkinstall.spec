# Authority: dag
# Soapbox: 0

Summary: CheckInstall installations tracker.
Name: checkinstall
Version: 1.5.3
Release: 3
License: GPL
Group: Applications/System
URL: http://asic-linux.com.mx/~izto/checkinstall/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://checkinstall.izto.org/files/source/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
CheckInstall keeps track of all the files created or modified by your
installation script ("make install" "make install_modules", "setup",
etc), builds a standard binary package and installs it in your system
giving you the ability to uninstall it with your distribution's
standard package management  utilities. 

%prep
%setup

### FIXME: Fix the path to not use /usr/local (Please fix upstream)
%{__perl} -pi.orig -e '
		s|/usr/local/sbin|\$(sbindir)|;
		s|/usr/local/bin|\$(bindir)|;
		s|/usr/local/lib|\$(libdir)|;
	' Makefile
%{__perl} -pi.orig -e 's|/usr/local|%{_prefix}|g' checkinstall checkinstallrc
%{__perl} -pi.orig -e 's|#PREFIX#|%{_prefix}|g' installwatch

%build
%{__make} %{?_smp_mflags} \
	PREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_bindir} \
			%{buildroot}%{_libdir}/checkinstall/
%makeinstall \
	PREFIX="%{_prefix}" \
	BINDIR="%{buildroot}%{_bindir}" \
	LIBDIR="%{buildroot}%{_libdir}"
#%{__install} -m0755 installwatch-*/installwatch %{buildroot}%{_bindir}
#%{__install} -m0755 checkinstall makepak %{buildroot}%{_sbindir}
#%{__install} -m0755 installwatch-*/installwatch.so %{buildroot}%{_libdir}
#%{__install} -m0755 checkinstallrc %{buildroot}%{_libdir}/checkinstall/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changelog COPYING CREDITS FAQ README RELNOTES TODO
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/checkinstall/
%{_libdir}/*.so

%changelog
* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 1.5.3-3
- Fixed the longstanding undefined symbol (__builtin_va_start) bug.

* Thu Oct 16 2003 Dag Wieers <dag@wieers.com> - 1.5.3-2
- Fix PREFIX on RH80, RH73 and RH62. (Volodymyr M. Lisivka)

* Fri Oct 10 2003 Dag Wieers <dag@wieers.com> - 1.5.3-1
- Fix install location.

* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 1.5.3-0
- Initial package. (using DAR)
