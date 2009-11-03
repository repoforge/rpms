# $Id$
# Authority: cmr
# Upstream: Olivier Salaun <os AT cru,fr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name AuthCAS

Summary: Client library for CAS 2.0 authentication server
Name: perl-AuthCAS
Version: 1.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/AuthCAS/

Source: http://www.cpan.org/authors/id/O/OS/OSALAUN/AuthCAS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Client library for CAS 2.0 authentication server.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/AuthCAS.3pm*
#%{perl_vendorlib}/AuthCAS/
%{perl_vendorlib}/AuthCAS.pm

%changelog
* Sat Jul 04 2009 Unknown - 1.4-1
- Initial package. (using DAR)
