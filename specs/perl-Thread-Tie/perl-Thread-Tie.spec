# $Id$
# Authority: dgehl

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Thread-Tie

Summary: Tie variables into a thread of their own
Name: perl-Thread-Tie
Version: 0.13
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Thread-Tie/

Source: http://search.cpan.org/CPAN/authors/id/E/EL/ELIZABETH/Thread-Tie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Thread::Serialize) >= 0.07
BuildRequires: perl(load) >= 0.11
Requires: perl(Thread::Serialize) >= 0.07
Requires: perl(load) >= 0.11

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The standard shared variable scheme used by Perl, is based on tie-ing
the variable to some very special dark magic. This dark magic ensures
that shared variables, which are copied just as any other variable
when a thread is started, update values in all of the threads where 
they exist as soon as the value of a shared variable is changed.

Needless to say, this could use some improvement.

The Thread::Tie module is a proof-of-concept implementation of another
approach to shared variables. Instead of having shared variables exist 
in all the threads from which they are accessible, shared variable 
exist as "normal", unshared variables in a seperate thread. Only a 
tied object exists in each thread from which the shared variable is 
accesible.

Through the use of a client-server model, any thread can fetch and/or 
update variables living in that thread. This client-server 
functionality is hidden under the hood of tie().


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
%doc %{_mandir}/man3/Thread::Tie.3pm*
%doc %{_mandir}/man3/Thread::Tie::Array.3pm*
%doc %{_mandir}/man3/Thread::Tie::Handle.3pm*
%doc %{_mandir}/man3/Thread::Tie::Hash.3pm*
%doc %{_mandir}/man3/Thread::Tie::Scalar.3pm*
%doc %{_mandir}/man3/Thread::Tie::Thread.3pm*
%dir %{perl_vendorlib}/Thread/
%{perl_vendorlib}/Thread/Tie.pm
%dir %{perl_vendorlib}/Thread/Tie/
%{perl_vendorlib}/Thread/Tie/Array.pm
%{perl_vendorlib}/Thread/Tie/Handle.pm
%{perl_vendorlib}/Thread/Tie/Hash.pm
%{perl_vendorlib}/Thread/Tie/Scalar.pm
%{perl_vendorlib}/Thread/Tie/Thread.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.13-1
- Updated to version 0.13.

* Fri Jun 22 2007 Dominik Gehl <gehl@inverse.ca> - 0.12-1
- Initial package.
