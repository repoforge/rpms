# $Id$
# Authority: dag

# Dist: nodist

%define real_name l1-linux

Summary: Driver for Attansic L1 Gigabit Ethernet controllers
Name: dkms-atl1
Version: 1.2.40.2
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Kernel
URL: http://atl1.sourceforge.net/

Source: ftp://hogchain.net/pub/linux/attansic/vendor_driver/l1-linux-v%{version}.tar.gz
Patch: atl1-1.2.40.2-irqreturn_t.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: gcc, make, dkms

%description
Driver (Linux kernel module) for Attansic L1 Gigabit Ethernet controllers.

%prep
%setup -n %{real_name}-v%{version}
%patch0 -p1 -b .kconfig

%build

%install
%{__rm} -rf %{buildroot}

%define dkms_name atl1
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a src/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__install} -Dp -m0644 atl1.7 %{buildroot}%{_mandir}/man7/atl1.7

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
%defattr(-,root,root, 0755)
%doc copying readme release_note.txt
%doc %{_mandir}/man7/atl1.7*
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

%changelog
* Mon Feb 06 2008 manuel "lonely wolf" wolfshant <wolfy@fedoraproject.org> - 1.2.40.2-1
- Initial RPM version.
