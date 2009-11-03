# $Id$
# Authority: dgehl

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Thread-Conveyor-Monitored

Summary: Monitor a belt for specific content
Name: perl-Thread-Conveyor-Monitored
Version: 0.12
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Thread-Conveyor/

Source: http://www.cpan.org/modules/by-module/Thread/Thread-Conveyor-Monitored-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Thread::Conveyor::Monitored module implements a single worker
thread that takes of boxes of values from a belt created with 
Thread::Conveyor and which checks the boxes for specific content.

It can be used for simply logging actions that are placed on the belt.
Or only output warnings if a certain value is encountered in a box. Or
create a safe sandbox for Perl modules that are not thread-safe yet.

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
%doc %{_mandir}/man3/Thread::Conveyor::Monitored.3pm*
%dir %{perl_vendorlib}/Thread/Conveyor/
%{perl_vendorlib}/Thread/Conveyor/Monitored.pm

%changelog
* Fri Jun 22 2007 Dominik Gehl <gehl@inverse.ca> - 0.12-1
- Initial package.
