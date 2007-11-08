# $Id$
# Authority: dries
# Upstream: Fayland &#26519; <fayland$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Han-PinYin

Summary: Retrieves the Mandarin of a Chinese character
Name: perl-Lingua-Han-PinYin
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Han-PinYin/

Source: http://search.cpan.org//CPAN/authors/id/F/FA/FAYLAND/Lingua-Han-PinYin-%{version}.tar.gz
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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/Han/
%{perl_vendorlib}/Lingua/Han/PinYin.pm
%{perl_vendorlib}/Lingua/Han/PinYin/

%changelog
* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
