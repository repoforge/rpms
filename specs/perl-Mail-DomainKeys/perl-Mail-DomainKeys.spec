# $Id$
# Authority: dag
# Upstream: Anthony D. Urso <anthonyu$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-DomainKeys

Summary: Perl module that implements DomainKeys
Name: perl-Mail-DomainKeys
Version: 1.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Mail-DomainKeys/

Source: http://www.cpan.org/modules/by-module/Mail/Mail-DomainKeys-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Crypt::OpenSSL::RSA)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Mail-DomainKeys is a Perl module that implements DomainKeys.

%prep
%setup -n %{real_name}-%{version}

%build
echo "n" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST META.yml README THANKS
%doc %{_mandir}/man3/Mail::DomainKeys.3pm*
%dir %{perl_vendorlib}/Mail/
%{perl_vendorlib}/Mail/DomainKeys/
%{perl_vendorlib}/Mail/DomainKeys.pm

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
