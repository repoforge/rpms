# Authority: dag
# Archs: i686 i586 i386 athlon
# Distcc: 0
# Soapbox: 0

%define _sbindir /sbin
%define _libmoddir /lib/modules

%{!?kernel:%define kernel %(rpm -q kernel-source --qf '%{RPMTAG_VERSION}-%{RPMTAG_RELEASE}' | tail -1)}

%define kversion %(echo "%{kernel}" | sed -e 's|-.*||')
%define krelease %(echo "%{kernel}" | sed -e 's|.*-||')

%define moduledir /fs/opengfs
%define modules ogfs.o memexp.o

Summary: OpenGFS clustered filesystem.
Name: opengfs
Version: 0.2.1
Release: 0
License: GPL
Group: System Environment/Utilities
URL: http://opengfs.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/opengfs/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: kernel-source

%description
Utilities for managing OpenGFS filesystems and daemons for running them.

%package -n kernel-module-opengfs
Summary: Linux OpenGFS clustered filesystem drivers.
Group: System Environment/Kernel

Requires: kernel = %{kversion}-%{krelease}
Obsoletes: opengfs-modules
Provides: opengfs-modules
Provides: kernel-modules

%description -n kernel-module-opengfs
Linux OpenGFS clustered filesystem drivers.

These drivers are built for kernel %{kversion}-%{krelease}.
They might work with newer/older kernels.

%package -n kernel-smp-module-opengfs
Summary: Linux OpenGFS clustered filesystem drivers.
Group: System Environment/Kernel

Requires: kernel = %{kversion}-%{krelease}
Obsoletes: opengfs-modules
Provides: opengfs-modules
Provides: kernel-modules

%description -n kernel-smp-module-opengfs
Linux Linmodem drivers for SMP.

These drivers are built for kernel %{kversion}-%{krelease}smp.
They might work with newer/older kernels.

%prep
%setup

%build
%{__rm} -rf %{buildroot}
echo -e "\nDriver version: %{version}\nKernel version: %{kversion}-%{krelease}\n"

### Prepare UP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__perl} -pi -e 's|%{krelease}custom|%{krelease}|' Makefile
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}.config .config
%{__make} -s symlinks oldconfig dep
cd -

### Make UP module.
%configure \
	--disable-dependency-tracking \
	--with-linux_srcdir="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	--with-linux_moduledir="%{buildroot}%{_libmoddir}/%{kversion}-%{krelease}"
%{__make} %{?_smp_mflags} all
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}
cd -

### Prepare SMP kernel.
cd %{_usrsrc}/linux-%{kversion}-%{krelease}
%{__make} -s distclean
%{__cp} -f configs/kernel-%{kversion}-%{_target_cpu}-smp.config .config
%{__make} -s symlinks oldconfig dep
cd -

### Make SMP module.
%configure \
	--disable-dependency-tracking \
	--with-linux_srcdir="%{_libmoddir}/%{kversion}-%{krelease}/build" \
	--with-linux_moduledir="%{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp"
%{__make} %{?_smp_mflags} all
%{__install} -d -m0755 %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}
%{__install} -m0644 %{modules} %{buildroot}%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}

%install
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS POLICY README TODO
%doc %{_mandir}/man?/*
%{_sbindir}/*

%files -n kernel-module-opengfs
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}%{moduledir}/

%files -n kernel-smp-module-opengfs
%defattr(-, root, root, 0755)
%{_libmoddir}/%{kversion}-%{krelease}smp%{moduledir}/

%changelog
* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Initial package. (using DAR)
