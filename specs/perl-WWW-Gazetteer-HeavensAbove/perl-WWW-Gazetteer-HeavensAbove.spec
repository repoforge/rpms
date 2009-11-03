# $Id$
# Authority: dries
# Upstream: Philippe &quot;BooK&quot; Bruhat <book$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WWW-Gazetteer-HeavensAbove

Summary: Find location of world towns and cities
Name: perl-WWW-Gazetteer-HeavensAbove
Version: 0.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WWW-Gazetteer-HeavensAbove/

Source: http://www.cpan.org/modules/by-module/WWW/WWW-Gazetteer-HeavensAbove-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/WWW/Gazetteer/HeavensAbove.pm
%dir %{perl_vendorlib}/WWW/Gazetteer/

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.18-1
- Updated to version 0.18.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
