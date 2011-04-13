# $Id$
# Authority: dag

Summary: Intel video BIOS hack to support certain resolutions 
Name: 915resolution
Version: 0.5.3
Release: 1%{?dist}
License: Public Domain 
Group: Applications/System
URL: http://www.geocities.com/stomljen/ 

Source: http://www.geocities.com/stomljen/915resolution-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
915resolution is a tool to modify the video BIOS of the 800 and 900 series
Intel graphics chipsets. This includes the 845G, 855G, and 865G chipsets,
as well as 915G, 915GM, and 945G chipsets. This modification is necessary
to allow the display of certain graphics resolutions for an Xorg or XFree86
graphics server.

915resolution's modifications of the BIOS are transient. There is no risk of
permanent modification of the BIOS. This also means that 915resolution must
be run every time the computer boots inorder for it's changes to take effect.

915resolution is derived from the tool 855resolution. However, the code
differs substantially. 915resolution's code base is much simpler.
915resolution also allows the modification of bits per pixel. 

%prep
%setup

%{__chmod} -x dump_bios

%build
%{__make} clean
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 915resolution %{buildroot}%{_sbindir}/915resolution

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changes.log dump_bios *.txt
%{_sbindir}/915resolution

%changelog
* Tue Oct 10 2006 Dag Wieers <dag@wieers.com> - 0.5.2-2
- Fixed group name.

* Mon Aug 14 2006 Dag Wieers <dag@wieers.com> - 0.5.2-1
- Initial package. (using DAR)
