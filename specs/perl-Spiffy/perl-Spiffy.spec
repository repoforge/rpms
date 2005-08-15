# $Id$
# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Spiffy

Summary: Spiffy Perl Interface Framework For You
Name: perl-Spiffy
Version: 0.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spiffy/

Source: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/Spiffy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
"Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It
attempts to fix all the nits and warts of traditional Perl OO, in a
clean, straightforward and (perhaps someday) standard way.

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
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Spiffy.pm

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
