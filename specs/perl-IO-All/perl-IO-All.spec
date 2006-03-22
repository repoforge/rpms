# $Id$
# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-All

Summary: Object oriented interface for the Perl IO modules
Name: perl-IO-All
Version: 0.33
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-All/

Source: http://www.cpan.org/modules/by-module/IO/IO-All-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/IO/
%{perl_vendorlib}/IO/All.pm
%{perl_vendorlib}/IO/All.pod
%{perl_vendorlib}/IO/All/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.33-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Updated to release 0.33.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 0.31-1
- Initial package.
