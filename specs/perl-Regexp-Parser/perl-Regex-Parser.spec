# $Id$
# Authority: cmr
# Upstream: Jeff Pinyan <japhy,734+CPAN$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-Parser

Summary: Perl module named Regexp-Parser
Name: perl-Regexp-Parser
Version: 0.20
Release: 3
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-Parser/

Source: http://www.cpan.org/modules/by-module/Regexp/Regexp-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Provides: perl(Regexp::Parser::Handlers)
Provides: perl(Regexp::Parser::Objects)
Provides: perl(Regexp::Parser::Diagnostics)

%description
perl-Regexp-Parser is a Perl module.

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
%doc %{_mandir}/man3/Regexp::Parser.3pm*
%doc %{_mandir}/man3/Regexp::Parser::Handlers.3pm*
%doc %{_mandir}/man3/Regexp::Parser::Objects.3pm*
%dir %{perl_vendorlib}/Regexp/
#%{perl_vendorlib}/Regexp/Parser/
%{perl_vendorlib}/Regexp/Parser.pm
%{perl_vendorlib}/Perl6/Rule/Parser.pm
%{perl_vendorlib}/Regexp/Parser/Diagnostics.pm
%{perl_vendorlib}/Regexp/Parser/Handlers.pm
%{perl_vendorlib}/Regexp/Parser/Objects.pm



%changelog
* Mon Sep 07 2009 Christoph Maser <cmr@financial.com> - 0.20-3
- another missing provides 

* Mon Sep 07 2009 Christoph Maser <cmr@financial.com> - 0.20-2
- Missing provides 

* Mon Sep 07 2009 Christoph Maser <cmr@financial.com> - 0.20-1
- Initial package. (using DAR)
