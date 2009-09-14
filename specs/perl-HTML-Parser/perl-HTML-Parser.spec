# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$activestate,com>

##ExcludeDist: el5
# Rationale: spamassasin 3.20 needs this core package to be updated

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Parser

Summary: Perl module that implements a HTML parser class
Name: perl-HTML-Parser
Version: 3.62
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Parser/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.006
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Tagset) >= 3
BuildRequires: perl(HTTP::Headers)
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
Requires: perl >= 0:5.006

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README TODO eg/
%doc %{_mandir}/man3/HTML::*.3pm*
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
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 3.62-1
- Updated to version 3.62.

* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 3.61-1
- Updated to version 3.61.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 3.56-1
- Updated to release 3.56.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 3.55-1
- Initial package. (using DAR)
