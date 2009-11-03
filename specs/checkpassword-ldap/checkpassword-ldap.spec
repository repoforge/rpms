# $Id$
# Authority: dag
# Upstream: Herve Commowick <hervec$sports,fr>

Summary: Provides a simple, uniform password-checking interface using an LDAP database.
Name: checkpassword-ldap
Version: 0.01
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://chkpasswd-ldap.sourceforge.net/

Source: http://dl.sf.net/chkpasswd-ldap/checkpassword-ldap.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openldap-devel

%description
checkpassword implementation that searches an LDAP database.

%prep

%build
${CC:-%{__cc}} %{optflags} -MT checkpassword-pam.o -MD -MP -MF "checkpassword-ldap.Tpo" -c -o checkpassword-ldap.o %{SOURCE0}
${CC:-%{__cc}} %{optflags} -o checkpassword-ldap checkpassword-ldap.o -lldap -ldl

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 checkpassword-ldap %{buildroot}%{_bindir}/checkpassword-ldap

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
