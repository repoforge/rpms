# $Id$

# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define real_name Carp-Assert
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Executable commments
Name: perl-Carp-Assert
Version: 0.18
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Carp-Assert/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/Carp-Assert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Carp::Assert is intended for a purpose like the ANSI C library assert.h.

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
%{perl_vendorlib}/Carp/Assert.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.18-1
- Initial package.
