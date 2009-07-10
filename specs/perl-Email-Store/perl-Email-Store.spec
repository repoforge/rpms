# $Id$
# Authority: cmr
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Store

Summary: Perl module named Email-Store
Name: perl-Email-Store
Version: 0.256
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Store/

Source: http://www.cpan.org/modules/by-module/Email/Email-Store-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

Requires: perl(Class::DBI)
Requires: perl(Class::Data::Inheritable)
Requires: perl(Ima::DBI)

%description
perl-Email-Store is a Perl module.

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
%doc Changes LICENSE MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Email::Store.3pm*
%doc %{_mandir}/man3/Email::Store::Attachment.3pm*
%doc %{_mandir}/man3/Email::Store::DBI.3pm*
%doc %{_mandir}/man3/Email::Store::Date.3pm*
%doc %{_mandir}/man3/Email::Store::Entity.3pm*
%doc %{_mandir}/man3/Email::Store::List.3pm*
%doc %{_mandir}/man3/Email::Store::Mail.3pm*
%dir %{perl_vendorlib}/Email/
%{perl_vendorlib}/Email/Store.pm
%{perl_vendorlib}/Email/Store/Attachment.pm
%{perl_vendorlib}/Email/Store/Date.pm
%{perl_vendorlib}/Email/Store/DBI.pm
%{perl_vendorlib}/Email/Store/Entity.pm
%{perl_vendorlib}/Email/Store/Entity/Correlator/List.pm
%{perl_vendorlib}/Email/Store/Entity/Correlator/Trivial.pm
%{perl_vendorlib}/Email/Store/List.pm
%{perl_vendorlib}/Email/Store/Mail.pm

%changelog
* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 0.256-1
- Updated to version 0.256.

* Thu Jul  2 2009 Steve Huff <hakamadare@users.sourceforge.net> - 0.255-2
- uncaptured Perl dependencies 

* Thu Jun 11 2009 Unknown - 0.255-1
- Initial package. (using DAR)
