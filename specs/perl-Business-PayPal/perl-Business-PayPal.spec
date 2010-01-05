# $Id$
# Authority: dag
# Upstream: Fred Moyer <fred@redhotpenguin.com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-PayPal

Summary: Perl extension for automating PayPal transactions
Name: perl-Business-PayPal
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-PayPal/

Source: http://search.cpan.org/CPAN/authors/id/P/PH/PHRED/Business-PayPal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(CGI)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(Net::SSLeay) >= 1.14
Requires: perl(CGI)
Requires: perl(Digest::MD5)
Requires: perl(Net::SSLeay) >= 1.14

%filter_from_requires /^perl*/d
%filter_setup


%description
Perl extension for automating PayPal transactions.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Business::PayPal.3pm*
%dir %{perl_vendorlib}/Business/
#%{perl_vendorlib}/Business/PayPal/
%{perl_vendorlib}/Business/PayPal.pm
%{perl_vendorlib}/Business/getppcert.pl

%changelog
* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
