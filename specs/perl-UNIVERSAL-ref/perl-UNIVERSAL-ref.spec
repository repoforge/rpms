# $Id$
# Authority: dag
# Upstream: Joshua ben Jore <jjore$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-ref

Summary: Perl module to turn ref() into a multimethod
Name: perl-UNIVERSAL-ref
Version: 0.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-ref/

Source: http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-ref-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-UNIVERSAL-ref is a Perl module to turn ref() into a multimethod.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/UNIVERSAL::ref.3pm*
%dir %{perl_vendorarch}/auto/UNIVERSAL/
%{perl_vendorarch}/auto/UNIVERSAL/ref/
%dir %{perl_vendorarch}/UNIVERSAL/
%{perl_vendorarch}/UNIVERSAL/ref.pm

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.11-1
- Initial package. (using DAR)
