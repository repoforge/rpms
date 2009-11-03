# $Id$
# Authority: cmr
# Upstream: Adriano R, Ferreira <ferreira$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-Size-Perl

Summary: Perl extension for retrieving terminal size (Perl version)
Name: perl-Term-Size-Perl
Version: 0.029
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-Size-Perl/

Source: http://www.cpan.org/modules/by-module/Term/Term-Size-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
# From yaml requires
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Test::More)


%description
Perl extension for retrieving terminal size (Perl version).

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
%doc %{_mandir}/man3/Term::Size::Perl.3pm*
%doc %{_mandir}/man3/Term::Size::Params.3pm*
%dir %{perl_vendorlib}/Term/
%dir %{perl_vendorlib}/Term/Size/
%{perl_vendorlib}/Term/Size/Perl/Params.pm
%{perl_vendorlib}/Term/Size/Perl.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.029-1
- Initial package. (using DAR)
