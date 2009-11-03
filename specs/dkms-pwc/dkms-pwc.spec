# $Id$
# Authority: matthias
# Dist: nodist

%define date 20061018
%define time 042701

Summary: Driver for Philips USB webcams
Name: dkms-pwc
Version: 10.0.11
Release: 1.%{date}%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://saillard.org/linux/pwc/
Source: http://saillard.org/linux/pwc/snapshots/pwc-v4l2-%{date}-%{time}.tar.bz2
Patch0: pwc-v4l2-20061018-042701-no-config.h.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc
Requires(post): dkms
Requires(preun): dkms

%description
Free Philips USB Webcam driver for Linux that supports VGA resolution,
newer kernels and replaces the old pwcx module.


%prep
%setup -n pwc-v4l2-%{date}-%{time}
%patch0 -p1 -b .no-config.h


%build


%install
%{__rm} -rf %{buildroot}

%define dkms_name pwc
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a * %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
BUILT_MODULE_NAME[0]=pwc
DEST_MODULE_LOCATION[0]=/kernel/drivers/media/video/pwc
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
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Thu Oct 19 2006 Matthias Saou <http://freshrpms.net/> 10.0.11-1.20061018
- Initial RPM release.

