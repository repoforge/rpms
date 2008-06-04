# $Id$
# Authority: matthias
# ExclusiveDist: el4 el5
# Dist: nodist

Summary: Linux kernel module for FUSE (Filesystem in USErspace)
Name: dkms-fuse
Version: 2.7.3
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://fuse.sourceforge.net/
Source: http://dl.sf.net/fuse/fuse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms

%description
With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains the FUSE userspace tools to
mount a FUSE filesystem.

%prep
%setup -n fuse-%{version}

%build

%install
%{__rm} -rf %{buildroot}

%define dkms_name fuse
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a kernel/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="./configure --enable-kernel-module --with-kernel=${kernel_source_dir} && make"
BUILT_MODULE_NAME[0]=fuse
DEST_MODULE_LOCATION[0]=/kernel/drivers/fs/fuse
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
* Mon Jun 02 2008 Dag Wieers <dag@wieers.com> - 2.7.3-1
- Updated to release 2.7.3.

* Thu Feb 07 2008 Dag Wieers <dag@wieers.com> - 2.7.2-1
- Updated to release 2.7.2.

* Mon Aug 06 2007 Dag Wieers <dag@wieers.com> - 2.7.0-1
- Updated to release 2.7.0.

* Thu Feb 22 2007 Matthias Saou <http://freshrpms.net/> 2.6.3-1
- Initial RPM release.

