# $Id$
# Authority: dries
# Upstream: P Kent <pause$selsyn,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Timestamp

Summary: Create timestamp objects for testing or profiling
Name: perl-Test-Timestamp
Version: 1.2
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Timestamp/

Source: http://www.cpan.org/modules/by-module/Test/Test-Timestamp-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module you can create one or more timestamp objects which can
be used to record the exact time when a certain point in your code was
executed. The Devel::DProf module and its relatives all time subroutine
calls, which is usually a good enough resolution for profiling your code
and finding slow parts, but sometimes you need to examine a routine in
finer detail - hence the idea of timestamps. This routine uses
Time::HiRes

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Test/Timestamp.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
