# Authority: dag

%define rname vnc_reflector

Summary: A VNC server which acts as a proxy for a number of VNC clients.
Name: vncreflector
Version: 1.2.4
Release: 0
Group: User Interface/Desktops
License: GPL
URL: http://sourceforge.net/projects/vnc-reflector/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/vnc-reflector/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libjpeg-devel, zlib-devel

%description
VNC Reflector is a specialized VNC server which acts as a proxy sitting
between real VNC server (a host) and a number of VNC clients. It was
designed to work efficiently with large number of clients.

%prep
%setup -n %{rname}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 vncreflector %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog LICENSE README
%{_bindir}/*

%changelog
* Mon Jun 30 2003 Dag Wieers <dag@wieers.com> - 1.2.4-0
- Initial package. (using DAR)
