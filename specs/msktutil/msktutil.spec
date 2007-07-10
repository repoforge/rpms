# $Id: $
# Authority: dag
# Upstream: Christoph Maser <cmr$financial,com>

Summary: Program for (kerberos) interoperability with Active Directory 
Name: msktutil
Version: 0.3.16
Release: 1
License: GPL
Group: System Administration
URL: http://download.systemimager.org/~finley/msktutil/

Source: http://download.systemimager.org/~finley/msktutil/%{name}_%{version}-4.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openldap-devel, gcc, krb5-devel
Requires: openldap, cyrus-sasl-gssapi, krb5-workstation

%description
A program for interoperability with Active Directory
 that can:
 - Create a computer account in Active Directory
 - Create a system Kerberos keytab
 - Add and remove principals to and from that keytab
 - Change the computer account's password

 Website: http://www.pppl.gov/~dperry/


%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} install

%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README
%doc LICENSE
%doc INSTALL
%doc %{_mandir}/man1/msktutil.1*
%{_sbindir}/msktutil

%changelog
* Fri Jul 06 2007 Christoph Maser <cmr$financial,com> 0.3.16-1
- Initial package
