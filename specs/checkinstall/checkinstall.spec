# $Id$
# Authority: dag

Summary: CheckInstall installations tracker
Name: checkinstall
Version: 1.6.0
Release: 3%{?dist}
License: GPL
Group: Applications/System
URL: http://asic-linux.com.mx/~izto/checkinstall/

Source: http://checkinstall.izto.org/files/source/checkinstall-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
		s|/usr/local/sbin|\$(sbindir)|g;
		s|/usr/local/bin|\$(bindir)|g;
		s|/usr/local/lib|\$(libdir)|g;
	' Makefile
%{__perl} -pi.orig -e '
		s|/usr/local|%{_prefix}|g;
		s|/lib\b|/%{_lib}|g;
		s|#PREFIX#|%{_prefix}|g;
	' checkinstall checkinstallrc* installwatch-*/installwatch

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
	LIBDIR="%{buildroot}%{_libdir}" \
	INSTALLWATCH_PREFIX=%{_prefix}
#%{__install} -p -m0755 installwatch-*/installwatch %{buildroot}%{_bindir}
#%{__install} -p -m0755 checkinstall makepak %{buildroot}%{_sbindir}
#%{__install} -p -m0755 installwatch-*/installwatch.so %{buildroot}%{_libdir}
#%{__install} -p -m0755 checkinstallrc %{buildroot}%{_libdir}/checkinstall/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS Changelog COPYING CREDITS FAQ README RELNOTES TODO
%{_bindir}/installwatch
%{_sbindir}/checkinstall
%{_sbindir}/makepak
%{_libdir}/checkinstall/
%{_libdir}/*.so

%changelog
* Tue Jun 06 2006 Dag Wieers <dag@wieers.com> - 1.6.0-3
- Fixed a stale reference to /usr/lib on x86_64. (Stefan.Neufeind)

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.0-2
- Fixed the path to installwatch, thanks to Renato Ramonda. (atrpms bugzilla bug 723)

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Updated to release 1.6.0.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 1.5.3-3
- Fixed the longstanding undefined symbol (__builtin_va_start) bug.

* Thu Oct 16 2003 Dag Wieers <dag@wieers.com> - 1.5.3-2
- Fix PREFIX on RH80, RH73 and RH62. (Volodymyr M. Lisivka)

* Fri Oct 10 2003 Dag Wieers <dag@wieers.com> - 1.5.3-1
- Fix install location.

* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 1.5.3-0
- Initial package. (using DAR)
