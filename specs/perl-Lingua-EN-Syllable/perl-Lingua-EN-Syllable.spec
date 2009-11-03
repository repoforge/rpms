# $Id$
# Authority: dries
# Upstream: Greg Fast <gdf$speakeasy,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-EN-Syllable

Summary: Routine for estimating syllable count in words
Name: perl-Lingua-EN-Syllable
Version: 0.251
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-EN-Syllable/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-EN-Syllable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Lingua::EN::Syllable provides one subroutine, syllable(), which
estimates the number of syllables in the word passed to it.  It
guesses correctly about 80-90% of the time, but it's smaller and
faster than a dictionary lookup.  So you can't really use it for
writing random haiku, but you can do things like estimate reading
grade level.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Lingua/EN/Syllable.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.251-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.251-1
- Initial package.
