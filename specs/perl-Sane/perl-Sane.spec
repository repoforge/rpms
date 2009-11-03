# $Id$
# Authority: dag
# Upstream: Jeffrey Ratcliffe

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sane

Summary: Perl extension for the SANE (Scanner Access Now Easy) Project
Name: perl-Sane
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sane/

Source: http://www.cpan.org/authors/id/R/RA/RATCLIFFE/Sane-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: sane-backends-devel
BuildRequires: perl
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: pkgconfig

%description
Perl extension for the SANE (Scanner Access Now Easy) Project.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Sane.3pm*
%{perl_vendorarch}/auto/Sane/
%{perl_vendorarch}/Sane.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.01-1
- Initial package. (using DAR)
