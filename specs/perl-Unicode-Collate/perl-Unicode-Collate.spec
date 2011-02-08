# $Id$
# Authority: dag
# Upstream: SADAHIRO Tomoyuki <SADAHIRO$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-Collate

Summary: Perl module that implements Unicode Collation Algorithm
Name: perl-Unicode-Collate
Version: 0.72
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Collate/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SADAHIRO/Unicode-Collate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Carp)
BuildRequires: perl(DynaLoader)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test)
BuildRequires: perl(constant)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
Requires: perl(Carp)
Requires: perl(DynaLoader)
Requires: perl(File::Spec)
Requires: perl(Test)
Requires: perl(constant)
Requires: perl(strict)
Requires: perl(warnings)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
perl-Unicode-Collate is a Perl module that implements Unicode Collation
Algorithm.

This package contains the following Perl module:

    Unicode::Collate

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
%doc %{_mandir}/man3/Unicode::Collate.3pm*
%doc %{_mandir}/man3/Unicode::Collate::CJK::Big5.3pm.gz
%doc %{_mandir}/man3/Unicode::Collate::CJK::GB2312.3pm.gz
%doc %{_mandir}/man3/Unicode::Collate::CJK::JISX0208.3pm.gz
%doc %{_mandir}/man3/Unicode::Collate::CJK::Korean.3pm.gz
%doc %{_mandir}/man3/Unicode::Collate::CJK::Pinyin.3pm.gz
%doc %{_mandir}/man3/Unicode::Collate::CJK::Stroke.3pm.gz
%doc %{_mandir}/man3/Unicode::Collate::Locale.3pm.gz
%{perl_vendorarch}/Unicode/
%{perl_vendorarch}/auto/Unicode/

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.72-1
- Updated to version 0.72.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.52-1
- Initial package. (using DAR)
