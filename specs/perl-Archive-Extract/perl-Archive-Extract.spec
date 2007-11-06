# $Id$
# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Archive-Extract

Summary: Generic archive extracting mechanism
Name: perl-Archive-Extract
Version: 0.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Archive-Extract/

Source: http://www.cpan.org/modules/by-module/Archive/Archive-Extract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
A generic archive extracting mechanism.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Archive/
%{perl_vendorlib}/Archive/Extract.pm

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Updated to release 0.18.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.07-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
