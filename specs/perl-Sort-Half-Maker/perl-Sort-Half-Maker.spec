# $Id$
# Authority: dries
# Upstream: Adriano Ferreira <ferreira$shoo,cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sort-Half-Maker

Summary: Create half-sort subs easily
Name: perl-Sort-Half-Maker
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sort-Half-Maker/

Source: http://search.cpan.org//CPAN/authors/id/F/FE/FERREIRA/Sort-Half-Maker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Create half-sort subs easily.

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
%doc %{_mandir}/man3/Sort::Half::Maker*
%{perl_vendorlib}/Sort/Half/Maker.pm
%dir %{perl_vendorlib}/Sort/Half/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
