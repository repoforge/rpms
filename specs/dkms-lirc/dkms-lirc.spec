# $Id$
# Authority: matthias
# Dist: nodist

# We disable lirc_gpio (build fails) and lirc_parallel (not SMP safe)
%define modules lirc_atiusb lirc_bt829 lirc_cmdir lirc_dev lirc_i2c lirc_igorplugusb lirc_imon lirc_it87 lirc_mceusb lirc_mceusb2 lirc_sasem lirc_serial lirc_sir lirc_streamzap

Summary: Drivers for lirc supported hardware
Name: dkms-lirc
Version: 0.8.2
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.lirc.org/
Source: http://dl.sf.net/lirc/lirc-%{version}.tar.bz2
Patch0: lirc-0.8.2-alldrivers.patch
Patch1: lirc-0.8.2-2.6.23-unregister_chrdev-void.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc, make, lirc
Requires(post): dkms
Requires(preun): dkms
BuildRequires: autoconf, gcc-c++
# Kind of bogus since it's the configure check that requires it
BuildRequires: kernel, kernel-devel

%description
Drivers (Linux kernel modules) for various infrared remote controls and
receivers supported by lirc.


%prep
%setup -n lirc-%{version}
%patch0 -p1 -b .alldrivers
%patch1 -p1 -b .2.6.23-unregister_chrdev-void


%build
# We patched configure.in to remove some drivers
autoconf
# Get the most recent kernel's build path. Just as bogus as the buildreq...
%configure \
    --with-kerneldir=`ls -1 -d /lib/modules/*/build | tail -1` \
    --with-driver=all


%install
%{__rm} -rf %{buildroot}

%define dkms_name lirc
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a drivers/ config.h config.status configure.in \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="make -C drivers KERNEL_LOCATION=${kernel_source_dir}"
CLEAN[0]="make -C drivers clean"
EOF
# Here we loop since all the many drivers are in their own directory
i=0; for module in %{modules}; do
%{__cat} >> %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << EOF
BUILT_MODULE_NAME[${i}]=${module}
BUILT_MODULE_LOCATION[${i}]=drivers/${module}
DEST_MODULE_LOCATION[${i}]=/kernel/drivers/input/lirc
EOF
(( i++ ))
done
# And the last line of the file, to keep the "usual" order
%{__cat} >> %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << EOF
AUTOINSTALL="YES"
EOF

# Clean up... makes module builds fail
#find %{buildroot} -name .deps | xargs %{__rm} -rf


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
%defattr(-,root,root,-)
%doc COPYING
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Mon Oct 22 2007 Matthias Saou <http://freshrpms.net/> 0.8.2-1
- Update to 0.8.2 (patch from Miroslav Lichvar).
- Include patch to fix compilation with 2.6.23+ kernels.

* Mon Jan  8 2007 Matthias Saou <http://freshrpms.net/> 0.8.1-1
- Update to 0.8.1 final.

* Wed Oct 18 2006 Matthias Saou <http://freshrpms.net/> 0.8.1-0.1.pre2
- Initial RPM release.

