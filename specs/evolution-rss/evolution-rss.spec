# $Id$
# Authority: hadams

Summary: Evolution plugin for rss feed support
Name: evolution-rss
Version: 0.0.4
Release: 2
License: GPL
Group: Applications/Internet
URL: http://mips.edu.ms/evo/index.php/Evolution_RSS_Reader_Plugin

Source: http://mips.edu.ms/evolution-rss-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext-devel, evolution-devel, perl(XML::Parser)
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
%{_datadir}/evolution/*/errors/org-gnome-evolution-rss.error
%dir %{_datadir}/evolution/*/images/
%{_datadir}/evolution/*/images/rss.png
%dir %{_libdir}/evolution/*/plugins/
%{_libdir}/evolution/*/plugins/liborg-gnome-evolution-rss.so
%{_libdir}/evolution/*/plugins/org-gnome-evolution-rss.eplug
%{_libdir}/evolution/*/plugins/org-gnome-evolution-rss.xml
%{_libdir}/bonobo/servers/GNOME_Evolution_RSS_*.server
%exclude %{_libdir}/evolution/*/plugins/liborg-gnome-evolution-rss.la
### Sorry Heiko, this is totally unacceptable !
#/glade/*

%changelog
* Mon Jul 03 2007 Heiko Adams <info@fedora-blog.de> - 0.0.4-2
- Restored rpmforge like formats.

* Mon Jul 03 2007 Heiko Adams <info@fedora-blog.de> - 0.0.4-1
- Updated to release 0.0.4.

* Sat Jun 30 2007 Heiko Adams <info@fedora-blog.de> - 0.0.3-2
- Rebuild for RPMforge.

* Sun May 20 2007 Piotr Pacholak <obi.gts@gmail.com> - 0.0.3-2
- Initial release.
