# $Id$
# Authority: dag

%define real_name red-eye

Summary: gimp script to implement Red-Eye removal technique
Name: gimp-script-red-eye
Version: 0.95
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.linuxjournal.com/article.php?sid=6567

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: red-eye.scm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gimp-devel >= 1.2
Requires: gimp >= 1.2, gimp-plugin-channel-mixer

%description
A gimp script to implement Red-Eye removal technique.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 %{SOURCE0} %{buildroot}%{_libdir}/gimp/1.2/scripts/red-eye.scm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/gimp/1.2/scripts/*

%changelog
* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 0.95-0
- Initial package. (using DAR)

