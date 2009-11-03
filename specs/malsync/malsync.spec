# $Id$
# Authority: dag

%define sourcedir stable/%{version}/distribution/tar/generic/source

Summary: Utilities to update from AvantGo and MobileLink web site to Palm's
Name: malsync
Version: 2.1.1
Release: 0.2%{?dist}
License: MPL
Group: Applications/Communications
URL: http://www.tomw.org/malsync/

Source: http://www.tomw.org/%{name}/%{name}_%{version}.src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: pilot-link-devel

%description
Utilities to update from Avantgo and MobileLink web site to Palm's.

%prep

%setup -n %{name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 malsync %{buildroot}%{_bindir}/malsync

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Doc/README* mal/client/unix/{HISTORY,TODO} mal/MPL-1_0.txt README
%{_bindir}/malsync

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.1.1-0.2
- Rebuild for Fedora Core 5.

* Thu Feb 27 2003 Dag Wieers <dag@wieers.com> - 2.0.6-0
- Build with dar.

* Sat Dec 15 2001 Dag Wieers <dag@wieers.com> - 2.0.6-dag.2
- Updated to 2.0.6.

* Sat Dec 16 2000 Dag Wieers <dag@wieers.com> - 2.0.4-dag.2
- Initial package.
