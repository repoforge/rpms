# $Id$
# Authority: matthias

%define real_name ndiswrapper

Summary: Kernel module to allow the use of NDIS drivers 
Name: dkms-ndiswrapper
Version: 1.54
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://ndiswrapper.sourceforge.net/

Source: http://downloads.sf.net/ndiswrapper/ndiswrapper-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i386 x86_64
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms
Provides: ndiswrapper = %{version}-%{release}

%description
This kernel module implements the Microsoft NDIS (Network Driver Interface
Specification) API within the linux kernel.  It allows the use of binary
drivers written to this specification to be run natively in the Linux kernel.

%prep
%setup -n %{real_name}-%{version}

%build
%{__make} -C utils CFLAGS="%{optflags} -I../driver"

%install
%{__rm} -rf %{buildroot}
%{__make} -C utils install DESTDIR="%{buildroot}"
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/ndiswrapper
%{__install} -Dp -m0644 ndiswrapper.8 %{buildroot}%{_mandir}/man8/ndiswrapper.8

%define dkms_name ndiswrapper
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a driver/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="make KERNEL_LOCATION=${kernel_source_dir}"
CLEAN[0]="make clean"
BUILT_MODULE_NAME[0]=ndiswrapper
DEST_MODULE_LOCATION[0]=/kernel/drivers/net/wireless/ndiswrapper
AUTOINSTALL="YES"
EOF

%clean
%{__rm} -rf %{buildroot}

%post
# Add to DKMS registry
dkms add -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
# Rebuild and make available for the currenty running kernel
dkms build -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
dkms install -m %{dkms_name} -v %{dkms_vers} %{?quiet} --force || :

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{dkms_vers} %{?quiet} --all || :

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL README
%doc %{_mandir}/man8/ndiswrapper.8*
%dir %{_sysconfdir}/ndiswrapper/
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
/sbin/loadndisdriver
%{_sbindir}/ndiswrapper
%{_sbindir}/ndiswrapper-buginfo

%changelog
* Sun Jan 25 2009 Dag Wieers <dag@wieers.com> - 1.54-1
- Updated to release 1.54.

* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 1.53-1
- Updated to release 1.53.

* Mon Oct 22 2007 Matthias Saou <http://freshrpms.net/> 1.48-1
- Update to 1.48.

* Mon Jun 25 2007 Matthias Saou <http://freshrpms.net/> 1.47-1
- Update to 1.47.

* Fri May 18 2007 Matthias Saou <http://freshrpms.net/> 1.44-1
- Update to 1.44.

* Wed Mar  7 2007 Matthias Saou <http://freshrpms.net/> 1.38-1
- Update to 1.38.

* Mon Feb 12 2007 Matthias Saou <http://freshrpms.net/> 1.37-1
- Update to 1.37.

* Wed Nov 29 2006 Matthias Saou <http://freshrpms.net/> 1.30-1
- Update to 1.30 and minor spec file cleanup.
- Remove noarch, since there is a binary in the package.
- Provides plain versionned "ndiswrapper" too.
- Include INSTALL file since it contains instructions on installing INF files.

* Sat Oct 28 2006 Jon Nettleton <http://freshrpms.net/> 1.27-1
- Initial RPM release.

