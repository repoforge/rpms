# $Id$
# Authority: dries
# Upstream: Salvador Fandi&#241;o Garc&#237;a <salva$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-SmallProf

Summary: Per-line Perl profiler
Name: perl-Devel-SmallProf
Version: 2.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-SmallProf/

Source: http://www.cpan.org/modules/by-module/Devel/Devel-SmallProf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Devel::SmallProf profiler is focused on the time taken for a
program run on a line-by-line basis. It is intended to be as "small"
in terms of impact on the speed and memory usage of the profiled
program as possible and also in terms of being simple to use.

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Devel/SmallProf.pm

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Updated to release 2.01.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.00_03-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.00_03-1
- Initial package.
