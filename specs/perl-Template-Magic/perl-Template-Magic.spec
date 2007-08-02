# $Id$
# Authority: dries
# Upstream: Domizio Demichelis <perl,4pro,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Magic

Summary: Magic merger of runtime values with templates
Name: perl-Template-Magic
Version: 1.39
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Magic/

Source: http://search.cpan.org//CPAN/authors/id/D/DO/DOMIZIO/Template-Magic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Magic merger of runtime values with templates.

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
%doc %{_mandir}/man3/Template::Magic*
%doc %{_mandir}/man3/Bundle::Template::Magic*
%{perl_vendorlib}/Bundle/Template/Magic.pm
%{perl_vendorlib}/Template/Magic.pm
%{perl_vendorlib}/Template/Magic/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.39-1
- Initial package.
