# $Id$
# Authority: dag

# Dist: nodist

%define real_name r8168

Summary: Driver for RTL8111/8168B PCI Express Gigabit Ethernet controllers
Name: dkms-r8168
Version: 8.004.00
Release: 1
License: GPL+
Group: System Environment/Kernel
URL: http://www.realtek.com.tw/

Source: ftp://202.65.194.212/cn/nic/r8168-%{version}.tar.bz2
Patch1: r8168-8.004.00-modversions.patch
Patch2: r8168-8.004.00-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms

%description
Driver (Linux kernel module) for RTL8111/8168B PCI Express Gigabit Ethernet
controllers.

%prep
%setup -n %{real_name}-%{version}
%patch1 -p1 -b .modversions
%patch2 -p1 -b .makefile

%build

%install
%{__rm} -rf %{buildroot}

%define dkms_name r8168
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a src/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} <<'EOF' >%{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf
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
%defattr(-, root, root, 0755)
%doc readme release_note.txt
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

%changelog
* Mon Feb 06 2008 Manuel "lonely wolf" Wolfshant <wolfy@fedoraproject.org> - 8.004.00-1
- Initial rpm version. Shamelessly copy from dkms-r1000 by Matthias Saou
