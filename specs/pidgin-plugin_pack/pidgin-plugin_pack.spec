# $Id$
# Authority: dag

%define real_name purple-plugin_pack

Summary: Plugin Pack for Pidgin
Name: pidgin-plugin_pack
Version: 2.0.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://plugins.guifications.org/trac/

Source: http://downloads.guifications.org/plugins/Plugin%20Pack%20Archive/purple-plugin_pack-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, libtool, gettext, xmms-devel, pidgin-devel, gtk2-devel
Obsoletes: gaim-plugin_pack <= %{version}-%{release}
Provides: gaim-plugin_pack = %{version}-%{release}

%description
Plugin Pack is a collection of plugins for the open source
instant messaging client Pidgin.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang plugin_pack

%clean
%{__rm} -rf %{buildroot}

%files -f plugin_pack.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/*.txt
%dir %{_libdir}/pidgin/
%{_libdir}/pidgin/*.so
%dir %{_libdir}/purple-2/
%{_libdir}/purple-2/*.so
%dir %{_datadir}/pixmaps/pidgin/
%{_datadir}/pixmaps/pidgin/plugin_pack/
%exclude %{_libdir}/pidgin/*.la
%exclude %{_libdir}/purple-2/*.la

%changelog
* Sat Mar 01 2008 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.

* Sun Jul 01 2007 Dag Wieers <dag@wieers.com> - 1.0-0.beta7
- Updated to release 1.0beta7.

* Thu Jun 07 2007 Dag Wieers <dag@wieers.com> - 1.0-0.beta6
- Updated to release 1.0beta6.

* Mon Apr 03 2006 Dag Wieers <dag@wieers.com> - 1.0-0.beta3
- Initial package. (using DAR)
