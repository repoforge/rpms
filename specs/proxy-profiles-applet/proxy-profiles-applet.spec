# $Id$

# Authority: dag

Summary: Proxy profiles applet
Name: proxy-profiles-applet
Version: 0.4
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: ftp://impre.ssive.net/pub/proxy-profiles-applet/

Source: ftp://impre.ssive.net/pub/proxy-profiles-applet/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, libgnomeui-devel, gnome-panel-devel

%description
Proxy Profiles Applet allows you to switch between preset profiles of the GNOME
network proxy setings

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
%doc ChangeLog COPYING README
%{_libexecdir}/*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/proxy-profiles-applet/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4-0.2
- Rebuild for Fedora Core 5.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Initial package. (using DAR)
