# $Id$
# Authority: dag

Summary: Advanced intrusion detection environment
Name: aide
Version: 0.10
Release: 1
License: GPL
Group: Applications/System
URL: http://www.cs.tut.fi/~rammer/aide.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/aide/aide-%{version}.tar.gz
Source1: aide.conf
Source2: README.quickstart
Patch1: aide-useless-includes.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
Buildrequires: flex, bison, m4
Buildrequires: mhash-devel, zlib-devel

### Postgresql support doesn't build.
#Buildconflicts: postgresql-devel

%description 
AIDE (Advanced Intrusion Detection Environment) is a file integrity
checker and intrusion detection program.

%prep
%setup
%patch1 -p1

%{__perl} -pi.orig -e 's|^C(PP)?FLAGS=.+$||' configure
%{__perl} -pi.orig -e 's|%{_sysconfdir}/aide.db|%{_localstatedir}/lib/aide.db|' config.h
%{__perl} -pi.orig -e 's|<prefix>/etc/aide.db|%{_localstatedir}/lib/aide.db|' doc/aide.1
%{__perl} -pi.orig -e 's|<prefix>/etc/aide.conf|%{_sysconfdir}/aide.conf|' doc/aide.1

%build
%configure \
	--with-config_file="%{_sysconfdir}/aide.conf" \
	--with-zlib \
	--with-mhash \
	--enable-mhash 
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	bindir="%{buildroot}%{_sbindir}"
%{__install} -D -m0600 %{SOURCE1} %{buildroot}%{_sysconfdir}/aide.conf
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/aide/

%{__install} -m0644 %{SOURCE2} README.quickstart
%{__install} -D -m0644 doc/aide.1.ru %{buildroot}%{_mandir}/ru/man1/aide.1
%{__install} -D -m0644 doc/aide.conf.5.ru %{buildroot}%{_mandir}/ru/man5/aide.conf.5

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README* ./doc/manual.html
%doc %{_mandir}/man?/aide.*
%doc %lang(ru) %{_mandir}/ru/man?/aide.*

%defattr(0600, root, root, 0755)
%config(noreplace) %{_sysconfdir}/aide.conf

%defattr(0700, root, root, 0755)
%{_sbindir}/aide

%defattr(0700, root, root, 0700)
%{_localstatedir}/lib/aide/

%changelog
* Thu Oct 07 2004 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
