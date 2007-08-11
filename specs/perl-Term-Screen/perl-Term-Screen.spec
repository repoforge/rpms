# $Id$
# Authority: dries
# Upstream: Jonathan Stowe

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Term-Screen

Summary: Term::Cap based screen positioning module
Name: perl-Term-Screen
Version: 1.03
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Term-Screen/

Source: http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/Term-Screen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
A Simple all perl Term::Cap based screen positioning module.

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
%dir %{perl_vendorlib}/Term/
%{perl_vendorlib}/Term/Screen.pm

%changelog
* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Initial package.
