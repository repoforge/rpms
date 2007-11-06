# $Id$
# Authority: dries
# Upstream: Neil Watkiss <nwatkiss$ttul,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Inline-Python

Summary: Write Perl subs and classes in Python
Name: perl-Inline-Python
Version: 0.22
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Inline-Python/

Source: http://www.cpan.org/modules/by-module/Inline/Inline-Python-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker), python-devel

%description
Inline::Python lets you write Perl subroutines and classes in
Python. You don't have to use any funky techniques for sharing most
types of data between the two languages, either. Inline::Python comes
with its own data translation service. It converts any Python structures
it knows about into Perl structures, and vice versa.

%prep
%setup -n %{real_name}-%{version}

%build
echo 1 | CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Inline/
%{perl_vendorarch}/Inline/Python.*
%dir %{perl_vendorarch}/auto/Inline/
%{perl_vendorarch}/auto/Inline/Python/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
