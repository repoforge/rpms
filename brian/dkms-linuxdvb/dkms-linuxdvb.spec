Summary: Linux DVB kernel drivers
Name: dkms-linuxdvb
Version: 0.5.14
Release: 2.bs%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://www.linuxtv.org/
Packager: Brian Schueler <brian.schueler@gmx.de>
Vendor: LinuxTV, http://www.linuxtv.org

Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms
Provides: linuxdvb = %{version}-%{release}

%description
linuxdvb is a set of linux DVB drivers from the official Linux TV project
for receiving TV streams from terristrial, satellite and cable DVB
(Digital Video Broadcast) equipment.



%prep
%setup


%build

%install
%{__rm} -rf %{buildroot}

%define dkms_name linuxdvb
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a linux-dvb %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="cd linux-dvb && make distclean && make && make install && /sbin/depmod -a"
CLEAN="cd linux-dvb && make distclean"
AUTOINSTALL=yes
BUILT_MODULE_NAME[0]="dvb-ttpci"
BUILT_MODULE_LOCATION[0]="linux-dvb/v4l"
DEST_MODULE_NAME[0]="dvb-ttpci"
DEST_MODULE_LOCATION[0]="/kernel/drivers/media/dvb/ttpci"
EOF

# Firmware installation
%{__mkdir_p} %{buildroot}/lib/firmware/
%{__cp} -a firmware/* %{buildroot}/lib/firmware/

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
/lib/firmware/


%changelog
* Wed Mar 12 2008 Brian Schueler 0.5.14-1
- Hauppauge HVR4000 tuner switch without reloading driver

* Mon Dec 10 2007 Brian Schueler 0.5.13-1
- Updated to 2.5.13
- Add support for Hauppauge HVR4000

* Sat Sep 29 2007 Brian Schueler 0.5.12-1
- Updated to 2.5.12

* Mon May  28 2007 Brian Schueler 0.5.11-1
- Initial RPM release.

