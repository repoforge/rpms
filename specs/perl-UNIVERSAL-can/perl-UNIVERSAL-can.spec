# $Id$
# Authority: dries
# Upstream: chromatic <chromatic$wgz,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-can

Summary: Hack around people calling UNIVERSAL::can() as a function
Name: perl-UNIVERSAL-can
Version: 1.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-can/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/UNIVERSAL-can-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Hack around people calling UNIVERSAL::can() as a function.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/UNIVERSAL/can.pm

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1.2
- Rebuild for Fedora Core 5.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
