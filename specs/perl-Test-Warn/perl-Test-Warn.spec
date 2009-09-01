# $Id$
# Authority: dries
# Upstream: Alexandr Ciornii <alexchorny$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Warn

Summary: Perl extension to test methods for warnings
Name: perl-Test-Warn
Version: 0.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Warn/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/Test-Warn-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
#BuildRequires: perl(File::Spec)
#BuildRequires: perl(Sub::Uplevel) >= 0.12
#BuildRequires: perl(Test::Builder) >= 0.13
#BuildRequires: perl(Test::Builder::Tester) >= 1.02
#BuildRequires: perl(Test::More)
BuildRequires: perl(Tree::DAG_Node)
BuildRequires: perl >= 5.006

# From yaml requires ( the ones wich are not found automatically )
Requires: perl(File::Spec)
Requires: perl(Test::Builder) >= 0.13
Requires: perl(Test::Builder::Tester) >= 1.02
Requires: perl(Test::More)
Requires: perl(Tree::DAG_Node)


%description
This module provides a few convenience methods for testing warning based
code.

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
%doc %{_mandir}/man3/Test::Warn.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Warn/
%{perl_vendorlib}/Test/Warn.pm

%changelog
* Tue Sep  1 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Updated to version 0.21.

* Wed Nov 26 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Wed Jun 11 2008 Dries Verachtert <dries@ulyssis.org> - 0.10-2
- Added Tree::DAG_Node requirement, thanks to Sven Sternberger.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
