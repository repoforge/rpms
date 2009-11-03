# $Id$
# Authority: dag

Summary: Read or set the region setting on a DVD drive
Name: regionset
Version: 0.1
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://linvdr.org/projects/regionset/

Source: http://linvdr.org/download/regionset/regionset-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
regionset is a tool to read and set the region setting on a DVD drive.

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CC="%{__cc} %{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 regionset %{buildroot}%{_sbindir}/regionset

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%{_sbindir}/regionset

%changelog
* Fri Mar 11 2005 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
