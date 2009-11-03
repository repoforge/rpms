# $Id$
# Authority: dag
# Dist: nodist

%define real_name ivtv

Summary: iTVC15/16 and CX23415/16 driver
Name: dkms-ivtv
Version: 0.10.6
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://ivtvdriver.org/

Source: http://dl.ivtvdriver.org/ivtv/archive/0.10.x/ivtv-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: gcc, make, dkms, ivtv
Requires: ivtv-firmware-dec >= 2.02.023
Requires: ivtv-firmware-enc >= 2.04.024
Requires: ivtv-firmware-audio

%description
iTVC15/16 and CX23415/16 driver.

%prep
%setup -n %{real_name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}

%define dkms_name ivtv
%define dkms_vers %{version}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a driver/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} <<'EOF' >%{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="src=/usr/src/${PACKAGE_NAME}-${PACKAGE_VERSION}/ ; make"
CLEAN="make clean"

BUILT_MODULE_NAME[0]="ivtv"
BUILT_MODULE_NAME[1]="ivtv-fb"
#BUILT_MODULE_NAME[2]="saa7127"
#BUILT_MODULE_NAME[3]="tveeprom"
#BUILT_MODULE_NAME[4]="msp3400"
#BUILT_MODULE_NAME[5]="saa7115"

DEST_MODULE_LOCATION[0]="/kernel/drivers/media/video/ivtv"
DEST_MODULE_LOCATION[1]="/kernel/drivers/media/video/ivtv"
#DEST_MODULE_LOCATION[2]="/kernel/drivers/media/video/ivtv"
#DEST_MODULE_LOCATION[3]="/kernel/drivers/media/video/ivtv"
#DEST_MODULE_LOCATION[4]="/kernel/drivers/media/video/ivtv"
#DEST_MODULE_LOCATION[5]="/kernel/drivers/media/video/ivtv"
AUTOINSTALL=yes
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
%doc ChangeLog* COPYING README* doc/*
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

%changelog
* Sun Jun 15 2008 Dag Wieers <dag@wieers.com> - 0.10.6-1
- Initial package. (using DAR)
