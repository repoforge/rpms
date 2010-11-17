# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

### EL6 ships with perl-Test-Taint-1.04-9.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Taint

Summary: Perl module implements tools to test taintedness
Name: perl-Test-Taint
Version: 1.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Taint/

Source: http://www.cpan.org/modules/by-module/Test/Test-Taint-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Test-Taint is a Perl module implements tools to test taintedness.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Test::Taint.3pm*
%dir %{perl_vendorarch}/Test/
%{perl_vendorarch}/Test/Taint.pm
%dir %{perl_vendorarch}/auto/Test/
%{perl_vendorarch}/auto/Test/Taint/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.04-1
- Initial package. (using DAR)
