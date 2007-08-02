# $Id$
# Authority: dries
# Upstream: Jonathan Rockway <jrockway$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-LogWarnings

Summary: Log perl warnings to the Catalyst log
Name: perl-Catalyst-Plugin-LogWarnings
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-LogWarnings/

Source: http://search.cpan.org//CPAN/authors/id/J/JR/JROCKWAY/Catalyst-Plugin-LogWarnings-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This plugin redirects perl's warn() warnings to a Catalyst log
($c->log->warn), allowing you to filter warnings, log warnings to a
database, Log4Perl, etc.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Catalyst/Plugin/LogWarnings.pm
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
