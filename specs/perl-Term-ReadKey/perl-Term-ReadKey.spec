# $Id$

# Authority: dries
# Upstream: Kenneth Albanowski <kjahds$kjahds,com>

%define real_name TermReadKey
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Module for simple terminal control 
Name: perl-Term-ReadKey
Version: 
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/TermReadKey/

Source: http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.gz
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
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Term/ReadKey.pm
%{perl_vendorarch}/auto/Term/ReadKey/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - -1
- Updated to release .

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 2.21-1
- Initial package.
