# $Id$
# Authority: dries
# Upstream: John D. Shearer <jshearer$netguy,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-DHCPparse

Summary: Perl extension for parsing dhcpd lease files
Name: perl-Text-DHCPparse
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-DHCPparse/

Source: http://search.cpan.org//CPAN/authors/id/J/JS/JSHEARER/Text-DHCPparse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Perl extension for parsing dhcpd lease files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Text::DHCPparse*
%{perl_vendorlib}/Text/DHCPparse.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
