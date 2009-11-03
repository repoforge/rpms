# $Id$
# Authority: dries
# Upstream: Chia-liang Kao <clkao$clkao,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVN-Mirror

Summary: Subversion repository mirroring tool
Name: perl-SVN-Mirror
Version: 0.75
Release: 2%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Mirror/

Source: http://www.cpan.org/modules/by-module/SVN/SVN-Mirror-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Date::Format)
BuildRequires: perl(File::chdir)
BuildRequires: perl(SVN::Core) >= 1.2.0
BuildRequires: perl(SVN::Simple::Edit)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(URI::file)
Requires: perl(Class::Accessor)
Requires: perl(Date::Format)
Requires: perl(File::chdir)
Requires: perl(SVN::Core) >= 1.2.0
Requires: perl(SVN::Simple::Edit)
Requires: perl(Term::ReadKey)
Requires: perl(URI::Escape)
Requires: perl(URI::file)
AutoReq: no

%description
SVN::Mirror is a subversion repository mirroring tool.

%prep
%setup -n %{real_name}-%{version}

%build
echo "n" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc CHANGES README SIGNATURE TODO
%doc %{_mandir}/man?/*
%{_bindir}/svm
%dir %{perl_vendorlib}/SVN/
%{perl_vendorlib}/SVN/Mirror.pm
%{perl_vendorlib}/SVN/Mirror/

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.75-2
- Change to manual dependencies

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.75-1
- Updated to version 0.75.
- Rewrote build-requirements from META.yml

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.73-1
- Updated to release 0.73.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.72-1
- Updated to release 0.72.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.70-1
- Updated to release 0.70.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.68-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.68-1
- Updated to release 0.68.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.67-1
- Updated to release 0.67.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Updated to release 0.61.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.56-1
- Updated to release 0.56.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Updated to release 0.51.

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 0.49-1
- Update to release 0.49.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Initial package.
