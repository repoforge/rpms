# $Id$
# Authority: dag

Summary: Plugin pack for Gaim
Name: gaim-plugin_pack
%define real_version 1.0beta3
Version: 1.0
Release: 0.beta3%{?dist}
License: GPL
Group: Applications/Internet
URL: http://plugins.guifications.org/trac/

Source: http://downloads.guifications.org/plugins/Plugin%20Pack%20Archive/gaim-plugin_pack-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, libtool, gettext, gaim-devel, gtk2-devel

%description
Plugin Pack is a collection of plugins for the open source
instant messaging client Gaim

%prep
%setup -n %{name}-%{real_version}

### Remove broken plugins
%{__rm} -f {markerline,nicksaid}/.{build,plugin}

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
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/*.txt
%dir %{_libdir}/gaim/
#exclude %{_libdir}/gaim/*.a
%exclude %{_libdir}/gaim/*.la
%{_libdir}/gaim/*.so

%changelog
* Mon Apr 03 2006 Dag Wieers <dag@wieers.com> - 1.0-0.beta3
- Initial package. (using DAR)
