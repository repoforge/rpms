# $Id$

# Authority: dries
# Upstream: Damian Conway <damian$conway,org>

%define real_name Filter-Simple
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Simplified source filtering
Name: perl-Filter-Simple
Version: 0.79
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Filter-Simple/

Source: http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Filter-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module permits simplified source filtering.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Filter/Simple.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

# perl_vendorlib: /usr/lib/perl5/vendor_perl/5.8.0
# perl_vendorarch: /usr/lib/perl5/vendor_perl/5.8.0/i386-linux-thread-multi
# perl_archlib: /usr/lib/perl5/5.8.0/i386-linux-thread-multi
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Tue Dec 07 2004 Dries Verachtert <dries@ulyssis.org> - 0.79-1
- Initial package.
