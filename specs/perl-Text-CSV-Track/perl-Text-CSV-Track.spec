# $Id$
# Authority: dries
# Upstream: Jozef Kutej <jozef$kutej,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-CSV-Track

Summary: Module to work with .csv file that stores some value(s) per identificator
Name: perl-Text-CSV-Track
Version: 0.6
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-CSV-Track/

Source: http://search.cpan.org//CPAN/authors/id/J/JK/JKUTEJ/Text-CSV-Track-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Module to work with .csv file that stores some value(s) per identificator.

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
%doc %{_mandir}/man3/Text::CSV::Track*
%{perl_vendorlib}/Text/CSV/Track.pm
%{perl_vendorlib}/Text/CSV/Track/

%changelog
* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
