# $Id$
# Authority: dries
# Upstream: Adam Paynter <adapay$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-I18N-Request

Summary: Plugin for localizing/delocalizing paths and parameters
Name: perl-Catalyst-Plugin-I18N-Request
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-I18N-Request/

Source: http://search.cpan.org//CPAN/authors/id/A/AD/ADAPAY/Catalyst-Plugin-I18N-Request-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Plugin for localizing/delocalizing paths and parameters.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Catalyst::Plugin::I18N::Request*
%{perl_vendorlib}/Catalyst/Plugin/I18N/Request.pm
%dir %{perl_vendorlib}/Catalyst/Plugin/I18N/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
