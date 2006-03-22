# $Id$
# Authority: dries
# Upstream: Michael Schilli <m$perlmeister,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Proc-Simple

Summary: Launch and control background processes
Name: perl-Proc-Simple
Version: 1.21
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Proc-Simple/

Source: http://www.cpan.org/modules/by-module/Proc/Proc-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
The Proc::Simple package provides objects mimicing real-life processes
from a user's point of view.

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
%dir %{perl_vendorlib}/Proc/
%{perl_vendorlib}/Proc/Simple.pm
%dir %{perl_vendorlib}/auto/Proc/
%{perl_vendorlib}/auto/Proc/Simple

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.21-1.2
- Rebuild for Fedora Core 5.

* Wed Dec 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
