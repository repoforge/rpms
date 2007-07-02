# $Id$
# Authority: hadams

Summary: Evolution plugin for rss feed support
Name: evolution-rss
Version: 0.0.3
Release: 2
License: GPL
Group: Productivity/Networking/Email/Clients
URL: http://mips.edu.ms/evo/index.php/Evolution_RSS_Reader_Plugin

Source: http://mips.edu.ms/evolution-rss-%{version}.tar.gz
Requires: evolution
BuildRequires: gettext-devel, evolution-devel, perl(XML::Parser)
BuildRoot: %{_tmppath}/%{name}-%{version}-root

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
%dir %{_libdir}/evolution/*/plugins/
%{_libdir}/evolution/*/plugins/*

%changelog
* Sat Jun 30 2007 Heiko Adams <info@fedora-blog.de> - 0.0.3-2
- Rebuild for RPMforge.

* Sun May 20 2007 Piotr Pacholak <obi.gts@gmail.com> - 0.0.3-1
- Initial release.
