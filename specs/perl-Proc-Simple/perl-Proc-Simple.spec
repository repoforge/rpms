# $Id$

# Authority: dries
# Upstream: Michael Schilli <m$perlmeister,com>

%define real_name Proc-Simple
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Launch and control background processes
Name: perl-Proc-Simple
Version: 1.21
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-Simple/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/Proc-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
The Proc::Simple package provides objects mimicing real-life processes
from a user's point of view.

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
%{perl_vendorlib}/Proc/Simple.pm
%{perl_vendorlib}/auto/Proc/Simple
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
