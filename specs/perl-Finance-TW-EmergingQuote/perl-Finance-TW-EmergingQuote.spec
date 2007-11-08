# $Id$
# Authority: dries
# Upstream: Chia-liang Kao (&#39640;&#22025;&#33391;) <clkao$clkao,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Finance-TW-EmergingQuote

Summary: Check stock quotes from Taiwan Emerging Stock
Name: perl-Finance-TW-EmergingQuote
Version: 0.25
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Finance-TW-EmergingQuote/

Source: http://search.cpan.org//CPAN/authors/id/C/CL/CLKAO/Finance-TW-EmergingQuote-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Check stock quotes from Taiwan Emerging Stock.

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
%doc %{_mandir}/man3/Finance::TW::EmergingQuote*
%{perl_vendorlib}/Finance/TW/EmergingQuote.pm
%dir %{perl_vendorlib}/Finance/TW/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
