# $Id$
# Authority: dries
# Upstream: Jeff Rodriguez <jeff$jeffrodriguez,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parallel-Fork-BossWorker

Summary: Extension for easily creating forking queue processing application
Name: perl-Parallel-Fork-BossWorker
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parallel-Fork-BossWorker/

Source: http://www.cpan.org/modules/by-module/Parallel/Parallel-Fork-BossWorker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) >= 4:5.8.8

%description
Perl extension for easily creating forking queue processing application.

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
%doc Changes README
%doc %{_mandir}/man3/Parallel::Fork::BossWorker*
%{perl_vendorlib}/Parallel/Fork/BossWorker.pm
%dir %{perl_vendorlib}/Parallel/Fork/

%changelog
* Wed Jun 13 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Updated to release 0.03.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
