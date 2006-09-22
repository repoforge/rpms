# $Id$
# Authority: dries
# Upstream: Philippe &quot;BooK&quot; Bruhat <book$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Gazetteer-HeavensAbove

Summary: Find location of world towns and cities
Name: perl-WWW-Gazetteer-HeavensAbove
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Gazetteer-HeavensAbove/

Source: http://search.cpan.org//CPAN/authors/id/B/BO/BOOK/WWW-Gazetteer-HeavensAbove-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module allows you to request information about cities
in one of the 207 countries supported by http://www.heavens-above.com/,
in a very simple manner.

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WWW/Gazetteer/HeavensAbove.pm
%dir %{perl_vendorlib}/WWW/Gazetteer/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
