# $Id: checkpassword-pam.spec 78 2004-03-09 15:32:47Z dag $

# Authority: dag
# Upstream: Herve Commowick <hervec@sports.fr>

Summary: Provides a simple, uniform password-checking interface using an LDAP database. 
Name: checkpassword-ldap
Version: 0.01
Release: 1
License: GPL
Group: System Environment/Base
URL: http://chkpasswd-ldap.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/chkpasswd-ldap/checkpassword-ldap.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
checkpassword implementation that searches an LDAP database.

%prep

%build
${CC:-%{__cc}} %{optflags} -MT checkpassword-pam.o -MD -MP -MF "checkpassword-ldap.Tpo" -c -o checkpassword-ldap.o %{SOURCE0}
${CC:-%{__cc}} %{optflags} -o checkpassword-ldap checkpassword-ldap.o -lldap -ldl

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 checkpassword-ldap %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*

%changelog
* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
