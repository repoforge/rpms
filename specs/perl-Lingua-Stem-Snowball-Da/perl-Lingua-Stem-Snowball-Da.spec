# $Id$
# Authority: dries
# Upstream: Dennis Haney <davh$davh,dk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Stem-Snowball-Da

Summary: Porters stemming algorithm for Denmark
Name: perl-Lingua-Stem-Snowball-Da
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Stem-Snowball-Da/

Source: http://search.cpan.org/CPAN/authors/id/C/CI/CINE/Lingua-Stem-Snowball-Da-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Lingua::Stem::Snowball::Da is a perl port of the danish
stemmer at http://snowball.sourceforge.net, it was originally altered
from the Lingua::Stem::Snowball::Se.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Lingua/Stem/Snowball/Da.pm
%{perl_vendorlib}/Lingua/Stem/Snowball/stemmer.pl

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
