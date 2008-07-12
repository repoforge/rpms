%define module_name thor-nonraid
%define version 0.0.0.5

Name:		dkms-%{module_name}
Version:	%version
Release:	1.omb
Summary:	DKMS-ready driver for Marvell S-ATA Thor non-RAID Controller 
License:	GPL
Source:         %{module_name}-%{version}.tar.gz
Patch0:		thor-nonraid-makefile_kernelrelease.patch
Group:		Development/Kernel
Requires(pre):	dkms
Requires(post): dkms
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-root
Obsoletes:	%{module_name}-dkms
Provides:	%{module_name}-dkms

%description
This driver kit contains Linux drivers for the Marvell S-ATA Thor non-RAID Controller.

%prep
%setup -q -n %{module_name}-%{version}
%patch0 -p1


%build
# empty. dkms makes and installs

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_usrsrc}/%{module_name}-%{version}-%{release}
cp -rf * %{buildroot}/usr/src/%{module_name}-%{version}-%{release}
%{__cat} > %{buildroot}%{_usrsrc}/%{module_name}-%{version}-%{release}/dkms.conf << 'EOF'
# Items below here should not have to change with each driver version
PACKAGE_NAME="%{module_name}"
PACKAGE_VERSION="%{version}-%{release}"
CLEAN="make clean"
MAKE[0]="make"
BUILT_MODULE_LOCATION[0]=.		# location of driver
BUILT_MODULE_NAME[0]=mv61xx
DEST_MODULE_LOCATION[0]=/kernel/drivers/ata
AUTOINSTALL="YES"
EOF

%post
  dkms add -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade
  dkms build -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade
  dkms install -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade

%preun
  dkms remove -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade --all
	
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_usrsrc}/%{module_name}-%{version}-%{release}

%changelog
* Sat Jul 12 2008 omb
initial version
