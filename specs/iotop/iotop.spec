# $Id$
# Authority: dag

Summary: Top like utility for I/O
Name: iotop
Version: 0.1
Release: 1
License: GPL
Group: Applications/System
URL: http://guichaz.free.fr/misc/#iotop

Source: http://guichaz.free.fr/misc/%{name}.py
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.5
Requires: python >= 2.5

%description
Linux has always been able to show how much I/O was going on
(the bi and bo columns of the vmstat 1 command).
iotop is a Python program with a top like UI used to
show of behalf of which process is the I/O going on.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 %{SOURCE0} %{buildroot}%{_bindir}/iotop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/iotop

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.1-1
- Initial package. (using DAR)
