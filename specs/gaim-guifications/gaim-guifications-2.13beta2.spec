# $Id$
# Authority: dag

Summary: Guifications Plugin for Gaim
Name: gaim-guifications
%define real_version 2.13beta2
Version: 2.13
Release: 0.beta2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://gaim.guifications.org/

Source: http://downloads.guifications.org/plugins/Guifications2%20Archive/gaim-guifications-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, libtool, gettext, gaim-devel, gtk2-devel

%description
Guifications is a graphical notification plugin for the open source
instant messaging client Gaim

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README doc/*.dia doc/*.png
%{_datadir}/pixmaps/gaim/guifications/
%dir %{_libdir}/gaim/
#exclude %{_libdir}/gaim/guifications.a
%exclude %{_libdir}/gaim/guifications.la
%{_libdir}/gaim/guifications.so

%changelog
* Mon Mar 17 2006 Dag Wieers <dag@wieers.com> - 2.13-0.beta2
- Updated to release 2.13beta2.

* Mon Mar 13 2006 Dag Wieers <dag@wieers.com> - 2.12-1
- Initial package. (using DAR)
