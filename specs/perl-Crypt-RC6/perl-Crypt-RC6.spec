# $Id$

# Authority: dries
# Upstream: John Hughes <jhughes$frostburg,edu>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-RC6

Summary: Crypt::CBC compliant RC6 block cipher encryption module
Name: perl-Crypt-RC6
Version: 1.0
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-RC6/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-RC6-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
A Crypt::CBC compliant RC6 block cipher encryption module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Crypt/RC6.pm
%{perl_vendorarch}/auto/Crypt/RC6

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
