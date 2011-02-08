# $Id$
# Authority: dgehl

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Thread-Conveyor

Summary: Transport of any data-structure between threads
Name: perl-Thread-Conveyor
Version: 0.19
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Thread-Conveyor/

Source: http://search.cpan.org/CPAN/authors/id/E/EL/ELIZABETH/Thread-Conveyor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Thread::Serialize)
BuildRequires: perl(Thread::Tie) >= 0.09
BuildRequires: perl(load)
Requires: perl(Thread::Serialize)
Requires: perl(Thread::Tie) >= 0.09
Requires: perl(load)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The Thread::Conveyor object is a thread-safe data structure that 
mimics the behaviour of a conveyor belt. One or more worker threads
can put boxes with frozen values and references on one end of the belt
to be taken off by one or more worker threads on the other end of the
belt to be thawed and returned.

A box may consist of any combination of scalars and references to
scalars, arrays (lists) and hashes. Freezing and thawing is currently
done with the Thread::Serialize module, but that may change in the 
future. Objects and code references are currently not allowed.

By default, the maximum number of boxes on the belt is limited to 50.
Putting of boxes on the belt is halted if the maximum number of boxes
is exceeded. This throttling feature was added because it was found 
that excessive memory usage could be caused by having the belt growing
too large. Throttling can be disabled if so desired.

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
%doc %{_mandir}/man3/Thread::Conveyor.3pm*
%doc %{_mandir}/man3/Thread::Conveyor::Array.3pm*
%doc %{_mandir}/man3/Thread::Conveyor::Throttled.3pm*
%doc %{_mandir}/man3/Thread::Conveyor::Tied.3pm*
%dir %{perl_vendorlib}/Thread/
%{perl_vendorlib}/Thread/Conveyor.pm
%dir %{perl_vendorlib}/Thread/Conveyor/
%{perl_vendorlib}/Thread/Conveyor/Array.pm
%{perl_vendorlib}/Thread/Conveyor/Throttled.pm
%{perl_vendorlib}/Thread/Conveyor/Tied.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.19-1
- Updated to version 0.19.

* Fri Jun 22 2007 Dominik Gehl <gehl@inverse.ca> - 0.17-1
- Initial package.
