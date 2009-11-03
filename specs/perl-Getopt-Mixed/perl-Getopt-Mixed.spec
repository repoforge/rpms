# $Id$
# Authority: dries
# Upstream: Christopher J. Madsen <cjm$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Getopt-Mixed

Summary: Getopt processing with both long and short options
Name: perl-Getopt-Mixed
Version: 1.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Getopt-Mixed/

Source: http://www.cpan.org/modules/by-module/Getopt/Getopt-Mixed-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provides GNU-style option processing for Perl 5 scripts,
with both long and short options.  Please see the documentation at the
end of the module for instructions on its use and licensing
restrictions.

%prep
%setup -n %{real_name}-%{version}

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Getopt::Mixed.3pm*
%dir %{perl_vendorlib}/Getopt/
%{perl_vendorlib}/Getopt/Mixed.pm

%changelog
* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 1.10-1
- Updated to latest upstream version { old source not available }

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.008-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.008-1
- Initial package.
