# Authority: dag

Summary: Allows changing of desktop resolution and refresh rate.
Name: multires
Version: 0.2.4
Release: 0
License: GPL
Group: Applications/System
URL: http://multires.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libgnomeui-devel >= 2.0

%description
GNOME Multires is an applet for the GNOME 2 panel which allows changing
of desktop resolution and refresh rate.

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
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/pixmaps/*

%changelog
* Mon Mar 10 2003 Dag Wieers <dag@wieers.com> - 0.2.4-0
- Initial package. (using DAR)
