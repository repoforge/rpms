# $Id$
# Authority: dries
# Upstream: Kenneth Albanowski <kjahds$kjahds,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name TermReadKey

Summary: Module for simple terminal control 
Name: perl-Term-ReadKey
Version: 
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TermReadKey/

Source: http://www.cpan.org/modules/by-module/TermReadKey/TermReadKey-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module, ReadKey, provides ioctl control for terminals and Win32
consoles so the input modes can be changed (thus allowing reads of a single
character at a time), and also provides non-blocking reads of stdin, as well
as several other terminal related features, including retrieval/modification
of the screen size, and retrieval/modification of the control characters.

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
%doc README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Term/
%{perl_vendorarch}/Term/ReadKey.pm
%dir %{perl_vendorarch}/auto/Term/
%{perl_vendorarch}/auto/Term/ReadKey/

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - -1
- Updated to release .

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 2.21-1
- Initial package.
