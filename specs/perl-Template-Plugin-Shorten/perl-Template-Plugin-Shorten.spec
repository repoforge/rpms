# $Id$
# Authority: dries
# Upstream: Kentaro Kuribayashi <kentaro$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Plugin-Shorten

Summary: Template plugin to shorten/lengthen URLs
Name: perl-Template-Plugin-Shorten
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Plugin-Shorten/

Source: http://search.cpan.org//CPAN/authors/id/K/KE/KENTARO/Template-Plugin-Shorten-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Template plugin to shorten/lengthen URLs.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Template::Plugin::Shorten*
%{perl_vendorlib}/Template/Plugin/Shorten.pm
%dir %{perl_vendorlib}/Template/Plugin/

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
