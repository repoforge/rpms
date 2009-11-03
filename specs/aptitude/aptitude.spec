# $Id$
# Authority: dag
# Upstream: Daniel Burrows <Daniel_Burrows@alumni.brown.edu>

%define real_version 0.4.4.orig

Summary: Curses-based apt frontend
Name: aptitude
Version: 0.4.4
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://algebraicthunk.net/~dburrows/projects/aptitude/

Source: http://http.us.debian.org/debian/pool/main/a/aptitude/aptitude_%{version}.orig.tar.gz
Patch0: aptitude-0.4.4-alt1.patch
Patch1: aptitude-0.4.4-xsl-stylesheets.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apt-devel
BuildRequires: cppunit-devel
BuildRequires: docbook-dtd42-xml
BuildRequires: docbook-style-xsl
BuildRequires: gettext-devel
BuildRequires: html2text
BuildRequires: libsigc++20-devel
BuildRequires: libxslt-devel
BuildRequires: po4a

%description
Aptitude is a curses-based apt frontend with a number of useful extended 
features, including: a mutt-like syntax for matching packages in a flexible 
manner, persistence of user actions, and extreme flexibility and customization. 

%prep
%setup -n %{name}-%{real_version}
%patch0 -p1 -b .apt-rpm-altlinux
%patch1 -p1 -b .sgml

### Filter out languages that go below the minimal translation barrier
%{__perl} -pi -e 's|^SUBDIRS=cs de en fi fr ja po4a$|SUBDIRS=cs de en fi po4a|' doc/Makefile.am

%build
### Remove some generated files as in original altlinux patch but keep mkinstalldirs
%{__rm} -f INSTALL Makefile.in aclocal.m4 config.guess config.h.in config.sub \
  configure depcomp install-sh missing po/stamp-po \
  src/Makefile.in src/cmdline/Makefile.in src/generic/Makefile.in \
  src/generic/apt/Makefile.in src/generic/problemresolver/Makefile.in \
  src/generic/util/Makefile.in src/mine/Makefile.in src/vscreen/Makefile.in \
  src/vscreen/config/Makefile.in tests/Makefile.in
libtoolize --copy --force
aclocal -I m4
autoheader
automake -a -c
autoconf
export CPPFLAGS="-DRPM_VERSION=0x040406"
%configure --disable-werror
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" STATEDIR="%{_localstatedir}/aptitude"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0775)
%doc %{_docdir}/aptitude
%doc %{_mandir}/man8/aptitude.8.*
%doc %{_mandir}/*/man8/aptitude.8.*
%dir %{_datadir}/aptitude
%{_bindir}/aptitude
%{_datadir}/aptitude/
%dir %{_localstatedir}/aptitude/

%changelog
* Wed Oct 29 2008 Dag Wieers <dag@wieers.com> - 0.4.4-1
- Initial package. (using DAR)
