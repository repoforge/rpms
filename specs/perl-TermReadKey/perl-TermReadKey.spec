# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name TermReadKey

summary: Perl module for simple terminal control
Name: perl-TermReadKey
Version: 2.30
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TermReadKey/

Source: http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.gz
#Source: http://www.cpan.org/modules/by-module/TermReadKey/TermReadKey-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl

%description
Term::ReadKey is a compiled perl module dedicated to providing simple
control over terminal driver modes (cbreak, raw, cooked, etc.,) support for
non-blocking reads, if the architecture allows, and some generalized handy
functions for working with terminals. One of the main goals is to have the
functions as portable as possible, so you can just plug in "use Term::ReadKey"
on any architecture and have a good likelyhood of it working.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorarch}/Term/
%{perl_vendorarch}/Term/ReadKey.pm
%dir %{perl_vendorarch}/auto/Term/
%{perl_vendorarch}/auto/Term/ReadKey/

%changelog
* Mon Jun 05 2006 Dag Wieers <dag@wieers.com> - 2.30-1
- Initial package. (using DAR)
