# $Id$
# Authority: dag

# Dist: nodist

%define real_name rtl818x
%define real_version 1.0.1-b

Summary: Driver for RTL8180, SA2400/GRF5101/MAX2820, RTL8185/RTL8187 and RTL8225 Wireless cards
Name: dkms-rtl818x
Version: 1.0.1b
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://www.realtek.com.tw/

Source: http://dl.sf.net/rtl818x/rtl818x-%{real_version}.tar.gz
Patch0: rtl818x-cvs20080525-modversions.patch
Patch1: rtl818x-cvs20080525-module_param.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms

%description
Driver for RTL8180, SA2400/GRF5101/MAX2820, RTL8185/RTL8187 and RTL8225
Wireless cards.

%prep
%setup -n %{real_name}-%{real_version}
#patch0 -p0
#patch1 -p0

%build

%install
%{__rm} -rf %{buildroot}

%define dkms_name rtl818x
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a * %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} <<'EOF' >%{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
CLEAN="make clean"
MAKE="make modules"
AUTOINSTALL="YES"

BUILT_MODULE_NAME[0]="rtl818x"
BUILT_MODULE_LOCATION[0]="drivers/net/wireless/rtl818x/"
DEST_MODULE_LOCATION[0]="/kernel/drivers/net/wireless/"

BUILT_MODULE_NAME[1]="ieee80211-rtl"
BUILT_MODULE_LOCATION[1]="net/ieee80211/"
DEST_MODULE_LOCATION[1]="/kernel/net/ieee80211/"

BUILT_MODULE_NAME[2]="ieee80211_crypt-rtl"
BUILT_MODULE_LOCATION[2]="net/ieee80211/"
DEST_MODULE_LOCATION[2]="/kernel/net/ieee80211/"

BUILT_MODULE_NAME[3]="ieee80211_crypt_ccmp-rtl"
BUILT_MODULE_LOCATION[3]="net/ieee80211/"
DEST_MODULE_LOCATION[3]="/kernel/net/ieee80211/"

BUILT_MODULE_NAME[4]="ieee80211_crypt_tkip-rtl"
BUILT_MODULE_LOCATION[4]="net/ieee80211/"
DEST_MODULE_LOCATION[4]="/kernel/net/ieee80211/"

BUILT_MODULE_NAME[5]="ieee80211_crypt_wep-rtl"
BUILT_MODULE_LOCATION[5]="net/ieee80211/"
DEST_MODULE_LOCATION[5]="/kernel/net/ieee80211/"
EOF

%clean
%{__rm} -rf %{buildroot}

%post
### Add to DKMS registry
dkms add -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
### Rebuild and make available for the currenty running kernel
dkms build -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
dkms install -m %{dkms_name} -v %{dkms_vers} %{?quiet} --force || :

%preun
### Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{dkms_vers} %{?quiet} --all || :

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYRIGHT DOWNLOAD INSTALL LICENSE README*
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

%changelog
* Sun May 25 2008 Dag Wieers <dag@wieers.com> - 1.0.1b-1
- Updated package. (using DAR)
