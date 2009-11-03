# $Id$
# Authority: dag

Summary: Site Management Tool for webmasters
Name: webcheck
Version: 1.10.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://ch.tudelft.nl/~arthur/webcheck/

Source: http://ch.tudelft.nl/~arthur/webcheck/webcheck-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-devel
Requires: python

Obsoletes: linbot <= %{version}-%{release}

%description
Webcheck (fka Linbot) allows webmasters to:
 - View the structure of a site
 - Track down broken links
 - Find potentially outdated web pages
 - List links pointing to external sites
 - View portfolio of inline images
 - Do all this periodically and without user intervention

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0644 favicon.ico %{buildroot}%{_localstatedir}/www/webcheck/favicon.ico
%{__install} -Dp -m0644 webcheck.1 %{buildroot}%{_mandir}/man1/webcheck.1

%{__install} -Dp -m0755 webcheck.css %{buildroot}%{_libdir}/webcheck/webcheck.css
%{__install} -p -m0755 *.py %{buildroot}%{_libdir}/webcheck/
#%{__cp} -av contrib/ fancytooltips/ parsers/ plugins/ schemes/ %{buildroot}%{_libdir}/webcheck/
%{__cp} -av fancytooltips/ parsers/ plugins/ schemes/ %{buildroot}%{_libdir}/webcheck/

%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f ../lib/webcheck/webcheck.py %{buildroot}%{_bindir}/webcheck

### Generate normal (.pyc) and optimized (.pyo) byte-compiled files.
%{__python} -c 'import compileall; compileall.compile_dir("%{buildroot}", 10, "/", 1)' 
%{__python} -O -c 'import compileall; compileall.compile_dir("%{buildroot}", 10, "/", 1)'

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING HACKING NEWS README TODO
%doc %{_mandir}/man1/webcheck.1*
%config %{_libdir}/webcheck/config.py
%{_bindir}/webcheck
%{_libdir}/webcheck/
%{_localstatedir}/www/webcheck/
%ghost %{_libdir}/webcheck/*.pyo
%ghost %{_libdir}/webcheck/*/*.pyo

%changelog
* Wed Aug 22 2007 Dag Wieers <dag@wieers.com> - 1.10.1-1
- Updated to release 1.10.1.

* Sat Apr 21 2007 Dag Wieers <dag@wieers.com> - 1.9.8-1
- Cosmetic changes.

* Tue Apr 17 2007 R P Herrold <info@owlriver.com> 1.9.8-1orc
- pick up latest, there was a security matter in the intervening time
  since our last packaging

* Mon Oct 23 2000 Arnaldo Carvalho de Melo <acme@conectiva.com.br>
- more macros
- /usr/lib/linbot is part of this package

* Wed Sep 13 2000 Rodrigo Barbosa <rodrigob@conectiva.com>
- Adopted rpm macros
- Spec changes to build as non-root
