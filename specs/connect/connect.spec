# $Id$

# Authority: dag

Summary: Create connections through HTTP-proxy's and SOCKS-servers.
Name: connect
Version: 1.41
Release: 1
License: GPL
Group: Applications/Internet

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Small program that lets you create connections through HTTP-proxy's
and SOCKS-servers.

%prep
%setup -n %{name}

%build
gcc %{optflags} -o connect connect.c

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/connect

%changelog
* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 1.41-0
- Initial package. (using DAR)
