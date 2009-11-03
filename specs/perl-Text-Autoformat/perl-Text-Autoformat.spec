# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Autoformat

Summary: Automatic text wrapping and reformatting
Name: perl-Text-Autoformat
Version: 1.666.0
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Autoformat/

Source: http://www.cpan.org/modules/by-module/Text/Text-Autoformat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Text::Autoformat provides intelligent formatting of
plaintext without the need for any kind of embedded mark-up. The module
recognizes Internet quoting conventions, a wide range of bulleting and
number schemes, centred text, and block quotations, and reformats each
appropriately. Other options allow the user to adjust inter-word
and inter-paragraph spacing, justify text, and impose various
capitalization schemes.

This package contains the following Perl module:

    Text::Autoformat

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
%doc %{_mandir}/man3/Text::Autoformat.3pm*
%dir %{perl_vendorlib}/Text/
#%{perl_vendorlib}/Text/Autoformat/
%{perl_vendorlib}/Text/Autoformat.pm

%changelog
* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 1.666.0-1
- Updated to version 1.666.0.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Sun Dec 19 2004 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
