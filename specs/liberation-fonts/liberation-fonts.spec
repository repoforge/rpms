# $Id$
# Authority: dag


%{?rh7:%define _without_fontconfig 1}
%{?el2:%define _without_fontconfig 1}

Summary: Fonts to replace commonly used Microsoft Windows Fonts
Name: liberation-fonts
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: https://www.redhat.com/promo/fonts/

#Source: https://www.redhat.com/f/fonts/liberation-fonts-ttf-3.tar.gz
Source: liberation-fonts-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
%{!?_without_fontconfig:Requires: fontconfig}

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup

%install
%{__install} -d -m0755 %{buildroot}%{_datadir}/fonts/liberation/
%{__install} -p -m0644 *.ttf %{buildroot}%{_datadir}/fonts/liberation/

%post
%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
	%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc COPYING License.txt
%{_datadir}/fonts/liberation/

%changelog
* Sun Jul 22 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Updated to release 0.2.

* Wed May 16 2007 Dag Wieers <dag@wieers.com> - 0.1-4
- Initial import into RPMforge.

* Wed Apr 25 2007 Meethune Bhowmick <bhowmick@redhat.com> 0.1-4
- Require fontconfig package for post and postun

* Tue Apr 24 2007 Meethune Bhowmick <bhowmick@redhat.com> 0.1-3
- Bump version to fix issue in RHEL4 RHN

* Thu Mar 29 2007 Richard Monk <rmonk@redhat.com> 0.1-2rhis
- New license file

* Thu Mar 29 2007 Richard Monk <rmonk@redhat.com> 0.1-1rhis
- Inital packaging
