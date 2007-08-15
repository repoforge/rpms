# $Id$
# Authority: dries
# Upstream: Ash Berlin <ash%20%3c+%3e%20cpan%20org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Model-File

Summary: File based storage model for Catalyst
Name: perl-Catalyst-Model-File
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Model-File/

Source: http://search.cpan.org//CPAN/authors/id/A/AS/ASH/Catalyst-Model-File-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
File based storage model for Catalyst.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/Catalyst::*
%{perl_vendorlib}/Catalyst/Model/
%{perl_vendorlib}/Catalyst/Helper/Model/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
