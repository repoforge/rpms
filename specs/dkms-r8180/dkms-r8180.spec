# $Id$
# Authority: dag

# Dist: nodist

%define real_name rtl8180

Summary: Driver for RTL8180 and SA2400 Wireless cards
Name: dkms-r8180
Version: 0.21
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.realtek.com.tw/

Source: http://dl.sf.net/rtl8180-sa2400/rtl8180-%{version}.tar.gz
Patch0: rtl8180-0.21-modversions.patch
Patch1: rtl8180-0.21-module_param.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms

%description
Driver for RTL8180 and SA2400 Wireless cards.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p0
%patch1 -p0

%build

%install
%{__rm} -rf %{buildroot}

%define dkms_name r8180
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a * %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} <<'EOF' >%{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf
BUILT_MODULE_NAME=%{dkms_name}
DEST_MODULE_LOCATION=/kernel/drivers/net/wireless
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
AUTOINSTALL="YES"
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
%doc AUTHORS CHANGES COPYING INSTALL LICENSE README*
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

%changelog
* Sun May 25 2008 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated package. (using DAR)
