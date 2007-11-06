# $Id$
# Authority: dries
# Upstream: Fayland <fayland$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Han-Cantonese

Summary: Retrieve the Cantonese(GuangDongHua) of Chinese character(HanZi)
Name: perl-Lingua-Han-Cantonese
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Han-Cantonese/

Source: http://search.cpan.org/CPAN/authors/id/F/FA/FAYLAND/Lingua-Han-Cantonese-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Retrieve the Cantonese(GuangDongHua) of Chinese character(HanZi).

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
%{perl_vendorlib}/Lingua/Han/Cantonese.pm
%{perl_vendorlib}/Lingua/Han/Cantonese/

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Updated to release 0.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
