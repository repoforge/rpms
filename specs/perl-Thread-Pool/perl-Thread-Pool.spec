# $Id$
# Authority: dgehl

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Thread-Pool

Summary: Group of threads for performing similar jobs
Name: perl-Thread-Pool
Version: 0.33
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Thread-Pool/

Source: http://search.cpan.org/CPAN/authors/id/E/EL/ELIZABETH/Thread-Pool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Thread::Conveyor) >= 0.15
BuildRequires: perl(Thread::Conveyor::Monitored) >= 0.11
Requires: perl(Thread::Conveyor) >= 0.15
Requires: perl(Thread::Conveyor::Monitored) >= 0.11

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The Thread::Pool allows you to set up a group of (worker) threads to
execute a (large) number of similar jobs that need to be executed
asynchronously. The routine that actually performs the job (the "do"
routine), must be specified as a name or a reference to a (anonymous)
subroutine.

This module only functions on Perl versions 5.8.0 and later.
And then only when threads are enabled with -Dusethreads.  It
is of no use with any version of Perl before 5.8.0 or without
threads enabled.
%prep
%setup -n %{real_name}-%{version}

%build
%{expand: %%define optflags %{optflags} -fPIC}
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README CHANGELOG TODO
%doc %{_mandir}/man3/Thread::Pool.3pm*
%dir %{perl_vendorlib}/Thread/
%{perl_vendorlib}/Thread/Pool.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.33-1
- Updated to version 0.33.

* Fri Jun 22 2007 Dominik Gehl <gehl@inverse.ca> - 0.32-1
- Initial package.
