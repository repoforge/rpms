%define module_name qc-usb
%define version 0.6.6

Name:		dkms-%{module_name}
Version:	%version
Release:	1.bs
Summary:	DKMS-ready driver for the QuickCam-compatible USB web cameras
License:	GPL
Source:		http://qce-ga.sourceforge.net/%{module_name}-%{version}.tar.gz
Group:		Development/Kernel
Requires(pre):	dkms
Requires(post): dkms
Buildroot:	%{_tmppath}/%{name}-%{version}-root
Buildarch:	noarch
Obsoletes:	%{module_name}-dkms
Provides:	%{module_name}-dkms

%description
This package contains a DKMS-ready linux driver for the QuickCam Express
and other QuickCam-related and QuickCam-compatible USB web cameras.

The qc-usb driver is known to work with the following webcams:

    * Dexxa Webcam
    * Labtec Webcam (old model)
    * LegoCam
    * Logitech QuickCam Express (old model)
    * Logitech QuickCam Notebook (some models)
    * Logitech QuickCam Web

Generally, any USB camera with a USB vendor ID of 0x46d and a USB product ID of
0x840, 0x850, or 0x870 (so, 0x46d:0x840, for example), should work. You can see
the USB ID using operating system utilities such as lsusb in Linux.

%prep
%setup -q -c -n %{module_name}-%{version}
chmod -R go=u-w .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/src/
cp -rf * %{buildroot}/usr/src/%{module_name}-%{version}-%{release}
cat > %{buildroot}/usr/src/%{module_name}-%{version}-%{release}/dkms.conf <<EOF

PACKAGE_VERSION="%{version}-%{release}"

# Items below here should not have to change with each driver version
PACKAGE_NAME="%{module_name}"
MAKE[0]="make quickcam.ko"
CLEAN="make clean"
BUILT_MODULE_NAME[0]="quickcam"
DEST_MODULE_LOCATION[0]="/kernel/3rdparty/qc-usb/"
DEST_MODULE_NAME[0]="quickcam"
AUTOINSTALL=yes
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
/usr/src/%{module_name}-%{version}-%{release}

%changelog
* Thu Nov 15 2007 Brian Schueler <brian.schueler@gmx.de> rebuild for RHEL5/FC6
* Tue Apr 17 2007 ocilent1 <ocilent1 at gmail dot com> 0.6.6-1pclos2007
- Build for PCLinuxOS 2007

