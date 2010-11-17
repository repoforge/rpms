# $Id$
# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

### EL6 ships with perl-UNIVERSAL-can-1.15-1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-can

Summary: Hack around people calling UNIVERSAL::can() as a function
Name: perl-UNIVERSAL-can
Version: 1.16
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-can/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/UNIVERSAL-can-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Module::Build) 
BuildRequires: perl(Scalar::Util)
#BuildRequires: perl(Test::Simple) >= 0.60
BuildRequires: perl(Test::Simple)
BuildRequires: perl >= v5.6.2
Requires: perl(Scalar::Util)
#Requires: perl(Test::Simple) >= 0.60
Requires: perl(Test::Simple)
Requires: perl >= v5.6.2

%filter_from_requires /^perl*/d
%filter_setup


%description
Hack around people calling UNIVERSAL::can() as a function.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Build.PL --installdirs vendor --destdir %{buildroot}
./Build

%install
%{__rm} -rf %{buildroot}
./Build pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/UNIVERSAL/can.pm

%changelog
* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 1.16-1
- Updated to version 1.16.

* Thu Jul 16 2009 Christoph Maser <cmr@financial.com> - 1.15-1
- Updated to version 1.15.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
