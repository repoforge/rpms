# $Id$
# Authority: dag
# Upstream: Gil M. Thomer <gil$thomer,com>

Summary: Tunneling IP over ICMP
Name: icmptx
Version: 0.01
Release: 1
License: GPL
Group: Applications/Networking
URL: http://thomer.com/icmptx/

Source: http://thomer.com/icmptx/icmptx-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
icmptx is a tool for tunneling IP over ICMP.

%prep
%setup

%build
%{__make} %{?_smp_mflags} flags="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 icmptx %{buildroot}%{_bindir}/icmptx

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/icmptx

%changelog
* Tue Oct 14 2008 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
