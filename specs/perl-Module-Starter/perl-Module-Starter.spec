# $Id$

# Authority: dries
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define real_name Module-Starter
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Simple starterkit for any module
Name: perl-Module-Starter
Version: 1.34
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Starter/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Module-Starter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
A simple starterkit for any module.

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
%doc Changes
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/*
%{perl_vendorlib}/Module/Starter.pm
%{perl_vendorlib}/Module/Starter

%changelog
* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.34-1
- Updated to release 1.34.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Initial package.
