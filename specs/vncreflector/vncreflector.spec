# $Id$
# Authority: dag

%define real_name vnc_reflector

Summary: VNC server which acts as a proxy for a number of VNC clients
Name: vncreflector
Version: 1.2.4
Release: 0.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://sf.net/projects/vnc-reflector/

Source: http://dl.sf.net/vnc-reflector/vnc_reflector-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libjpeg-devel, zlib-devel
Obsoletes: vnc-reflector <= %{version}-%{release}

%description
VNC Reflector is a specialized VNC server which acts as a proxy sitting
between real VNC server (a host) and a number of VNC clients. It was
designed to work efficiently with large number of clients.

%prep
%setup -n %{real_name}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 vncreflector %{buildroot}%{_bindir}/vncreflector

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README
%{_bindir}/vncreflector

%changelog
* Mon Jun 30 2003 Dag Wieers <dag@wieers.com> - 1.2.4-0
- Initial package. (using DAR)
