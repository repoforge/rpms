# $Id$
# Authority: dag

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_fontconfig 1}
%{?el2:%define _without_fontconfig 1}

Summary: Fonts to replace commonly used Microsoft Windows Fonts
Name: liberation-fonts
Version: 0.1
Release: 4
License: GPL
Group: User Interface/X
URL: https://www.redhat.com/promo/fonts/

#Source: https://www.redhat.com/f/fonts/liberation-fonts-%{version}.tar.gz
Source: liberation-fonts-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
%{!?_without_fontconfig:Requires: fontconfig}

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems: Times New Roman,
Arial, and Courier New.

%prep
%setup -c

%install
%{__install} -Dp -m0644 License.txt %{buildroot}%{_datadir}/fonts/liberation/License.txt
%{__install} -p -m0644 *.ttf %{buildroot}%{_datadir}/fonts/liberation/

%post
%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
	%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc License.txt
%{_datadir}/fonts/liberation/

%changelog
* Wed May 16 2007 Dag Wieers <dag@wieers.com> - 0.1-4
- Require fontconfig package for post and postun

* Wed Apr 25 2007 Meethune Bhowmick <bhowmick@redhat.com> 0.1-4
- Require fontconfig package for post and postun

* Tue Apr 24 2007 Meethune Bhowmick <bhowmick@redhat.com> 0.1-3
- Bump version to fix issue in RHEL4 RHN

* Thu Mar 29 2007 Richard Monk <rmonk@redhat.com> 0.1-2rhis
- New license file

* Thu Mar 29 2007 Richard Monk <rmonk@redhat.com> 0.1-1rhis
- Inital packaging
