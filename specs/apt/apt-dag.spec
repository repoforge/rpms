# Authority: atrpms
# Upstream: Gustavo Niemeyer <niemeyer$conectiva,com>

%{?dist: %{expand: %%define %dist 1}}
%define LIBVER 3.3

Summary: Debian's Advanced Packaging Tool with RPM support
Name: apt
Version: 0.5.15cnc5
Release: 1
License: GPL
Group: System Environment/Base
URL: https://moin.conectiva.com.br/AptRpm

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://moin.conectiva.com.br/files/AptRpm/attachments/apt-%{version}.tar.bz2
Patch0: apt-0.5.15cnc1-rpmpriorities.patch
Patch1: apt-0.5.5cnc5-nodignosig.patch
Patch2: apt-0.5.15cnc4-nopromote.patch
#Patch3: apt-0.5.5cnc6-rpm402.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: rpm-devel >= 4.0, zlib-devel, gettext
%{!?rh6:BuildRequires: bzip2-devel, libstdc++-devel, docbook-utils}

%{?fc1:BuildRequires: beecrypt-devel, elfutils-devel}
%{?el3:BuildRequires: beecrypt-devel, elfutils-devel}
%{?rh9:BuildRequires: beecrypt-devel, elfutils-devel}
%{?rh8:BuildRequires: libelf-devel}
%{?rh7:BuildRequires: libelf}
%{?el2:BuildRequires: libelf}
%{?rh6:BuildRequires: libelf}

Requires: rpm >= 4.0, zlib, bzip2-libs, libstdc++

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
%setup
%patch0 -b .rpmpriorities
#patch1 -b .nodignosig
#patch2 -p1 -b .nopromote
#{?rh62:%patch3 -b .402}

%{?fc2:%{__perl} -pi.orig -e 's|RPM APT-HTTP/1.3|Dag Apt Repository RH FC2 APT-HTTP/1.3|' methods/http.cc}
%{?fc1:%{__perl} -pi.orig -e 's|RPM APT-HTTP/1.3|Dag Apt Repository RH FC1 APT-HTTP/1.3|' methods/http.cc}
%{?el3:%{__perl} -pi.orig -e 's|RPM APT-HTTP/1.3|Dag Apt Repository RH EL3 APT-HTTP/1.3|' methods/http.cc}
%{?rh9:%{__perl} -pi.orig -e 's|RPM APT-HTTP/1.3|Dag Apt Repository RH 9 APT-HTTP/1.3|' methods/http.cc}
%{?rh8:%{__perl} -pi.orig -e 's|RPM APT-HTTP/1.3|Dag Apt Repository RH 8.0 APT-HTTP/1.3|' methods/http.cc}
%{?rh7:%{__perl} -pi.orig -e 's|RPM APT-HTTP/1.3|Dag Apt Repository RH 7.3 APT-HTTP/1.3|' methods/http.cc}
%{?el2:%{__perl} -pi.orig -e 's|RPM APT-HTTP/1.3|Dag Apt Repository RH EL2.1 APT-HTTP/1.3|' methods/http.cc}
%{?rh6:%{__perl} -pi.orig -e 's|RPM APT-HTTP/1.3|Dag Apt Repository RH 6.2 APT-HTTP/1.3|' methods/http.cc}

%{__cat} <<EOF >dag.list
### Dag Apt Repository
### """"""""""""""""""
### More information of this repository at:
###	http://dag.wieers.com/apt/

### Dag Apt Repository for Red Hat Fedore Core 2
%{!?fc2:#}rpm http://apt.sw.be fedora/2/en/i386 dag
#rpm-src http://apt.sw.be fedora/2/en/i386 dag

### Dag Apt Repository for Red Hat Fedore Core 1
%{!?fc1:#}rpm http://apt.sw.be fedora/1/en/i386 dag
#rpm-src http://apt.sw.be fedora/1/en/i386 dag

### Dag Apt Repository for Red Hat Enterprise Linux 3
%{!?el3:#}rpm http://apt.sw.be redhat/el3/en/i386 dag
#rpm-src http://apt.sw.be redhat/el3/en/i386 dag

### Dag Apt Repository for Red Hat 9
%{!?rh9:#}rpm http://apt.sw.be redhat/9/en/i386 dag
#rpm-src http://apt.sw.be redhat/9/en/i386 dag

### Dag Apt Repository for Red Hat 8.0
%{!?rh8:#}rpm http://apt.sw.be redhat/8.0/en/i386 dag
#rpm-src http://apt.sw.be redhat/8.0/en/i386 dag

### Dag Apt Repository for Red Hat 7.3
%{!?rh7:#}rpm http://apt.sw.be redhat/7.3/en/i386 dag
#rpm-src http://apt.sw.be redhat/7.3/en/i386 dag

### Dag Apt Repository for Red Hat Enterprise Linux 2.1
%{!?el2:#}rpm http://apt.sw.be redhat/as2.1/en/i386 dag
#rpm-src http://apt.sw.be redhat/as2.1/en/i386 dag

### Dag Apt Repository for Red Hat 6.2
%{!?rh6:#}rpm http://apt.sw.be redhat/6.2/en/i386 dag
#rpm-src http://apt.sw.be redhat/6.2/en/i386 dag
EOF

%{__cat} <<EOF >os.list
### List of available apt repositories available from ayo.freshrpms.net.
### This file should contain an uncommented default suitable for your system.
###
### See http://ayo.freshrpms.net/ for a list of other repositories and mirrors.

### Red Hat Fedora Core 2
%{!?fc2:#}rpm http://ayo.freshrpms.net fedora/linux/2/i386 core updates
#rpm-src http://ayo.freshrpms.net fedora/linux/2/i386 core updates

### Red Hat Fedora Core 1
%{!?fc1:#}rpm http://ayo.freshrpms.net fedora/linux/1/i386 core updates
#rpm-src http://ayo.freshrpms.net fedora/linux/1/i386 core updates

### Red Hat Linux 9
%{!?rh9:#}rpm http://ayo.freshrpms.net redhat/9/i386 os updates
#rpm-src http://ayo.freshrpms.net redhat/9/i386 os updates

### Red Hat Linux 8.0
%{!?rh8:#}rpm http://ayo.freshrpms.net redhat/8.0/i386 os updates
#rpm-src http://ayo.freshrpms.net redhat/8.0/i386 os updates

### Red Hat Linux 7.3
%{!?rh7:#}rpm http://ayo.freshrpms.net redhat/7.3/i386 os updates
#rpm-src http://ayo.freshrpms.net redhat/7.3/i386 os updates

### Red Hat Linux 6.2
%{!?rh6:#}rpm http://ayo.freshrpms.net redhat/6.2/i386 os powertools updates
#rpm-src http://ayo.freshrpms.net redhat/6.2/i386 os powertools updates
EOF

%{__cat} <<EOF >freshrpms.list
### List of available apt repositories available from ayo.freshrpms.net.
### This file should contain an uncommented default suitable for your system.
###
### See http://ayo.freshrpms.net/ for a list of other repositories and mirrors.

### Red Hat Fedora Core 2
%{!?fc2:#}rpm http://ayo.freshrpms.net fedora/linux/2/i386 freshrpms
#rpm-src http://ayo.freshrpms.net fedora/linux/2/i386 freshrpms

### Red Hat Fedora Core 1
%{!?fc1:#}rpm http://ayo.freshrpms.net fedora/linux/1/i386 freshrpms
#rpm-src http://ayo.freshrpms.net fedora/linux/1/i386 freshrpms

### Red Hat Linux 9
%{!?rh9:#}rpm http://ayo.freshrpms.net redhat/9/i386 freshrpms
#rpm-src http://ayo.freshrpms.net redhat/9/i386 freshrpms

### Red Hat Linux 8.0
%{!?rh8:#}rpm http://ayo.freshrpms.net redhat/8.0/i386 freshrpms
#rpm-src http://ayo.freshrpms.net redhat/8.0/i386 freshrpms

### Red Hat Linux 7.3
%{!?rh7:#}rpm http://ayo.freshrpms.net redhat/7.3/i386 freshrpms
#rpm-src http://ayo.freshrpms.net redhat/7.3/i386 freshrpms

### Red Hat Linux 6.2
%{!?rh6:#}rpm http://ayo.freshrpms.net redhat/6.2/i386 freshrpms
#rpm-src http://ayo.freshrpms.net redhat/6.2/i386 freshrpms
EOF

%{__cat} <<EOF >newrpms.list
### See http://newrpms.sunsite.dk/ for more information.

### Red Hat Fedora Core 2
%{!?fc2:#}rpm http://newrpms.sunsite.dk/apt/ redhat/en/i386/fc2 newrpms
#rpm-src http://newrpms.sunsite.dk/apt/ redhat/en/i386/fc2 newrpms

### Red Hat Fedora Core 1
%{!?fc1:#}rpm http://newrpms.sunsite.dk/apt/ redhat/en/i386/fc1 newrpms
#rpm-src http://newrpms.sunsite.dk/apt/ redhat/en/i386/fc1 newrpms

### Red Hat Linux 9
%{!?rh9:#}rpm http://newrpms.sunsite.dk/apt/ redhat/en/i386/9.0 newrpms 
#rpm-src http://newrpms.sunsite.dk/apt/ redhat/en/i386/9.0 newrpms 

### Red Hat Linux 8.0
%{!?rh8:#}rpm http://newrpms.sunsite.dk/apt/ redhat/en/i386/8.0 newrpms 
#rpm-src http://newrpms.sunsite.dk/apt/ redhat/en/i386/8.0 newrpms 
EOF

%{__cat} <<EOF >atrpms.list
### See http://atrpms.physik.fu-berlin.de/ for more information.
### Possible sections: at-stable, at-good, at-testing, at-bleeding

### Red Hat Fedora Core 2
#rpm http://apt.physik.fu-berlin.de fedora/2/en/i386 at-testing
#rpm-src http://apt.physik.fu-berlin.de fedora/2/en/i386 at-testing

### Red Hat Fedora Core 1
#rpm http://apt.physik.fu-berlin.de fedora/1/en/i386 at-testing
#rpm-src http://apt.physik.fu-berlin.de fedora/1/en/i386 at-testing

### Red Hat Linux 9
#rpm http://apt.physik.fu-berlin.de redhat/9/en/i386 at-testing
#rpm-src http://apt.physik.fu-berlin.de redhat/9/en/i386 at-testing

### Red Hat Linux 8.0
#rpm http://apt.physik.fu-berlin.de redhat/8.0/en/i386 at-testing
#rpm-src http://apt.physik.fu-berlin.de redhat/8.0/en/i386 at-testing

### Red Hat Linux 7.3
#rpm http://apt.physik.fu-berlin.de redhat/7.3/en/i386 at-testing
#rpm-src http://apt.physik.fu-berlin.de redhat/7.3/en/i386 at-testing
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
#{__autoconf}
%configure \
	--disable-dependency-tracking \
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
%{__install} -m0644 rpmpriorities apt.conf %{buildroot}%{_sysconfdir}/apt/
%{__install} -m0644 dag.list os.list freshrpms.list newrpms.list atrpms.list %{buildroot}%{_sysconfdir}/apt/sources.list.d/
touch %{buildroot}%{_sysconfdir}/apt/preferences \
	%{buildroot}%{_sysconfdir}/apt/vendors.list

#%{__ln_s} -f %{_libdir}libapt-pkg-libc6.3-5.so.0 %{buildroot}%{_libdir}libapt-pkg-libc6.3-5.so.%{LIBVER}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

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
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/apt/
%{_localstatedir}/cache/apt/
%{_localstatedir}/state/apt/

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/apt-pkg/
#exclude %{_libdir}/*.la

%changelog
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
