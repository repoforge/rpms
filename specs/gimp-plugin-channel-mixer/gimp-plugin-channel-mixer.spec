# $Id$

# Authority: dag

%define rname channel_mixer

Summary: Gimp plugin that combines values of the RGB channels
Name: gimp-plugin-channel-mixer
Version: 1.1
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://registry.gimp.org/plugin?id=1918

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://registry.gimp.org/file/channel_mixer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gimp-devel >= 1.2
Requires: gimp >= 1.2

%description
A gimp plugin that combines values of the RGB channels.

%prep
%setup -n %{rname}-%{version}

%build
%{__make} %{?_smp_mflag}

%install
%{__install} -d -m0755 %{buildroot}%{_libdir}/gimp/1.2/plug-ins/
%{__install} -m0755 channel_mixer %{buildroot}%{_libdir}/gimp/1.2/plug-ins/

%files
%defattr(-, root, root, 0755)
%doc README channel_mixer.html
%{_libdir}/gimp/1.2/plug-ins/*

%changelog
* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)
