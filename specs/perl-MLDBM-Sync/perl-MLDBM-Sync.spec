# $Id: $

# Authority: dries
# Upstream:

%define real_name MLDBM-Sync
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Safe concurrent access to MLDBM databases
Name: perl-MLDBM-Sync
Version: 0.30
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MLDBM-Sync/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/C/CH/CHAMAS/MLDBM-Sync-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
Requires: perl-MLDBM

%description
This module wraps around the MLDBM interface, by handling concurrent
access to MLDBM databases with file locking, and flushes i/o explicity
per lock/unlock. The new [Read]Lock()/UnLock() API can be used to
serialize requests logically and improve performance for bundled reads &
writes.

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
%doc README CHANGES
%{_mandir}/man3/*
%{perl_vendorlib}/MLDBM/Sync.pm
%{perl_vendorlib}/MLDBM/Sync/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Initial package.
