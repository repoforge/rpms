# $Id$
# Authority: matthias
# Dist: nodist

%define fromkernel 2.6.22.1

Summary: Driver for reading and writing on NTFS formatted volumes
Name: dkms-ntfs
Version: 2.1.28
Release: 2%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.linux-ntfs.org/
# Created after extracting linux kernel sources and running:
# tar cjvf ntfs-%{version}-from-%{fromkernel}.tar.bz2 \
# Documentation/filesystems/ntfs.txt COPYING fs/ntfs/
Source: ntfs-%{version}-from-%{fromkernel}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms

%description
Driver (Linux kernel module) for reading and writing on NTFS formatted volumes.


%prep
%setup -c
# Move the file to not have it mixed with the sources but included as %doc
%{__mv} fs/ntfs/ChangeLog .


%build


%install
%{__rm} -rf %{buildroot}

%define dkms_name ntfs
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a fs/ntfs/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="make -C ${kernel_source_dir} M=${dkms_tree}/%{dkms_name}/%{dkms_vers}/build CONFIG_NTFS_FS=m CONFIG_NTFS_RW=y"
CLEAN[0]="make -C ${kernel_source_dir} M=${dkms_tree}/%{dkms_name}/%{dkms_vers}/build clean"
BUILT_MODULE_NAME[0]=ntfs
DEST_MODULE_LOCATION[0]=/kernel/fs/ntfs
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
%doc ChangeLog COPYING Documentation/filesystems/ntfs.txt
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Mon Jul 23 2007 Matthias Saou <http://freshrpms.net/> 2.1.28-2
- Update with module source from 2.6.22.1 to fix build on recent F7 kernels.

* Mon Mar 26 2007 Matthias Saou <http://freshrpms.net/> 2.1.28-1
- Update with module source from 2.6.20.4 to fix build on recent FC6 kernels.

* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 2.1.27-2
- Update with module source from 2.6.19.1 to fix build on recent FC6 kernels.
- Remove now included noblksize patch.

* Fri Oct 20 2006 Matthias Saou <http://freshrpms.net/> 2.1.27-1
- Initial RPM release.
- Create source the same way as the rpm.livna.org package does.
- Fix build with noblksize patch made from an undocumented change in the
  rpm.livna.org package's (not so) pristine sources.

