# $Id$
# Authority: hadams

Name:		evolution-rss
Version:	0.0.8
Release:	1
Summary:	Evolution plugin for rss feed support
URL:		http://mips.edu.ms/evo/index.php/Evolution_RSS_Reader_Plugin
Group:		Productivity/Networking/Email/Clients
License:	GPL
Source:         http://mips.edu.ms/evolution-rss-%{version}.tar.gz
Requires:       evolution
BuildRequires:  gettext-devel, evolution-devel, perl(XML::Parser)
BuildRequires:  firefox-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

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
%{_datadir}/evolution/*/images/*
%dir %{_libdir}/evolution/*/plugins/
%{_libdir}/evolution/*/plugins/*
%{_libdir}/bonobo/servers/*
%{_datadir}/evolution/*/glade/*
%{_bindir}/evolution-import-rss
/etc/gconf/schemas/evolution-rss.schemas

%changelog
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
