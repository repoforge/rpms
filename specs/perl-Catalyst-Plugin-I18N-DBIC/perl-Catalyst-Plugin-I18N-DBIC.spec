# $Id$
# Authority: dries
# Upstream: Ian Docherty <pause$iandocherty,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-I18N-DBIC

Summary: Internationalization for Catalyst data loaded from a database
Name: perl-Catalyst-Plugin-I18N-DBIC
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-I18N-DBIC/

Source: http://search.cpan.org//CPAN/authors/id/I/IC/ICD/Catalyst-Plugin-I18N-DBIC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Internationalization for Catalyst data loaded from a database.

%prep
%setup -n %{real_name}

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
%doc %{_mandir}/man3/Catalyst::Plugin::I18N::DBIC*
%{perl_vendorlib}/Catalyst/Plugin/I18N/DBIC.pm

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
