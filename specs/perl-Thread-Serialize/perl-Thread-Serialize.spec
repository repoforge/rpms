# $Id$
# Authority: dgehl

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Thread-Serialize

Summary: serialize data-structures between threads
Name: perl-Thread-Serialize
Version: 0.10
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Thread-Serialize/

Source: http://www.cpan.org/modules/by-module/Thread/Thread-Serialize-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The Thread::Serialize module is a library for centralizing the 
routines used to serialize data-structures between threads.
Because of this central location, other modules such as 
Thread::Conveyor, Thread::Pool or Thread::Tie can benefit from 
the same optimizations that may take place here in the future.

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
%doc %{_mandir}/man3/Thread::Serialize.3pm*
%dir %{perl_vendorlib}/Thread/
%{perl_vendorlib}/Thread/Serialize.pm

%changelog
* Fri Jun 22 2007 Dominik Gehl <gehl@inverse.ca> - 0.10-1
- Initial package.
