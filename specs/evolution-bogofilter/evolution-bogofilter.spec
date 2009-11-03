# $Id$
# Authority: dag

%define evolution_basename %(basename %{_libdir}/pkgconfig/evolution-plugin*.pc .pc)

%define real_name bf-eplugin

Summary: Evolution plugin for bogofilter support
Name: evolution-bogofilter
Version: 0.2.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://people.altlinux.ru/~mhz/software/projects/bf-eplugin/

Source: http://people.altlinux.ru/~mhz/software/projects/bf-eplugin/bf-eplugin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, evolution-devel, evolution-data-server-devel
Requires: bogofilter

%description
This plugin implements junk filtering for the Evolution mailer, provided by 
the bogofilter utility. Bogofilter (http://www.bogofilter.org) is a fast and 
nimble mail filter using a so-called Bayesian technique to classify junk and 
non-junk email.

%prep
%setup -n %{real_name}-%{version}

%{__perl} -pi.orig -e 's|evolution-plugin-2.6|%{evolution_basename}|g' configure

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%{__make} install DESTDIR="%{buildroot}"

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule /etc/gconf/schemas/%{real_name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %{_sysconfdir}/gconf/schemas/bf-eplugin.schemas
%dir %{_libdir}/evolution/
%dir %{_libdir}/evolution/*/
%dir %{_libdir}/evolution/*/plugins/
%{_libdir}/evolution/*/plugins/*.eplug
%{_libdir}/evolution/*/plugins/*.so
%exclude %{_libdir}/evolution/*/plugins/*.la

%changelog
* Sat Jun 16 2007 Heiko Adams <info@fedora-blog.de> 0.2.0-1
- Initial package for RPMforge.
