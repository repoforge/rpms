# $Id$
# Authority: dries
# Upstream: Makis Marmaridis <makis$scm,uws,edu,au>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-Random-String

Summary: Perl extension for creating random strings
Name: perl-Data-Random-String
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Random-String/

Source: http://search.cpan.org//CPAN/authors/id/M/MA/MAKIS/Data-Random-String-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Perl extension for creating random strings.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Data::Random::String*
%{perl_vendorlib}/Data/Random/String.pm

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
