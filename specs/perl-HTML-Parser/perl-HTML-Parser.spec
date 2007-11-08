# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

# ExcludeDist: el5
# Rationale: spamassasin 3.20 needs this core package to be updated

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Parser

Summary: Perl module that implements a HTML parser class
Name: perl-HTML-Parser
Version: 3.55
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Parser/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
HTML-Parser is a Perl module that implements a HTML parser class.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README TODO
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/HTML/Entities.pm
%{perl_vendorarch}/HTML/Filter.pm
%{perl_vendorarch}/HTML/HeadParser.pm
%{perl_vendorarch}/HTML/LinkExtor.pm
%{perl_vendorarch}/HTML/Parser.pm
%{perl_vendorarch}/HTML/PullParser.pm
%{perl_vendorarch}/HTML/TokeParser.pm
%dir %{perl_vendorarch}/auto/HTML/
%{perl_vendorarch}/auto/HTML/Parser/

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 3.55-1
- Initial package. (using DAR)
