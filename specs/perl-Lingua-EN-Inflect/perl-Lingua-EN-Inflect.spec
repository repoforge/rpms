# $Id$
# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-EN-Inflect

Summary: Convert singular to plural
Name: perl-Lingua-EN-Inflect
Version: 1.891
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-EN-Inflect/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Lingua-EN-Inflect-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Test::More)
BuildRequires: perl(version)
Requires: perl(Test::More)
Requires: perl(version)

%filter_from_requires /^perl*/d
%filter_setup

%description
The exportable subroutines of Lingua::EN::Inflect provide plural
inflections and "a"/"an" selection for English words.

Plural forms of all nouns, most verbs, and some adjectives are
provided. Where appropriate, "classical" variants (for example:
"brother" -> "brethren", "dogma" -> "dogmata", etc.) are also
provided.

This package contains the following Perl module:

    Lingua::EN::Inflect


%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g;' *.pl

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
%doc %{_mandir}/man3/Lingua::EN::Inflect.3pm*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/EN/
#%{perl_vendorlib}/Lingua/EN/Inflect/
%{perl_vendorlib}/Lingua/EN/Inflect.pm
%{perl_vendorlib}/Lingua/EN/*.pl

%changelog
* Tue Dec 22 2009 Christoph Maser <cmr@financial.com> - 1.891-1
- Updated to version 1.891.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.89-1
- Updated to release 1.89.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.88-1
- Initial package.
