# $Id$
# Authority: dries
# Upstream: Ralf S. Engelschall <rse$engelschall,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-GuruMeditation

Summary: Guru Meditation for CGIs
Name: perl-CGI-GuruMeditation
Version: 1.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-GuruMeditation/

Source: http://search.cpan.org//CPAN/authors/id/R/RS/RSE/CGI-GuruMeditation-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Guru Meditation for CGIs.

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
%doc README
%doc %{_mandir}/man3/CGI::GuruMeditation*
%{perl_vendorlib}/CGI/GuruMeditation.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
