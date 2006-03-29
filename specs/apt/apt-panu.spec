# $Id$
# Authority: dag
# Upstream: Panu Matilainen <pmatilai$laiskiainen,org>

# Tag: test

%{?dist: %{expand: %%define %dist 1}}
%define LIBVER 3.3

Summary: Debian's Advanced Packaging Tool with RPM support
Name: apt
%define real_version 01032006
Version: 0.5.15lorg2
Release: 0.20060301
License: GPL
Group: System Environment/Base
URL: https://moin.conectiva.com.br/AptRpm

Source: http://laiskiainen.org/apt/testing/apt-repomd-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: rpm-devel >= 3.0.5, zlib-devel, gettext
BuildRequires: readline-devel, bison, gcc-c++, libtool
BuildRequires: pkg-config >= 0.9
%{!?rh6:BuildRequires: bzip2-devel, libstdc++-devel, docbook-utils}

%{!?dist:BuildRequires: beecrypt-devel, elfutils-devel}
%{?fc4:BuildRequires: beecrypt-devel, elfutils-devel}
%{?el4:BuildRequires: beecrypt-devel, elfutils-devel}
%{?fc3:BuildRequires: beecrypt-devel, elfutils-devel}
%{?fc2:BuildRequires: beecrypt-devel, elfutils-devel}
%{?fc1:BuildRequires: beecrypt-devel, elfutils-devel}
%{?el3:BuildRequires: beecrypt-devel, elfutils-devel}
%{?rh9:BuildRequires: beecrypt-devel, elfutils-devel}
%{?rh8:BuildRequires: libelf-devel}
%{?rh7:BuildRequires: libelf}
%{?el2:BuildRequires: libelf}
%{?rh6:BuildRequires: libelf}

Requires: rpm >= 3.0.5, zlib, bzip2-libs, libstdc++

%description
A port of Debian's apt tools for RPM based distributions, or at least
originally for Conectiva and now Red Hat Linux. It provides the apt-get
utility that provides a simpler, safer way to install and upgrade packages.
APT features complete installation ordering, multiple source capability and
several other unique features.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-repomd-%{real_version}

%{__perl} -pi.orig -e 's|RPM APT-HTTP/1.3|RPMforge RPM Repository %{dist}/%{_arch} APT-HTTP/1.3|' methods/http.cc

%{__cat} <<EOF >os.list
# Name: FreshRPMS OS/updates
# URL: http://ayo.freshrpms.net/

### Fedora Core
%{!?fc5:#}rpm http://ayo.freshrpms.net fedora/linux/5/%{_arch} core updates
%{!?fc4:#}rpm http://ayo.freshrpms.net fedora/linux/4/%{_arch} core updates
%{!?fc3:#}rpm http://ayo.freshrpms.net fedora/linux/3/%{_arch} core updates
%{!?fc2:#}rpm http://ayo.freshrpms.net fedora/linux/2/%{_arch} core updates
%{!?fc1:#}rpm http://ayo.freshrpms.net fedora/linux/1/%{_arch} core updates

### Red Hat Linux
%{!?rh9:#}rpm http://ayo.freshrpms.net redhat/9/i386 os updates
%{!?rh8:#}rpm http://ayo.freshrpms.net redhat/8.0/i386 os updates
%{!?rh7:#}rpm http://ayo.freshrpms.net redhat/7.3/i386 os updates
%{!?rh6:#}rpm http://ayo.freshrpms.net redhat/6.2/i386 os powertools updates
EOF

%{__cat} <<'EOF' >apt.conf
APT {
	Clean-Installed "false";
	Get {
		Assume-Yes "false";
		Download-Only "false";
		Show-Upgraded "true";
		Fix-Broken "false";
		Ignore-Missing "false";
		Compile "false";
	};
};

Acquire {
	Retries "0";
	HTTP {
		Proxy ""; // http://user:pass@host:port/
	};
};

RPM {
	Ignore { };
	Hold { };
	Options { };
	Install-Options "";
	Erase-Options "";
//	Pre-Install-Pkgs { "/usr/bin/apt-sigchecker"; };
	Source {
		Build-Command "rpmbuild --rebuild";
	};
	Allow-Duplicated {
		"^kernel$";
		"^kernel-";
		"^gpg-pubkey$";
	};
};
EOF

%build
%{?fc5:libtoolize -f && autoreconf}
%{?fc4:libtoolize -f && autoreconf}
#{__autoconf}
%configure \
	--program-prefix="%{?_program_prefix}" \
	--includedir="%{_includedir}/apt-pkg"
#	--with-hashmap
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	includedir="%{buildroot}%{_includedir}/apt-pkg"
%find_lang %{name}

%{__install} -d -m0755 \
		%{buildroot}%{_sysconfdir}/apt/{apt.conf.d,sources.list.d} \
		%{buildroot}%{_localstatedir}/cache/apt/{archives/partial,genpkglist,gensrclist} \
		%{buildroot}%{_localstatedir}/state/apt/lists/partial \
		%{buildroot}%{_libdir}/apt/scripts/
%{__install} -p -m0644 rpmpriorities apt.conf %{buildroot}%{_sysconfdir}/apt/
%{__install} -p -m0644 os.list %{buildroot}%{_sysconfdir}/apt/sources.list.d/
touch %{buildroot}%{_sysconfdir}/apt/preferences \
	%{buildroot}%{_sysconfdir}/apt/vendors.list

#%{__ln_s} -f %{_libdir}libapt-pkg-libc6.3-5.so.0 %{buildroot}%{_libdir}libapt-pkg-libc6.3-5.so.%{LIBVER}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS* COPYING* TODO contrib/ doc/examples/
%doc %{_mandir}/man?/*
%dir %{_sysconfdir}/apt/
%config(noreplace) %{_sysconfdir}/apt/apt.conf
%config(noreplace) %{_sysconfdir}/apt/preferences
#config(noreplace) %{_sysconfdir}/apt/sources.list
%config(noreplace) %{_sysconfdir}/apt/vendors.list
%config %{_sysconfdir}/apt/rpmpriorities
%config(noreplace) %{_sysconfdir}/apt/apt.conf.d/
%config(noreplace) %{_sysconfdir}/apt/sources.list.d/
%{_bindir}/apt-cache
%{_bindir}/apt-cdrom
%{_bindir}/apt-config
%{_bindir}/apt-get
%{_bindir}/apt-shell
%{_bindir}/genbasedir
%{_bindir}/genpkglist
%{_bindir}/gensrclist
%{_bindir}/countpkglist
%{_libdir}/apt/
%{_libdir}/libapt-pkg-*.so.*
%{_localstatedir}/cache/apt/
%{_localstatedir}/state/apt/

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libapt-pkg.a
%exclude %{_libdir}/libapt-pkg.la
%{_libdir}/libapt-pkg.so
%{_includedir}/apt-pkg/
#exclude %{_libdir}/*.la

%changelog
* Sun Mar 05 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg2-0.20060301
- Experimental version from Panu with repomd and multilib support.

* Mon Jan 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.15cnc7-1
- Added libtoolize and autoreconf fix for Fedora Core 5, thanks
  to Stephen Clement.
- Updated to release 0.5.15cnc7.

* Sat Nov 20 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc6-4
- Added readline-devel as buildrequirement for apt-shell.

* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc6-3
- Fix for apt-bug triggered by mach.

* Fri Jun 04 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc6-2
- Make apt understand about architectures.

* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc6-1
- Updated to release 0.5.15cnc6.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc1-1
- Added RHAS21 repository.

* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc5-0
- Updated to release 0.5.15cnc5.

* Sat Dec 06 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc4-1
- Disabled the epoch promotion behaviour on RH9.

* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc4-0
- Updated to release 0.5.15cnc4.

* Tue Nov 25 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc3-0
- Updated to release 0.5.15cnc3.

* Mon Nov 10 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc2-0
- Updated to release 0.5.15cnc2.

* Mon Nov 10 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc1-1
- Fixed apt pinning.
- Added RHFC1 repository.

* Sat Nov 08 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc1-0
- Updated to release 0.5.15cnc1.

* Sun Oct 26 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc6-1
- Added RHEL3 repository.

* Tue Jun 10 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc6-0
- Added newrpms and enable it by default.
- Updated to release 0.5.5cnc6.

* Tue Jun 03 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc5-4
- Added freshrpms and enable it by default.

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc5-3
- Work around a bug in apt (apt.conf).

* Fri May 30 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc5-2
- Moved sources.list to sources.d/

* Wed Apr 16 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc5-1
- Updated to release 0.5.5cnc5.

* Tue Apr 08 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc4.1-2
- RH90 repository rename from redhat/9.0 to redhat/9.

* Sat Apr 05 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc4.1-1
- FreshRPMS fixes to repository locations.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc4.1-0
- Updated to release 0.5.5cnc4.1.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc3-0
- Updated to release 0.5.5cnc3.

* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc2-0
- Updated to release 0.5.5cnc2.

* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 0.5.4cnc9-0
- Initial package. (using DAR)
