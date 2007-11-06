# $Id$
# Authority: dries
# Upstream: Julius C. Duque <jcduque$lycos,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Digest-SHA2

Summary: Variable-length one-way hash function
Name: perl-Digest-SHA2
Version: 1.1.0
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Digest-SHA2/

Source: http://search.cpan.org/CPAN/authors/id/J/JC/JCDUQUE/Digest-SHA2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
A variable-length one-way hash function.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Digest/
%{perl_vendorarch}/Digest/SHA2.pm
%dir %{perl_vendorarch}/auto/Digest/
%{perl_vendorarch}/auto/Digest/SHA2/

%changelog
* Mon May  8 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Initial package.
