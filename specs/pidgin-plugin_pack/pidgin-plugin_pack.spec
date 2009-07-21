# $Id$
# Authority: dag

### FIXME: SPEC file should probably be renamed to purple-plugin_pack

%define real_name purple-plugin_pack

Summary: Plugin Pack for Pidgin
Name: pidgin-plugin_pack
Version: 2.5.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://plugins.guifications.org/trac/

#Source: http://plugins.guifications.org/trac/downloads/22
Source: purple-plugin_pack-2.5.1.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: libtool
BuildRequires: pidgin-devel
BuildRequires: pkgconfig
BuildRequires: xmms-devel
### Require purple-plugin_pack for translations and to help people install all the plugins
Requires: purple-plugin_pack = %{version}-%{release}

Obsoletes: gaim-plugin_pack <= %{version}-%{release}
Provides: gaim-plugin_pack = %{version}-%{release}

%description
Plugin Pack is a collection of plugins for the open source
instant messaging client Pidgin.

%package -n purple-plugin_pack
Summary: Plugin Pack for libpurple and derived IM clients
Group: Applications/Internet

%description -n purple-plugin_pack
Plugin Pack is a collection of plugins for libpurple and derived IM clients.

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

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README doc/*.txt
%dir %{_libdir}/pidgin/
%{_libdir}/pidgin/*.so
%dir %{_datadir}/pixmaps/pidgin/
%{_datadir}/pixmaps/pidgin/plugin_pack/
%dir %{_datadir}/pixmaps/pidgin/protocols/
%{_datadir}/pixmaps/pidgin/protocols/*/napster.png
%exclude %{_libdir}/pidgin/*.la

%files -n purple-plugin_pack -f plugin_pack.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README doc/*.txt
%dir %{_libdir}/purple-2/
%{_libdir}/purple-2/*.so
%exclude %{_libdir}/purple-2/*.la

%changelog
* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 2.5.1-1
- Updated to release 2.5.1.

* Sat Mar 01 2008 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.
- Split package into purple-plugin_pack and pidgin-plugin_pack.

* Sun Jul 01 2007 Dag Wieers <dag@wieers.com> - 1.0-0.beta7
- Updated to release 1.0beta7.

* Thu Jun 07 2007 Dag Wieers <dag@wieers.com> - 1.0-0.beta6
- Updated to release 1.0beta6.

* Mon Apr 03 2006 Dag Wieers <dag@wieers.com> - 1.0-0.beta3
- Initial package. (using DAR)
