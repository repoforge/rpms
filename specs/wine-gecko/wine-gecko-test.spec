# $Id$
# Authority: dag

# Tag: rft
# Dist: nodist

Summary: Wine Gecko
Name: wine-gecko
Version: 1.4
Release: 1%{?dist}
License: LGPLv2+
Group: Applications/Emulators
URL: http://www.winehq.org/

Source0: http://dl.sf.net/wine/wine_gecko-%{version}-x86.msi
Source1: http://dl.sf.net/wine/wine_gecko-%{version}-x86_64.msi
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: %{ix86} x86_64

%description
Wine implements its own version of Internet Explorer. The implementation is
based on a custom version of Mozilla's Gecko Layout Engine.

%install
%{__rm} -rf %{buildroot}
%ifarch %{ix86}
%{__install} -Dp -m644 %{SOURCE0} %{buildroot}%{_datadir}/wine/gecko/wine_gecko-%{version}-x86.msi
%endif
%ifarch x86_64
%{__install} -Dp -m644 %{SOURCE1} %{buildroot}%{_datadir}/wine/gecko/wine_gecko-%{version}-x86_64.msi
%endif

%files
%defattr(-, root, root, 0755)
%ifarch %{ix86}
%{_datadir}/wine/gecko/wine_gecko-%{version}-x86.msi
%endif
%ifarch x86_64
%{_datadir}/wine/gecko/wine_gecko-%{version}-x86_64.msi
%endif

%changelog
* Sun Jan 22 2012 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Wed Aug 10 2011 Dag Wieers <dag@wieers.com> - 1.2.0-1
- Updated to release 1.2.0.

* Sun Sep 19 2010 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Updated to release 1.1.0.

* Sat Sep 18 2010 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Initial package. (using DAR)
