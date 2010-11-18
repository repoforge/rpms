# $Id$
# Authority: matthias

# ExclusiveDist: el4

Summary: QEMU accelerator kernel module
Name: dkms-kqemu
%define real_version 1.4.0pre1
Version: 1.4.0
Release: 0.1.pre1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://fabrice.bellard.free.fr/qemu/

Source: http://www.nongnu.org/qemu/kqemu-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: dkms
Requires: make
Requires: gcc

%description
QEMU accelerator kernel module, a host driver to achieve near native
performances when using QEMU as a virtualizer.

%prep
%setup -n kqemu-%{real_version}

%build

%install
%{__rm} -rf %{buildroot}

%define dkms_name kqemu
%define dkms_vers %{real_version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a * %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="./configure --kernel-path=${kernel_source_dir} && make"
BUILT_MODULE_NAME[0]=kqemu
DEST_MODULE_LOCATION[0]=/kernel/drivers/misc
AUTOINSTALL="YES"
EOF

# Configuration for udev
%{__mkdir_p} %{buildroot}/etc/udev/rules.d
%{__cat} > %{buildroot}/etc/udev/rules.d/60-kqemu.rules << 'EOF'
KERNEL=="kqemu", NAME="%k", MODE="0666"
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
/etc/udev/rules.d/60-kqemu.rules
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

%changelog
* Sat May 02 2009 Dag Wieers <dag@wieers.com> - 1.4.0-0.1.pre1
- Updated to release 1.4.0pre1.

* Wed Jun 20 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-0.2.pre11
- Include udev configuration file to get the dev node created automatically.

* Thu Feb 15 2007 Dag Wieers <dag@wieers.com> - 1.3.0-0.1.pre11
- Updated to release 1.3.0pre11.

* Tue Feb  6 2007 Matthias Saou <http://freshrpms.net/> 1.3.0-0.1.pre10
- Initial RPM release.
