# $Id$
# Authority: dries
# Upstream: Fayland Lam <fayland$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Han-Cantonese

Summary: Retrieve the Cantonese(GuangDongHua) of Chinese character(HanZi)
Name: perl-Lingua-Han-Cantonese
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Han-Cantonese/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-Han-Cantonese-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Lingua::Han::Utils) >= 0.1
BuildRequires: perl(Test::More)

%description
Retrieve the Cantonese(GuangDongHua) of Chinese character(HanZi).

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
%doc %{_mandir}/man3/Lingua::Han::Cantonese.3pm*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/Han/
%{perl_vendorlib}/Lingua/Han/Cantonese/
%{perl_vendorlib}/Lingua/Han/Cantonese.pm

%changelog
* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.06-1
- Updated to release 0.06.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
