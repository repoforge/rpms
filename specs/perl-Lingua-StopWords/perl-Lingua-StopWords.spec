# $Id$
# Authority: dries
# Upstream: Marvin Humphrey <marvin$rectangular,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-StopWords

Summary: Stop words for several languages
Name: perl-Lingua-StopWords
Version: 0.09
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-StopWords/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-StopWords-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Stop words for several languages.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Lingua::StopWords.3pm*
%dir %{perl_vendorlib}/Lingua/
%{perl_vendorlib}/Lingua/StopWords/
%{perl_vendorlib}/Lingua/StopWords/
%{perl_vendorlib}/Lingua/StopWords.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Tue Jan 09 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
