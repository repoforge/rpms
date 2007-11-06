# $Id$
# Authority: dries
# Upstream: Alex Pavlovic <alex$taskforce-1,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Domain-TLD

Summary: Retrieve currently available tld names and descriptions
Name: perl-Net-Domain-TLD
Version: 1.65
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Domain-TLD/

Source: http://www.cpan.org/modules/by-module/Net/Net-Domain-TLD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
The purpose of this module is to provide user with current list of
available top level domain names including new ICANN additions and
ccTLDs

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Domain/TLD.pm

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.65-1
- Updated to release 1.65.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.62-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.62-1
- Updated to release 1.62.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Initial package.
