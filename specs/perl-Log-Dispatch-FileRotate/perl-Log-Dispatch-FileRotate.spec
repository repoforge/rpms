# $Id$
# Authority: dries
# Upstream: Mark Pfeiffer <markpf$mlp-consulting,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Dispatch-FileRotate

Summary: Automatically archive and rotate logfiles
Name: perl-Log-Dispatch-FileRotate
Version: 1.16
Release: 1
License: Unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Dispatch-FileRotate/

Source: http://www.cpan.org/modules/by-module/Log/Log-Dispatch-FileRotate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)
Requires: perl, perl-Log-Dispatch

%description
This module provides a simple object for logging to files under the
Log::Dispatch::* system, and automatically rotating them according to
different constraints. This is basically a Log::Dispatch::File wrapper
with additions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/Log/Dispatch/FileRotate/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Log/Dispatch/FileRotate.pm

%changelog
* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Sat Jun 5 2004 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Initial package.
