# $Id$
# Authority: dries
# Upstream: Fayland &#26519; <fayland$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Han-PinYin

Summary: Retrieves the Mandarin of a Chinese character
Name: perl-Lingua-Han-PinYin
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Han-PinYin/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-Han-PinYin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module retrieve the Mandarin(PinYin) of Chinese character(HanZi).

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
%doc %{_mandir}/man3/Lingua::Han::PinYin.3pm*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/Han/
%{perl_vendorlib}/Lingua/Han/PinYin/
%{perl_vendorlib}/Lingua/Han/PinYin.pm

%changelog
* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
