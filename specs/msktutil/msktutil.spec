# $Id$
# Authority: dag
# Upstream: Christoph Maser <cmr$financial,com>


Summary: Program for (kerberos) interoperability with Active Directory 
Name: msktutil
%define real_version 0.3.16
%define source_version 0.3.16-4
Version: 0.3.16.4
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://download.systemimager.org/~finley/msktutil/

Source: http://download.systemimager.org/~finley/msktutil/msktutil_%{source_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openldap-devel, krb5-devel
Requires: cyrus-sasl-gssapi

%description
A program for interoperability with Active Directory that can:

  create a computer account in Active Directory,
  create a system Kerberos keytab,
  add and remove principals to and from that keytab and
  change the computer account's password.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL LICENSE README
%doc %{_mandir}/man1/msktutil.1*
%{_sbindir}/msktutil

%changelog
* Wed Jul 11 2007 Dag Wieers <dag@wieers.com> - 0.3.16.4-1
- Cosmetic changes and version change.

* Fri Jul 06 2007 Christoph Maser <cmr$financial,com> 0.3.16-1
- Initial package.
