# $Id$
# Authority: dries
# Upstream: Steven Lembark <lembark$wrkhors,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-ForceEval

Summary: Checks for subs which die by using eval
Name: perl-Sub-ForceEval
Version: 1.32
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-ForceEval/

Source: http://search.cpan.org//CPAN/authors/id/L/LE/LEMBARK/Sub-ForceEval-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This evals the attributd sub, and checks for an 
eval on the stack if it dies. If there is one 
then the exception is propagated via "die $@";
if not then cluck is used to dump a stack trace
and the error message.

This is useful for sub's that know they throw what
should be non-fatal exceptions or for calls inside
of long-running processes that need to decide quickly
if they have been called properly. It can also be 
useful for modules that use modules that use Fatal,
which can lead to the code issuing exceptions that
aren't explicit in the code.

This is generally more useful in testing than production,
but can also be useful for tracking down failures.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Sub::ForceEval*
%{perl_vendorlib}/Sub/ForceEval.pm

%changelog
* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 1.32-1
- Updated to release 1.32.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Initial package.
