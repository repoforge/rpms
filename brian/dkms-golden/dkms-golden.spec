%define module_name golden
%define version 1.08

Name:		dkms-%{module_name}
Version:	%version
Release:	1.omb%{?dist}
Summary:	DKMS-ready driver for SUNIX Serial Universal PCI 4037T
License:	GPL
Source:         %{module_name}-%{version}.tar.gz
Group:		Development/Kernel
Requires(pre):	dkms
Requires(post): dkms
BuildRequires:	ncurses-devel
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-root
Obsoletes:	%{module_name}-dkms
Provides:	%{module_name}-dkms

%description
This driver kit contains Linux drivers for the SUNIX Golden I/O Serial
Universal PCI Card 4037T.

%prep
%setup -q -n %{module_name}-%{version}


%build
# empty. dkms makes and installs

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_usrsrc}/%{module_name}-%{version}-%{release}
cp -rf * %{buildroot}/usr/src/%{module_name}-%{version}-%{release}
make clean
%{__cat} > %{buildroot}%{_usrsrc}/%{module_name}-%{version}-%{release}/dkms.conf << 'EOF'
# Items below here should not have to change with each driver version
PACKAGE_NAME="%{module_name}"
PACKAGE_VERSION="%{version}-%{release}"
CLEAN="make clean"
MAKE[0]="make"
BUILT_MODULE_LOCATION[0]=driver		# location of driver
BUILT_MODULE_NAME[0]=snx_golden
DEST_MODULE_LOCATION[0]=/kernel/drivers/char
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
* Sat May  24 2008 omb
initial version
