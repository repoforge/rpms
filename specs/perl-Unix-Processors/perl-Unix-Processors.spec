# $Id$
# Authority: dries
# Upstream: Wilson Snyder <wsnyder$wsnyder,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unix-Processors

Summary: Per-processor information
Name: perl-Unix-Processors
Version: 2.033
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unix-Processors/

Source: http://search.cpan.org/CPAN/authors/id/W/WS/WSNYDER/Unix-Processors-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This package provides access to per-processor information from Perl.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Unix/Processors.pm
%{perl_vendorarch}/Unix/Processors
%{perl_vendorarch}/auto/Unix/Processors

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.033-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 2.033-1
- Updated to release 2.033.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.032-1
- Updated to release 2.032.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 2.031-1
- Updated to release 2.031.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.030-1
- Initial package.
