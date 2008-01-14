# $Id$
# Authority: matthias
# Dist: nodist

Summary: Driver for RTL8111/8168B PCI Express Gigabit Ethernet controllers
Name: dkms-r1000
Version: 1.06
Release: 2
License: GPL+
Group: System Environment/Kernel
URL: http://www.realtek.com.tw/
Source: ftp://61.56.86.122/cn/nic/r1000_v%{version}.tgz
Patch0: r1000_v1.05-pci_register_driver.patch
Patch1: r1000_v1.06-modversions.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms

%description
Driver (Linux kernel module) for RTL8111/8168B PCI Express Gigabit Ethernet
controllers.


%prep
%setup -n r1000_v%{version}
%patch0 -p1 -b .pci_register_driver
%patch1 -p1 -b .modversions


%build


%install
%{__rm} -rf %{buildroot}

%define dkms_name r1000
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a src/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="make KVER=${kernelver}"
CLEAN[0]="make clean"
BUILT_MODULE_NAME[0]=%{dkms_name}
DEST_MODULE_LOCATION[0]=/kernel/drivers/net
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
%defattr(-,root,root,-)
%doc release_note.txt README
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Mon Jan 14 2007 Matthias Saou <http://freshrpms.net/> 1.06-2
- Add missing make requirement.

* Mon Oct 22 2007 Matthias Saou <http://freshrpms.net/> 1.06-1
- Update to 1.06 (the upstream 1.07 tarball is completely busted!).
- Include patch s/pci_module_init/pci_register_driver/ for recent kernels.

* Wed Dec  6 2006 Ugo Viti <http://www.initzero.it> 1.05-1
- Updated to 1.05 release.

* Mon Nov 13 2006 Ugo Viti <http://www.initzero.it> 1.04-1
- Initial RPM release.

