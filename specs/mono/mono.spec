# $Id$

# Authority: dag

### FIXME: Makefiles don't allow -jX (parallel compilation)
# Distcc: 0

Summary: Mono CIL runtime, suitable for running .NET code
Name: mono
Version: 0.31
Release: 0
License: LGPL
Group: System Environment/Base
URL: http://www.go-mono.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://www.go-mono.com/archive/mono-%{version}.tar.gz
#Source1: http://www.go-mono.com/archive/mcs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, glib2-devel, libxml2-devel, libxslt-devel
BuildRequires: pkgconfig, icu, libicu-devel
Requires: /sbin/ldconfig
#Requires: mono-classes

%description
The Mono runtime implements a JIT engine for the ECMA CLI
virtual machine as well as a byte code interpreter, the
class loader, the garbage collector, threading system and
metadata access libraries.

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

### FIXME: Makefiles still have /usr/include hardcoded which breaks building as user. (Please fix upstream)
%{__perl} -pi.orig -e 's|\$\(privateincludedir\)|%{buildroot}%{_includedir}/mono/private|' libgc/include/Makefile*

#%{__ln_s} -f amd64/ mono/arch/x86-64
%{__perl} -pi.orig -e 's|(arch_target)=x86-64|$1=amd64|' configure*

### FIXME: TODO: Make wine and mono work together once and for all
%{__cat} <<'EOF' >mono.sysv
#!/bin/sh
#
# Allow users to run Mono (.Net) applications by just clicking on them
# (or typing ./file.exe)
#
# chkconfig: - 98 02
# description: Allow users to run Mono (.Net) applications by just clicking \
#	       on them (or typing ./file.exe)

source %{_initrddir}/functions

### Disable wine (conflicts)
chkconfig --level 12345 wine off

[ -x %{_bindir}/mono ] || exit 1

RETVAL=0

start() {
	echo $"Registering binary handler for Mono (.Net) applications"
	if [ ! -e /proc/sys/fs/binfmt_misc/register ]; then
		/sbin/modprobe binfmt_misc &>/dev/null
		mount -t binfmt_misc none /proc/sys/fs/binfmt_misc
	fi
	if [ -e /proc/sys/fs/binfmt_misc/register ]; then
		echo ':CLR:M::MZ::%{_bindir}/mono:' >/proc/sys/fs/binfmt_misc/register || :
		echo ':dotNet:M::MZ::%{_bindir}/mono:' > /proc/sys/fs/binfmt_misc/register || :
	else
		echo "No binfmt_misc support."
		RETVAL=1
	fi
}

stop() {
	echo $"Unregistering binary handler for Mono (.Net) applications"
	if [ -e /proc/sys/fs/binfmt_misc/CLR ]; then
		echo "-1" >/proc/sys/fs/binfmt_misc/CLR || :
	fi
}

restart() {
	stop
	start
}

mono_status() {
	if [ -e /proc/sys/fs/binfmt_misc/CLR ]; then
		echo $"Mono (.Net) binary format handlers are registered."
		return 0
	else
		echo $"Mono (.Net) binary format handlers are not registered."
		return 3
	fi
}

case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart|reload)
	restart
	;;
  condrestart)
	[ -e %{_localstatedir}/lock/subsys/$prog ] && restart
	RETVAL=$?
	;;
  status)
	mono_status
	RETVAL=$?
	;;
  *)
	echo $"Usage: $0 {start|stop|restart|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} %{?_smp_mflags} \
	CC="${CC:-%{__cc}} -gdwarf-2"

%install
%{__rm} -rf %{buildroot}

%makeinstall
#	privateincludedir="%{buildroot}%{_includedir}/mono/private"
%{__install} -d -m0755 %{buildroot}%{_initrddir}
%{__install} -m0755 mono.sysv %{buildroot}%{_initrddir}/mono

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post 
/sbin/ldconfig 2>/dev/null
/sbin/chkconfig --add mono

%postun 
/sbin/ldconfig 2>/dev/null
if [ $1 -eq 0 ]; then
        /sbin/chkconfig --del mono
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING.LIB NEWS README web/
%doc %{_mandir}/man1/mcs.*
%doc %{_mandir}/man1/mono.*
%doc %{_mandir}/man1/mint.*
%doc %{_mandir}/man1/oldmono.*
%config %{_initrddir}/*
%config %{_sysconfdir}/mono/
%{_bindir}/mbas*
%{_bindir}/mcs*
%{_bindir}/mint*
%{_bindir}/mono*
%{_libdir}/*.so.*
%{_libdir}/*.dll

%files devel
%defattr(-, root, root, 0755)
%doc docs/
%doc %{_mandir}/man5/*
%doc %{_mandir}/man1/cert2spc.*
%doc %{_mandir}/man1/certmgr.*
%doc %{_mandir}/man1/chktrust.*
%doc %{_mandir}/man1/cilc.*
%doc %{_mandir}/man1/disco.*
%doc %{_mandir}/man1/genxs.*
%doc %{_mandir}/man1/ilasm.*
%doc %{_mandir}/man1/makecert.*
%doc %{_mandir}/man1/monodis.*
%doc %{_mandir}/man1/monoburg.*
%doc %{_mandir}/man1/monop.*
%doc %{_mandir}/man1/monostyle.*
%doc %{_mandir}/man1/secutil.*
%doc %{_mandir}/man1/setreg.*
%doc %{_mandir}/man1/signcode.*
%doc %{_mandir}/man1/sn.*
%doc %{_mandir}/man1/soapsuds.*
%doc %{_mandir}/man1/sqlsharp.*
%doc %{_mandir}/man1/wsdl.*
%{_bindir}/al*
%{_bindir}/cert2spc*
%{_bindir}/certmgr*
%{_bindir}/chktrust*
%{_bindir}/cilc*
%{_bindir}/disco*
%{_bindir}/genxs*
%{_bindir}/ilasm*
%{_bindir}/MakeCert*
%{_bindir}/makecert*
%{_bindir}/monodis
%{_bindir}/monograph
%{_bindir}/monoresgen*
%{_bindir}/monosn
%{_bindir}/pedump
%{_bindir}/resgen*
%{_bindir}/secutil*
%{_bindir}/setreg*
%{_bindir}/signcode*
%{_bindir}/sn
%{_bindir}/soapsuds*
%{_bindir}/sqlsharp*
%{_bindir}/wsdl*
%{_bindir}/xsd*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mono/
%{_datadir}/mono/
#exclude %{_libdir}/*.la

%changelog
* Fri Mar 19 2004 Dag Wieers <dag@wieers.com> - 0.31-0
- Updated to release 0.31.

* Sat Feb 28 2004 Dag Wieers <dag@wieers.com> - 0.30.2-0
- Updated to release 0.30.2.

* Fri Feb 27 2004 Dag Wieers <dag@wieers.com> - 0.30.1-0
- Updated to release 0.30.1.

* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 0.29-0
- Updated to release 0.29.

* Sat Oct 04 2003 Dag Wieers <dag@wieers.com> - 0.28-0
- Updated to release 0.28.

* Sat Aug 16 2003 Dag Wieers <dag@wieers.com> - 0.26-0
- Updated to release 0.26.

* Thu Jun 26 2003 Dag Wieers <dag@wieers.com> - 0.25-0
- Updated to release 0.25.

* Sun May 25 2003 Dag Wieers <dag@wieers.com> - 0.24-1
- Added Mono binfmt-support sysv script.

* Wed May 07 2003 Dag Wieers <dag@wieers.com> - 0.24-0
- Updated to release 0.24.

* Mon Mar 17 2003 Dag Wieers <dag@wieers.com> - 0.23-0
- Initial package. (using DAR)
