# $Id$
# Authority: matthias
# Dist: nodist

%define snapshot 20060521

%define kmod_name acx

Summary: Common files for the ACX kernel module
Name: %{kmod_name}-kmod-common
Version: 0.0.0.%{snapshot}
Release: 1%{?dist}
Group: System Environment/Kernel
License: GPL
URL: http://acx100.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: kmod-%{kmod_name} = %{version}
Requires: acx100-firmware
Requires: acx111-firmware

%description
Common files for the ACX kernel module.


%prep


%build


%install
%{__rm} -rf %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, -)


%changelog
* Wed May 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.0.20060521-1
- Update to 20060521.

* Fri Mar 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.0.20060215-1
- Initial RPM release, based on the new Extras kernel module template.

