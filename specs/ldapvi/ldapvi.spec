# $Id$
# Authority: dag
# Upstream: <ldapvi$lists,askja,de>

Summary: Interactive LDAP client for Unix terminals
Name: ldapvi
Version: 1.7
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://www.lichteblau.com/ldapvi/

Source: http://www.lichteblau.com/download/ldapvi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: openldap-devel >= 2.2, ncurses-devel, readline-devel, pkgconfig, openssl-devel
Requires: openldap-clients >= 2.2, ncurses, openssl

%description
ldapvi is an interactive LDAP client for Unix terminals. Using it, you
can update LDAP entries with a text editor. Think of it as vipw for LDAP.

%prep
%setup

### FIXME: Makefile does not use DESTDIR (Please fix upstream)
%{__perl} -pi.orig -e '
        s|\@prefix\@/share/doc|\$(DESTDIR)%{_docdir}|g;
        s|\@mandir\@|\$(DESTDIR)%{_mandir}|g;
        s|\@bindir\@|\$(DESTDIR)%{_bindir}|g;
    ' GNUmakefile.in

%build
%configure
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} -C manual

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/doc/ldapvi/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS manual/bg.png manual/manual.css manual/manual.html
%doc %{_mandir}/man1/ldapvi.1*
%{_bindir}/ldapvi

%changelog
* Thu Sep 13 2007 Dag Wieers <dag@wieers.com> - 1.7-2
- Cosmetic changes.

* Wed Jul 25 2007 Fabian Arrotin <fabian.arrotin@arrfab.net> - 1.7-1
- Initial Release for el5.
