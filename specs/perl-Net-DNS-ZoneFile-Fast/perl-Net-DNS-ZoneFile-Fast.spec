# $Id$
# Authority: dries
# Upstream: Wes Hardaker <wjhns117$hardakers,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-DNS-ZoneFile-Fast

Summary: Parse BIND zone files
Name: perl-Net-DNS-ZoneFile-Fast
Version: 1.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS-ZoneFile-Fast/

Source: http://www.cpan.org/modules/by-module/Net/Net-DNS-ZoneFile-Fast-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(IO::File)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Net::DNS) >= 0.65
BuildRequires: perl(Net::DNS::SEC) >= 0.15


%description
The Net::DNS::ZoneFile::Fast module provides an ability to parse zone
files that BIND8 and BIND9 use, fast.  Currently it provides a single
function, I<parse()>, which returns a reference to an array of
traditional I<Net::DNS::RR> objects, so that no new API has to be
learned in order to manipulate zone records.

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
%doc %{_mandir}/man3/Net::DNS::ZoneFile::Fast.3pm*
%dir %{perl_vendorlib}/Net/
%dir %{perl_vendorlib}/Net/DNS/
%dir %{perl_vendorlib}/Net/DNS/ZoneFile/
#%{perl_vendorlib}/Net/DNS/ZoneFile/Fast/
%{perl_vendorlib}/Net/DNS/ZoneFile/Fast.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 1.12-1
- Updated to version 1.12.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.11-1
- Updated to version 1.11.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 0.91-1
- Updated to release 0.91.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Updated to release 0.7.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Initial package.
