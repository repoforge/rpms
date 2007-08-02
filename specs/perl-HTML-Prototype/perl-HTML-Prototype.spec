# $Id$
# Authority: dries
# Upstream: Sascha Kiefer <perl$intertivityNOSP4M,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Prototype

Summary: Generate HTML and Javascript for the Prototype library
Name: perl-HTML-Prototype
Version: 1.48
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Prototype/

Source: http://search.cpan.org//CPAN/authors/id/E/ES/ESSKAR/HTML-Prototype-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Generate HTML and Javascript for the Prototype library.

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
%doc %{_mandir}/man3/HTML::Prototype*
%{perl_vendorlib}/HTML/Prototype.pm
%{perl_vendorlib}/HTML/Prototype/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.48-1
- Initial package.
