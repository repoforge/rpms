# $Id$
# Authority: dries
# Upstream: Simon Cozens <simon$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt_Auto

Summary: Framework for command-line applications
Name: perl-Getopt-Auto
Version: 1.9.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Auto/

Source: http://search.cpan.org/CPAN/authors/id/G/GL/GLEACH/Getopt_Auto-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Readonly)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Output)


%description
Framework for command-line applications.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%{perl_vendorlib}/Getopt/Auto.pm

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 1.9.1-1
- Updated to version 1.9.1.

* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 1.9.0-1
- Updated to version 1.9.0.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
