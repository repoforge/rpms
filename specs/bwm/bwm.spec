# $Id$

# Authority: dag

Summary: Bandwidth Monitor
Name: bwm
Version: 1.1.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://packages.debian.org/unstable/net/bwm.html

Source: bwm.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Bandwidth monitor is a very simple utility that allows the user to
view the bandwidth currently being consumed to and from each network
interface, the total bandwidth in use on each interface, and the total
bandwidth in use on all interfaces.

%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bwm  %{buildroot}%{_bindir}/bwm

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc changes.txt readme.txt
%{_bindir}/bwm

%changelog
* Mon Dec 30 2002 Dag Wieers <dag@wieers.com> - 1.1.0
- Initial package. (using DAR)
