# $Id$
# Authority: dries
# Upstream: Steven Lembark <lembark$wrkhors,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-ForceEval
%define real_version 0.004004

Summary: Checks for subs which die by using eval
Name: perl-Sub-ForceEval
Version: 2.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-ForceEval/

Source: http://www.cpan.org/modules/by-module/Sub/Sub-ForceEval-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

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
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Sub::ForceEval.3pm*
%dir %{perl_vendorlib}/Sub/
#%{perl_vendorlib}/Sub/ForceEval/
%{perl_vendorlib}/Sub/ForceEval.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.04-1
- Updated to release 2.04.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release 2.02.

* Thu Jan 04 2007 Dries Verachtert <dries@ulyssis.org> - 1.32-1
- Updated to release 1.32.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.30-1
- Initial package.
