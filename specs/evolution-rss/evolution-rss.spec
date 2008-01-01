# $Id$
# Authority: hadams

Summary: Evolution plugin for rss feed support
Name: evolution-rss
Version: 0.0.7
Release: 1
License: GPL
Group: Applications/Internet
URL: http://mips.edu.ms/evo/index.php/Evolution_RSS_Reader_Plugin

Source: http://mips.edu.ms/evolution-rss-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildRequires: gettext-devel, evolution-devel, perl(XML::Parser)
BuildRequires: firefox-devel
Requires: evolution

%description
RSS Evolution plugin enables evolution to read rss feeds.

%prep
%setup

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
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%dir %{_datadir}/evolution/
%dir %{_datadir}/evolution/*/
%dir %{_datadir}/evolution/*/errors/
%{_datadir}/evolution/*/errors/*
%{_datadir}/evolution/*/glade/*
%{_datadir}/evolution/*/images/*
%dir %{_libdir}/evolution/*/plugins/
%{_libdir}/evolution/*/plugins/*
%{_libdir}/bonobo/servers/*
%{_bindir}/evolution-import-rss
/etc/gconf/schemas/evolution-rss.schemas

%changelog
* Thu Dec 13 2007 Heiko Adams <info-2007@fedora-blog.de> - 0.0.7-1
- Update to 0.0.7

* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 0.0.6-2
- Fix group tag.

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
