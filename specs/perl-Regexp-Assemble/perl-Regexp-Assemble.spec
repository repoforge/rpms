# $Id$
# Authority: dries
# Upstream: David Landgren <david$landgren,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Regexp-Assemble

Summary: Create Regular expressions
Name: perl-Regexp-Assemble
Version: 0.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Regexp-Assemble/

Source: http://search.cpan.org/CPAN/authors/id/D/DL/DLAND/Regexp-Assemble-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
You can create regular expressions with this module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Regexp/Assemble.pm

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Updated to release 0.31.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.28-1
- Updated to release 0.28.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.27-1
- Updated to release 0.27.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Initial package.
