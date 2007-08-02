# $Id$
# Authority: dries
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Email-Simple-Creator

Summary: Constructor for Email::Simple
Name: perl-Email-Simple-Creator
Version: 1.41
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Email-Simple-Creator/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Email-Simple-Creator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This package provides a constructor for Email::Simple.

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
%doc Changes README
%doc %{_mandir}/man3/Email::Simple::Creator*
%dir %{perl_vendorlib}/Email/Simple/
%{perl_vendorlib}/Email/Simple/Creator.pm

%changelog
* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 1.41-1
- Initial package.
