# $Id$
# Authority: hadams

Name:		evolution-rss
Version:	0.0.8
Release:	3
Summary:	Evolution plugin for rss feed support
URL:		http://gnome.eu.org/evo/index.php/Evolution_RSS_Reader_Plugin
Group:		Productivity/Networking/Email/Clients
License:	GPL
Source:         hhttp://gnome.eu.org/evolution-rss-%{version}.tar.gz

Patch0: 	evolution-rss-0.0.8-empty-desc.patch
Patch1: 	evolution-rss-0.0.8-norss-popup.patch
Patch2: 	evolution-rss-0.0.8-norss-enabled.patch
Patch3: 	evolution-rss-0.0.8-xulrunner.patch

Requires:       evolution, xulrunner
Requires(pre): 	GConf2
Requires(post): GConf2
Requires(preun):GConf2

#BuildRequires:  gettext-devel, evolution-devel, perl(XML::Parser)
#BuildRequires:  firefox-devel

BuildRequires: gettext
BuildRequires: evolution-devel
BuildRequires: evolution-data-server-devel 
BuildRequires: dbus-glib-devel
BuildRequires: gecko-libs = 1.9
BuildRequires: gecko-devel = 1.9
BuildRequires: perl(XML::Parser)
BuildRequires: libtool
BuildRequires: xulrunner-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-root

%description
RSS Evolution plugin enables evolution to read rss feeds.

%prep
%setup -q -n evolution-rss-%{version}
%patch0 -p1 -b .empty-fix
%patch1 -p1 -b .norss-popup
%patch2 -p1 -b .norss-enabled
%patch3 -p1 -b .xulrunner

%build
autoreconf -i -f
%configure --disable-webkit
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install DESTDIR="%{buildroot}" INSTALL="install -p"
find %{buildroot} -name \*\.la -print | xargs rm -f

%find_lang %{name}

%pre
if [ "$1" -gt 1 ]; then
	export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
	gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
	%{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
/sbin/ldconfig

%preun
if [ "$1" -eq 0 ]; then
	export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
	gconftool-2 --makefile-uninstall-rule \
		%{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang 
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%dir %{_datadir}/evolution/
%dir %{_datadir}/evolution/*/
%dir %{_datadir}/evolution/*/errors/
%{_datadir}/evolution/*/errors/*
%{_datadir}/evolution/*/images/*
%dir %{_libdir}/evolution/*/plugins/
%{_libdir}/evolution/*/plugins/*
%{_libdir}/bonobo/servers/*
%{_datadir}/evolution/*/glade/*
%{_bindir}/evolution-import-rss
/etc/gconf/schemas/evolution-rss.schemas

%changelog
* Mon Jul 07 2008 Heiko Adams <info-2007@fedora-blog.de> - 0.0.8-3
- rebuild for FF3 final

* Sun Jun 29 2008 Heiko Adams <info-2007@fedora-blog.de> - 0.0.8-2
- rebuild for el5.2

* Mon Mar 03 2008 Heiko Adams <info-2007@fedora-blog.de> - 0.0.8-1
- Update to 0.0.8

* Thu Dec 13 2007 Heiko Adams <info-2007@fedora-blog.de> - 0.0.7-1
- Update to 0.0.7

* Fri Oct 19 2007 Heiko Adams <info@fedora-blog.de> - 0.0.6-1
- Version update

* Sat Sep 08 2007 Heiko Adams <info@fedora-blog.de> - 0.0.5-1
- Version update

* Mon Jul 03 2007 Heiko Adams <info@fedora-blog.de> - 0.0.4-2
- Restored rpmforge like formats

* Mon Jul 03 2007 Heiko Adams <info@fedora-blog.de> - 0.0.4-1
- update to 0.0.4

* Sat Jun 30 2007 Heiko Adams <info@fedora-blog.de> - 0.0.3-2
- Rebuild for RPMforge

* Sun May 20 2007 Piotr Pacholak <obi.gts@gmail.com> - 0.0.3-2
- Initial release
