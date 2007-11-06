# $Id$
# Authority: dries
# Upstream: Mark Overmeer <mark$overmeer,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-Types

Summary: Definition of MIME types
Name: perl-MIME-Types
Version: 1.20
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-Types/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-Types-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
A start for a more detailed data-structure to keep knowledge
about various data types are defined by MIME.  Some basic
treatments with mime types are implemented.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/MIME/*

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Updated to release 1.19.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Updated to release 1.17.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Initial package.
