# Authority: dag

Summary: ELF binary-to-process comparison tool.
Name: elfcmp
Version: 1.0.0
Release: 0
License: GPL
Group: System Environment/Base
URL: http://www.hick.org/code/skape/elfcmp/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.hick.org/code/skape/elfcmp/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

#BuildRequires: 

%description
ELF binary-to-process comparison tool.

%prep
%setup

%{__perl} -pi.orig -e '
		s|/usr/bin$|\$(bindir)|g;
	' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*

%changelog
* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
