# $Id$
# Authority: dag

%define real_name channel_mixer

Summary: Gimp plugin that combines values of the RGB channels
Name: gimp-plugin-channel-mixer
Version: 1.1
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://registry.gimp.org/plugin?id=1918

Source: http://registry.gimp.org/file/channel_mixer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gimp-devel >= 1.2
Requires: gimp >= 1.2

%description
A gimp plugin that combines values of the RGB channels.

%prep
%setup -n %{real_name}-%{version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/gimp/1.2/plug-ins/
%{__install} -m0755 channel_mixer %{buildroot}%{_libdir}/gimp/1.2/plug-ins/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README channel_mixer.html
%{_libdir}/gimp/1.2/plug-ins/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-0.2
- Rebuild for Fedora Core 5.

* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)

