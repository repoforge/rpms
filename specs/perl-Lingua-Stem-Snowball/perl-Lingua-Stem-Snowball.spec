# $Id$

# Authority: dries
# Upstream: Fabien Potencier <fabpot$cpan,org>

%define real_name Lingua-Stem-Snowball
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Perl interface to Snowball stemmers
Name: perl-Lingua-Stem-Snowball
Version: 0.8
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Stem-Snowball/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/F/FA/FABPOT/Lingua-Stem-Snowball-chmod-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Perl interface to Snowball stemmers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Lingua/Stem/Snowball.pm
%{perl_vendorarch}/Lingua/Stem/add_stemmer.pl
%{perl_vendorarch}/auto/Lingua/Stem/Snowball/Snowball.*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
