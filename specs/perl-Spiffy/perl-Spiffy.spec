# $Id$

# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define real_name Spiffy
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Spiffy Perl Interface Framework For You
Name: perl-Spiffy
Version: 0.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Spiffy/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Spiffy.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Updated to release 0.21.

* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
