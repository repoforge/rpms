# $Id$
# authority: matthias
# Dist: nodist

%define kmod_name acx

Summary: Common files for the ACX kernel module
Name: %{kmod_name}-kmod-common
Version: 0.0.0
Release: 1
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
* Fri Mar 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-1
- Initial RPM release, based on the new Extras kernel module template.

