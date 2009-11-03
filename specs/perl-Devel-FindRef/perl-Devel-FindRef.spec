# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-FindRef

Summary: Perl module named Devel-FindRef
Name: perl-Devel-FindRef
Version: 1.422
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-FindRef/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/Devel-FindRef-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(common::sense)


%description
perl-Devel-FindRef is a Perl module.

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
%doc %{_mandir}/man3/Devel::FindRef.3pm*
%dir %{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/auto/Devel/FindRef/
%dir %{perl_vendorarch}/Devel/
%{perl_vendorarch}/Devel/FindRef.pm

%changelog
* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 1.422-1
- Updated to version 1.422.

* Sun Jul 19 2009 Dag Wieers <dag@wieers.com> - 1.42-1
- Initial package. (using DAR)
