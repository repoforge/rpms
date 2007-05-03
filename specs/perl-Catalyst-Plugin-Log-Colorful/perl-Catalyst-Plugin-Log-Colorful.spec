# $Id$
# Authority: dries
# Upstream: Tomohiro Teranishi <tomyhero$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Log-Colorful

Summary: Catalyst Plugin for Colorful Log
Name: perl-Catalyst-Plugin-Log-Colorful
Version: 0.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Log-Colorful/

Source: http://search.cpan.org//CPAN/authors/id/T/TO/TOMYHERO/Catalyst-Plugin-Log-Colorful-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Catalyst Plugin for Colorful Log.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Catalyst::Plugin::Log::Colorful*
%{perl_vendorlib}/Catalyst/Plugin/Log/Colorful.pm
%dir %{perl_vendorlib}/Catalyst/Plugin/Log/
%dir %{perl_vendorlib}/Catalyst/Plugin/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
