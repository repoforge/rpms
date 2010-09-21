# $Id$
# Authority: dag

# Dist: nodist

Summary: Wine Gecko
Name: wine-gecko
Version: 1.0.0
Release: 1%{?dist}
License: LGPLv2+
Group: Applications/Emulators
URL: http://www.winehq.org/

Source: http://dl.sf.net/wine/wine_gecko-%{version}-x86.cab
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: i386

%description
Wine implements its own version of Internet Explorer. The implementation is
based on a custom version of Mozilla's Gecko Layout Engine.

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m644 %{SOURCE0} %{buildroot}%{_datadir}/wine/gecko/wine_gecko-%{version}-x86.cab

%files
%defattr(-, root, root, 0755)
%{_datadir}/wine/gecko/wine_gecko-%{version}-x86.cab

%changelog
* Sat Sep 18 2010 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package. (using DAR)
