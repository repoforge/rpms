# $Id$
# Authority: matthias

# ExclusiveDist: el4

%define date 20070508

Summary: Generic Softwares Package for Camera Adapters kernel module
Name: dkms-gspca
Version: 1.0.18
Release: 1%{?dist}
License: GPL
Group: System Environment/Kernel
URL: http://mxhaard.free.fr/
Source: http://mxhaard.free.fr/spca50x/Download/gspcav1-%{date}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms

%description
Generic Softwares Package for Camera Adapters. Kernel modules which supports
a wide variety of USB webcams.


%prep
%setup -n gspcav1-%{date}
# Remove useless executable bit from header and source files
find . -name '*.h' -exec chmod -x {} \;
find . -name '*.c' -exec chmod -x {} \;


%build


%install
%{__rm} -rf %{buildroot}

%define dkms_name gspca
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a * %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
BUILT_MODULE_NAME[0]=gspca
DEST_MODULE_LOCATION[0]=/kernel/drivers/usb/media
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
%doc changelog
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Fri May 18 2007 Matthias Saou <http://freshrpms.net/> 1.0.18-1
- Update to 1.0.18.

* Wed Jan 24 2007 Matthias Saou <http://freshrpms.net/> 1.0.12-1
- Minor spec file cleanup.
- Name dkms-gspca to make transition to the future v4l2 module easier.
- Use a more usual type of version (1.0.12 vs. 01.00.12).

* Mon Jan 12 2007 Jon Nettleton <http://freshrpms.net/> 01.00.12-1
- Updated codebase to the newest release

* Mon Jan 08 2007 Jon Nettleton <http://freshrpms.net/> 01.00.10-1
- Initial RPM release.

