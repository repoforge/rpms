
Summary: OpenAFS Kernel Module
Name: dkms-openafs-kernel
Version: 1.4.4
Release: bs
License: IBM Public License
Group: System Environment/Kernel
URL: http://www.openafs.org
Packager: Brian Schueler <brian.schueler@gmx.de>
Vendor: BS Repository

Source: openafs-kernel-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc
Requires(post): dkms
Requires(preun): dkms

%description
OpenAFS filesystem kernel module for the machine to act as an AFS client with caching support


%prep
%setup -n openafs-kernel-%{version}


%build


%install
%{__rm} -rf %{buildroot}

%define dkms_name openafs-kernel
%define dkms_vers %{version}-%{release}
%define quiet -q

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a . %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/.

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
MAKE[0]="cd src && make clean ; ./configure && make && cd src/libafs && rm -f MODLOAD && ln -s MODLOAD-`uname -r`* MODLOAD && cd ../../../"
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
BUILT_MODULE_NAME[0]=openafs
BUILT_MODULE_LOCATION[0]=src/src/libafs/MODLOAD
DEST_MODULE_LOCATION[0]=/kernel/fs/openafs
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
%doc README
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Tue Dec 11 2007 Brian Schueler <brian.schueler@gmx.de> 1.4.4
- Initial RPM release.

