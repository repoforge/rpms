# $Id$
# Authority: dries
# Upstream: Neil Watkiss <NEILW$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Inline-Python

Summary: Write Perl subs and classes in Python
Name: perl-Inline-Python
Version: 0.28
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Inline-Python/

Source: http://www.cpan.org/modules/by-module/Inline/Inline-Python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: python-devel

%description
Inline::Python lets you write Perl subroutines and classes in
Python. You don't have to use any funky techniques for sharing most
types of data between the two languages, either. Inline::Python comes
with its own data translation service. It converts any Python structures
it knows about into Perl structures, and vice versa.

%prep
%setup -n %{real_name}-%{version}

%build
echo "1" | CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST META.yml README ToDo
%doc %{_mandir}/man3/Inline::Python.3pm*
%dir %{perl_vendorarch}/auto/Inline/
%{perl_vendorarch}/auto/Inline/Python/
%dir %{perl_vendorarch}/Inline/
%{perl_vendorarch}/Inline/Python.pm
%{perl_vendorarch}/Inline/Python.pod

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.28-1
- Updated to version 0.28.

* Wed Oct 08 2008 Dag Wieers <dag@wieers.com> - 0.25-1
- Updated to release 0.25.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
