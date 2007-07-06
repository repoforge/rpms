# $Id$
# Authority: hadams

Summary: Guifications Plugin for Pidgin
Name: pidgin-guifications
%define real_version 2.14
Version: 2.14
Release: 1
License: GPL
Group: Applications/Internet
URL: http://gaim.guifications.org/

Source: http://downloads.guifications.org/plugins//Guifications2/pidgin-guifications-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, libtool, gettext, pidgin-devel, gtk2-devel

%description
Guifications is a graphical notification plugin for the open source
instant messaging client Pidgin

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang guifications

%clean
%{__rm} -rf %{buildroot}

%files -f guifications.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README doc/*.dia doc/*.png
%{_datadir}/pixmaps/pidgin/guifications/
%dir %{_libdir}/pidgin/
#exclude %{_libdir}/pidgin/guifications.a
%exclude %{_libdir}/pidgin/guifications.la
%{_libdir}/pidgin/guifications.so

%changelog
* Fri Jul 06 2007 Heiko Adams <info@fedora-blog.de> - 2.14-1
- Updated to release 2.14

* Thu Jun 07 2006 Dag Wieers <dag@wieers.com> - 2.13-0.beta6
- Updated to release 2.13beta6.

* Mon Apr 03 2006 Dag Wieers <dag@wieers.com> - 2.13-0.beta3
- Updated to release 2.13beta3.

* Mon Mar 17 2006 Dag Wieers <dag@wieers.com> - 2.13-0.beta2
- Updated to release 2.13beta2.

* Mon Mar 13 2006 Dag Wieers <dag@wieers.com> - 2.12-1
- Initial package. (using DAR)
