# $Id$
# Authority: dries
# Upstream: Ken Williams <ken$mathforum,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-ParseXS
%define real_version 2.2002

Summary: Converts Perl XS code into C code
Name: perl-ExtUtils-ParseXS
Version: 2.20.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-ParseXS/

Source: http://www.cpan.org/modules/by-module/ExtUtils/ExtUtils-ParseXS-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp) 
BuildRequires: perl(DynaLoader) 
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::CBuilder) 
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Cwd) 
BuildRequires: perl(Exporter) 
BuildRequires: perl(File::Basename) 
BuildRequires: perl(File::Spec) 
BuildRequires: perl(Symbol) 

%description
With this module, you can Convert Perl XS code into C code.

%prep
%setup -n %{real_name}-%{real_version}

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
%doc Changes INSTALL MANIFEST META.yml README
%doc %{_mandir}/man3/ExtUtils::ParseXS.3pm*
%dir %{perl_vendorlib}/ExtUtils/
%{perl_vendorlib}/ExtUtils/ParseXS.pm
%{perl_vendorlib}/ExtUtils/xsubpp

%changelog
* Mon Jul 23 2009 Christoph Maser <cmr@financial.com> - 2.20.02-1
- Updated to version 2.20.02.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 2.20-1
- Updated to version 2.20.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 2.19-1
- Updated to release 2.19.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.18-1
- Updated to release 2.18.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 2.17-1
- Updated to release 2.17.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 2.16-1
- Updated to release 2.16.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.10-1
- Updated to release 2.10.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.08-1
- Initial package.
