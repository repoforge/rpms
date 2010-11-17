# $Id$
# Authority: dries
# Upstream: Tassilo von Parseval <tassilo,parseval$post,rwth-aachen,de>

### EL6 ships with perl-List-MoreUtils-0.22-10.el6
# Tag: rft

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name List-MoreUtils
%define real_version 0.25_02

Summary: Additions to List::Util
Name: perl-List-MoreUtils
Version: 0.25.2
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/List-MoreUtils/

Source: http://search.cpan.org/CPAN/authors/id/V/VP/VPARSEVAL/List-MoreUtils-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module provide the missing functionality from List::Util (see
"SUGGESTED ADDITIONS" in its manpage).

%prep
%setup -n %{real_name}-%{real_version}

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
%doc %{_mandir}/man3/List::MoreUtils.3pm*
%dir %{perl_vendorarch}/List/
%{perl_vendorarch}/List/MoreUtils.pm
%dir %{perl_vendorarch}/auto/List/
%{perl_vendorarch}/auto/List/MoreUtils/

%changelog
* Wed Aug 05 2009 Christoph Maser <cmr@financial.com> - 0.25.2-1
- Updated to version 0.25.2 (Dev. release, setting test-Tag)

* Fri Jul 31 2009 Christoph Maser <cmr@financial.com> - 0.25.1-1
- Updated to version 0.25.1

* Mon Jul 13 2009 Christoph Maser <cmr@financial.com> - 0.23-1
- Updated to version 0.23.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Updated to release 0.17.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
