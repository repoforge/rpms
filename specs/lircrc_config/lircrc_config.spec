# Authority: dag

Summary: A GNOME .lircrc configuration program.
Name: lircrc_config
Version: 0.1.1
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.lirc.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/lirc/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

#BuildRequires: 

%description
A GNOME .lircrc configuration program.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO samples/
%{_bindir}/*
%{_datadir}/lircrc_config/

%changelog
* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 0.1.1-0
- Initial package. (using DAR)
