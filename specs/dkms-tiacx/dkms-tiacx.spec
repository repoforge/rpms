# $Id$
# Authority: matthias
# Dist: nodist

Summary: Driver for Texas Instruments' ACX100/ACX111 wireless network chips
Name: dkms-tiacx
Version: 0.4.7
Release: 5.20070101%{?dist}
License: GPLv2 or MPLv1.1
Group: System Environment/Kernel
URL: http://www.kernel.org/pub/linux/kernel/people/akpm/
Source: http://www.cmartin.tk/acx/acx-20070101.tar.bz2
Patch0: acx-20070101-macraw.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc
Requires: acx100-firmware, acx111-firmware
Requires(post): dkms
Requires(preun): dkms

%description
Driver (Linux kernel module) for network interface cards based on Texas
Instruments' ACX100/ACX111 wireless network chips.


%prep
%setup -n acx-20070101
%patch0 -p1
# All files are u-w :-(
%{__chmod} -R u+w .


%build


%install
%{__rm} -rf %{buildroot}

%define dkms_name tiacx
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a * %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="make -C ${kernel_source_dir} M=${dkms_tree}/%{dkms_name}/%{dkms_vers}/build"
CLEAN[0]="make -C ${kernel_source_dir} M=${dkms_tree}/%{dkms_name}/%{dkms_vers}/build clean"
BUILT_MODULE_NAME[0]=acx
DEST_MODULE_LOCATION[0]=/kernel/drivers/net/wireless
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
%defattr(-,root,root,-)
%doc Changelog README
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 0.4.7-5.20070101
- Switch back to the acx100.sf.net source acx-20070101 since tiacx seems to
  have vanished from mm and wireless-2.6 kernel patches (legal reasons?).
- Patch out the "mac.raw" which produces a build error with recent kernels.

* Sat Oct 28 2006 Matthias Saou <http://freshrpms.net/> 0.4.7-4
- Switch to the sources found in the 2.6.18-mm3 kernel since the others
  always made my test machine freeze, but these work.

* Tue Oct 10 2006 Matthias Saou <http://freshrpms.net/> 0.4.7-3
- Add the rpm release to the dkms module version, to make updating the module
  to a fixed same version work (--rpm_safe_upgrade doesn't work as advertised).
- Force modules install so that the same version can be overwritten instead of
  uninstalled by the old package's %%preun when updating.
- Add build time quiet flag for the scriplets. Undefine to do verbose testing.

* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 0.4.7-2
- Further patch Makefile to simplify the dkms.conf entries.

* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 0.4.7-1
- Initial RPM release.

