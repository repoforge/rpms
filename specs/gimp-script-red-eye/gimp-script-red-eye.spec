# $Id$
# Authority: dag

%{?fc1:%define _without_gimp2 1}
%{?el3:%define _without_gimp2 1}
%{?rh9:%define _without_gimp2 1}
%{?rh8:%define _without_gimp2 1}
%{?rh7:%define _without_gimp2 1}

%define real_name red-eye

Summary: gimp script to implement Red-Eye removal technique
Name: gimp-script-red-eye
Version: 0.95
Release: 2.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.linuxjournal.com/article.php?sid=6567

Source: red-eye.scm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_gimp2:BuildRequires: gimp-devel >= 2.0}
%{!?_without_gimp2:Requires: gimp >= 2.0}
%{?_without_gimp2:BuildRequires: gimp-devel >= 1.2}
%{?_without_gimp2:Requires: gimp >= 1.2, gimp-plugin-channel-mixer}

%description
A gimp script to implement Red-Eye removal technique.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{!?_without_gimp2:%{__install} -Dp -m0755 %{SOURCE0} %{buildroot}%{_libdir}/gimp/2.0/scripts/red-eye.scm}
%{?_without_gimp2:%{__install} -Dp -m0755 %{SOURCE0} %{buildroot}%{_libdir}/gimp/1.2/scripts/red-eye.scm}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{!?_without_gimp2:%{_datadir}/gimp/2.0/scripts/red-eye.scm}
%{?_without_gimp2:%{_libdir}/gimp/1.2/scripts/red-eye.scm}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.95-2.2
- Rebuild for Fedora Core 5.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 0.95-2
- Fixed location for gimp2 plugin. (Chris Weyl)

* Wed Sep 29 2004 Dag Wieers <dag@wieers.com> - 0.95-1
- Fixes for gimp2. (Chris Weyl)

* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 0.95-0
- Initial package. (using DAR)
