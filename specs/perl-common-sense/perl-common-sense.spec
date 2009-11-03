# $Id$
# Authority: cmr

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name common-sense

Summary: Perl module named common-sense
Name: perl-common-sense
Version: 0.04
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/common-sense/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/common-sense-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
s module implements some sane defaults for Perl programs, as defined by two typical (or not so typical - use your common sense) specimens of Perl coders.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README
%doc %{_mandir}/man3/common::sense.3pm.gz
%{perl_vendorlib}/common/sense.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.03
- initial package
* Wed Jul 08 2009 Christoph Maser <cmr@financial.com> - 3.6-1
- Initial package. (using DAR)
