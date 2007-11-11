# $Id$
# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Similarity

Summary: Calculate the similarity of two strings
Name: perl-String-Similarity
Version: 1.02
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Similarity/

Source: http://www.cpan.org/modules/by-module/String/String-Similarity-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The "similarity"-function calculates the similarity index of its two
arguments. A value of 0 means that the strings are entirely
different. A value of 1 means that the strings are identical.
Everything else lies between 0 and 1 and describes the amount of
similarity between the strings.

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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/String/
%{perl_vendorarch}/String/Similarity.pm
%dir %{perl_vendorarch}/auto/String/
%{perl_vendorarch}/auto/String/Similarity

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
