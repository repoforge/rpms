Summary: Nozomi 3G PCMCIA driver
Name: nozomi
Version: 2.2
Release: 1.bs%{?dist}
Epoch: 1
License: GPL
Group: System Environment/Kernel
Packager: Brian Schueler <brian.schueler@gmx.de>
URL: http://www.pharscape.org

Source0: http://unspecified/nozomi-%{version}.tar.gz
Source1: umts
Source2: wvdial-umts.conf
Source3: ifcfg-umts
Source4: umts-interface
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: dkms gcc make wvdial kernel-devel >= 2.6.9
BuildRequires(post): dkms gcc make
BuildRequires(preun): dkms gcc make

%description
This Package includes a driver for UMTS 3G PCMCIA cards sold by Option

%prep
%setup %{Source0}

%build

%install
%{__install} -D -m 0600 %{SOURCE1} %{buildroot}/%{_sysconfdir}/ppp/peers/umts
%{__install} -D -m 0600 %{SOURCE2} %{buildroot}/%{_sysconfdir}/wvdial-umts.conf
%{__install} -D -m 0755 %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig/network-scripts/ifcfg-umts
%{__install} -D -m 0755 %{SOURCE4} %{buildroot}/%{_sysconfdir}/rc.d/init.d/umts-interface


%define dkms_name nozomi
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a ../%{dkms_name}-%{version}/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
MAKE[0]="make clean && make"
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
BUILT_MODULE_NAME[0]=%{dkms_name}
BUILT_MODULE_LOCATION[0]=.
DEST_MODULE_LOCATION[0]=/kernel/drivers/net
AUTOINSTALL="YES"
EOF

### Clean up buildroot
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
%config(noreplace) %{_sysconfdir}/ppp/peers/umts
%config(noreplace) %{_sysconfdir}/wvdial-umts.conf
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{_sysconfdir}/sysconfig/network-scripts/ifcfg-umts
%{_sysconfdir}/rc.d/init.d/umts-interface

%changelog
* Thu Aug 27 2007 Brian Schueler <brian.schueler@gmx.de> - 2.2.1-1
- Initial package.
