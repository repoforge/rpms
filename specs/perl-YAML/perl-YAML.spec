# $Id$

# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

%define real_name YAML
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Machine parseable data serialization format
Name: perl-YAML
Version: 0.35
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/I/IN/INGY/YAML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
YAML is an abbreviation of YAML Ain't Markup Language. It's a straightforward 
machine-parseable data serialization format.

%prep
%setup -n %{real_name}-%{version}

%build
echo y | %{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
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
%doc %{_mandir}/man1/*
%{_bindir}/*
%{perl_vendorlib}/YAML.*
%{perl_vendorlib}/YAML/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Initial package.
