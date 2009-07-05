# $Id$
# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-All

Summary: Object oriented interface for the Perl IO modules
Name: perl-IO-All
Version: 0.39
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-All/

Source: http://www.cpan.org/modules/by-module/IO/IO-All-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 1:5.6.1

%description
IO::All combines all of the best Perl IO modules into a single Spiffy
object oriented interface to greatly simplify your everyday Perl IO
idioms. It exports a single function called "io", which returns a new
IO::All object. And that object can do it all!

The IO::All object is a proxy for IO::File, IO::Dir, IO::Socket,
IO::String, Tie::File, File::Spec, File::Path and File::ReadBackwards;
as well as all the DBM and MLDBM modules. You can use most of the
methods found in these classes and in IO::Handle (which they inherit
from). IO::All adds dozens of other helpful idiomatic methods including
file stat and manipulation functions.

IO::All is pluggable, and modules like IO::All::LWP and IO::All::Mailto
add even more functionality. Optionally, every IO::All object can be
tied to itself. This means that you can use most perl IO builtins on it:
readline, getc, print, printf, syswrite, sysread, close.

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
%doc %{_mandir}/man3/IO::All.3pm*
%doc %{_mandir}/man3/IO::All::*.3pm*
%dir %{perl_vendorlib}/IO/
%{perl_vendorlib}/IO/All/
%{perl_vendorlib}/IO/All.pm
%{perl_vendorlib}/IO/All.pod

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.39-1
- Updated to version 0.39.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.38-1
- Updated to release 0.38.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Updated to release 0.35.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
