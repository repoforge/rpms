# $Id$
# Authority: matthias
# Dist: nodist

%define kmod_name ipw3945

Summary: Common files for the ipw3945 kernel module
Name: %{kmod_name}-kmod-common
Version: 0.0.73
Release: 1%{?dist}
Group: System Environment/Kernel
License: GPL
URL: http://ipw3945.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: kmod-%{kmod_name} = %{version}
Requires: ipw3945-firmware

%description
Common files for the ipw3945 kernel module.


%prep


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/etc/modules.d
%{__cat} > %{buildroot}/etc/modules.d/ipw3945 << EOF
install ipw3945 /sbin/modprobe --ignore-install ipw3945 ; sleep 0.5 ; /sbin/ipw3945d --quiet
remove ipw3945 /sbin/ipw3945d --kill ; /sbin/modprobe -r --ignore-remove ipw3945
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, -)
%attr(0644, root, root) %config /etc/modules.d/ipw3945


%changelog
* Fri Mar 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.73-1
- Initial RPM release, based on the new Extras kernel module template.

