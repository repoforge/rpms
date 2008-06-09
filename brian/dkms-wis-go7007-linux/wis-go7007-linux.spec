%define module_name wis-go7007-linux
%define version 0.9.8

Name:		dkms-%{module_name}
Version:	%version
Release:	1.bs%{?dist}
Summary:	DKMS-ready driver for WIS go7007 frame grabbers
License:	GPL
Source:		http://oss.wischip.com/%{module_name}-%{version}.tar.bz2
Patch0:		wis-go7007-linux-0.9.8-makefile.patch
Patch1:		http://bart.ulyssis.org/go7007-update.patch
Patch2:		wis-go7007_0.9.8_2.6.21.patch
Group:		Development/Kernel
Requires(pre):	dkms
Requires(post): dkms
#BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-root
Obsoletes:	%{module_name}-dkms
Provides:	%{module_name}-dkms

%description
This driver kit contains Linux drivers for the WIS GO7007SB multi-format
video encoder.  Only kernel version 2.6.x is supported.  The video stream
is available through the Video4Linux2 API and the audio stream is available
through the ALSA API (or the OSS emulation layer of the ALSA system).

%prep
%setup -q -n %{module_name}-%{version}
#%patch1 -p1
%patch0 -p1
%patch2 -p1
# too late in the game
#perl -pi -e's,(-I\$\(shell pwd\)),-I%{_includedir}/v4l -I%{_includedir}/alsa-driver -H $1,' kernel/Makefile
perl -pi -e's,(-I\$\(shell pwd\)),-H $1,' kernel/Makefile


%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_usrsrc}/%{module_name}-%{version}-%{release}
mkdir -p %{buildroot}/lib/firmware
mkdir -p %{buildroot}/usr/bin
cp -rvi firmware/* %{buildroot}/lib/firmware
cp -rvi apps/gorecord apps/modet %{buildroot}/usr/bin/
cp -rf * %{buildroot}/usr/src/%{module_name}-%{version}-%{release}
make clean
%{__cat} > %{buildroot}%{_usrsrc}/%{module_name}-%{version}-%{release}/dkms.conf << 'EOF'
# Items below here should not have to change with each driver version
PACKAGE_NAME="%{module_name}"
PACKAGE_VERSION="%{version}-%{release}"
CLEAN="make clean"
MAKE[0]="make KERNELSRC=${kernel_source_dir}"
BUILT_MODULE_LOCATION[0]=kernel
BUILT_MODULE_LOCATION[1]=kernel
BUILT_MODULE_LOCATION[2]=kernel
BUILT_MODULE_LOCATION[3]=kernel
BUILT_MODULE_LOCATION[4]=kernel
BUILT_MODULE_LOCATION[5]=kernel
BUILT_MODULE_LOCATION[6]=kernel
BUILT_MODULE_LOCATION[7]=kernel
BUILT_MODULE_LOCATION[8]=kernel
BUILT_MODULE_LOCATION[9]=kernel
BUILT_MODULE_NAME[0]=go7007
BUILT_MODULE_NAME[1]=wis-saa7113
BUILT_MODULE_NAME[2]=wis-tw9903
BUILT_MODULE_NAME[3]=go7007-usb
BUILT_MODULE_NAME[4]=wis-saa7115
BUILT_MODULE_NAME[5]=wis-uda1342
BUILT_MODULE_NAME[6]=snd-go7007
BUILT_MODULE_NAME[7]=wis-sony-tuner
BUILT_MODULE_NAME[8]=wis-ov7640
BUILT_MODULE_NAME[9]=wis-tw2804
DEST_MODULE_LOCATION[0]=/kernel/extra
DEST_MODULE_LOCATION[1]=/kernel/extra
DEST_MODULE_LOCATION[2]=/kernel/extra
DEST_MODULE_LOCATION[3]=/kernel/extra
DEST_MODULE_LOCATION[4]=/kernel/extra
DEST_MODULE_LOCATION[5]=/kernel/extra
DEST_MODULE_LOCATION[6]=/kernel/extra
DEST_MODULE_LOCATION[7]=/kernel/extra
DEST_MODULE_LOCATION[8]=/kernel/extra
DEST_MODULE_LOCATION[9]=/kernel/extra
AUTOINSTALL="YES"
EOF

%post
  dkms add -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade
  dkms build -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade
  dkms install -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade

%preun
  dkms remove -m %{module_name} -v %{version}-%{release} --rpm_safe_upgrade --all
	
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_usrsrc}/%{module_name}-%{version}-%{release}
/lib/firmware
%{_bindir}

%changelog
* Fri May  2 2008 Brian Schueler <brian.schueler@gmx.de>
initial version

