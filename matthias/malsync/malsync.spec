# Authority: dag

%define sourcedir stable/%{version}/distribution/tar/generic/source

Summary: Utilities to update from AvantGo and MobileLink web site to Palm's.
Name: malsync
Version: 2.1.1
Release: 0
License: MPL
Group: Applications/Communications
URL: http://www.tomw.org/malsync/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.tomw.org/%{name}/%{name}_%{version}.src.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: pilot-link-devel

%description
Utilities to update from Avantgo and MobileLink web site to Palm's.

%prep

%setup -n %{name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 malsync %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Doc/README* mal/MPL-1_0.txt mal/client/unix/{HISTORY,TODO} README
%{_bindir}/*

%changelog
* Thu Feb 27 2003 Dag Wieers <dag@wieers.com> - 2.0.6-0
- Build with dar.

* Sat Dec 15 2001 Dag Wieers <dag@wieers.com> - 2.0.6-dag.2
- Updated to 2.0.6.

* Sat Dec 16 2000 Dag Wieers <dag@wieers.com> - 2.0.4-dag.2
- Initial package.
