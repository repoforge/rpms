
Summary: Driver for D-Link DFE-580TX 4-Port Ethernet controllers
Name: dkms-sundance
Version: 0.1
Release: 0.bs%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.d-link.de/
Packager: Brian Schueler <brian.schueler@gmx.de>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

#Source: ftp://ftp.dlink.de/dfe/dfe-580tx/driver_software/DFE-580tx_drv_revALL_linux24_ALL_en_021107.zip
Source: sundance-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc
Requires(post): dkms
Requires(preun): dkms

%description
Driver (Linux kernel module) for D-Link DFE-580TX 4-Port Ethernet controllers.


%prep
%setup -n sundance-%{version}


%build


%install
%{__rm} -rf %{buildroot}

%define dkms_name sundance
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a 2.[46] Makefile %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
MAKE[0]="make dkms"
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
BUILT_MODULE_NAME[0]=%{dkms_name}
BUILT_MODULE_LOCATION[0]=build
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
%doc README
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Wed Aug 15 2007 Brian Schueler <brian.schueler@gmx.de> 0.0.1 
- Initial RPM release.

