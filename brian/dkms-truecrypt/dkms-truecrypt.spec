%define dkms_name truecrypt
%define dkms_vers %{version}-%{release}
%define quiet -q

Summary: Free open-source disk encryption software
Name: dkms-truecrypt
Version: 4.3b
Release: 3.am%{?dist}
License: GPLv2
Group: System Environment/Kernel
URL: http://www.truecrypt.org/
Source: truecrypt-%{version}-source-code.tar.gz
Patch1: dm.h.patch
Patch2:	truecrypt-%{version}-kernel-2.6.23.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms
Provides: truecrypt = %{version}-%{release}
ExclusiveArch: i386 x86_64

%description
Manages encrypted TrueCrypt volumes, which can be mapped as virtual block
devices and used as any other standard block device. All data being read from
a mapped TrueCrypt volume is transparently decrypted and all data
being written to it is transparently encrypted. 

%prep
%setup -n truecrypt-%{version}-source-code
%patch1 -p1
%patch2 -p1
mkdir dkms
cp -a Common Crypto Linux dkms

%build
cd Linux/Cli
%{__make} NO_WARNINGS=1
cd ../../

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0755 Linux/Cli/truecrypt %{buildroot}%{_bindir}/truecrypt
%{__install} -D -m 0644 Linux/Cli/Man/truecrypt.1 %{buildroot}%{_mandir}/man1/truecrypt.1

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a dkms/* %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="cd Linux/Kernel ; make KERNEL_SRC=${kernel_source_dir}"
CLEAN[0]="cd Linux/Kernel ; make clean KERNEL_SRC=${kernel_source_dir}"
BUILT_MODULE_NAME[0]=truecrypt
BUILT_MODULE_LOCATION[0]="Linux/Kernel"
DEST_MODULE_LOCATION[0]=/kernel/extra/truecrypt
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
%doc License.txt Readme.txt
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{_bindir}/truecrypt
%{_mandir}/man1/truecrypt.1*


%changelog
* Fri Nov 30 2007 Adam Miller <kirov.sama@gmail.com> 4.3a-3
- Fix inclusion of binaries in dkms source

* Fri Nov 30 2007 Adam Miller <kirov.sama@gmail.com> 4.3a-2
- Narrow the parts of truecrypt source dkms needs

* Thu Nov 29 2007 Adam Miller <kirov.sama@gmail.com> 4.3a-1
- Initial spec
